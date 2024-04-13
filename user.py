from dbConnect import connection_database


def insert_user(name):
    if not isinstance(name, str):
        raise ValueError("O valor do campo name deve ser uma String")
    connection = connection_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name_user) VALUE (%s)", (name,))
    connection.commit()
    cursor.close()
    connection.close()


def get_users():
    connection = connection_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    return users


def update_user(old_name, new_name):
    connection = connection_database()
    cursor = connection.cursor()
    cursor.execute('UPDATE users SET name_user = %s WHERE name_user = %s', (new_name, old_name))
    cursor.close()
    connection.close()


def delete_user(name):
    connection = connection_database()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM users WHERE name_user = %s', (name,))
    connection.commit()
    cursor.close()
    connection.close()

