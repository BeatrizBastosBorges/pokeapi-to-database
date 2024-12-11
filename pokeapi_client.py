import requests
import time
from db_config import get_connection

def fetch_pokemon_data(pokemon_id, delay=5):
    """Obtém os dados de um Pokémon específico pela API, com tentativa de reenvio em caso de erro."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    while True:
        try:
            print(f"Tentando buscar Pokémon ID {pokemon_id}...")
            response = requests.get(url)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erro ao buscar o Pokémon {pokemon_id}: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Erro ao tentar se conectar à API para o Pokémon {pokemon_id}: {e}")
            print(f"Aguardando {delay} segundos antes de tentar novamente...")
            time.sleep(delay)

def get_pokemon_from_db(pokemon_id):
    """Obtém os dados de um Pokémon do banco de dados."""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM pokemons WHERE id = %s", (pokemon_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()