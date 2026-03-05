import boto3

dynamodb = boto3.resource("dynamodb")

def get_table():
    return dynamodb.Table("clima_dados")