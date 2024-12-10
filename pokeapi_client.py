import requests

def fetch_pokemon_data(pokemon_id):
    """Obtém os dados de um Pokémon específico pela API."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar o Pokémon {pokemon_id}: {response.status_code}")
        return None