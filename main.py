import time
from pokeapi_client import fetch_pokemon_data
from save_pokemon import save_pokemon_to_db
from db_config import get_connection

def pokemon_exists(pokemon_id):
    """Verifica se o Pokémon já existe no banco de dados."""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM pokemons WHERE id = %s", (pokemon_id,))
        return cursor.fetchone()[0] > 0
    finally:
        cursor.close()
        connection.close()

def main():
    while True:
        for pokemon_id in range(1, 152):
            print(f"Buscando Pokémon ID {pokemon_id}...")

            if pokemon_exists(pokemon_id):
                print(f"Pokémon ID {pokemon_id} já existe no banco de dados.")
                continue

            data = fetch_pokemon_data(pokemon_id)
            if data:
                pokemon = {
                    'id': data['id'],
                    'name': data['name'],
                    'height': data['height'],
                    'weight': data['weight']
                }
                save_pokemon_to_db(pokemon)
                print(f"Pokémon {pokemon['name']} salvo com sucesso!")

        print("Aguardando 30 segundos para a próxima execução...")
        time.sleep(30)

if __name__ == "__main__":
    main()