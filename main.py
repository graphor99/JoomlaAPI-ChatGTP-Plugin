
from JoomlaAPI import JoomlaAPI
import random

# Initialize the JoomlaAPI class with the provided parameters
joomla = JoomlaAPI(auth_apikey="YOUR_API_KEY_HERE", 
                   base_url="http://localhost/joomla", 
                   base_path="/api/index.php/v1")

# Test creating an article in a specific category
response_article = joomla.create_article(
    title="Test Article",
    content="This is a test article content.",
    category_id=2,  # Example category ID
    alias=f"test-article-{random.randint(1, 10000)}",
    language="en-GB",
    metakey="example, test, article",
    metadesc="This is a test article description."
)

print(response_article)

# List all articles
articles = joomla.list_articles()
print(articles)

# If you have an article ID from previous operations, you can use the following methods:

# Get specific article details
# article_details = joomla.get_article(ARTICLE_ID_HERE)
# print(article_details)

# Update an article
# updated_data = {
#     "title": "Updated Title",
#     "articletext": "Updated content for the article."
# }
# update_response = joomla.update_article(ARTICLE_ID_HERE, updated_data)
# print(update_response)

# Delete an article
# delete_response = joomla.delete_article(ARTICLE_ID_HERE)
# print(delete_response)
