import json
import re

# Charger le mapping des couleurs depuis conversion.json
with open("conversion.json", "r") as f:
    color_map = json.load(f)

# Charger le fichier input
with open("input/example.txt", "r") as f:
    input_lines = [line.strip() for line in f.readlines()]

# Colonnes de A à G pour la grille
columns = ["A", "B", "C", "D", "E", "F", "G"]

def clean_note(note):
    """
    Retire le chiffre de l'octave et garde tous les caractères spéciaux autour de la lettre.
    Exemples :
        'C3' -> 'C'
        'C°3' -> 'C°'
        '(A4)' -> '(A)'
        'E2|' -> 'E|'
    """
    # Extraire la lettre principale
    match = re.search(r"[A-G]", note)
    if not match:
        return note
    letter = match.group(0)

    # Conserver tous les caractères spéciaux autour de la lettre (tout sauf les chiffres)
    prefix_match = re.match(r"[^A-G\d]*", note)   # tout avant la lettre sauf chiffres
    prefix = prefix_match.group(0) if prefix_match else ""

    # Tout après la lettre
    suffix_match = re.search(r"[^0-9]*$", note)  # tout après la lettre sauf chiffres
    suffix = suffix_match.group(0) if suffix_match else ""

    return f"{prefix}{letter}{suffix}"

# Générer les 6 grilles côte à côte
num_grids = 6  # pour les 6 couleurs
html_lines = []

# Header pour les grilles
header = "   ".join(columns) + "   "
header = (header + "   ") * num_grids
html_lines.append(header)
html_lines.append("-" * len(header))

# Pour chaque ligne de temps
cell_width = 4  # largeur fixe pour chaque colonne

for i, line in enumerate(input_lines):
    notes_in_line = line.split()
    row = []
    for grid_index in range(num_grids):
        grid_row = []
        grid_color = color_map.get(str(grid_index + 1), "black")
        for col in columns:
            found = False
            for note in notes_in_line:
                letter_match = re.search(r"[A-G]", note)
                if letter_match:
                    letter = letter_match.group(0)
                    match =  re.search(r'\d+', note)  # recherche un ou plusieurs chiffres
                    number = int(match.group())
                    if number == grid_index + 1 and letter == col:
                        display_note = clean_note(note)
                        # Ajouter un span coloré + espace pour fixer la largeur
                        grid_row.append(f'<span style="color:{grid_color};  font-weight:bold; font-size:16px">{display_note}</span>' + " " * (cell_width - len(display_note)))
                        found = True
                        break
            if not found:
                # Ajouter un point avec padding
                grid_row.append(f'<span style="color:{grid_color}">.</span>' + " " * (cell_width - 1))
        row.append("".join(grid_row))
    # Ajouter la ligne complète
    html_lines.append("   ".join(row))

# Ligne séparatrice finale
html_lines.append("-" * len(header))

# Générer le HTML
html_content = "<html><body><pre style='font-family: monospace;'>\n" + "\n".join(html_lines) + "\n</pre></body></html>"

# Sauvegarder en UTF-8
with open("output/colored_pianoroll.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Fichier output/colored_pianoroll.html généré avec 6 grilles colorées et alignées !")
