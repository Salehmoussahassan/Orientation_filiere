#########################################
Dans ce cadre, le projet consiste à mettre en place un système d'orientation et de choix de filières pour des élèves ayant décroché leur bacalauréat série scientifique.

Le projet consiste à faire l'orientation et le choix de filières pour les élèves de la série scientifique et le système qui permet de calculer la moyenne de matières scientifiques depuis la seconde scientifique , de la première scientifique , de la terminale scientifique et celles du baccalauréat puis le système calcule leur somme et puis divise la moyenne et lui oriente en une série de matières.
Tout abord l'utilisateur entre son nom , son âge et son sexe, 
Conditions sur l'orientation si la moyenne est égal à 20 et > à 18 le comité d'orientation vous accorde un certain nombre de filières :

1- Médecine 
2- informatique 
3- pharmacie 
4- aviation civile 
Si la moyenne est <=18 ou > 16 le comité d'orientation vous accorde un certain nombre de filières :
1- mathématiques pures
2- génie civil 
3- pétrochimie 
4- météorologie 
Si la moyenne est<= 16 ou > 14 le comité d'orientation vous accorde un certain nombre de filières :
1- physique 
2- chimie 
3- agronomie 
4- élevage 
Si la moyenne est <= 14 ou >12 le comité d'orientation vous accorde un certain nombre de filières :
1- biologie 
2- géologie 
3- hydrologie 
4- géographie 
Si la moyenne est <= 12 ou >10 le comité d'orientation vous accorde un certain nombre de filières :
1- économie 
2- gestionnaire 
3- soin 
4- électronique 
Sinon la moyenne est > 20 ou < 10 désolé vous n'aviez pas de filières scientifiques 

###############################################################################

En fin le résultat est donner sous format d'un tableau 

####################################################################################

Pour une bonne fonctionnalité, il est recommandé à l'utilsateur d'installer

1- pip install python ou python3
2- pip install prettytable (pour l'affichage du resulatat sous format d'untableau)

#########################################################################################

Voici un exemple concret 
############################################################################################

log(base) saleh@saleh:~/Bureau/Orientation$ python orientation.py

############################################################################################

Bienvenue dans le système d'orientation des élèves scientifiques !
Entrez votre nom : Saleh
Entrez votre âge : 21
Entrez votre sexe (M/F) : M
Entrez les moyennes de vos matières scientifiques :
Moyenne en Seconde scientifique : 19
Moyenne en Première scientifique : 17
Moyenne en Terminale scientifique : 16
Moyenne au Baccalauréat scientifique : 17.75

Calcul terminé.
Votre moyenne générale est : 17.44


########### Résultats d'Orientation ########################

+-------+-----+------+---------+----------------------+
|  Nom  | Âge | Sexe | Moyenne | Filières disponibles |
+-------+-----+------+---------+----------------------+
| Saleh |  21 |  M   |  17.44  | Mathématiques pures  |
|       |     |      |         |     Génie civil      |
|       |     |      |         |     Pétrochimie      |
|       |     |      |         |     Météorologie     |
+-------+-----+------+---------+----------------------+


########################################################################################"