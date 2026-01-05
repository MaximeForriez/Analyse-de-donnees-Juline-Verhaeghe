# Élements de corrections

## Séance 2.

### Questions

- **Question 8.** Il faut comprendre que les variables qualitatives sont beaucoup générales que les variables quantitatives. Vous pouvez transformer n'importe quelle variable quantitative en variable qualitative, mais l'inverse est impossible. Il est vrai que l'on effectue davantage de traitement avec les variables quantitatives, parce que c'est plus simple mathématiquement, mais les outils permettant de traiter les variables qualitatives sont en général très puissants, plus puissants que les analyses strictement quantitatives. Plus généralement, les mathématiques sont d'abord qualitatives avant d'être quantitatives.

- **Question 9.** Il y a une confusion entre amplitude et étendue. Vous n'avez pas défini la densité.

### Code

- Les commentaires statistiques sont corrects.

- Le code ne s'exécute pas, car vous n'avez pas respecté l'architecture dans votre dépôt. L'adresse `"./src/data/resultats-elections-presidentielles-2022-1er-tour.csv"` n'existe pas sur votre compte `GitHub` que j'ai cloné. Il fallait écrire `"./data/resultats-elections-presidentielles-2022-1er-tour.csv"` pour respecter votre architecture.

- Il y a un problème d'encodage à la lecture du fichier. Il fallait ajouter `encoding="utf-8"` et écrire :

```
    with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv", "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
```

- Une fois ces deux points corrigés, votre code fonctionne correctement.

## Séance 3.

### Questions

- **Question 1.** Vous mettez la bonne réponse attendue à la séance 2, question 8. Cela nuit à la cohérence de votre rapport.

- **Question 3.** Vous ne définissez pas clairement la médiane, même si vous avez compris à quoi elle sert.

- **Question 5.** Vous ne citez pas les quantiles les plus utilisés : quartiles et déciles. Il manque les quartiles et les déciles dans la description de la boîte de dispersion.

Globalement, les notions sont comprises, mais il faut être un peu plus précis dans la description des indicateurs statistiques.

### Code

- Le code ne s'exécute pas, car vous n'avez pas respecté l'architecture dans votre dépôt. L'adresse `"./src/data/..."` n'existe pas sur votre compte `GitHub` que j'ai cloné. Il fallait écrire `"./data/..."` pour respecter votre architecture.

- Bonus : OK

- Globalement, bon travail.

## Séance 4

### Questions

- Très bon travail. Notions parfaitement comprises.

### Code

- Très bon travail, mais le code sur les lois continues ne marchent pas.

## Séance 5

### Questions

- Bon travail. Notions parfaitement comprises.

- Il manque quelques éléments comme les enjeux autour du choix des estimateurs, le lien entre une statistique exhaustive et un jeu de données massif, *etc*.

### Code

- Le code est propre. Très bon travail.

- Le test de normalité ne calcule pas les bonnes *p-value*.

## Séance 6

### Questions

- Très bon travail. Notions parfaitement comprises.

### Code

- Très bon travail.

- Bonus : quelques idées, mais ce n'est pas le résultat attendu.

## Séance Bonus

- Très bon travail. Ce n'est pas tout à fait le résultat demandé, mais votre algorithme ne demande que quelques corrections mineures.

## Humanités numériques

- Votre réflexion est trop légère.

## Remarques générales

- Aucun dépôt régulier sur `GitHub`.
