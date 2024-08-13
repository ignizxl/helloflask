-- Remove existing tables if they exist
DROP TABLE IF EXISTS tb_usuario;
DROP TABLE IF EXISTS tb_produto;
DROP TABLE IF EXISTS tb_categoria;
DROP TABLE IF EXISTS tb_setor;

-- Create tb_usuario table
CREATE TABLE tb_usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL
);

-- Create tb_categoria table
CREATE TABLE tb_categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

-- Create tb_setor table
CREATE TABLE tb_setor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

-- Create tb_produto table
CREATE TABLE tb_produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria_id INTEGER NOT NULL,
    setor_id INTEGER NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES tb_categoria(id),
    FOREIGN KEY (setor_id) REFERENCES tb_setor(id)
);

-- Insert initial data into tb_usuario
INSERT INTO tb_usuario (nome, nascimento)
VALUES ('Administrador', '2024-07-23');
