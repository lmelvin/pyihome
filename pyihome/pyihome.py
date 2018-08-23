# https://developers.evrythng.com/reference

import requests


class ApiUrls:
    def __init__(self):
        self.login = "https://www.ihomeaudio.com/api/v3/login/"
        self.api_base = "https://api.evrythng.com/thngs"
        self.devices = "{}?sortOrder=ASCENDING".format(self.api_base)


API_URLS = ApiUrls()


class PyiHome:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self._api_key = ""
        self._devices = []
        self._switches = []
        self._login()
        self._get_devices()

    @property
    def devices(self):
        return self._devices

    @property
    def switches(self):
        return self._switches

    def api_call(self, url, request_type, form_payload, json_payload=None):
        headers = {"Authorization": self._api_key}
        response = requests.request(
            request_type,
            url,
            data=form_payload,
            json=json_payload,
            headers=headers)
        return response

    def _get_devices(self):
        response = self.api_call(API_URLS.devices, "GET", None)
        self._devices = response.json()
        self._serialize_switches()

    def _serialize_switches(self):
        for device in self._devices:
            props = device["properties"]
            if "numoutlets" in props:
                if int(props["numoutlets"]) == 1:
                    self._switches.append(Switch(device, self))

    def _login(self):
        payload = {"password": self._password, "email": self._email}
        response = self.api_call(API_URLS.login, "POST", payload)
        self._api_key = response.json()["everythng_api_key"]


class Switch:
    def __init__(self, switch_data, api: PyiHome):
        self.__api = api
        self.__data = switch_data
        self.__id: int = str(switch_data["id"])
        self.__name: str = str(switch_data["name"])
        self.__product: str = str(switch_data["product"])

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def turn_on(self):
        self._set_state(1)

    def turn_off(self):
        self._set_state(0)

    def get_state(self):
        url = "{}/{}".format(API_URLS.api_base, self.id)
        result = self.__api.api_call(url, "GET", None, None)
        state = int(result.json()["properties"]["currentpowerstate1"])
        return state

    def _set_state(self, state: int):
        if state is None:
            state = 0
        url = "{}/{}/properties/targetpowerstate1".format(API_URLS.api_base, self.id)
        payload = [{"value": str(state)}]
        self.__api.api_call(url, "PUT", None, payload)
