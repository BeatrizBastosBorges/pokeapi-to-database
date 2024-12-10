from db_config import get_connection

def initialize_database():
    """Cria a tabela 'pokemons' no banco de dados, se não existir."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemons (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            height INT,
            weight INT
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    initialize_database()

    if __name__ == "__main__":
        try:
            conn = get_connection()
            print("Conexão bem-sucedida!")
            conn.close()
        except Exception as e:
            print(f"Erro na conexão: {e}")
