import requests

class JoomlaAPI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_article(self, title, content, category_id, alias, language="*", metadesc="", metakey=""):
        url = f"{self.base_url}/api/index.php/v1/content/article"
        data = {
            "alias": alias,
            "articletext": content,
            "catid": category_id,
            "language": language,
            "metadesc": metadesc,
            "metakey": metakey,
            "title": title
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def create_category(self, title, description):
        url = f"{self.base_url}/api/index.php/v1/content/category"
        data = {
            "title": title,
            "description": description
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()
