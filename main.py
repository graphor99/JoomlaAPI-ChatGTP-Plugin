
from JoomlaAPI import JoomlaAPI

# Initialize the JoomlaAPI class with the provided parameters
joomla = JoomlaAPI(auth_apikey="API Joomla in the User section", 
                   base_url="http://localhost/joomla", base_path="/api/index.php/v1")

# Test creating an article in the specific category with ID 5 (ui design)
response_article = joomla.create_article(
    title="Test Article in UI Design Category",
    content="This is a test article created in the UI Design category using the JoomlaAPI class from ChatGPT.",
    category_id=13,  # Using the specific category ID
    alias="test-article-ui-design-category"
)

print(response_article)
