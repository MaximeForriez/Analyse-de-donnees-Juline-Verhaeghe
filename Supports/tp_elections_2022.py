import pandas as pd
import matplotlib.pyplot as plt
import os

# Créer le dossier pour les images si nécessaire
os.makedirs('images', exist_ok=True)

# 4 & 5. Lecture et affichage du fichier CSV
with open('data/resultats-elections-presidentielles-2022-1er-tour.csv', 'r', encoding='utf-8') as fichier:
    contenu = pd.read_csv(fichier, sep=';')
    print("Contenu du DataFrame:")
    print(contenu)
    print("\n")

# 6. Calculer le nombre de lignes et de colonnes
nb_lignes = len(contenu)
nb_colonnes = len(contenu.columns)
print(f"Nombre de lignes: {nb_lignes}")
print(f"Nombre de colonnes: {nb_colonnes}")
print("\n")

# 7. Point sur la nature statistique des variables
# Liste des types de colonnes (à adapter selon les métadonnées)
types_colonnes = {
    'Code du département': str,
    'Libellé du département': str,
    'Inscrits': int,
    'Abstentions': int,
    'Votants': int,
    'Blancs': int,
    'Nuls': int,
    'Exprimés': int,
    # Ajouter les colonnes des candidats (voix): int
}

# 8. Afficher le nom des colonnes
print("Nom des colonnes:")
print(contenu.head())
print("\n")

# 9. Sélectionner le nombre des inscrits
inscrits = contenu['Inscrits']
print("Nombre d'inscrits par département:")
print(inscrits)
print("\n")

# 10. Calculer les effectifs des colonnes quantitatives
effectifs = []
types_quantitatifs = [int, float]

for colonne in contenu.columns:
    # Vérifier si la colonne contient des données numériques
    if contenu[colonne].dtype in ['int64', 'float64']:
        effectif = contenu[colonne].sum()
        effectifs.append({
            'Colonne': colonne,
            'Effectif': effectif
        })

print("Effectifs des colonnes quantitatives:")
for item in effectifs:
    print(f"{item['Colonne']}: {item['Effectif']}")
print("\n")

# 11. Diagrammes en barres pour inscrits et votants par département
for idx, row in contenu.iterrows():
    dept = row['Libellé du département']
    
    # Diagramme inscrits
    plt.figure(figsize=(8, 6))
    plt.bar(['Inscrits'], [row['Inscrits']], color='blue')
    plt.title(f"Nombre d'inscrits - {dept}")
    plt.ylabel("Nombre")
    plt.tight_layout()
    plt.savefig(f"images/inscrits_{dept.replace(' ', '_')}.png")
    plt.close()
    
    # Diagramme votants
    plt.figure(figsize=(8, 6))
    plt.bar(['Votants'], [row['Votants']], color='green')
    plt.title(f"Nombre de votants - {dept}")
    plt.ylabel("Nombre")
    plt.tight_layout()
    plt.savefig(f"images/votants_{dept.replace(' ', '_')}.png")
    plt.close()

print("Diagrammes en barres créés dans le dossier 'images/'")

# 12. Diagrammes circulaires pour blancs, nuls, exprimés et abstentions
for idx, row in contenu.iterrows():
    dept = row['Libellé du département']
    
    labels = ['Blancs', 'Nuls', 'Exprimés', 'Abstentions']
    valeurs = [row['Blancs'], row['Nuls'], row['Exprimés'], row['Abstentions']]
    colors = ['lightgray', 'red', 'green', 'orange']
    
    plt.figure(figsize=(8, 8))
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title(f"Répartition des votes - {dept}")
    plt.tight_layout()
    plt.savefig(f"images/repartition_{dept.replace(' ', '_')}.png")
    plt.close()

print("Diagrammes circulaires créés dans le dossier 'images/'")

# 13. Histogramme de la distribution des inscrits
plt.figure(figsize=(10, 6))
plt.hist(contenu['Inscrits'], bins=10, density=True, edgecolor='black', alpha=0.7)
plt.title("Distribution des inscrits")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Densité")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("images/histogramme_inscrits.png")
plt.close()

print("Histogramme de distribution créé")

# BONUS: Diagrammes circulaires des voix par candidat pour chaque département
# Identifier les colonnes des candidats (celles avec "Voix" dans le nom)
colonnes_candidats = [col for col in contenu.columns if 'Voix' in col or col.startswith('M.') or col.startswith('Mme')]

if colonnes_candidats:
    for idx, row in contenu.iterrows():
        dept = row['Libellé du département']
        
        voix_candidats = [row[col] for col in colonnes_candidats]
        
        plt.figure(figsize=(10, 10))
        plt.pie(voix_candidats, labels=colonnes_candidats, autopct='%1.1f%%', startangle=90)
        plt.title(f"Répartition des voix par candidat - {dept}")
        plt.tight_layout()
        plt.savefig(f"images/candidats_{dept.replace(' ', '_')}.png")
        plt.close()
    
    # Diagramme pour l'ensemble de la France
    total_voix = [contenu[col].sum() for col in colonnes_candidats]
    
    plt.figure(figsize=(12, 12))
    plt.pie(total_voix, labels=colonnes_candidats, autopct='%1.1f%%', startangle=90)
    plt.title("Répartition des voix par candidat - France entière")
    plt.tight_layout()
    plt.savefig("images/candidats_France.png")
    plt.close()
    
    print("Bonus: Diagrammes des candidats créés")

print("\nToutes les manipulations sont terminées!")