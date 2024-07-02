from typing import Union
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

'''
+ @app.get('/'):
- Este é um decorador que define um endpoint HTTP GET para a raiz da aplicação (o caminho /).
++ def read_root()::
- Define a função read_root que será chamada quando uma requisição GET for feita ao caminho /.
++ return {'Hello': "World"}:
A função retorna um dicionário com a mensagem {'Hello': "World"}. Este será o corpo da resposta JSON enviada ao cliente.

+ ('/')
- Basically the path after the specific domain name of your API.
O endpoint raiz ('/') é o ponto de partida da sua API FastAPI (Ou qlqr outra ferramenta), 
respondendo às requisições feitas para a URL base da aplicação. 
Ele serve como uma forma simples e eficaz de verificar se a API está funcionando corretamente, 
e pode fornecer informações básicas ou mensagens iniciais aos usuários da API.
'''
@app.get('/') 
def read_root():
    return {'Hello': "Welcome"}

@app.get('/posts')
def get_data():
    return {'data': 'Your data has been captured!'}

@app.post('/createdpost')
def create_post(new_post: Post):
    print(new_post.title)
    return {'data': 'new_post'}

# @app.get('/item/{item_id}')
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {'item_id': item_id, 'q': q}

'''
+ Section 3
Nesse primeiro script foi feito a configuração do ambiente virtual: python.exe -m venv venv
Após isso foi realizado a instalação da primeira dependência (FastAPI): pip install fastapi[all]
E escrito as linhas acima segundo a documentação disponível em: https://fastapi.tiangolo.com/
On Terminal: fastapi.exe dev .\scripts\main.py

+ Explicações gerais
++ .get
- Faz parte de vários métodos disponíveis para HTTP. Para saber mais: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods ou https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods

++ Cenário
- Após chamar a função `fastapi.exe dev .\scripts\main.py` qualquer alteração que eu fizer no script
será necessário reiniciá-lo, porém o processo é feito automaticamente, pois o fastapi.exe entende as alterações.

++ Cenário 2
- The order in fact, does matter! So you have to keep that in mind. 
And it can impact the way you API ultimately works.
Quando fazemos a inserção de decoretors para `HTTP Methods iguais` e o mesmo "path" (url) 
o primeiro que estiver no script será realizado, enquanto os subsequentes serão ignorados.
'''