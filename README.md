# Web-Scraping-Instagram

## Description
Cette application Python a été créée pour effectuer le web scraping des publications Instagram comportant le hashtag #harcèlement. Elle collecte les données pertinentes et génère un fichier CSV contenant les informations extraites.

## Prérequis
- Python 3.11
- Docker

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/MedHisoka11/WebScraper_Insta.git


installez les dépendances :

Copy code
pip install -r requirements.txt

Utilisation:
Open credentials.py and provide your Instagram username and password.

Copy code

python main.py
Les données extraites seront enregistrées dans un fichier CSV nommé harassment_posts.csv dans le répertoire du projet.
Conteneurisation avec Docker

Vous pouvez également conteneuriser l'application à l'aide de Docker. Suivez ces étapes :

Construisez l'image Docker :

Copy code
docker build -t  web-wcraping-instagram .

Exécutez le conteneur Docker :

Copy code
docker run -v $(pwd):/app web-wcraping-instagram

