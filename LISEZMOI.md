# Comparateur d'Évaluateurs d'Expressions Mathématiques

## Description
Ce projet implémente et compare différents évaluateurs d'expressions mathématiques en Python crées à l'occasion d'un projet pour le club informatique du Lycée. Le but est de comparer l'efficacité de différentes méthodes (itérative, récursive, et la fonction `eval` intégrée de Python) en termes de performance et de précision.

## Structure du Projet
- `evaluate_recursive.py`: Contient l'implémentation récursive de l'évaluateur d'expressions.
- `evaluate_iterative.py`: Contient l'implémentation itérative de l'évaluateur d'expressions.
- `testcases/`: Répertoire contenant des fichiers de test avec des expressions mathématiques.
- `main.py`: Script principal qui exécute les évaluateurs sur les cas de test et compare leurs performances.

## Fonctionnement
Le script principal (`performances.py`) lit les expressions mathématiques à partir de fichiers dans le répertoire `testcases`. Il exécute ensuite chaque expression à travers les trois évaluateurs (itératif, récursif, et intégré) et mesure le temps nécessaire pour chaque évaluation. Les résultats et les temps d'exécution sont affichés pour comparaison.

## Utilisation
Pour utiliser ce projet, suivez ces étapes :
1. Placez vos expressions mathématiques de test dans des fichiers séparés dans le répertoire `testcases`.
2. Exécutez le script principal avec Python :
```bash
python performances.py
```
3. Consultez les résultats affichés sur la console pour comparer les performances des différents évaluateurs.
