import requests
import json

class ApiUrls:
    def __init__(self):        
        self.login = "https://www.ihomeaudio.com/api/v3/login/"
        self.api_base = "https://api.evrythng.com"
        self.devices = self.api_base + "/thngs?sortOrder=ASCENDING"

API_URLS = ApiUrls()

class Switch:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self._api_key = ""
        self.login()

    def get_devices(self):
        headers = {"Authorization": self._api_key}
        response = requests.get(API_URLS.devices, headers=headers)
        return response.json()

    def login(self):
        payload = {"password": self._password, "email": self._email}
        response = requests.post(API_URLS.login, payload)
        self._api_key = response.json()["everythng_api_key"]