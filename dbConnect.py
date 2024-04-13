import mysql.connector


def connection_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test_py"
    )
    return connection
