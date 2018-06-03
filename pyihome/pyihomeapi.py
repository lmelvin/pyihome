import requests
import json

# https://developers.evrythng.com/reference
class ApiUrls:
    def __init__(self):
        self.login = "https://www.ihomeaudio.com/api/v3/login/"
        self.api_base = "https://api.evrythng.com/thngs"
        self.devices = self.api_base + "?sortOrder=ASCENDING"

class ApiHeaders:
    def __init__(self):
        self._api_key = ""

API_URLS = ApiUrls()
API_HEADERS = ApiHeaders()

class PyiHomeApi:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self.login()

    def api_call(self, url, type, formPayload, jsonPayload=None):
        headers = {"Authorization": API_HEADERS._api_key}
        response = requests.request(type, url, data=formPayload, json=jsonPayload, headers=headers)
        return response
    
    def get_devices(self):
        response = self.api_call(API_URLS.devices, "GET", None)
        return response.json()

    def login(self):
        payload = {"password": self._password, "email": self._email}
        response = self.api_call(API_URLS.login, "POST", payload)
        API_HEADERS._api_key = response.json()["everythng_api_key"]

    class Switch:
        def get_state(self, device_id):
            url = "{}/{}".format(API_URLS.api_base, device_id)
            result = PyiHomeApi.api_call(self, url, "GET", None, None)
            state = int(result.json()["properties"]["currentpowerstate1"])
            return state

        def turn_on(self, device_id):
            self._set_state(device_id, 1)
        
        def turn_off(self, device_id):
            self._set_state(device_id, 0)
        
        def _set_state(self, device_id, state):
            if state == None:
                state = 0
            url = "{}/{}/properties/targetpowerstate1".format(API_URLS.api_base, device_id)
            payload = [{"value":str(state)}]
            PyiHomeApi.api_call(self, url, "PUT", None, payload)