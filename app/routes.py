from fastapi import APIRouter
from boto3.dynamodb.conditions import Key
from app.database import get_table

router = APIRouter()
table = get_table()

@router.get("/")
def home():
    return {"message": "API Climática rodando"}

@router.get("/clima")
def buscar_por_local(location: str):
    response = table.query(
        KeyConditionExpression=Key("Location").eq(location)
    )
    return response["Items"]

@router.get("/temperatura/media")
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

@router.get("/clima-periodo")
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

    
@router.get("/temperatura/max")
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


@router.get("/temperatura/tendencia")
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