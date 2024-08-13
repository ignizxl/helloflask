import sqlite3
from Globals import DATABASE_NAME

def initialize_database():
    """Cria e inicializa o banco de dados usando o script SQL fornecido."""
    with sqlite3.connect(DATABASE_NAME) as connection:
        with open('schema.sql') as file:
            script = file.read()
            connection.executescript(script)

if __name__ == "__main__":
    initialize_database()
