from db_config import get_connection

def initialize_database():
    """Cria a tabela 'pokemons' no banco de dados, se não existir."""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("SHOW TABLES LIKE 'pokemons'")
    result = cursor.fetchone()

    if result:
        print("A tabela 'pokemons' já existe no banco de dados.")
    else:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INT PRIMARY KEY,
                name VARCHAR(255),
                height INT,
                weight INT
            )
        """)
        connection.commit()
        print("Tabela 'pokemons' criada com sucesso!")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    initialize_database()
