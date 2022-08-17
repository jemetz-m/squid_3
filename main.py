# Script fondateur de SQUID 3.0
import os

folder = os.getcwd()

if os.path.exists(folder + '\\squid_folder') == False :
    print("Le folder demandé n'existe pas.")
else :
    print("Le folder est déjà existant")



