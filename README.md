# CRUD básico na Micro Framework Flask

Estou iniciando meus estudos em flask, uma micro framework de python, ou seja algo não tão robusto, com maior flexibilidade na escolha de bibliotecas para desenvolvimento, usado para desenvolvimento web.

Neste projeto adicionei apenas as funcionalidades básicas CRUD para teste do meu conhecimento.

**Rota "/insert-form" renderiza um formulário para inserir um novo usuário, ao clicar em "submit" ele chama a função de inserir um novo usuário:**

Essa é a interação de adicionar um novo usuário:

![image](https://github.com/matheusaugusto98521/basic-crud-flask/assets/116231786/b413e725-fdfd-415d-8e60-4f8f72684b61)


**Resultado:**

![image](https://github.com/matheusaugusto98521/basic-crud-flask/assets/116231786/5c3e11f7-db94-4385-b4db-5ee0fd1ecb6c)



**Rota "/getAll' Exibi todos os usuários criados:**

![Captura de tela 2024-04-13 202453](https://github.com/matheusaugusto98521/basic-crud-flask/assets/116231786/4e4ba968-fa18-4da3-ad60-53528ccfa94f)


**Rota "/update-form" me permite trocar o nome de um usuário existente por outro nome, quando clico em "submit" ele chama o serviço de atualizar o nome e executa isso:**

Essa é a interação de trocar o nome:

![image](https://github.com/matheusaugusto98521/basic-crud-flask/assets/116231786/b9412413-fa70-4735-9773-e5fbcedb3f3b)


**Esse foi o resultado:**

![image](https://github.com/matheusaugusto98521/basic-crud-flask/assets/116231786/9225c168-7eca-48c8-b5d2-562053d70746)


**Rota "/delete-form" me permite colocar o nome do usuário a ser deletado, quando clico em "submit" ele chama o método de deletar:**

Essa é a interação de escolher o nome a ser deletado:


![image](https://github.com/matheusaugusto98521/basic-crud-flask/assets/116231786/bd658709-3a4c-44c0-b5cb-4a82f476901e)


**Resultado:**


![image](https://github.com/matheusaugusto98521/basic-crud-flask/assets/116231786/2b1e829b-e866-4a90-ad27-7d2f3b52695a)


**Desenvolvi em um servidor local mesmo somente para testes, usando o MySQL como banco de dados, utilizei a biblioteca _mysql.connector_ para realizar a conexão, espero que tenham gostado**





