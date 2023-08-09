import random

from JoomlaAPI import JoomlaAPI

def create_dynamic_article(title, content, category_id, alias=None):
    # Initialize the JoomlaAPI class with the provided parameters
    joomla = JoomlaAPI(auth_apikey="c2hhMjU2Ojc4Mzo2Mjg2ZTg4OGNiNjJmZWI5NWJiOGUzZTVlMTdkZjVhMjUxZTA2N2YxZGViYTkxNDMzYjgyMTRhYTQzOTI2ZmU5", 
                       base_url="http://localhost/joomla", base_path="/api/index.php/v1")

    # Create the article with the provided details
    response_article = joomla.create_article(title, content, category_id, alias)
    return response_article

# Sample execution (this can be replaced by dynamic values from ChatGPT or user input)
response = create_dynamic_article(
    title="Dynamic Test Article",
    content="This is a dynamically created test article using the JoomlaAPI class from ChatGPT.",
    category_id=13,  # Example category ID
    alias="dynamic-test-article"
)

print(response)
