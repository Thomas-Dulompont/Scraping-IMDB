import streamlit as st
from pymongo import MongoClient
import time
from random import choice

client = MongoClient("mongodb://localhost:27017")
db = client["Scraping"]

film = db['Film']
serie = db['Serie']

with st.sidebar:
    radio = st.radio(
    "Navigation : ",
    ('🏠 Accueil' ,'📚 Brief', '💨 Quick Search',))

if radio == "🏠 Accueil":
    st.header('Scraping - Films & Séries')
    st.markdown(
        "Vous êtes cinéphile et vous souhaitez vous créer une base de données personnelle pour rechercher vos films et séries préférés.  \n"
        "Dans un premier temps, vous allez récupérer des données disponibles en ligne sur des sites comme **imdb.com**. Pour extraire ces données, vous utiliserez le framework **scrapy**.  \n "
        "Dans un deuxième temps, vous allez utiliser une base de données **NoSQL** *(MongoDB)* pour stocker vos données.  \n "
        "Enfin, vous créerez une application avec **Streamlit** pour afficher vos résultats. (Bienvenue)  \n "
    )
    st.markdown(
        '### Les objectifs du brief :  \n'
        '- Scraper les données du site "imdb.com"  \n'
        '- Nettoyé et remplir ces données dans une BBD Mongodb  \n'
        '- Créer une application Web avec Streamlit  \n'
        '- Mettre en place des outils de recherches pour les films et séries  \n'
    )
if radio == "📚 Brief":
    tab1, tab2, tab3, tab4= st.tabs(["📚 Brief - Questions", "🎞️ Films - Boite à Outils", "📺 Series - Boite à Outils", "📘 Divers - Les Statistiques"])
    with tab1:
        st.subheader('📚 Brief - Questions')
        st.markdown('Ici sont listés toutes les questions du brief ainsi que les réponses à celles ci !')

        with st.expander("▪︎ Question n°1 - Quel est le film le plus long ?"):
            best_film = film.find().sort("duree",-1)[0]
            st.markdown(
                "#  \n"
                f"Le film de plus long sur les 250 films les mieux notés au monde est : **{best_film['title']}**  \n"
                f"Ce film de **{best_film['date']}**, à était produit à **{best_film['pays']}** et dure **{best_film['duree']} mins** ! [En savoir plus]({best_film['imdb_url']})  \n"
                "  \n"
                "Voici le code utilisé pour obtenir ce resultat :  \n"
                )
            st.code('film.find().sort("duree",-1)[0]')

        with st.expander("▪︎ Question n°2 - Quels sont les 5 films les mieux notés ?"):
            top5 = film.find().sort("score",-1).limit(5)
            score_mean = (float(top5[0]['score']) + float(top5[1]['score']) + float(top5[2]['score']) + float(top5[3]['score']) + float(top5[4]['score'])) / 5
            st.markdown(
                "#  \n"
                f"Les 5 films les mieux notés sont :  \n - [{top5[0]['title']}]({top5[0]['imdb_url']})  \n - [{top5[1]['title']}]({top5[1]['imdb_url']})  \n - [{top5[2]['title']}]({top5[2]['imdb_url']})  \n - [{top5[3]['title']}]({top5[3]['imdb_url']}) \n - [{top5[4]['title']}]({top5[4]['imdb_url']})  \n  "
                f"#  \n"
                f"Ces films ont un score moyen de {score_mean} / 10 !\n"
                "  \n"
                "Voici le code utilisé pour obtenir ce resultat :  \n"
            )
            st.code('film.find().sort("score",-1).limit(5)')

        with st.expander("▪︎ Question n°3 - Dans combien de films a joué Morgan Freeman ? Tom Cruise ?"):
            morgan_freeman = film.count_documents({"acteurs" :"Morgan Freeman"})
            tom_cruise = film.count_documents({"acteurs" :"Tom Cruise"})
            st.markdown(
                "#  \n"
                f"Morgan Freeman a joué dans **{morgan_freeman} films** des 250 films les mieux notés au monde !  \n"
                f"Alors que Tom Cruise lui a joué dans **{tom_cruise} films** dans ce même classement !   \n"
                "#  \n"
                "Voici le code utilisé pour obtenir ce resultat :  \n"
            )
            st.code('film.count_documents({"acteurs" :"Mon_Acteur"})')
            st.write("*On remplace ''Mon_Acteur'' par le nom de l'acteur cherché*")

        with st.expander("▪︎ Question n°4 - Quels sont les 3 meilleurs films d’horreur ? Dramatique ? Comique ?"):
            top3_horror = list(film.find({"genre": "Horror"}).sort("score",-1).limit(3))
            top3_drama = list(film.find({"genre": "Drama"}).sort("score",-1).limit(3))
            top3_comedy = list(film.find({"genre": "Comedy"}).sort("score",-1).limit(3))
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(
                    "#  \n"
                    "🎃 **Top3 Horreur**  \n"
                    f" - [{top3_horror[0]['title']}]({top3_horror[0]['imdb_url']})  \n"
                    f" - [{top3_horror[1]['title']}]({top3_horror[1]['imdb_url']})  \n"
                    f" - [{top3_horror[2]['title']}]({top3_horror[2]['imdb_url']})  \n"
                    "#  \n"
                    )
            with col2:
                st.markdown(
                    "#  \n"
                    "🤧 **Top3 Dramatique**  \n"
                    f" - [{top3_drama[0]['title']}]({top3_drama[0]['imdb_url']})  \n"
                    f" - [{top3_drama[1]['title']}]({top3_drama[1]['imdb_url']})  \n"
                    f" - [{top3_drama[2]['title']}]({top3_drama[2]['imdb_url']})  \n"
                    "#  \n"
                    )
            with col3:
                st.markdown(
                    "#  \n"
                    "😆 **Top3 Commedie**  \n"
                    f" - [{top3_comedy[0]['title']}]({top3_comedy[0]['imdb_url']})  \n"
                    f" - [{top3_comedy[1]['title']}]({top3_comedy[1]['imdb_url']})  \n"
                    f" - [{top3_comedy[2]['title']}]({top3_comedy[2]['imdb_url']})  \n"
                    "#  \n"
                    )

            st.code('film.find({"genre": "Mon_Genre_de_Film"}).sort("score",-1).limit(3)')
            st.write("*On remplace ''Mon_Genre_de_Film'' par le nom de le genre de film cherché*")

        with st.expander("▪︎ Question n°5 - Parmi les 100 films les mieux notés, quel pourcentage sont américains ? Français ?"):
            top_100 = list(film.find().sort("score", -1).limit(100))
            france = len([f for f in top_100 if f['pays'] == "France"])
            us = len([f for f in top_100 if f['pays'] == "United States"])
            st.markdown(
                "#  \n"
                f"Dans le Top 100 des meilleurs films au monde **{us}%** sont Américains et **{france}%** sont français !\n"
                "#  \n"
                "Voici le code utilisé pour obtenir ce resultat :  \n"
            )
            st.code('top_100 = list(film.find().sort("score", -1).limit(100))')
            st.code('france = len([f for f in top_100 if f["pays"] == "France"])')
            st.code('united_states = len([f for f in top_100 if f["pays"] == "United States"])')
            st.write("*On sait donc que la variable du pays va contenir le pourcentage de film dans ce même pays*")

        with st.expander("▪︎ Question n°6 - Quel est la durée moyenne d’un film en fonction du genre ?"):
            top_100 = list(film.find().sort("score", -1).limit(100))
            france = len([f for f in top_100 if f['pays'] == "France"])
            us = len([f for f in top_100 if f['pays'] == "United States"])
            st.markdown(
                "#  \n"
                f"Dans le Top 100 des meilleurs films au monde **{us}%** sont Américains et **{france}%** sont français !\n"
                "#  \n"
                "Voici le code utilisé pour obtenir ce resultat :  \n"
            )
            st.code('top_100 = list(film.find().sort("score", -1).limit(100))')
            st.code('france = len([f for f in top_100 if f["pays"] == "France"])')
            st.code('united_states = len([f for f in top_100 if f["pays"] == "United States"])')
            st.write("*On sait donc que la variable du pays va contenir le pourcentage de film dans ce même pays*")

    with tab2:
        st.subheader('🎞️ Films - Boite à Outils')
        st.markdown('Voici une boite à outils pour rechercher un Film parmis une grande bibliothèque !')

        with st.expander("📋 - Recherche par Titre"):
            st.markdown(
                "#  \n"
                f"Entrer le nom du film que vous cherchez pour avoir des informations sur celui ci.  \n"
                )
            title = st.text_input(label='Entrer un titre de film : ', value='')
            if title != '':
                f = film.find_one({'title':title})
                st.subheader(f'Voici le resultat pour le titre "{title}" :')
                if f != None:
                    col1, col2 = st.columns(2)
                    with col1:
                        try:
                            st.image(f['img_url'], width=300)
                        except:
                            st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)
                    with col2:
                        st.subheader(f['title'])
                        st.write("**Pays** : " + f['pays'])
                        st.write("**Date** : " + f['date'])
                        st.write('**Publique** : ' + f['public'])
                        st.write('**Note** : '+ str(f['score']) +' / 10')
                        st.write('**Description**: ')
                        st.write(f['description'])
                        st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                    st.markdown("""---""")
                else:
                    st.warning('😵‍💫 Impossible de trouver un film ou avec ce titre...')

        with st.expander("⭐️ - Recherche par Nom d'acteur(s)"):
            st.markdown(
                "#  \n"
                f"Entrer le nom d'un ou plusieurs acteurs pour voir la liste des films ou il(s) joue(nt).   \n"
                )
            acteurs = film.find()
            list_acteurs = []
            for a in acteurs:
                for i in a['acteurs']:
                    if i not in list_acteurs:
                        list_acteurs.append(i)
            acteurs = st.multiselect(
            'Entrer vos acteurs favoris : ',
            list_acteurs)
            films_acteurs = list(film.find({ "acteurs": { "$all": acteurs}}).sort("score", -1))
            if len(films_acteurs) != 0:
                    st.subheader('Voici la liste des films ou apparaissent ces acteurs :')
                    for f in film.find({ "acteurs": { "$all": acteurs}}).sort("score", -1):
                        col1, col2 = st.columns(2)
                        with col1:
                            try:
                                st.image(f['img_url'], width=300)
                            except:
                                st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)
                        with col2:
                            st.subheader(f['title'])
                            st.write("**Pays** : " + f['pays'])
                            st.write("**Date** : " + f['date'])
                            st.write('**Publique** : ' + f['public'])
                            st.write('**Note** : '+ str(f['score']) +' / 10')
                            st.write('**Description**: ')
                            st.write(f['description'])
                            st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                        st.markdown("""---""")
            elif len(films_acteurs) == 0 and len(acteurs) > 0:
                st.warning('😵‍💫 Impossible de trouver un film ou ces acteurs jouent ensembles...')

        with st.expander("🗂️ - Recherche par Genre"):
            st.markdown(
                "#  \n"
                f"Entrer votre Genre de film favoris pour trouver les meilleurs films de cette catégorie.   \n"
                )
            genre = st.selectbox(
            "Selectionner un Genre de Film :",
                ("Selectionner un genre", 'Horror', 'Mystery', 'Thriller', 'Drama', 'Biography', 'Music', 'Animation', 'Adventure', 'Family', 'Crime', 'Fantasy', 'Action', 'Comedy', 'Sci-Fi', 'History', 'Romance', 'Film-Noir', 'War', 'Sport', 'Western', 'Musical')
            )
            if genre != "Selectionner un genre":
                films = film.find({"genre" : genre}).sort("score", -1)
                st.subheader(f'Voici les films dans de genre "{genre}" dans notre bibliothèque :')
                for f in films:
                    col1, col2 = st.columns(2)
                    with col1:
                        try:
                            st.image(f['img_url'], width=300)
                        except:
                            st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)

                    with col2:
                        st.subheader(f['title'])
                        st.write("**Pays** : " + f['pays'])
                        st.write("**Date** : " + f['date'])
                        if f['public'] == None:
                            st.write('**Publique** : ' + "Non communiqué")
                        else:
                            st.write('**Publique** : ' + f['public'])
                        st.write('**Note** : '+ str(f['score']) +' / 10')
                        st.write('**Description**: ')
                        st.write(f['description'])
                        st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                    st.markdown("""---""")
        
        with st.expander("🕝 - Recherche par Durée"):
            st.markdown(
            "#  \n"
            f"Entrer la durée minimale et maximale en minutes pour découvrir les films qui sont dans cette durée !   \n"
            )
            col1, col2 = st.columns(2)
            with col1:
                min = st.slider( "⬇️ Durée Minimale (en minutes):",min_value=1, max_value=300)
            with col2:
                max = st.slider( "⬆️ Durée Maximale (en minutes):",min_value=1, max_value=300)
            if st.button('Rechercher'):
                film_result = list(film.find({ "duree": { "$gt": min, '$lt': max} }).sort("score", -1))
                if len(film_result) > 0:
                    st.subheader(f'Voici les films qui durent entre {min} et {max} minutes :')
                    for f in film_result:
                        col1, col2 = st.columns(2)
                        with col1:
                            try:
                                st.image(f['img_url'], width=300)
                            except:
                                st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)

                        with col2:
                            st.subheader(f['title'])
                            st.write("**Pays** : " + f['pays'])
                            st.write("**Date** : " + f['date'])
                            if f['public'] == None:
                                st.write('**Publique** : ' + "Non communiqué")
                            else:
                                st.write('**Publique** : ' + f['public'])
                            st.write('**Note** : '+ str(f['score']) +' / 10')
                            st.write('**Description**: ')
                            st.write(f['description'])
                            st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                        st.markdown("""---""")
                else:
                    st.warning('😵‍💫 Impossible de trouver un film avec cette tranche de durée...')

        with st.expander("💯 - Recherche par Note"):
            st.markdown(
            "#  \n"
            f"Selectionner une note minimale pour la recherche de vos films.   \n"
            )
            score = st.slider( "Note minimale :",min_value=0.0, max_value=10.0, step=0.1)
            if st.button('Rechercher '):
                film_result = list(film.find({ "score": { "$gt": min} }).sort("score", -1))
                if len(film_result) > 0:
                    st.subheader(f'Voici les films qui ont plus de {score}/10 de score :')
                    for f in film_result:
                        col1, col2 = st.columns(2)
                        with col1:
                            try:
                                st.image(f['img_url'], width=300)
                            except:
                                st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)

                        with col2:
                            st.subheader(f['title'])
                            st.write("**Pays** : " + f['pays'])
                            st.write("**Date** : " + f['date'])
                            if f['public'] == None:
                                st.write('**Publique** : ' + "Non communiqué")
                            else:
                                st.write('**Publique** : ' + f['public'])
                            st.write('**Note** : '+ str(f['score']) +' / 10')
                            st.write('**Description**: ')
                            st.write(f['description'])
                            st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                        st.markdown("""---""")
                else:
                    st.warning(f'😵‍💫 Impossible de trouver un ayant plus de {score} score ...')


    with tab3:
        st.subheader('📺 Serie - Boite à Outils')
        st.markdown('Voici une boite à outils pour rechercher un Serie parmis une grande bibliothèque !')

        with st.expander("📋 - Recherche par Titre"):
            st.markdown(
                "#  \n"
                f"Entrer le nom de la serie que vous cherchez pour avoir des informations sur celle ci.  \n"
                )
            title = st.text_input(label='Entrer un titre de la serie : ', value='')
            if title != '':
                f = serie.find_one({'title':title})
                st.subheader(f'Voici le resultat pour le titre "{title}" :')
                if f != None:
                    col1, col2 = st.columns(2)
                    with col1:
                        try:
                            st.image(f['img_url'], width=300)
                        except:
                            st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)
                    with col2:
                        st.subheader(f['title'])
                        st.write("**Pays** : " + f['pays'])
                        st.write("**Date** : " + f['date'])
                        st.write('**Publique** : ' + f['public'])
                        st.write('**Note** : '+ str(f['score']) +' / 10')
                        st.write('**Description**: ')
                        st.write(f['description'])
                        st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                    st.markdown("""---""")
                else:
                    st.warning('😵‍💫 Impossible de trouver une serie avec ce titre...')

        with st.expander("⭐️ - Recherche par Nom d'acteur(s)"):
            st.markdown(
                "#  \n"
                f"Entrer le nom d'un ou plusieurs acteurs pour voir la liste des series ou il(s) joue(nt).   \n"
                )
            acteurs = serie.find()
            list_acteurs = []
            for a in acteurs:
                for i in a['acteurs']:
                    if i not in list_acteurs:
                        list_acteurs.append(i)
            acteurs = st.multiselect(
            'Entrer vos acteurs favoris : ',
            list_acteurs)
            serie_acteurs = list(serie.find({ "acteurs": { "$all": acteurs}}).sort("score", -1))
            if len(serie_acteurs) != 0:
                    st.subheader('Voici la liste des series ou apparaissent ces acteurs :')
                    for f in serie.find({ "acteurs": { "$all": acteurs}}).sort("score", -1):
                        col1, col2 = st.columns(2)
                        with col1:
                            try:
                                st.image(f['img_url'], width=300)
                            except:
                                st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)
                        with col2:
                            st.subheader(f['title'])
                            st.write("**Pays** : " + f['pays'])
                            st.write("**Date** : " + f['date'])
                            st.write('**Publique** : ' + f['public'])
                            st.write('**Note** : '+ str(f['score']) +' / 10')
                            st.write('**Description**: ')
                            st.write(f['description'])
                            st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                        st.markdown("""---""")
            elif len(serie_acteurs) == 0 and len(acteurs) > 0:
                st.warning('😵‍💫 Impossible de trouver une serie ou ces acteurs jouent ensembles...')

        with st.expander("🗂️ - Recherche par Genre"):
            st.markdown(
                "#  \n"
                f"Entrer votre Genre de serie favoris pour trouver les meilleurs series de cette catégorie.   \n"
                )
            genre = st.selectbox(
            "Selectionner un Genre de Serie :",
                ("Selectionner un genre", 'Documentary', 'Animation', 'Crime', 'Drama', 'Action', 'Adventure', 'Sci-Fi', 'Comedy', 'Biography', 'History', 'Thriller', 'Reality-TV', 'Mystery', 'War', 'Horror', 'Romance', 'Game-Show', 'Fantasy', 'Family', 'Music', 'Musical', 'Sport', 'Talk-Show', 'Western', 'Short', 'News')
            )
            if genre != "Selectionner un genre":
                series = serie.find({"genre" : genre}).sort("score", -1)
                st.subheader(f'Voici les series dans de genre "{genre}" dans notre bibliothèque :')
                for f in series:
                    col1, col2 = st.columns(2)
                    with col1:
                        try:
                            st.image(f['img_url'], width=300)
                        except:
                            st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)

                    with col2:
                        st.subheader(f['title'])
                        st.write("**Pays** : " + f['pays'])
                        st.write("**Date** : " + f['date'])
                        if f['public'] == None:
                            st.write('**Publique** : ' + "Non communiqué")
                        else:
                            st.write('**Publique** : ' + f['public'])
                        st.write('**Note** : '+ str(f['score']) +' / 10')
                        st.write('**Description**: ')
                        st.write(f['description'])
                        st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                    st.markdown("""---""")
        
        with st.expander("🕝 - Recherche par Durée"):
            st.markdown(
            "#  \n"
            f"Entrer la durée minimale et maximale en minutes pour découvrir les series qui sont dans cette tranche de durée !   \n"
            )
            col1, col2 = st.columns(2)
            with col1:
                min_s = st.slider( "⬇️ Durée Minimale (en minutes) :",min_value=1, max_value=300)
            with col2:
                max_s = st.slider( "⬆️ Durée Maximale (en minutes) :",min_value=1, max_value=300)
            if st.button(' Rechercher'):
                series_result = list(serie.find({ "duree": { "$gt": min_s, '$lt': max_s} }).sort("score", -1))
                if len(series_result) > 0:
                    st.subheader(f'Voici les series qui durent entre {min_s} et {max_s} minutes :')
                    for f in series_result:
                        col1, col2 = st.columns(2)
                        with col1:
                            try:
                                st.image(f['img_url'], width=300)
                            except:
                                st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)

                        with col2:
                            st.subheader(f['title'])
                            if f['pays'] == None:
                                st.write('**Pays** : ' + "Non communiqué")
                            else:
                                st.write('**Pays** : ' + f['pays'])
                            st.write("**Date** : " + f['date'])
                            if f['public'] == None:
                                st.write('**Publique** : ' + "Non communiqué")
                            else:
                                st.write('**Publique** : ' + f['public'])
                            st.write('**Note** : '+ str(f['score']) +' / 10')
                            st.write('**Description**: ')
                            st.write(f['description'])
                            st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                        st.markdown("""---""")
                else:
                    st.warning('😵‍💫 Impossible de trouver une serie avec cette tranche de durée...')

        with st.expander("💯 - Recherche par Note"):
            st.markdown(
            "#  \n"
            f"Selectionner une note minimale pour la recherche de vos series.   \n"
            )
            score = st.slider( "Note minimale:",min_value=0.0, max_value=10.0, step=0.1)
            if st.button(' Rechercher '):
                series_result = list(serie.find({ "score": { "$gt": min} }).sort("score", -1))
                if len(series_result) > 0:
                    st.subheader(f'Voici les series qui ont plus de {score}/10 de score :')
                    for f in series_result:
                        col1, col2 = st.columns(2)
                        with col1:
                            try:
                                st.image(f['img_url'], width=300)
                            except:
                                st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=300)

                        with col2:
                            st.subheader(f['title'])
                            st.write("**Pays** : " + f['pays'])
                            st.write("**Date** : " + f['date'])
                            if f['public'] == None:
                                st.write('**Publique** : ' + "Non communiqué")
                            else:
                                st.write('**Publique** : ' + f['public'])
                            st.write('**Note** : '+ str(f['score']) +' / 10')
                            st.write('**Description**: ')
                            st.write(f['description'])
                            st.markdown(f'[En savoir plus]({f["imdb_url"]})')
                        st.markdown("""---""")
                else:
                    st.warning(f'😵‍💫 Impossible de trouver un ayant plus de {score} score ...')

    with tab4:
        st.subheader('📘 Divers - Les Statistiques')
        st.markdown(
            f'Soon...'
        )

if radio == "💨 Quick Search":
    st.subheader('Quick Search 💨')
    st.markdown(
        '*💡 Cliquer sur **"Surprennez moi !"** pour avoir un film aléatoire.*'
    )
    st.write("Vous cherchez :")
    col1, col2 = st.columns(2)
    with col1:
        is_film = st.checkbox(label="un Film", value=True)
    with col2:
        is_serie = st.checkbox("une Série")

    title_search = st.text_input('Titre :' ,value='')

    list_acteurs=['Ne pas spécifier']
    for a in film.find():
        for i in a['acteurs']:
            if i not in list_acteurs:
                list_acteurs.append(i)
    for a in serie.find():
        for i in a['acteurs']:
            if i not in list_acteurs:
                list_acteurs.append(i)
    acteurs_search = st.multiselect('Avec comme acteurs : ', options=list_acteurs)
    genre_search = st.multiselect(
    " Selectionner un Genre :",
        ('Documentary', 'Animation', 'Crime', 'Drama', 'Action', 'Adventure', 'Sci-Fi', 'Comedy', 'Biography', 'History', 'Thriller', 'Reality-TV', 'Mystery', 'War', 'Horror', 'Romance', 'Game-Show', 'Fantasy', 'Family', 'Music', 'Musical', 'Sport', 'Talk-Show', 'Western', 'Short', 'News')
    )
    duree_search = st.slider(
        'Durée maximum (en minutes):', min_value=0, max_value=300, step=1
    )
    note_search = st.slider(
        ' Note minimale :', min_value=0.0, max_value=10.0, step=0.1
    )
    if st.button('Lancer la recherche'):
        if is_film:
            filters = [{ "score": { "$gt": note_search} }]
            if title_search != '':
                filters.append({"title" : title_search})
            if len(acteurs_search) != 0:
                filters.append({"acteurs": {"$all": acteurs_search}})
            if len(genre_search) != 0:
                filters.append({"genre" : {"$all": genre_search}})
            if duree_search != 0:
                filters.append({ "duree": {'$lt': duree_search} })
                

            dict_filter = {}
            for i in range(len(filters)):
                for k in filters[i]:
                    dict_filter[k] = filters[i][k] 
            list_film_result = list(film.find(dict_filter))

            if len(list_film_result) != 0:
                st.subheader('🥳 Voici les films qui correspondent à vos critères :')
                for result in list_film_result:
                    col1, col2 = st.columns(2)
                    with col1:
                        try:
                            st.image(result['img_url'], width=300)
                        except:
                            st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=3)
                    with col2:
                        st.subheader(result['title'])
                        st.write("**Pays** : " + result['pays'])
                        st.write("**Date** : " + result['date'])
                        if result['public'] == None:
                            st.write('**Publique** : ' + "Non communiqué")
                        else:
                            st.write('**Publique** : ' + result['public'])
                        st.write('**Note** : '+ str(result['score']) +' / 10')
                        st.write('**Description**: ')
                        st.write(result['description'])
                        st.markdown(f'[En savoir plus]({result["imdb_url"]})')
                    st.markdown("""---""")
            else:
                st.warning('😵‍💫 Aucun film ne corresponds à ces critères')

        if is_serie:
            filters = [{ "score": { "$gt": note_search} }]
            if title_search != '':
                filters.append({"title" : title_search})
            if len(acteurs_search) != 0:
                filters.append({"acteurs": {"$all": acteurs_search}})
            if len(genre_search) != 0:
                filters.append({"genre" : {"$all": genre_search}})
            if duree_search != 0:
                filters.append({ "duree": {'$lt': duree_search} })
                

            dict_filter = {}
            for i in range(len(filters)):
                for k in filters[i]:
                    dict_filter[k] = filters[i][k] 
            list_film_result = list(serie.find(dict_filter))
            if len(list_film_result) != 0:
                st.subheader('🥳 Voici les séries qui correspondent à vos critères :')
                for result in list_film_result:
                    col1, col2 = st.columns(2)
                    with col1:
                        try:
                            st.image(result['img_url'], width=300)
                        except:
                            st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=3)
                    with col2:
                        st.subheader(result['title'])
                        st.write("**Pays** : " + result['pays'])
                        st.write("**Date** : " + result['date'])
                        if result['public'] == None:
                            st.write('**Publique** : ' + "Non communiqué")
                        else:
                            st.write('**Publique** : ' + result['public'])
                        st.write('**Note** : '+ str(result['score']) +' / 10')
                        st.write('**Description**: ')
                        st.write(result['description'])
                        st.markdown(f'[En savoir plus]({result["imdb_url"]})')
                    st.markdown("""---""")
            else:
                 st.warning('😵‍💫 Aucune série ne corresponds à ces critères')
        elif is_film and is_serie:
            filters = [{ "score": { "$gt": note_search} }]
            if title_search != '':
                filters.append({"title" : title_search})
            if len(acteurs_search) != 0:
                filters.append({"acteurs": {"$all": acteurs_search}})
            if len(genre_search) != 0:
                filters.append({"genre" : {"$all": genre_search}})
            if duree_search != 0:
                filters.append({ "duree": {'$lt': duree_search} })
                

            dict_filter = {}
            for i in range(len(filters)):
                for k in filters[i]:
                    dict_filter[k] = filters[i][k] 
            list_film_result = list(film.find(dict_filter))
            list_serie_result = list(serie.find(dict_filter))
            list_total = list_film_result + list_serie_result

            if len(list_total) != 0:
                st.subheader('🥳 Voici les films / séries qui correspondent à vos critères :')
                for result in list_total:
                    col1, col2 = st.columns(2)
                    with col1:
                        try:
                            st.image(result['img_url'], width=300)
                        except:
                            st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=3)
                    with col2:
                        st.subheader(result['title'])
                        st.write("**Pays** : " + str(result['pays']))
                        st.write("**Date** : " + result['date'])
                        if result['public'] == None:
                            st.write('**Publique** : ' + "Non communiqué")
                        else:
                            st.write('**Publique** : ' + result['public'])
                        st.write('**Note** : '+ str(result['score']) +' / 10')
                        st.write('**Description**: ')
                        st.write(result['description'])
                        st.markdown(f'[En savoir plus]({result["imdb_url"]})')
                    st.markdown("""---""")
            else:
                st.warning('😵‍💫 Aucun film / série ne corresponds à ces critères')
    st.markdown(
        '#  \n'
        '**✨ Envie de nouveautés ?**  \n'
        )
    if st.button('Surprennez moi !'):
        film_result = list(film.find())
        serie_result = list(serie.find())
        result = choice(film_result + serie_result)
        try:
            AZERTYUIOP = result['nb_saison']
            result_type = "(Serie)"
        except:
            result_type = "(Film)"

        st.subheader('💥 Boom ! Voici notre suggestion :')
        col1, col2 = st.columns(2)
        with col1:
            try:
                st.image(result['img_url'], width=300)
            except:
                st.image("https://ih1.redbubble.net/image.1198305180.8026/fposter,small,wall_texture,product,750x1000.jpg", width=3)
        with col2:
            st.subheader(result['title'] + ' ' + result_type)
            st.write("**Pays** : " + result['pays'])
            st.write("**Date** : " + result['date'])
            if result['public'] == None:
                st.write('**Publique** : ' + "Non communiqué")
            else:
                st.write('**Publique** : ' + result['public'])
            st.write('**Note** : '+ str(result['score']) +' / 10')
            st.write('**Description**: ')
            st.write(result['description'])
            st.markdown(f'[En savoir plus]({result["imdb_url"]})')
        st.markdown("""---""")
