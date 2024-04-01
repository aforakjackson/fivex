import sys
import fivempy
from colorama import Fore, Back, Style, init
init()
# Crea una instancia de la clase Server con la dirección IP y el puerto del servidor
server = fivempy.Server("185.230.52.201:30120")  # El puerto predeterminado es 30120
print(Fore.GREEN + 'FiveXpy By Aforak')
# Accede a los atributos disponibles
cuenta = server.get_player_count()
#print(f"IP del servidor: {server.ip}")
print(Fore.WHITE + f"Número de jugadores en línea:" + Fore.GREEN + f" {cuenta}")

# Obtén la lista de jugadores en línea
player_list = server.get_player_list()

# Nombre del jugador que deseas verificar
player_name = input(Fore.WHITE + "Nombre de usuario:") #System [69] / _Fdezz / ^2Shino 웃 / Iker_OO / Hydra ON TOP

# Verifica si el jugador está en línea
is_online = player_name in player_list

# Imprime el resultado
print(f"¿{player_name} está en línea?" + Fore.YELLOW +  f" {is_online}")
# Obtén la lista de todos los jugadores
players = server.get_players()


# Busca al jugador en la lista de jugadores
player_details = next((player for player in players if player['name'] == player_name), None)

# Si el jugador está en línea, muestra sus detalles
if player_details is not None:
    print(Fore.GREEN + "[*]" + Fore.WHITE + " Detalles del jugador:" + Fore.GREEN +  f" {player_name}" + Fore.WHITE + f"{player_details}")
else:
    print(Fore.WHITE + "El jugador" + Fore.YELLOW + f" {player_name}" + Fore.RED +  " no está en línea" + Fore.WHITE + ", mostrando todos los usuarios en línea:")
    print(Fore.GREEN + f"{player_list}")

#INFO SERVER
# Accede al atributo 'info'
info = server.get_info()
print()
# Imprime la información del servidor
print(Fore.WHITE + "Versión del servidor:" + Fore.GREEN + f" {info['version']}")
print()
print(Fore.WHITE + "Variables:" + Fore.GREEN + f" {info['vars']}")
print()
print(Fore.WHITE + "Resources:" + Fore.GREEN + f" {info['resources']}")







