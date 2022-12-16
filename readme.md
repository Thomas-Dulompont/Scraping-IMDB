# Brief Scraping imdb.com

## Contexte :
Vous êtes cinéphile et vous souhaitez vous créer une base de données personnelle pour rechercher vos films et séries préférés.
Dans un premier temps, vous allez récupérer des données disponibles en ligne sur des sites comme imdb.com. Pour extraire ces données, vous utiliserez le framework scrapy.

Dans un deuxième temps, vous allez utiliser une base de données NoSQL (MongoDB) pour stocker vos données. 

Enfin, vous créerez une application avec Streamlit pour afficher vos résultats.

## Scrapper IMDB

Récupérer les données de imdb.com des sections :
- Meilleurs films (top 250)
- Meilleurs séries (top 250)
- (Facultatif) Scraper tous les films
- Scraper uniquement certains genres de film

Sur ces sites webs vous devez récupérer (au minimum) les informations suivantes :
- Titre
- Titre original
- Score
- Genre
- Année
- Durée
- Descriptions(synopsis)
- Acteurs(Casting principal)
- Public
- Pays
(facultatif) Langue d’origine

(facultatif) Informations spécifiques aux séries :
- Nombre de saisons
- Nombre d’épisodes

## Créer votre application
Créer des outils de recherche :
- par nom
- par acteur(s)
- par genre
- par durée (ajoutez une fonction pour sélectionner un film inférieur à x durées)
- par note (note minimale) 

**Bonus : Ajouter des graphiques**

## Modalités du projet :

Organisation :
- Projet individuel
- Présentation à l’oral de l’un des 4 livrables

Objectifs :
- Savoir scraper des données avec scrapy
- Savoir sélectionner des données avec MongoDB
- Créer une application avec streamlit
- Gérer un dossier avec github
- Debugger votre code en effectuant des recherches avec google et stackoverflow

Date butoire :
- Soutenance vendredi 13h30

Livrable :
- Code review
- Démo du fonctionnement de votre application



