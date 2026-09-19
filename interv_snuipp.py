#!/usr/bin/env python3

import os
from datetime import date

def get_infos_interv():
    """Demande à l'utilisateur les informations générales pour les interventions."""
    # Boucle pour s'assurer que l'entrée est un nombre entier valide
    while True:
        try:
            nb_str = input("Combien d'interventions ?: ")
            nb = int(nb_str)
            if nb > 0:
                break
            else:
                print("Veuillez entrer un nombre positif.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
            
    année_scolaire = input("Quelle année scolaire (ex: 2025 2026) : ").strip()
    # Amélioration : formatage plus propre avec f-string
    tag_année = f"CN {année_scolaire}"
    
    date_cn = input("Date du CN (ex: 18 et 19 novembre 2025) : ").strip()
    # Amélioration : ajout d'un espace pour la lisibilité
    tag_cn = f"CN des {date_cn}"
    
    return nb, tag_année, tag_cn, date_cn

def get_theme_interv(nb):
    """Demande à l'utilisateur de saisir les thèmes pour chaque intervention."""
    liste_interv = []
    for i in range(nb):
        # Utilisation d'une f-string pour un message clair
        theme = input(f"Entrez le thème de l'intervention numéro {i+1} : ")
        # Remplace les espaces par des underscores et nettoie les espaces en début/fin
        theme_formate = theme.replace(" ", "_").strip()
        liste_interv.append(theme_formate)
    return liste_interv

def create_interv(liste_interv, tag_année, tag_cn):
    """Crée les fichiers .md pour chaque intervention avec un en-tête YAML."""
    dt_str = date.today().strftime("%Y-%m-%d")
    print("------------------------\nCréation des fichiers d'interventions dans le répertoire courant\n------------------------")
    
    for theme in liste_interv:
        filename = f"{dt_str}_cn-snuipp_{theme}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            # Utilisation d'un multi-line string (triple guillemets) pour une meilleure lisibilité
            # et pour s'assurer que les sauts de ligne sont corrects.
            yaml_header = f"""---
title: "{theme.replace('_', ' ').title()}" # Titre plus parlant
post_status: publish
post_date: {dt_str}
taxonomy:
    category:
        - {tag_année}
        - {tag_cn}
---\n"""
            f.write(yaml_header)
        print(f"Fichier créé : {filename}")

def create_contribution(tag_année, tag_cn, date_cn):
    dt_str = date.today().strftime("%Y-%m-%d")
    print("------------------------\nCréation de l'article 'contribution' dans le répertoire courant\n------------------------")
    filename = f"{dt_str}_cn-snuipp_contribution.md"
    with open(filename, 'w', encoding='utf-8') as f:
        yaml_header = f"""---
title: "{f"Contribution aux débats du CN de la FSU SNUipp des {date_cn}"}"
post_status: publish
post_date: {dt_str}
taxonomy:
    category:
        - {tag_année}
        - {tag_cn}
---\n"""
        f.write(yaml_header)
    print(f"Fichier créé : {filename}")

# programme principal ---
def main():
    """
    Fonction principale qui orchestre la création des fichiers d'intervention CN.
    """
    print("--- Générateur de fichiers pour interventions CN ---")
    
    try:
        # 1. Récupérer les informations de l'utilisateur
        nb, tag_année, tag_cn, date_cn = get_infos_interv()
        # 2. Récupérer la liste des thèmes d'intervention
        liste_themes = get_theme_interv(nb)
        # 3. Créer les fichiers markdown dans le répertoire courant
        create_interv(liste_themes, tag_année, tag_cn)
        create_contribution(tag_année, tag_cn, date_cn)
        print("\nTous les fichiers ont été créés avec succès !")
    
    except KeyboardInterrupt:
        # Gère le cas où l'utilisateur appuie sur Ctrl+C pour quitter
        print("\nOpération annulée par l'utilisateur.")
    except Exception as e:
        # Si une erreur imprévue se produit n'importe où dans les fonctions appelées,
        # elle sera attrapée ici.
        print(f"\nUne erreur critique est survenue : {e}")
        print("Le programme a été interrompu.")

# --- NOUVEAU : Point d'entrée conditionnel ---
# Ce bloc garantit que main() n'est appelé QUE si on lance ce fichier directement.
if __name__ == "__main__":
    main()
