#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023

import os

# Créer le dossier img s'il n'existe pas
if not os.path.exists('img'):
    os.makedirs('img')

# ============================================================================
# PARTIE 1 : ANALYSE DES RÉSULTATS ÉLECTIONS PRÉSIDENTIELLES 2022
# ============================================================================

print("="*70)
print("ANALYSE DES ÉLECTIONS PRÉSIDENTIELLES 2022 - 1ER TOUR")
print("="*70)

# 1. Ouverture du fichier CSV avec with
with open('data/resultats-elections-presidentielles-2022-1er-tour.csv', 'r', encoding='utf-8') as f:
    df_elections = pd.read_csv(f, sep=';')

print(f"\nNombre de lignes : {len(df_elections)}")
print(f"\nAperçu des colonnes :\n{df_elections.columns.tolist()}")

# 2. Sélection des colonnes quantitatives
# On suppose que les colonnes quantitatives sont celles avec des nombres
colonnes_quantitatives = df_elections.select_dtypes(include=[np.number]).columns.tolist()
print(f"\nColonnes quantitatives identifiées : {colonnes_quantitatives}")

df_quant = df_elections[colonnes_quantitatives]

# 3. Calcul des paramètres statistiques
print("\n" + "="*70)
print("CALCUL DES PARAMÈTRES STATISTIQUES")
print("="*70)

# Liste pour stocker les résultats
parametres = {
    'Colonne': colonnes_quantitatives,
    'Moyenne': [],
    'Médiane': [],
    'Mode': [],
    'Écart-type': [],
    'Écart absolu moyen': [],
    'Étendue': []
}

for col in colonnes_quantitatives:
    # Moyenne
    moyenne = df_quant[col].mean()
    parametres['Moyenne'].append(moyenne)
    
    # Médiane
    mediane = df_quant[col].median()
    parametres['Médiane'].append(mediane)
    
    # Mode (on prend le premier mode s'il y en a plusieurs)
    mode = df_quant[col].mode()
    if len(mode) > 0:
        parametres['Mode'].append(mode[0])
    else:
        parametres['Mode'].append(np.nan)
    
    # Écart-type
    ecart_type = df_quant[col].std()
    parametres['Écart-type'].append(ecart_type)
    
    # Écart absolu à la moyenne
    ecart_abs_moyen = np.abs(df_quant[col] - moyenne).mean()
    parametres['Écart absolu moyen'].append(ecart_abs_moyen)
    
    # Étendue (max - min)
    etendue = df_quant[col].max() - df_quant[col].min()
    parametres['Étendue'].append(etendue)

# Création du DataFrame des paramètres
df_parametres = pd.DataFrame(parametres)

# Arrondir à 2 décimales
df_parametres = df_parametres.round(2)

# 4. Affichage des paramètres
print("\n")
print(df_parametres.to_string(index=False))

# 5. Distance interquartile et interdécile
print("\n" + "="*70)
print("DISTANCES INTERQUARTILE ET INTERDÉCILE")
print("="*70)

distances = {
    'Colonne': colonnes_quantitatives,
    'Distance interquartile (Q3-Q1)': [],
    'Distance interdécile (D9-D1)': []
}

for col in colonnes_quantitatives:
    # Distance interquartile
    q1 = df_quant[col].quantile(0.25)
    q3 = df_quant[col].quantile(0.75)
    dist_interquartile = q3 - q1
    distances['Distance interquartile (Q3-Q1)'].append(dist_interquartile)
    
    # Distance interdécile
    d1 = df_quant[col].quantile(0.1)
    d9 = df_quant[col].quantile(0.9)
    dist_interdecile = d9 - d1
    distances['Distance interdécile (D9-D1)'].append(dist_interdecile)

df_distances = pd.DataFrame(distances).round(2)
print("\n")
print(df_distances.to_string(index=False))

# 6. Boîtes à moustaches pour chaque colonne quantitative
print("\n" + "="*70)
print("CRÉATION DES BOÎTES À MOUSTACHES")
print("="*70)

for col in colonnes_quantitatives:
    plt.figure(figsize=(10, 6))
    plt.boxplot(df_quant[col].dropna(), vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='blue'),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='blue'),
                capprops=dict(color='blue'))
    plt.title(f'Boîte à moustaches - {col}', fontsize=14, fontweight='bold')
    plt.ylabel('Valeurs', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    # Sauvegarde
    nom_fichier = f"img/boxplot_{col.replace(' ', '_').replace('/', '_')}.png"
    plt.savefig(nom_fichier, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Boîte à moustaches sauvegardée : {nom_fichier}")

# ============================================================================
# PARTIE 2 : ANALYSE DES ÎLES (ISLAND-INDEX.CSV)
# ============================================================================

print("\n" + "="*70)
print("ANALYSE DE LA SURFACE DES ÎLES")
print("="*70)

# 7. Chargement du fichier island-index.csv
with open('data/island-index.csv', 'r', encoding='utf-8') as f:
    df_islands = pd.read_csv(f)

print(f"\nNombre d'îles : {len(df_islands)}")
print(f"Colonnes disponibles : {df_islands.columns.tolist()}")

# 8. Catégorisation et dénombrement par surface
# Définition des intervalles
intervalles = [
    (0, 10, ']0, 10]'),
    (10, 25, ']10, 25]'),
    (25, 50, ']25, 50]'),
    (50, 100, ']50, 100]'),
    (100, 2500, ']100, 2500]'),
    (2500, 5000, ']2500, 5000]'),
    (5000, 10000, ']5000, 10000]'),
    (10000, float('inf'), ']10000, +∞[')
]

# Algorithme de catégorisation
resultats_categorisation = {
    'Intervalle': [],
    'Nombre d\'îles': []
}

# Récupération de la colonne Surface
surface_col = 'Surface (km2)' if 'Surface (km2)' in df_islands.columns else df_islands.columns[0]
surfaces = df_islands[surface_col]

print(f"\nCatégorisation des îles par surface :")
print("-" * 50)

for borne_inf, borne_sup, label in intervalles:
    # Compter le nombre d'îles dans l'intervalle
    if borne_sup == float('inf'):
        count = len(surfaces[surfaces > borne_inf])
    else:
        count = len(surfaces[(surfaces > borne_inf) & (surfaces <= borne_sup)])
    
    resultats_categorisation['Intervalle'].append(label)
    resultats_categorisation['Nombre d\'îles'].append(count)
    print(f"{label:20s} : {count:4d} îles")

df_categorisation = pd.DataFrame(resultats_categorisation)

# ============================================================================
# BONUS : EXPORT DES RÉSULTATS
# ============================================================================

print("\n" + "="*70)
print("EXPORT DES RÉSULTATS (BONUS)")
print("="*70)

# Export en CSV
df_parametres.to_csv('img/parametres_statistiques.csv', index=False, sep=';', encoding='utf-8')
print("✓ Paramètres exportés : img/parametres_statistiques.csv")

df_distances.to_csv('img/distances_quantiles.csv', index=False, sep=';', encoding='utf-8')
print("✓ Distances exportées : img/distances_quantiles.csv")

df_categorisation.to_csv('img/categorisation_iles.csv', index=False, sep=';', encoding='utf-8')
print("✓ Catégorisation exportée : img/categorisation_iles.csv")

# Export en Excel
with pd.ExcelWriter('img/resultats_analyse.xlsx', engine='openpyxl') as writer:
    df_parametres.to_excel(writer, sheet_name='Paramètres', index=False)
    df_distances.to_excel(writer, sheet_name='Distances', index=False)
    df_categorisation.to_excel(writer, sheet_name='Catégorisation îles', index=False)

print("✓ Tous les résultats exportés : img/resultats_analyse.xlsx")

print("\n" + "="*70)
print("ANALYSE TERMINÉE AVEC SUCCÈS !")
print("="*70)