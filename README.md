# Python API Development Course

Estou acompanhandoo curso disponibilizado pela freeCodeAcademy.org e pode ser acessado através do link abaixo.
Tendo em vista que ele foi gravado a quase 2 anos estou realizado anotações gerais no ReadMe e diretamente nos scripts.
Para fins de acompanhamento de progressão
vou colocar uma flag chamado "iniciado" e "finalizado" para ver quanto tempo levou até a conclusão.
Inicie o curso dia 27/06 e a data de previsão de término, segundo algumas métricas que coloquei no ChatGPT, é 
dia 5/9/2024.

https://youtu.be/0sOvCWFmrtA?si=VAtGGNFm5cKzqUhZ


Em um dos comentários eu pude notar que um colega fez a section, onde:

### Section 1: Introduction
1. Course Project
- Featured API:
*Authentication*
*CRUD Operation*
*Validation*
*Documentaion*
- Tools
*Alembic* to allow us to make incremental changes to our database schema to track changes
*Postman* to construct HTTP package
*FastAPI* one featured that it uses is auto documentation functionality
*Postgres*
Python *SQL Alchemy* 
- Testing
- Deployment
*Ubuntu*
*Heroku*
*Docker*
*Cloud Provider*
- CI/CD

2. Course Intro
3. Course Project Overview 06:33

### Section 2: Setup & installation
4. Mac Python Installation 11:22
5. Mac VS Code install and setup 13:15
6. Windows Python Installation 16:37
7. Windows VS Code install and setup  18:30
8. Python virtual environment Basics 22:11
9. Virtual environment on windows 24:35
10. Virtual environment on Mac 28:56

### Section 3: FastAPI
- Iniciado: 27/06/24
11. Install dependencies w/ pip 34:17
12. Starting Fast API 36:21 -Continuar deste ponto
13. Path operations 39:23
![alt text](/img/MethodPathFunction.png)

14. Path Operation Order(yes it matters) 51:08
15. Intro to Postman 53:22
- It's just a tool that allows us to construct our own HTTP request. So we get to specify the individual fields of an HTTP request. What is the HTTP method? What's the URL? What are the headers that we're going to apply? What's the body? What kind of data is that going to carry?Is it going to have any authorization headers? 

16. HTTP Post Requests 57:34
![alt text](/img/HTTPvsPOST.png)

### HTTP GET VS POST Request
*HTTP GET Request*

16.1. Envio de Dados:
- A linha verde representa a requisição GET.
Em uma requisição GET, os dados são enviados como parte da URL. Isso significa que você pode ver os dados na barra de endereços do navegador.

- A requisição GET é geralmente usada para solicitar dados de um servidor. Por exemplo, acessar uma página da web ou buscar informações de uma API.

*HTTP POST Request*

16.2. Envio de Dados:
- A linha roxa representa a requisição POST.
Em uma requisição POST, os dados são enviados no corpo (body) da requisição HTTP, não na URL. Isso permite o envio de dados maiores e mais complexos, como formulários ou arquivos.

- A requisição POST é geralmente usada para enviar dados ao servidor para criação ou atualização. Por exemplo, enviar um formulário de cadastro ou fazer login em um site.
Recebimento de Dados:

- A API processa a requisição POST e envia uma resposta de volta ao cliente, também representada pela linha roxa.

- Os dados retornados não são visíveis na URL, o que oferece maior segurança e flexibilidade.

Comparação entre GET e POST

++ Visibilidade dos Dados:
GET: Dados são visíveis na URL.
POST: Dados são enviados no corpo da requisição, não visíveis na URL.

++ Uso Típico:
GET: Recuperar dados (ex.: acessar uma página da web, buscar informações).
POST: Enviar dados (ex.: enviar formulários, criar/atualizar recursos).

++ Limitações de Tamanho:
GET: Limitado pelo tamanho da URL.
POST: Pode enviar grandes volumes de dados no corpo da requisição.

++ Segurança:
GET: Menos seguro, pois os dados são expostos na URL.
POST: Mais seguro para dados sensíveis, já que os dados são enviados no corpo da requisição.

17. Schema Validation with Pydantic 1:07:29
18. CRUD Operations 1:22:45
![alt text](/img/CRUD.png)

How do I ensure that the user is sending what I wnat?
What ir the user sends a blank title?
How can we validate that the data the user sends is actually valid?
What we want to do is we want to force the user into a schema that we can expect?

`Pydantic` é uma poderosa ferramenta para validação e manipulação de dados no FastAPI. Ele permite definir modelos de dados de forma clara e garantir que os dados recebidos sejam válidos, facilitando a criação de APIs robustas e seguras.
`https://docs.pydantic.dev/latest/`
![alt text](/img/Why%20we%20need%20schema.png)

19. storing posts in Array 1:29:44
20. creating posts 1:34:06
21. Postman Collections & saving requests 1:38:15
Anytime we have a path parameter, it's always going to be returned as a string, even
if it represents an integer or a number, we always have to manually convert it ourselves.
22. Retrieve One Post 1:39:47
23. Path order Matters 1:48:10
We have to be careful when you structure our API, especially with paths and URLs. We must to make sure that we don't run into this type of issue.
Por exemplo:
import ...

@app.get('/posts/{id}')

@app.get('posts/latest')

Vai dar erro, pois o quando se trabalha com `path parameters` é necessário order os métodos corretamente,
ou seja, a chamada de /latest vem primeiro que /{id}

24. Changing response Status Codes 1:52:46
`https://developer.mozilla.org/en-US/docs/Web/HTTP/Status`

`from fastapi import status`
![alt text](/img/import_fastapi_status.png)

`HTTP 201 Creating`

Remember, anytime we create an entity based off of that documentation, we shoud send a 201
![alt text](/img/before_config_postcreate.png)

To fix this we need to add in decorator the parameter below:
*@app.post('/posts', status_code=status.HTTP_201_CREATED)*
![alt text](/img/after_config_postcreate.png)

25. Deleting Posts 2:01:49
Aqui puder pude ser exposto ao comportamento da API na hora de deletar uma determinada posição da lista
"my_posts". 
-Lembrando que o cenário é apenas para introduzir ao comportamento da biblioteca

Lidando com `TypeError: 'NoneType' object cannot be interpreted as an integer`
Este erro é quando colocamos um *id* inexistente basta colocar um condicional de status excpecion "simples".

26. Updating Posts 2:10:31
`@app.put('/posts/{id}')`
Usou-se parte da estrutura de criação de posts, como a classe e a estrutura de busca utilizado no *decorator* de Delete, porém desenvolvido uma nova lógica para inserção dos novos dados, ou seja, UPDATE da posição *id* 
escolhido.

27. Automatic Documentation 2:18:02
*Fast API automatically generates the documentation based off of the path operations that you've defined.*
`http://127.0.0.1:8000/docs` - Swagger UI
![alt text](/img/fastapi_docs.png)

`http://127.0.0.1:8000/redoc` - REDOC
![alt text](/img/fastapi_redoc.png)

28. Python packages 2:21:34

### Section 4: Databases
29. Database Intro 2:24:11
30. Postgres Windows Install 2:28:54
31. Postgres Mac Install 2:31:28
32. Database Schema & Tables 2:34:26
33. Managing Postgres with PgAdmin GUI 2:44:35
34. Your first SQL Query 3:12:10
35. Filter results with "where" keyword 3:19:43
36. SQL Operators 3:22:55
37. IN Keyword 3:26:38
38. Pattern matching with LIKE keyword 3:28:07
39. Ordering Results 3:31:59
40. LIMIT & OFFSET 3:36:27
41. Inserting Data 3:39:21
42. Deleting Data 3:47:16
43. Updating Data 3:50:11

### Section 5: Python + Raw SQL
44. Setup App Database 3:53:48
45. Connecting to database w/ Python 3:58:21
46. Retrieving Posts 4:08:00
47. Creating Post 4:11:53
48. Get One Post 4:19:18
49. Delete Post 4:24:12
50. Update Post 4:26:31

### Section 6: ORMs
51. ORM intro 4:31:18
52. SQLALCHEMY setup 4:35:33
53. Adding CreatedAt Column 4:55:25
54. Get All Posts 5:00:59
55. Create Posts 5:07:55
56. Get Post by ID 5:15:50
57. Delete Post 5:19:50
58. Update Post 5:22:31

### Section 7: Pydantic Models
59. Pydantic vs ORM Models 5:28:21
60. Pydantic Models Deep Dive 5:32:21
61. Response Model 5:38:57

### Section 8: Authentication & Users
62. Creating Users Table 5:50:08
63. User Registration Path Operation 5:54:50
64. Hashing User Passwords 6:03:27
65. Refractor Hashing Logic 6:08:49
66. Get User by ID 6:10:32
67. FastAPI Routers 6:17:13
68. Router Prefix 6:27:34
69. Router Tags 6:30:31
70. JWT Token Basics 6:32:49
71. Login Process   6:47:03
72. Creating a Token 7:00:44
73. OAuth2 PasswordRequestForm 7:09:58
74. Verify user is Logged In 7:13:23
75. Fixing Bugs 7:25:21
76. Protecting Routes 7:27:59
77. Test Expired Token 7:36:17
78. Fetching User in Protected Routes 7:38:13
79. Postman advanced Features 7:42:44

### Section 9: Relationships
80. SQL Relationship Basics 7:50:33
81. Postgres Foreign Keys 7:54:59
82. SQLAlchemy Foreign Keys 8:07:20
83. Update Post Schema to include User 8:13:40
84. Assigning Owner id when creating new post 8:17:59
85. Delete and Update only your own posts 8:21:01
86. Only Retrieving Logged in User's posts 8:27:48
87. Sqlalchemy Relationships 8:33:37
88. Query Parameters 8:38:32
89. Cleanup our main.py file 8:50:46
90. Environment Variables 8:53:53

### Section 10: Vote/Like System
91. Vote/Like Theory 9:21:20
92. Votes Table 9:26:36
93. Votes Sqlalchemy 9:31:33
94. Votes Route 9:34:11
95. SQL Joins 9:52:31
96. Joins in SqlAlchemy 10:15:26
97. Get One Post with Joins 10:28:21

### Section 11: Database Migration w/ Alembic
98. What is a database migration tool 10:30:18
99. Alembic Setup 10:33:45
100. Alembic First Revision 
101. Alembic Rollback database Schema 
102. Alembic finishing up the rest of the schema 
103. Disable SqlAlchemy create Engine 11:13:50

### Section 12: Pre Deployment Checklist
104. What is CORS????? 11:14:28
105. Git PreReqs 11:23:38
106. Git Install 11:27:40
107. Github 11:29:23

### Section 13: Deployment Heroku
108. Heroku intro  11:34:39
109. Create Heroku App 11:35:40
110. Heroku procfile 11:40:21
111. Adding a Postgres database 11:44:59
112. Environment Variables in Heroku 11:48:42
113. Alembic migrations on Heroku Postgres instance 11:58:59
114. Pushing changed to production 12:02:52

### Section 14: Deployment Ubuntu
115. Create an Ubuntu VM 12:05:04
116. Update packages 12:08:04
117. Install Python 12:10:47
118. Install Postgres & setup password 12:12:21
119. Postgres Config 12:17:28
120. Create new user and setup python environment 12:24:50
121. Environment Variables 12:34:06
122. Alembic migrations on production database 12:42:24
123. Gunicorn 12:45:57
124. Creating a Systemd service 12:54:12
125. NGINX 13:04:45
126. Setting up Domain name 13:10:45
127. SSL/HTTPS 13:15:19
128. NGINX enable 13:19:31
129. Firewall 13:20:06
130. Pushing code changes to Production 13:23:47

### Section 15: Docker
131. Dockerfile 13:26:09
132. Docker Compose 13:38:39
133. Postgres Container 13:48:34
134. Bind Mounts 13:56:22
135. Dockerhub 14:03:39
136. Production vs Development 14:08:08

### Section 16: Testing
137. Testing Intro 14:14:51
138. Writing your first test 14:17:19
139. The -s & -v flags 14:30:22
140. Testing more functions 14:31:44
141. Parametrize 14:35:29
142. Testing Classes 14:40:21
143. Fixtures 14:48:37
144. Combining Fixtures + Parametrize 14:55:40
145. Testing Exceptions 14:59:13
146. FastAPI TestClient 15:06:07
147. Pytest flags 15:14:26
148. Test create user 15:17:31
149. Setup testing database 15:25:23
150. Create & destroy database after each test 15:36:47
151. More Fixtures to handle database interaction 15:44:18
152. Trailing slashes in path 15:50:35
153. Fixture scope 15:53:12
154. Test user fixture 16:07:50
155. Test/validate token 16:14:40
156. Conftest.py 16:18:59
157. Failed login test 16:22:09
158. Get all posts test 16:28:28
159. Posts fixture to create test posts 16:29:34
160. Unauthorized Get Posts test 16:51:33
161. Get one post test 16:55:16
162. Create post test 16:59:19
163. Delete post test 17:08:05
164. Update post 17:15:17
165. Voting tests 17:22:09

### Section 17: CI/CD pipeline
166. CI/CD intro 17:34:15
167. Github Actions 17:43:29
168. Creating Jobs 17:49:32
169. Setup python/dependencies/pytest 17:57:38
170. Environment variables 18:06:14
171. Github Secrets 18:11:19
172. Testing database 18:18:14
173. Building Docker images 18:23:42
174. Deploy to Heroku 18:34:33
175. Failing tests in pipeline 18:49:10
176. Deploy to Ubuntu 18:52:18