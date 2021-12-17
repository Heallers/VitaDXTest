# JellySmackTest

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


############### Routes ###############

# GET /annotations
Permet de récupérer les annotations telles quel transmises au système


# GET /number_annotations_by_user (Feature 1)
Permet de récupérer le nombre d'annotations par user


# GET /number_annotations_by_project (Feature 1)
Permet de récupérer le nombre d'annotations par project_id


# GET /assets_with_majority_different_labels (Feature 2)
Permet de récupérer les assets d'un projet où la majorité des users n'ont pas mis le même label
- _project_id : L'identifiant du projet


# GET /projects_with_more_than_15_assets (Feature 3)
Permet de récupérer les projets avec plus de 15 assets pour un user et une période donnés
- _user  : L'identifiant du user
- _begin : Le début de la période. Format: '%Y-%m-%dT%H:%M:%SZ'
- _end   : La fin de la période. Format: '%Y-%m-%dT%H:%M:%SZ'


# GET /annotations_with_project_type
Permet de récupérer un projet avec son type, sous un format spécial (Feature 4)
- _project_id : L'identifiant du projet
