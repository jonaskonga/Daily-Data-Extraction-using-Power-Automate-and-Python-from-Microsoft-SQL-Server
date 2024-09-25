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
sql_query = "SELECT RELSEQUENCENUM,ASSETRELATIONNUM,SOURCEASSETNUM,TARGETASSETNUM FROM xxxxxxx"

# Charger les données depuis SQL Server dans un DataFrame pandas
assetlocrelation = pd.read_sql(sql_query, conn)

# Fermer la connexion à SQL Server
conn.close()

# Chemin vers le fichier CSV de sortie


csv_assetlocrelation1= f'C:/Users/{Username}/xxxxxxxxxxxxxxxxxxxxx/ASSETLOCRELATION_{current_date}.csv'
csv_assetlocrelation2= f'C:/Users/{Username}/xxxxxxxxxxxxxxxxx/ASSETLOCRELATION_{current_date}.csv'
csv_assetlocrelation3= f'//xxxxxxxxxxxxxxxxxxxx/ASSETLOCRELATION_{current_date}.csv'


# Exporter le DataFrame pandas vers un fichier CSV

assetlocrelation.to_csv(csv_assetlocrelation1, index=False, encoding='utf-8-sig', sep=';')
assetlocrelation.to_csv(csv_assetlocrelation2, index=False, encoding='utf-8-sig', sep=';')
assetlocrelation.to_csv(csv_assetlocrelation3, index=False, encoding='utf-8-sig', sep=';')