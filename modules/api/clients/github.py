import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def serch_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def __init__(self, base_url="https://api.github.com"):
        self.base_url = base_url

    def get_emojis(self):
        url = f"{self.base_url}/emojis"
        response = requests.get(url)
        return response.json()

    def list_commits(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        response = requests.get(url)
        return response.json()
