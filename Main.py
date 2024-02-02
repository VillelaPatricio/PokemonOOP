from PokémonOOP import *
from ASCII import *
print(".............Welcome to..............")
print(pokemon_title)

try:
    selection = input("Choose your Pokémon \n")
    selection = selection.title()
    my_pokemon = pokemon(str(selection))
    print("You have choosen: " + my_pokemon.name)
    print(my_pokemon.ASCII)
except KeyError:
    raise Abort("Pokemon not found in our databasa")

try:
    selection = input("Choose the Pokémon to battle against \n")
    selection = selection.title()
    enemy_pokemon = pokemon(str(selection))
    print("You'll battle against: " + enemy_pokemon.name)
    print(enemy_pokemon.ASCII)
except KeyError:
    raise Abort("Pokemon not found in our databasa")

print("If you want to: Attack -> Press A")
print("If you want to: Heal -> Press H")
print("If you want to: Special Attack -> Press S")

while enemy_pokemon.life > 0:
    player_choice = input("Press a letter to continue \n")

    if player_choice == "A":
        my_pokemon.attack(enemy_pokemon)
   
    if player_choice == "S":
        my_pokemon.special_attack(enemy_pokemon)

    if player_choice == "H":
        my_pokemon.heal(enemy_pokemon)