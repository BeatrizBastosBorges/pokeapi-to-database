from db_config import get_connection

def save_pokemon_to_db(pokemon):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO pokemons (id, name, height, weight)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        height = VALUES(height),
        weight = VALUES(weight)
    """

    data = (pokemon['id'], pokemon['name'], pokemon['height'], pokemon['weight'])

    try:
        cursor.execute(sql, data)
        connection.commit()
    except Exception as e:
        print(f"Erro ao salvar Pokémon {pokemon['name']}: {e}")
    finally:
        cursor.close()
        connection.close()

def update_pokemon_in_db(pokemon):
    """Atualiza os dados de um Pokémon no banco de dados."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""UPDATE pokemons 
                           SET name = %s, height = %s, weight = %s 
                           WHERE id = %s""", 
                           (pokemon['name'], pokemon['height'], pokemon['weight'], pokemon['id']))
        connection.commit()
        print(f"Pokémon {pokemon['name']} atualizado no banco de dados.")
    finally:
        cursor.close()
        connection.close()      