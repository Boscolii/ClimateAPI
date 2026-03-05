from fastapi import FastAPI
import boto3
from boto3.dynamodb.conditions import Key

app = FastAPI()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clima_dados')

@app.get("/")
def home():
    return {"message": "API Climática rodando"}

@app.get("/clima")
def buscar_por_local(location: str):
    response = table.query(
        KeyConditionExpression=Key("Location").eq(location)
    )
    return response["Items"]

@app.get("/media-temperatura")
def media_temperatura(location: str):
    response = table.query(
        KeyConditionExpression=Key("Location").eq(location)
    )

    items = response["Items"]

    if not items:
        return {"erro": "Cidade não encontrada"}

    temperaturas = [float(item["Temperature_C"]) for item in items if "Temperature_C" in item]

    media = sum(temperaturas) / len(temperaturas)

    return {
        "cidade": location,
        "media_temperatura": round(media, 2)
    }


@app.get("/clima-periodo")
def buscar_por_periodo(location: str, data_inicio: str, data_fim: str):
    response = table.query(
        KeyConditionExpression=
        Key("Location").eq(location) &
        Key("Date_Time").between(data_inicio, data_fim)
        )

    return {
        "cidade": location,
        "periodo": f"{data_inicio} até {data_fim}",
        "quantidade_registros": len(response["Items"]),
        "dados": response["Items"]
        }

    
@app.get("/dia-mais-quente")
def dia_mais_quente(location: str, data_inicio: str, data_fim: str):
    response = table.query(
        KeyConditionExpression=
        Key("Location").eq(location) &
        Key("Date_Time").between(data_inicio, data_fim)
    )

    items = response["Items"]

    if not items:
        return {"erro": "Nenhum dado encontrado"}
    maior_registro = max(items, key=lambda x: float(x["Temperature_C"]))

    return {
        "cidade": location,
        "periodo": f"{data_inicio} até {data_fim}",
        "dia_mais_quente": maior_registro["Date_Time"],
        "temperatura": float(maior_registro["Temperature_C"])
    }


@app.get("/tendencia-temperatura")
def tendencia(location: str):

    response = table.query(
        KeyConditionExpression=Key("Location").eq(location)
    )

    items = response["Items"]

    if len(items) < 2:
        return {"erro": "Dados insuficientes"}

    temperaturas = [float(i["Temperature_C"]) for i in items]

    tendencia = temperaturas[-1] - temperaturas[0]

    if tendencia > 0:
        status = "aumentando"
    elif tendencia < 0:
        status = "diminuindo"
    else:
        status = "estável"

    return {
        "cidade": location,
        "tendencia": status,
        "variacao": round(tendencia, 2)
    }