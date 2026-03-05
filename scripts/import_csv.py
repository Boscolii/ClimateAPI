import boto3
import pandas as pd
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clima_dados')

df = pd.read_csv("weather_data.csv")
df_sample = df.sample(10000)

print("Iniciando importação")

with table.batch_writer() as batch:
    for _, row in df_sample.iterrows():
        batch.put_item(
            Item={
                "Location": str(row["Location"]),
                "Date_Time": str(row["Date_Time"]),
                "Temperature_C": Decimal(str(row["Temperature_C"])),
                "Humidity_pct": Decimal(str(row["Humidity_pct"])),
                "Precipitation_mm": Decimal(str(row["Precipitation_mm"])),
                "Wind_Speed_kmh": Decimal(str(row["Wind_Speed_kmh"]))
            }
        )

print("Importação concluída")