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
sql_query = "SELECT * FROM xxxxxx"

# Charger les données depuis SQL Server dans un DataFrame pandas
asset = pd.read_sql(sql_query, conn)

# Fermer la connexion à SQL Server
conn.close()

# Chemin vers le fichier CSV de sortie

csv_asset1= f'C:/Users/{Username}/xxxxxxxxxxxxx/asset_{current_date}.csv'
csv_asset2= f'C:/Users/{Username}/xxxxxxxxxxxx/asset_{current_date}.csv'
csv_asset3= f'//xxxxxxxxxxxxxxx/asset_{current_date}.csv'


# Exporter le DataFrame pandas vers un fichier CSV

asset.to_csv(csv_asset1, index=False, encoding='utf-8-sig', sep=';')
asset.to_csv(csv_asset2, index=False, encoding='utf-8-sig', sep=';')
asset.to_csv(csv_asset3, index=False, encoding='utf-8-sig', sep=';')
