#coding:utf8

import pandas as pd
import requests

#Consulter : https://rtavenar.github.io/poly_python/content/api.html
#Autres A.P.I. : https://www.data.gouv.fr/dataservices/search

def geturl(method, format, stations, start, end, token):
    stationstexte = ""
    for element in stations:
        stationstexte = stationstexte + "&stations[]={}".format(element)
    return "https://www.infoclimat.fr/opendata/?version=2&method={}&format={}{}&start={}&end={}&token={}".format(method, format, stationstexte, start, end, token)

def testConnexion(reponse):
    if str(reponse) == "<Response [200]>":
        data = str(reponse.text)
        data = data.split("\n")#La fonction crée une liste des lignes à partir des sauts de ligne.
        data2 = []
        for element in data:
            data2.append(element.split(";"))#La fonction crée les colonnes lorsqu'elles existent pour chacune des lignes identifiées.
        return data2
    else:
        return "Erreur de connexion : {}".format(str(reponse))
    
method = "get" #méthode de l'A.P.I. Rest
format = "csv"#format des données
stations = ["ME099", "000BV"]#codes des données
start = "2025-10-01"#format : année-mois-jour
end = "2025-10-30" #format : année-mois-jour
token = "otNmj9c6lncMAwXSIiwKulGHlwgxzM4ac1PVi03MJXLyh0BA9k5w" #votre token

# Créer la variable url
url = geturl(method, format, stations, start, end, token)

reponse = requests.get(url)
print(reponse)
if reponse.status_code != 200:
    print(f"Erreur de connexion : {reponse.status_code}")
    exit()

data = testConnexion(reponse)
data2 = []
titre = []
metadata = []
for k, ligne in enumerate(data): 
    if k in [0, 1, 2, 3, 4, 6]:
        metadata.append(ligne)
    elif k == 5:
        titre.append(ligne)
    else:
        data2.append(ligne)
# 2. 
data = pd.DataFrame(data2, columns=titre[0])
df_metadata = pd.DataFrame(metadata)
data.to_excel("donnees_meteo.xlsx", index=False)
print("✓ Fichier Excel créé")
df_metadata.to_csv("metadata.csv", encoding="utf-8", index=False)
print("✓ Fichier CSV créé")


# BONUS 
def geturl_json(method, format, stations, start, end, token):
    stationstexte = ""
    for element in stations:
        stationstexte = stationstexte + "&stations[]={}".format(element)
    return "https://www.infoclimat.fr/opendata/?version=2&method={}&format={}{}&start={}&end={}&token={}".format(method, format, stationstexte, start, end, token)

def testConnexion_json(reponse):
    if str(reponse) == "<Response [200]>":
        data_json = reponse.json()
        return data_json
    else:
        return "Erreur de connexion : {}".format(str(reponse))

method = "get"
format = "json"
stations = ["ME099", "000BV"]
start = "2025-10-01"
end = "2025-10-30" 
token = "otNmj9c6lncMAwXSIiwKulGHlwgxzM4ac1PVi03MJXLyh0BA9k5w"

url = geturl_json(method, format, stations, start, end, token)

reponse = requests.get(url)
print(reponse)
if reponse.status_code != 200:
    print(f"Erreur de connexion : {reponse.status_code}")
    exit()

data_json = testConnexion_json(reponse)
# En JSON, contrairement au CSV, les données sont déjà structurées par l'API, donc il n'y a pas besoin de créer la boucle et séparer les données. 
metadata_json = {
    'status': data_json.get('status'),
    'stations': data_json.get('stations'),
    'metadata': data_json.get('metadata')
}
data2_json = data_json.get('data', [])
print(metadata_json)

data_from_json = pd.DataFrame(data2_json)
df_metadata_json = pd.DataFrame([metadata_json])

data_from_json.to_excel("donnees_meteo_json.xlsx", index=False)
print("\n✓ Fichier Excel JSON créé")

df_metadata_json.to_csv("metadata_json.csv", encoding="utf-8", index=False)
print("✓ Fichier CSV créé")

import json
with open("donnees_brutes.json", "w", encoding="utf-8") as f:
    json.dump(data_json, f, indent=2, ensure_ascii=False)
print("✓ Fichier JSON créé")

