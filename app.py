import sqlite3
from flask import Flask, request, jsonify
from Globals import DATABASE_NAME

app = Flask(__name__)

def get_db_connection():
    """Cria uma conexão com o banco de dados."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
    except sqlite3.Error:
        print('Não foi possível conectar ao banco de dados.')
    return conn

@app.route("/")
def index():
    """Retorna a versão da API."""
    return jsonify({"versao": 1}), 200

def get_usuarios():
    """Obtém todos os usuários do banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    resultset = cursor.execute('SELECT * FROM tb_usuario').fetchall()
    usuarios = [
        {
            "id": linha[0],
            "nome": linha[1],
            "nascimento": linha[2]
        }
        for linha in resultset
    ]
    conn.close()
    return usuarios

def set_usuario(data):
    """Cria um novo usuário no banco de dados."""
    nome = data.get('nome')
    nascimento = data.get('nascimento')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO tb_usuario (nome, nascimento) VALUES (?, ?)', 
        (nome, nascimento)
    )
    conn.commit()
    id = cursor.lastrowid
    data['id'] = id
    conn.close()
    return data

@app.route("/usuarios", methods=['GET', 'POST'])
def usuarios():
    """Gerencia listagem e criação de usuários."""
    if request.method == 'GET':
        usuarios = get_usuarios()
        return jsonify(usuarios), 200
    elif request.method == 'POST':
        data = request.json
        data = set_usuario(data)
        return jsonify(data), 201

def get_usuario_by_id(user_id):
    """Obtém um usuário específico pelo ID."""
    usuario_dict = None
    conn = get_db_connection()
    cursor = conn.cursor()
    linha = cursor.execute(
        'SELECT * FROM tb_usuario WHERE id = ?', 
        (user_id,)
    ).fetchone()
    if linha:
        usuario_dict = {
            "id": linha[0],
            "nome": linha[1],
            "nascimento": linha[2]
        }
    conn.close()
    return usuario_dict

def update_usuario(user_id, data):
    """Atualiza os dados de um usuário existente."""
    nome = data.get('nome')
    nascimento = data.get('nascimento')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE tb_usuario SET nome = ?, nascimento = ? WHERE id = ?', 
        (nome, nascimento, user_id)
    )
    conn.commit()
    row_update = cursor.rowcount
    conn.close()
    return row_update

@app.route("/usuarios/<int:user_id>", methods=['GET', 'DELETE', 'PUT'])
def usuario(user_id):
    """Gerencia um usuário específico com base no ID."""
    if request.method == 'GET':
        usuario = get_usuario_by_id(user_id)
        if usuario:
            return jsonify(usuario), 200
        else:
            return jsonify({}), 404
    elif request.method == 'PUT':
        data = request.json
        row_update = update_usuario(user_id, data)
        if row_update:
            return jsonify(data), 200
        else:
            return jsonify(data), 304
    elif request.method == 'DELETE':
        pass
        return '', 405

if __name__ == "__main__":
    app.run(debug=True)
