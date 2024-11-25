# Projet : Orientation des élèves scientifiques
# Auteur : Exemple pour débutants en Python

# Importation des modules nécessaires
from prettytable import PrettyTable

# Fonction pour calculer la moyenne des matières
def calculer_moyenne():
    print("Entrez les moyennes de vos matières scientifiques :")
    
    # Moyennes par année
    seconde = float(input("Moyenne en Seconde scientifique : "))
    premiere = float(input("Moyenne en Première scientifique : "))
    terminale = float(input("Moyenne en Terminale scientifique : "))
    baccalaureat = float(input("Moyenne au Baccalauréat scientifique : "))
    
    # Calcul de la moyenne générale
    total = seconde + premiere + terminale + baccalaureat
    moyenne = total / 4
    
    return moyenne

# Fonction pour afficher les filières disponibles selon la moyenne
def orienter_eleve(moyenne):
    print("\nCalcul terminé.")
    print(f"Votre moyenne générale est : {moyenne:.2f}\n")
    
    # Conditions d'orientation
    if moyenne > 20 or moyenne < 10:
        print("Désolé, vous n'avez pas de filières scientifiques disponibles.")
        return []
    elif moyenne >= 18:
        filieres = ["Médecine", "Informatique", "Pharmacie", "Aviation civile"]
    elif moyenne >= 16:
        filieres = ["Mathématiques pures", "Génie civil", "Pétrochimie", "Météorologie"]
    elif moyenne >= 14:
        filieres = ["Physique", "Chimie", "Agronomie", "Élevage"]
    elif moyenne >= 12:
        filieres = ["Biologie", "Géologie", "Hydrologie", "Géographie"]
    else:
        filieres = ["Économie", "Gestionnaire", "Soins", "Électronique"]
    
    return filieres

# Fonction pour afficher les résultats sous forme de tableau
def afficher_resultats(nom, age, sexe, moyenne, filieres):
    # Création du tableau
    tableau = PrettyTable()
    tableau.field_names = ["Nom", "Âge", "Sexe", "Moyenne", "Filières disponibles"]
    filieres_str = "\n".join(filieres) if filieres else "Aucune"
    
    # Ajout des données au tableau
    tableau.add_row([nom, age, sexe, f"{moyenne:.2f}", filieres_str])
    
    # Affichage du tableau
    print("\n*** Résultats d'Orientation ***")
    print(tableau)

# Fonction principale du programme
def programme_orientation():
    print("Bienvenue dans le système d'orientation des élèves scientifiques !")
    
    # Collecte des informations personnelles
    nom = input("Entrez votre nom : ")
    age = int(input("Entrez votre âge : "))
    sexe = input("Entrez votre sexe (M/F) : ").upper()
    
    # Calcul de la moyenne
    moyenne = calculer_moyenne()
    
    # Détermination des filières
    filieres = orienter_eleve(moyenne)
    
    # Affichage des résultats
    afficher_resultats(nom, age, sexe, moyenne, filieres)

# Point d'entrée du programme
if __name__ == "__main__":
    programme_orientation()
