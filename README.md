# Climate Analytics API

API de análise climática desenvolvida com FastAPI e AWS DynamoDB.

Este projeto demonstra a construção de uma API de dados climáticos utilizando arquitetura cloud simples.

## Tecnologias

- Python
- FastAPI
- AWS DynamoDB
- Boto3

## Funcionalidades

Endpoints disponíveis:

GET /clima  
Retorna dados climáticos de uma cidade.

GET /media-temperatura  
Calcula a média de temperatura de uma cidade.

GET /clima-periodo  
Busca registros climáticos em um intervalo de datas.

GET /dia-mais-quente  
Identifica o dia mais quente em um período.

GET /tendencia-temperatura  
Analisa a tendência de temperatura.

## Executar o projeto

Instalar dependências: pip install -r requirements.txt

Executar API: uvicorn main:app --reload

Acessar documentação automática: http://127.0.0.1:8000/docs


## Arquitetura

API construída com FastAPI que consulta dados armazenados no AWS DynamoDB.

## Autor

Henrique Boscoli
 
