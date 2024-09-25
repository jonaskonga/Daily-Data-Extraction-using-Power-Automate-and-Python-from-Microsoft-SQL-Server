import os,ast,pandas as pd

#recuperation des variables du système

user  = os.getlogin()


# Répertoire contenant la sauvegarde des fichiers

repertoire_stockage = r'\\xxxxxxxxxx\Export Emat'

repertoire_alerte = r'\\xxxxx\xxxxxxxxxxxx\Alertes_Extraction_Python'

repertoire_sauvegarde = f'C:/Users/{user}/xxxxxxx/xxxxxxxxxxx/Alertes_Python'




#Definition des variables

Taille_j1=[]
matrice_name_j1=[]
nom_complet=[]


#Parcourir tous les fichier du jour j dans Export emat, recuperer la taille puis stocker les noms#

for f in os.listdir(repertoire_stockage):
   fichier=os.path.join(repertoire_stockage,f)
   
   if os.path.isfile(fichier):
     if f[-3:] != "dat":
           Taille_j1.append(round(os.path.getsize(fichier)/1024))
           matrice_name_j1.append(f[:-12])
           nom_complet.append(f)



# Lire les fichiers variables.txt pour recuperer nos listes stockées 

file = open(f"{repertoire_sauvegarde}/variables.txt","r")

contenu = file.read()

file.close()

# decoupage en plusieurs lignes

lignes = contenu.splitlines()


# Récuperation de chaque ligne

numero_ligne = 0
for ligne in lignes:
    numero_ligne += 1
    if numero_ligne == 1:
        ligne1=ligne
    else:
        ligne2 = ligne

# spliter les variables pour recuperer les listes 

T1,Taille_j =ligne1.split('=',1)
m1,matrice_name_j = ligne2.split('=',1)


# Transformation des  listes en objet python

Taille_j =ast.literal_eval(Taille_j )
matrice_name_j = ast.literal_eval(matrice_name_j )
#os.remove(f"{repertoire_sauvegarde}/variables.txt")


# création des fichiers de notification

Taille_j_modif = Taille_j.copy()
matrice_name_j_modif = matrice_name_j.copy()
matrice_index = []
matrice_index_j = []
matrice_index_j1 = []
matrice_index_mod = []
resultat = []    
manquant = []
aujourdhui = []
hier = []
cas = 0
n = len(Taille_j)
n_1= len(Taille_j1)


    

# 1er cas : moins de fichier au jour j par rapport au jour j-1 mais aucun probleme avec la taille des fichiers en kilo-octet

if len(Taille_j1) < len(Taille_j):

 cas=1
 for element in matrice_name_j:
    if element not in matrice_name_j1:
        manquant.append(element)
        matrice_index.append(matrice_name_j.index(element))
        matrice_name_j_modif.remove(element)
        
    
 for i in  matrice_index: 
   for j in Taille_j_modif:
     if Taille_j_modif.index(j)==i:
           Taille_j_modif.remove(j)
         
         
# 2er cas : moins de fichier au jour j par rapport au jour j-1 avec en plus  un probleme avec la taille des fichiers  en kilo-octet   
  
  
 if len(Taille_j_modif) == len(Taille_j1):
 
# ne pas tenir compte du fichier  WFTransaction dans la verification  de la taille "
    #matrice_name_j
    for wtf in matrice_name_j:
     if wtf[:13]=="WFTransaction":
        index = matrice_name_j.index(wtf)
        matrice_name_j.remove(wtf)
        
    for wtf in Taille_j:
     if index == Taille_j.index(wtf):
        Taille_j.remove(wtf)
        
    #matrice_name_j1
       
    for wtf in matrice_name_j1:
     if wtf[:13]=="WFTransaction":
       index = matrice_name_j1.index(wtf)
       matrice_name_j1.remove(wtf)
      
    for wtf in Taille_j1:
     if index == Taille_j1.index(wtf):
        Taille_j1.remove(wtf)
        
    #matrice_name_j_modif
    
    for wtf in matrice_name_j_modif:
     if wtf[:13]=="WFTransaction":
       index = matrice_name_j_modif.index(wtf)
       matrice_name_j_modif.remove(wtf)
      
    for wtf in Taille_j_modif:
     if index == Taille_j_modif.index(wtf):
        Taille_j_modif.remove(wtf)
  
    
    for element in range(len(Taille_j1)):
        if (Taille_j1[element]) <= (0.99*Taille_j_modif[element]):
           cas = 2
           resultat.append(matrice_name_j_modif[element])
           aujourdhui.append(Taille_j1[element])
           hier.append(Taille_j_modif[element])
   
    

# 3er cas : la taile des fichiers a diminué en kilo-octet mais aucun problème avec le nombre des fichiers

elif len(Taille_j) == len(Taille_j1):

# ne pas tenir compte du fichier  WFTransaction dans la verification  de la taille "
    #matrice_name_j
    for wtf in matrice_name_j:
     if wtf[:13]=="WFTransaction":
        index = matrice_name_j.index(wtf)
        matrice_name_j.remove(wtf)
        
    for wtf in Taille_j:
     if index == Taille_j.index(wtf):
        Taille_j.remove(wtf)
        
    #matrice_name_j1   
    for wtf in matrice_name_j1:
     if wtf[:13]=="WFTransaction":
       index = matrice_name_j1.index(wtf)
       matrice_name_j1.remove(wtf)
      
    for wtf in Taille_j1:
     if index == Taille_j1.index(wtf):
        Taille_j1.remove(wtf)
        
    for element in range(len(Taille_j)):
        if (Taille_j1[element]) <= (0.99*Taille_j[element]):
            cas = 3
            resultat.append(matrice_name_j[element])
            aujourdhui.append(Taille_j1[element])
            hier.append(Taille_j[element])
            
# Creation d'un fichier 'ALERTE' en cas de problème dans le repertoire Sauvegarde 
   

f= open(f"{repertoire_sauvegarde}/ALERTE.txt","w+")

if cas == 1:
    f.write(f"Bonjour, Il se pourrait que l'extraction soit interrompu car le nombre de fichier extrait aujourd'hui({len(Taille_j1)}) est inferieur par rapport  au nombre d'hier({len(Taille_j)}). Voici le fichier manquant: \n")
    for i in range(len(manquant)):
  
        f.write(f"{manquant[i]}, \n")
        
elif cas == 2 :
    f.write(f"Bonjour, Il se pourrait que l'extraction soit interrompu car le nombre de fichier extrait aujourd'hui({len(Taille_j1)}) est inferieur par rapport  au nombre d'hier({len(Taille_j)}). Voici le fichier manquant: \n")
    for i in range(len(manquant)):
  
        f.write(f"{manquant[i]}, \n")
    f.write(".Voici d'autres problèmes rencontrés: \n")
    for i in range(len(resultat)):
  
        f.write(f"=)la taille de {resultat[i]} est de {aujourdhui[i]}ko aujourd'hui alors qu'hier il était de {hier[i]}ko \n")


elif cas == 3 :
    f.write(f"Bonjour, il ya un soucis dans l'extraction d'aujourdhui. Voici les details : \n")
    for i in range(len(resultat)):
  
        f.write(f"=)la taille de {resultat[i]} est de {aujourdhui[i]}ko aujourd'hui alors qu'hier il était de {hier[i]}ko \n")


else:
         f.write(f"Bonjour, bonne nouvelle l'extraction s'est bien deroulee. \n")

f.close()


