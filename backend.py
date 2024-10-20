import sqlite3

def get_db_connection():
    """Estabelece uma conexão com o banco de dados."""
    conn = sqlite3.connect('cadastro_usuarios.db')
    return conn

def adicionar_usuario(nome, email, telefone, nota):
    """Adiciona um novo usuário ao banco de dados."""
    if nome == "" or email == "" or telefone == "" or nota == "":
        return "Por favor, preencha todos os campos."

    # Verificar se a nota está dentro do intervalo de 0 a 10
    try:
        nota_float = float(nota)
        if nota_float < 0 or nota_float > 10:
            return "A nota deve ser um número entre 0 e 10."
    except ValueError:
        return "A nota deve ser um número."

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, telefone, nota) VALUES (?, ?, ?, ?)", 
                       (nome, email, telefone, nota))
        conn.commit()
        conn.close()
        return "Usuário cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        return "E-mail já cadastrado."

def listar_usuarios():
    """Lista todos os usuários cadastrados no banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, email, telefone, nota FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def inicializar_banco():
    """Cria o banco de dados e a tabela de usuários, se não existir."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone TEXT NOT NULL,
        nota REAL NOT NULL CHECK(nota >= 0 AND nota <= 10)
    )
    ''')
    conn.commit()
    conn.close()
