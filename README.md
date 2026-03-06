# Climate Analytics API

API desenvolvida em Python com FastAPI para análise e consulta de dados climáticos.
O projeto foi containerizado com Docker e implantado em uma instância AWS EC2, simulando uma arquitetura simples de backend em nuvem.

## Objetivo

Este projeto foi criado como prática de desenvolvimento backend e computação em nuvem reforçando:

* criação de APIs modernas
* containerização com Docker
* deploy em infraestrutura cloud
* integração com serviços da AWS

## Tecnologias utilizadas

* Python 3.11
* FastAPI
* Uvicorn
* Docker
* AWS EC2
* Boto3
* DynamoDB

## Rodando com Docker

### Build da imagem

```
docker build -t climate-api .
```

### Executar container

```
docker run -d -p 8000:8000 climate-api
```

A API estará disponível em:

```
http://localhost:8000
```

### AWS Demo

A API também está rodando em uma instância na AWS EC2:

http://54.207.66.63:8000/docs
 
Este servidor está hospedado em uma instância EC2 de teste e pode ficar indisponível caso a instância esteja desligada.

## Exemplo de requisição

```
GET /climate
```

Resposta esperada:

```
{
  "temperature": 25,
  "humidity": 70
}
```

## Deploy

O projeto foi implantado em uma instância AWS EC2, utilizando Docker para execução do container da API e integração com DynamoDB através da biblioteca boto3.

## Autor

Henrique Nogueira Boscoli
