#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./src/data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)
print("Contenu du DataFrame:")
print(contenu)
print("\n")

# 6. Calculer le nombre de lignes et de colonnes
nombre_lignes = len(contenu)
nombre_colonnes = len(contenu.columns)
print("Résumé du tableau de données")
print(f"Nombre de lignes : {nombre_lignes}")
print(f"Nombre de colonnes : {nombre_colonnes}")

# 7. Nature statistique des variables
print("\n Nature des variables")
contenu.info()

# 8. Nom des colonnes 
print("\n Nom des colonnes")
print(contenu.head(0))

# 9. Sélectionner le nombre des inscrits
print("\n Nombre des inscrits")
inscrits = contenu['Inscrits']
print(inscrits)

# 10. Calculer les effectifs de chaque colonne
print("\n Effectifs de chaque colonne")
effectifs_toutes = []
for colonne in contenu.columns:
    somme = contenu[colonne].sum()
    effectifs_toutes.append(somme)
print(effectifs_toutes)

print("\n Effectifs des colonnes quantitatives uniquement")
effectifs_quantitatives = []
for i, colonne in enumerate(contenu.columns):
    # Vérifier si la colonne est de type numérique (float64 ou int64)
    if contenu[colonne].dtype in ['float64', 'int64']:
        somme = contenu[colonne].sum()
        effectifs_quantitatives.append(somme)
        print(f"{colonne} : {somme}")
print(f"\nListe des effectifs quantitatifs : {effectifs_quantitatives}")

# 11.  Créer des diagrammes en barres pour chaque département
import os
# Créer le dossier pour stocker les images
if not os.path.exists('images_departements'):
    os.makedirs('images_departements')
print("\nCréation des diagrammes en barres")
# Boucle sur chaque département 
for index, row in contenu.iterrows():
    # Récupérer les données du département
    code_dept = row['Code du département']
    nom_dept = row['Libellé du département']
    inscrits = row['Inscrits']
    votants = row['Votants']
    # Créer le diagramme en barres
    plt.figure(figsize=(8, 6))
    categories = ['Inscrits', 'Votants']
    valeurs = [inscrits, votants]
    plt.bar(categories, valeurs, color=['blue', 'green'])
    plt.title(f'Département {code_dept} - {nom_dept}')
    plt.ylabel('Nombre de personnes')
    plt.xlabel('Catégories')
    # Ajouter les valeurs au-dessus des barres
    for i, v in enumerate(valeurs):
        plt.text(i, v, str(int(v)), ha='center', va='bottom')
    # Sauvegarder l'image
    nom_dept_clean = nom_dept.replace(" ", "_").replace("/", "-").replace("'", "")
    nom_fichier = f'images_departements/dept_{code_dept}_{nom_dept_clean}.png'
    plt.savefig(nom_fichier, dpi=100, bbox_inches='tight')
    print(f"Diagramme créé : {nom_fichier}")
print(f"\n✓ {len(contenu)} diagrammes créés dans le dossier 'images_departements/'")

# 12. Créer des diagrammes circulaires pour chaque département
print("\nCréation des diagrammes circulaires")

# Boucle sur chaque département 
for index, row in contenu.iterrows():
    # Récupérer les données du département
    code_dept = row['Code du département']
    nom_dept = row['Libellé du département']
    abstentions = row['Abstentions']
    blancs = row['Blancs']
    nuls = row['Nuls']
    exprimes = row['Exprimés']
    # Créer le diagramme circulaire
    plt.figure(figsize=(8, 8))
    categories = ['Abstentions', 'Blancs', 'Nuls', 'Exprimés']
    valeurs = [abstentions, blancs, nuls, exprimes]
    couleurs = ['red', 'lightgray', 'orange', 'green']
    plt.pie(valeurs, labels=categories, colors=couleurs, autopct='%1.1f%%', startangle=90)
    plt.title(f'Répartition des votes - Département {code_dept} - {nom_dept}')
    plt.axis('equal')  
    # Sauvegarder l'image 
    nom_dept_clean = nom_dept.replace(" ", "_").replace("/", "-").replace("'", "")
    nom_fichier = f'images_departements/pie_{code_dept}_{nom_dept_clean}.png'
    plt.savefig(nom_fichier, dpi=100, bbox_inches='tight')
    plt.close()  # Fermer la figure pour libérer la mémoire
    print(f"Diagramme circulaire créé : {nom_fichier}")

print(f"\n✓ {len(contenu)} diagrammes circulaires créés dans le dossier 'images_departements/'")

# 13. Histogramme de la distribution des inscrits
print("\nHistogramme de la distribution des inscrits")
plt.figure(figsize=(10, 6))

plt.hist(contenu['Inscrits'], bins=20, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribution des inscrits par département')
plt.xlabel('Nombre d\'inscrits')
plt.ylabel('Densité de probabilité')
plt.grid(True, alpha=0.3)
plt.savefig('images_departements/histogramme_inscrits.png', dpi=100, bbox_inches='tight')
plt.close()

print("Histogramme de distribution créé : images_departements/histogramme_inscrits.png")

# BONUS 
print("\nBONUS : Diagrammes circulaires")

colonnes_voix = ['Voix', 'Voix.1', 'Voix.2', 'Voix.3', 'Voix.4', 'Voix.5', 
                 'Voix.6', 'Voix.7', 'Voix.8', 'Voix.9', 'Voix.10', 'Voix.11']
colonnes_noms = ['Nom', 'Nom.1', 'Nom.2', 'Nom.3', 'Nom.4', 'Nom.5', 
                 'Nom.6', 'Nom.7', 'Nom.8', 'Nom.9', 'Nom.10', 'Nom.11']
colonnes_prenoms = ['Prénom', 'Prénom.1', 'Prénom.2', 'Prénom.3', 'Prénom.4', 'Prénom.5', 
                    'Prénom.6', 'Prénom.7', 'Prénom.8', 'Prénom.9', 'Prénom.10', 'Prénom.11']

noms_candidats = []
for i, col_nom in enumerate(colonnes_noms):
    nom = contenu[col_nom].iloc[0]
    prenom = contenu[colonnes_prenoms[i]].iloc[0]
    noms_candidats.append(f"{prenom} {nom}")

print(f"Candidats identifiés : {noms_candidats}")

# Créer un dossier pour les diagrammes des candidats
if not os.path.exists('images_candidats'):
    os.makedirs('images_candidats')

# 1. Diagramme circulaire pour chaque département
print("\n Création des diagrammes par département")
for index, row in contenu.iterrows():
    code_dept = row['Code du département']
    nom_dept = row['Libellé du département']
    
    # Récupérer les voix de chaque candidat pour ce département
    voix_dept = []
    for col_voix in colonnes_voix:
        voix_dept.append(row[col_voix])
    
    # Créer le diagramme circulaire
    plt.figure(figsize=(10, 8))
    plt.pie(voix_dept, labels=noms_candidats, autopct='%1.1f%%', startangle=90)
    plt.title(f'Répartition des voix par candidat - {code_dept} - {nom_dept}')
    plt.axis('equal')
    
    # Sauvegarder
    nom_dept_clean = nom_dept.replace(" ", "_").replace("/", "-").replace("'", "")
    nom_fichier = f'images_candidats/candidats_{code_dept}_{nom_dept_clean}.png'
    plt.savefig(nom_fichier, dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"Diagramme candidats créé : {nom_fichier}")

print(f"\n✓ {len(contenu)} diagrammes par département créés")

# 2. Diagramme circulaire pour l'ensemble de la France
print("\n Création du diagramme pour l'ensemble de la France")

# Calculer le total des voix pour chaque candidat sur toute la France
voix_france = []
for col_voix in colonnes_voix:
    total_voix = contenu[col_voix].sum()
    voix_france.append(total_voix)

# Créer le diagramme circulaire national
plt.figure(figsize=(12, 10))

# Utiliser une légende à part 
wedges, texts, autotexts = plt.pie(voix_france, autopct='%1.1f%%', startangle=90)
plt.title('Répartition des voix par candidat - ENSEMBLE DE LA FRANCE', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.legend(wedges, noms_candidats, title="Candidats", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

# Sauvegarder
plt.savefig('images_candidats/candidats_FRANCE_ENTIERE.png', dpi=100, bbox_inches='tight')
plt.close()

print("Diagramme France entière créé : images_candidats/candidats_FRANCE_ENTIERE.png")

# Afficher les résultats nationaux
print("\n Résultats nationaux")
for i, candidat in enumerate(noms_candidats):
    pourcentage = (voix_france[i] / sum(voix_france)) * 100
    print(f"{candidat} : {voix_france[i]:.0f} voix ({pourcentage:.2f}%)")