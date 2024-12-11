import time
from initialize_database import initialize_database
from pokeapi_client import fetch_pokemon_data, get_pokemon_from_db
from save_pokemon import save_pokemon_to_db, update_pokemon_in_db

def main():
    initialize_database()

    pokemon_id = 1
    while True:
        print(f"Buscando Pokémon ID {pokemon_id}...")

        data = None
        while not data:
            data = fetch_pokemon_data(pokemon_id)
            if not data:
                print(f"Erro ao buscar Pokémon ID {pokemon_id}")
                print(f"Aguardando 5 segundos antes de tentar novamente...")
                time.sleep(5)

        pokemon = {
            'id': data['id'],
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight']
        }

        existing_pokemon = get_pokemon_from_db(pokemon_id)
        if existing_pokemon:
            if (pokemon['name'] != existing_pokemon['name'] or
                pokemon['height'] != existing_pokemon['height'] or
                pokemon['weight'] != existing_pokemon['weight']):
                update_pokemon_in_db(pokemon)
            else:
                print(f"Pokémon ID {pokemon_id} já está atualizado.")
        else:
            save_pokemon_to_db(pokemon)
            print(f"Pokémon {pokemon['name']} salvo com sucesso!")

        pokemon_id += 1

        print("Aguardando 5 segundos antes da próxima execução...")
        time.sleep(5)

if __name__ == "__main__":
    main()