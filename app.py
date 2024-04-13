from flask import Flask, request, render_template
from user import insert_user, get_users, update_user, delete_user

"""
    Projeto para aprendizado de manipulação do banco de dados usando flask, aprendendo o CRUD
"""

app = Flask(__name__)


@app.route('/insert-form', methods=['GET'])
def insert_html():
    return render_template('insert_form.html')


@app.route('/update-form', methods=['GET'])
def update_html():
    return render_template('update_form.html')


@app.route('/delete-form', methods=['GET'])
def delete_html():
    return render_template('delete_user_form.html')


@app.route('/getAll', methods=['GET'])
def get_all_users():
    users = get_users()
    return render_template('get_users_interface.html', users=users)


@app.route('/insert', methods=['POST'])
def insert():
    name = request.form.get('name')
    insert_user(name)
    return "Usuário inserido com sucesso!"


@app.route('/update', methods=['POST'])
def update():
    old_name = request.form.get('old_name')
    new_name = request.form.get('new_name')
    update_user(old_name, new_name)
    return "User successfully updated"


@app.route('/delete', methods=['POST'])
def delete():
    name = request.form.get('name')
    delete_user(name)
    return "User successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)