# Piano partoche

Ce projet génère une représentation visuelle d'une partition de piano dans **Excel**, avec les notes colorées selon une convention de grilles et les caractères spéciaux conservés.

---

## Fonctionnalités

- Transformation d'une partition texte (`input/example.txt`) en un **piano roll Excel**.
- 6 grilles côte à côte représentant différentes catégories de notes.
- Lettres des notes colorées selon les règles définies dans `conversion.json`.
- Les caractères spéciaux `( )`, `°`, `|` sont conservés.
- Alignement des colonnes et lignes pour une visualisation claire.
- Fond des cellules blanc/transparent, seules les lettres sont colorées.
- Les cellules vides restent visibles via les bordures Excel.

---
## Format du fichier `input/example.txt`

- Chaque ligne représente un **temps**.  
- Les notes sont séparées par des espaces.  
- Exemple :

D4| A4
C4
D4| C°3
E4
B3
E4
(A4)
F4

- Les caractères spéciaux sont supportés :
  - `(A4)` → note courte  
  - `C°3` → note avec symbole  
  - `D4|` → note longue (barre `|` conservée)

---

## Format du fichier `conversion.json`

Définit la **couleur de chaque grille** (1 à 6) :

```json
{
    "1": "purple",
    "2": "orange",
    "3": "blue",
    "4": "green",
    "5": "red",
    "6": "gold"
}
```

Utilisation

Placer la partition texte dans input/example.txt.

Vérifier/adapter les couleurs dans conversion.json.

Modifier le fichier config pour modifier le nom du fichier de sortie et d'entrée. Sinon par défaut.

Lancer le script :

double clic sur le partoche.exe


Le fichier Excel sera généré dans output/colored_pianoroll.xlsx ou dans le fichier configuré.

