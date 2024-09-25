import subprocess
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd


#recuperation des variables du système

user  = os.getlogin()


# Répertoire contenant les scripts
repertoire_scripts = r'\\xxxxxxxxxxxxxxxx\Python Scripts'

# Répertoire contenant la sauvegarde des fichiers extraits du jour 

repertoire_stockage = r'\\xxxxxxxxxxxxxxxxxxxx\Export Emat'

# Répertoire pour la sauvergarde du fichier variable.txt 

repertoire_alerte = f'C:/Users/{user}/xxxxxx/xxxxxxxx/Alertes_Python'



Taille_j=[]
matrice_name_j=[]


# parcourir tous les fichier jour j-1 dans Export emat, recuperer la taille puis les supprimer#
    
for f in os.listdir(repertoire_stockage):
    fichier=os.path.join(repertoire_stockage,f)
    if os.path.isfile(fichier):
     if f[-3:] != "dat":
        Taille_j.append(round(os.path.getsize(fichier)/1024))
        matrice_name_j.append(f[:-12])
     os.remove(fichier)

    
# creer un fichier pour stocker nos listes

file = open(f"{repertoire_alerte}/variables.txt","w+")

file.write(f"Taille_j={Taille_j} \n")
file.write(f"matrice_name_j={matrice_name_j} \n")
#file.write(f"nbre_ligne_j={nbre_ligne_j} \n")

file.close()

# Liste des scripts à exécuter avec les chemins complets
scripts = [os.path.join(repertoire_scripts, f'script{i}.py') for i in range(1, 28)]

# Fonction pour exécuter un script

def execute_script(script):
    result = subprocess.run(['python', script], capture_output=True, text=True)
    return script, result

# Exécution des scripts en parallèle avec la fonction ThreadPoolExecutor()


with ThreadPoolExecutor() as executor:
    futures = {executor.submit(execute_script, script): script for script in scripts}
    for future in as_completed(futures):
        script, result = future.result()
        print(f"Exécution de {script}:")
        print(f"Code de retour: {result.returncode}")
        print("fichier 100 %")
        # print(f"Sortie d'erreur:\n{result.stderr}")

        if result.returncode != 0:
            print(f"Le script {script} a échoué mais l'exécution continue.")