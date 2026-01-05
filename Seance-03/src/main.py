#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023
# 4. Ouvrir le fichier CSV
df = pd.read_csv("./src/data/resultats-elections-presidentielles-2022-1er-tour.csv")

# 5. Statistiques descriptives sur les colonnes quantitatives
print("\n==== STATISTIQUES DESCRIPTIVES ====")

# Sélection des colonnes quantitatives
colonnes_quantitatives = df.select_dtypes(include=['float64', 'int64'])

print(f"\nNombre de colonnes quantitatives : {len(colonnes_quantitatives.columns)}")
print(f"Colonnes quantitatives : {colonnes_quantitatives.columns.tolist()}")

# MOYENNES 
print("\n- MOYENNES -")
moyennes = colonnes_quantitatives.mean().round(2).tolist()
print("Moyennes de chaque colonne :")
for i, col in enumerate(colonnes_quantitatives.columns):
    print(f"  {col} : {moyennes[i]}")

# MÉDIANES 
print("\n- MEDIANES -")
medianes = colonnes_quantitatives.median().round(2).tolist()
print("Médianes de chaque colonne :")
for i, col in enumerate(colonnes_quantitatives.columns):
    print(f"  {col} : {medianes[i]}")

# MODES
print("\n- MODES -")
modes = []
print("Modes de chaque colonne :")
for col in colonnes_quantitatives.columns:
    mode_val = colonnes_quantitatives[col].mode()
    if len(mode_val) > 0:
        mode_val = round(mode_val[0], 2)  # Arrondir le mode à 2 décimales
    else:
        mode_val = None
    modes.append(mode_val)
    print(f"  {col} : {mode_val}")

# ÉCARTS TYPES
print("\n- ECARTS TYPES -")
ecarts_types = colonnes_quantitatives.std().round(2).tolist()
print("Écarts types de chaque colonne :")
for i, col in enumerate(colonnes_quantitatives.columns):
    print(f"  {col} : {ecarts_types[i]}")

# ÉCARTS ABSOLUS À LA MOYENNE
print("\n- ECARTS ABSOLUS A LA MOYENNE -")
ecarts_absolus_moyenne = []
print("Écarts absolus à la moyenne de chaque colonne :")
for col in colonnes_quantitatives.columns:
    moyenne_col = colonnes_quantitatives[col].mean()
    ecart_absolu = np.abs(colonnes_quantitatives[col] - moyenne_col).mean()
    ecart_absolu = round(ecart_absolu, 2)  # Arrondir à 2 décimales
    ecarts_absolus_moyenne.append(ecart_absolu)
    print(f"  {col} : {ecart_absolu}")

# ÉTENDUES
print("\n- ETENDUES -")
etendues = []
print("Étendues de chaque colonne (max - min) :")
for col in colonnes_quantitatives.columns:
    etendue = colonnes_quantitatives[col].max() - colonnes_quantitatives[col].min()
    etendue = round(etendue, 2)  
    etendues.append(etendue)
    print(f"  {col} : {etendue}")

# 6. Afficher la liste des paramètres 
print("\nAFFICHAGE DE TOUS LES PARAMETRES")

parametres = {
    "Moyennes": moyennes,
    "Médianes": medianes,
    "Modes": modes,
    "Écarts types": ecarts_types,
    "Écarts absolus à la moyenne": ecarts_absolus_moyenne,
    "Étendues": etendues
}

for nom_param, valeurs in parametres.items():
    print(f"\n--- {nom_param.upper()} ---")
    for i, col in enumerate(colonnes_quantitatives.columns):
        print(f"  {col}: {valeurs[i]}")

# 7. Distance interquartile et interdécile
# DISTANCE INTERQUARTILE
print("\nDISTANCE INTERQUARTILE")
distances_interquartiles = []
print("Distance interquartile de chaque colonne :")
for col in colonnes_quantitatives.columns:
    q1 = colonnes_quantitatives[col].quantile(0.25)
    q3 = colonnes_quantitatives[col].quantile(0.75)
    distance_iq = round(q3 - q1, 2)
    distances_interquartiles.append(distance_iq)
    print(f"  {col} : Q1={q1:.2f}, Q3={q3:.2f}, Distance IQ={distance_iq}")

# DISTANCE INTERDECILE 
print("\nDISTANCE INTERDECILE")
distances_interdeciles = []
print("Distance interdécile de chaque colonne :")
for col in colonnes_quantitatives.columns:
    d1 = colonnes_quantitatives[col].quantile(0.10)
    d9 = colonnes_quantitatives[col].quantile(0.90)
    distance_id = round(d9 - d1, 2)
    distances_interdeciles.append(distance_id)
    print(f"  {col} : D1={d1:.2f}, D9={d9:.2f}, Distance ID={distance_id}")
# 8. Boîte à moustache 
print("\n\nCREATION DES BOITES A MOUSTACHE")

import os

# Créer le dossier img s'il n'existe pas
if not os.path.exists('img'):
    os.makedirs('img')
    print("✓ Dossier 'img' créé")

# Boucle sur chaque colonne quantitative
print("\nCréation des boîtes à moustache :")
for col in colonnes_quantitatives.columns:
    # Créer une nouvelle figure
    plt.figure(figsize=(10, 6))
    
    # Créer la boîte à moustache
    plt.boxplot(colonnes_quantitatives[col].dropna(), vert=True)
    plt.title(f'Boîte à moustache - {col}', fontsize=14, fontweight='bold')
    plt.ylabel('Valeurs', fontsize=12)
    plt.grid(True, alpha=0.3)
    nom_fichier_clean = col.replace(" ", "_").replace("/", "-").replace("'", "").replace("é", "e").replace("è", "e")
    nom_fichier = f'img/boite_a_moustache_{nom_fichier_clean}.png'
    plt.savefig(nom_fichier, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"  ✓ Boîte à moustache créée : {nom_fichier}")

# 9. Lire dossier Island index
df_islands = pd.read_csv("./src/data/island-index.csv")

# 10. Catégoriser et dénombrer les îles 
print("\n\nCATEGORISATION DES ILES PAR SURFACE")
print(df_islands.columns.tolist())
surfaces = df_islands['Surface (km²)']
categories = {
    ']0, 10]': (0, 10),
    ']10, 25]': (10, 25),
    ']25, 50]': (25, 50),
    ']50, 100]': (50, 100),
    ']100, 2500]': (100, 2500),
    ']2500, 5000]': (2500, 5000),
    ']5000, 10000]': (5000, 10000),
    ']10000, +∞[': (10000, float('inf'))
}
compteurs = {cat: 0 for cat in categories.keys()}

print("\nCatégorisation en cours...")
for surface in surfaces:
    for categorie, (borne_inf, borne_sup) in categories.items():
        if borne_inf < surface <= borne_sup:
            compteurs[categorie] += 1
            break  
print("\nRESULTAT DE LA CATEGORISATION")
print(f"{'Catégorie (km²)':<20} {'Nombre d’îles':<15}")
print("-" * 35)
total = 0
for categorie, nombre in compteurs.items():
    print(f"{categorie:<20} {nombre:<15}")
    total += nombre

print("-" * 35)
print(f"{'TOTAL':<20} {total:<15}")
print(f"\n✓ Vérification : {total} îles catégorisées sur {len(surfaces)} îles au total")

# Visualisation avec un diagramme en barres
print("\nCREATION DU DIAGRAMME EN BARRES")
plt.figure(figsize=(12, 6))

categories_labels = list(compteurs.keys())
valeurs = list(compteurs.values())

plt.bar(categories_labels, valeurs, color='steelblue', edgecolor='black')
plt.title('Répartition des îles par catégorie de surface', fontsize=14, fontweight='bold')
plt.xlabel('Catégories de surface (km²)', fontsize=12)
plt.ylabel('Nombre d\'îles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')

for i, v in enumerate(valeurs):
    plt.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('img/categorisation_iles_surface.png', dpi=100, bbox_inches='tight')
plt.close()

print("✓ Diagramme sauvegardé : img/categorisation_iles_surface.png")

# BONUS 
print("BONUS")
df_resultats = pd.DataFrame(list(compteurs.items()), columns=['Catégorie (km²)', "Nombre d'îles"])
df_resultats.loc[len(df_resultats)] = ['TOTAL', df_resultats["Nombre d'îles"].sum()]
import os
os.makedirs('Bonus', exist_ok=True)
df_resultats.to_csv('Bonus/resultats_categorisation_iles.csv', index=False, encoding='utf-8-sig')
df_resultats.to_excel('Bonus/resultats_categorisation_iles.xlsx', index=False, sheet_name='Categorisation_iles')
print("Bonus terminé: résultats importés")
