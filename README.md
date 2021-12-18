# VitaDXTest

############### Lancement ###############

Avoir les packages suivants installés:
- uvicorn
- fastapi
- json
- datetime

Éxécuter le fichier main.py

Aller sur le lien "http://localhost:8080/docs#/"


############### Notes ###############

Les annotations se trouvent dans le fichier data.json
Les "extra project fields" se trouvent dans projects.json

############### Project architecture ###############

Le Back peut fonctionner sous la forme d'une API avec différentes routes.
Cela permettrait, une fois hebergé, aux différentes équipes d'avoir accès aux données et de pouvoir plus facilement intégrer l'API à d'autres solutions existantes.

Pour une mise en production il faut tout d'abord que le Front puisse communiquer les annotations directement au Back.
On peut donc imaginer ici des routes supplémentaires pour insérer des nouvelles données.

Le Back doit quand à lui stocker toutes les informations dans une base de données.

On pourrait imaginer:
* une table pour les users
* une table pour les projets
* une table pour les annotations

|--------------|      |--------------|      |--------------|
|              |      |              |      |              |
|   FrontEnd   | ---- |   BackEnd    | ---- |     BDD      | 
|              |      |              |      |              | 
|--------------|      |--------------|      |--------------|

À cela doivent s'ajouter des tests unitaires (en python avec le package unittest) avec des données de test plus fournies.


############### Routes ###############

# GET /annotations
Permet de récupérer les annotations telles quel transmises au système


# GET /number_annotations_by_user 
Permet de récupérer le nombre d'annotations par user (Feature 1)


# GET /number_annotations_by_project 
Permet de récupérer le nombre d'annotations par project_id (Feature 1)


# GET /assets_with_majority_different_labels 
Permet de récupérer les assets d'un projet où la majorité des users n'ont pas mis le même label (Feature 2)
- _project_id : L'identifiant du projet


# GET /projects_with_more_than_15_assets 
Permet de récupérer les projets avec plus de 15 assets pour un user et une période donnés (Feature 3)
- _user  : L'identifiant du user
- _begin : Le début de la période. Format: '%Y-%m-%dT%H:%M:%SZ'
- _end   : La fin de la période. Format: '%Y-%m-%dT%H:%M:%SZ'


# GET /annotations_with_project_type
Permet de récupérer un projet avec son type, sous un format spécial (Feature 4)
- _project_id : L'identifiant du projet
