import pandas as pd
import pyodbc
import os
from datetime import datetime


#recuperer le nom d'utilisateur 
Username = os.getenv('USERNAME')


#Obtenir la date actuelle et la formatter
current_date = datetime.now().strftime('%Y%m%d')

# Paramètres de connexion à SQL Server
server = 'nom du serveur'
database = 'nom de la data base'
username = 'username'
password = 'password'

# Chaîne de connexion à SQL Server
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connexion à SQL Server via pyodbc
conn = pyodbc.connect(conn_str)


# Requête SQL à exécuter
sql_query = "SELECT * FROM xxxxx"

# Charger les données depuis SQL Server dans un DataFrame pandas
pm = pd.read_sql(sql_query, conn)

# Fermer la connexion à SQL Server
conn.close()

# Chemin vers le fichier CSV de sortie

csv_pm1= f'C:/Users/{Username}/xxxxxxxxxxxxxxxxxxxxxx/PM_{current_date}.csv'
csv_pm2= f'C:/Users/{Username}/xxxxxxxxxxxxxxxxxxx/PM_{current_date}.csv'
csv_pm3= f'//xxxxxxxxxxxxxxxxxxxx/PM_{current_date}.csv'

# Exporter le DataFrame pandas vers un fichier CSV

pm.to_csv(csv_pm1, index=False, encoding='utf-8-sig', sep=';')
pm.to_csv(csv_pm2, index=False, encoding='utf-8-sig', sep=';')
pm.to_csv(csv_pm3, index=False, encoding='utf-8-sig', sep=';')