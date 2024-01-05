"""
    Coleta dos tipos de tranferências realizadas nas despesas públicas
"""

# flake8: noqa
import requests as req
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# URL de requisição
URL = "https://api.portaldatransparencia.gov.br/api-de-dados/despesas/tipo-transferencia"

headers: dict = {
    "chave-api-dados": os.getenv("CHAVE-API"),
    "Accept": "application/json",
    "Accept-Charset": "charset=utf-8"
}

# Requisição
response = req.get(URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_excel('tipo_de_transferencia.xlsx')
else:
    print(f'Status code: {response.status_code}')
