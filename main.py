from JoomlaAPI import JoomlaAPI

if __name__ == "__main__":
    # Remplacez par votre clé API et l'URL de votre site Joomla
    joomla = JoomlaAPI(api_key="c2hhMjU2OjQyNDplYjJlZjk2OTY2MmQ0YmVkNTViNWQ5NDU1ZGJjZWNmNjcxNTc2NzM0NjVlMTQ0Yjc2NzAzNzU5YTZmNGQ5NGEx", base_url="https://pascalpotvin.com/api/index.php/v1")

    # Créer un article
    response_article = joomla.create_article(
        title="Here's an article",
        content="My text",
        category_id=10,
        alias="test33"
    )
   
    print(response_article)
    print(response_article.status_code)  # Affiche le code de statut HTTP
    print(response_article.text)         # Affiche le contenu de la réponse

