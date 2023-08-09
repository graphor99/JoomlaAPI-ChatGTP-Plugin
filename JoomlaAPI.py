
import requests

class JoomlaAPI:
    def __init__(self, auth_apikey, base_url, base_path="/api/index.php/v1"):
        self.auth_apikey = auth_apikey
        self.base_url = base_url.rstrip("/")  # Ensure no trailing slash
        self.base_path = base_path.rstrip("/")  # Ensure no trailing slash
        self.headers = {
            "Content-Type": "application/json",
            "X-Joomla-Token": self.auth_apikey
        }

    def create_article(self, title, content, category_id=2, alias=None):
        endpoint = f"{self.base_url}{self.base_path}/content/articles"
        
        # If no alias is provided, use the title but replace spaces with hyphens
        if alias is None:
            alias = title.replace(" ", "-").lower()

        data = {
            "alias": alias,
            "articletext": content,
            "catid": category_id,
            "language": "*",
            "metadesc": "",
            "metakey": "",
            "title": title
        }

        response = requests.post(endpoint, headers=self.headers, json=data)
        return response.json()
    
    # Category management methods
    def create_category(self, title, alias=None, parent_id=1):
        endpoint = f"{self.base_url}{self.base_path}/content/categories"
        if alias is None:
            alias = title.replace(" ", "-").lower()
        data = {
            "title": title,
            "alias": alias,
            "parent_id": parent_id
        }
        response = requests.post(endpoint, headers=self.headers, json=data)
        return response.json()

    def get_category(self, category_id):
        endpoint = f"{self.base_url}{self.base_path}/content/categories/{category_id}"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

    def update_category(self, category_id, updated_data):
        endpoint = f"{self.base_url}{self.base_path}/content/categories/{category_id}"
        response = requests.patch(endpoint, headers=self.headers, json=updated_data)
        return response.json()

    def delete_category(self, category_id):
        endpoint = f"{self.base_url}{self.base_path}/content/categories/{category_id}"
        response = requests.delete(endpoint, headers=self.headers)
        return response.json()

    def list_categories(self, filters=None):
        endpoint = f"{self.base_url}{self.base_path}/content/categories"
        if filters:
            params = filters
            response = requests.get(endpoint, headers=self.headers, params=params)
        else:
            response = requests.get(endpoint, headers=self.headers)
        return response.json()

    # Tag management methods (Note: Tags management is limited in Joomla API as of my last update)
    def list_tags(self):
        endpoint = f"{self.base_url}{self.base_path}/tags"
        response = requests.get(endpoint, headers=self.headers)
        return response.json()

