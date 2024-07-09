from typing import Union, Optional
from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None 

'''
++ Para testar os métodos desenvolvidos é necessário a instalação do Postman

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

+ Why calling `posts`
- This is standad convetion fo API's

'''

my_posts = [{"title": "title post 1", "content": "content post 1", "id": 1}, {"title": "favorite colors", 
                                                                              "content": "blue", "id": 2}]

def find_posts(id):
    for p in my_posts:
        if p['id'] == id:
            return p


@app.get('/') 
def root():
    return {'Hello': "Welcome"}

@app.get('/posts')
def get_posts():
    return {'data': my_posts}

# @app.post('/posts')
# def create_post(post: Post):
#     print(post)
#     print(post.model_dump())
#     return {'data': post}

# @app.post('/posts')
# def create_posts(post: Post):
#     print(post)
#     print(post.model_dump())
#     return {'message': post}

@app.post('/posts')
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 9999999)
    my_posts.append(post_dict)
    return {'message': post_dict}

# Retrieving one individual post
# The user will provide us the ID that he want it

@app.get('/posts/{id}') # This is gonna get embbeded in THE URL
def get_post(id: int, response: Response):
    post = find_posts(id)
    print(post)
    if not post:
        response.status_code = 404
    return {'post_detail': post}
    

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

+ How do we actually extract the data that we sent in the body? How do we retrieve that doby data?
- What we can do is within our path operation function we can assign in it some variable.

@app.post('/createposts')
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {'message': 'succesfully created posts'}
-- 
@app.post('/createposts')
def create_post(new_post: Post):
    print(new_post.rating)
    return {'message': 'succesfully created posts'}    

Este trecho irá extrair todos os campos do body, basicamente convertendo em um dicionário python e armazenando 
na variável chamada payLoad

+ Pydantic 
-- Detalhes no README
@app.post('/createposts')
def create_post(new_post: Post):
    print(payLoad)
    return {'message': 'succesfully created posts'}

- Moving Forward
-- We are going to really make use of pydantic models to ensure that the schemas not only receiving data 
from the front end, but also SENDING DATA BACK is all matching up with our organized schema.

+ Até este momento o aprendizado tratou-se de conhecermos o comportamento das funções através do `print` e
execuções de sessão dentro do Postman

+ Podemos manipular o HTTP Status do FastAPI com a biblioteca `Response`

'''