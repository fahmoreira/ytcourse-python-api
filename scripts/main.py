from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': "World"}

@app.get('/item/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}

'''
- Section3
Nesse primeiro script foi feito a configuração do ambiente virtual: python.exe -m venv venv
Após isso foi realizado a instalação da primeira dependência (FastAPI): pip install fastapi[all]
E escrito as linhas acima segundo a documentação disponível em: https://fastapi.tiangolo.com/
On Terminal: fastapi.exe dev .\scripts\main.py
'''