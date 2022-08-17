# Script fondateur de SQUID 3.0
import os

folder = os.getcwd()

exec(open(folder + "\\library.py").read())

if not os.path.exists(folder + "\\squid_folder"):

    os.makedirs(folder + '\\squid_folder')

    print("Le folder demandé vient d'être créé.")

    os.rmdir(folder + '\\squid_folder')

    print("Le folder demandé a été supprimé avec succès")

else :

    print("Le folder est déjà existant")

    os.rmdir(folder + '\\squid_folder')

    print("Le folder demandé a été supprimé avec succès")



