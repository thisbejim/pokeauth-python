import requests
import json
import time
from requests.exceptions import HTTPError


class login:
    def __init__(self, email, password):
        self.api_key = "AIzaSyDIO0qyF90wiDcg2uYXVQf_RuJnOLlbr68"
        self.database_url = "https://pokeauth.firebaseio.com"
        self.id = ""
        self.token = ""
        self.refreshToken = ""
        self.expiry = 0
        self.credentials = None
        self.requests = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=3)
        for scheme in ('http://', 'https://'):
            self.requests.mount(scheme, adapter)
        self.login(email, password)

    def login(self, email, password):
        # set new expiry
        self.get_expiry()
        # make request
        request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={0}".format(self.api_key)
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
        request_object = requests.post(request_ref, headers=headers, data=data)
        raise_detailed_error(request_object)
        # save details
        developer = request_object.json()
        self.id = developer["localId"]
        self.token = developer["idToken"]
        self.refreshToken = developer["refreshToken"]

    def get_user_token(self, uid):
        if time.time() >= self.expiry:
            self.refresh()
        request_ref = "{0}/users/{1}/access.json?auth={2}".format(self.database_url, uid, self.token)
        headers = {"content-type": "application/json; charset=UTF-8"}
        request_object = requests.get(request_ref, headers=headers)
        raise_detailed_error(request_object)
        access = request_object.json()
        return access

    def refresh(self):
        request_ref = "https://securetoken.googleapis.com/v1/token?key={0}".format(self.api_key)
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"grantType": "refresh_token", "refreshToken": self.refreshToken})
        request_object = requests.post(request_ref, headers=headers, data=data)
        raise_detailed_error(request_object)
        developer = request_object.json()
        self.id = developer["user_id"]
        self.token = developer["id_token"]
        self.refreshToken = developer["refresh_token"]

    def get_expiry(self):
        seconds_in_one_hour = 3600
        self.expiry = int(time.time()+seconds_in_one_hour)


def raise_detailed_error(request_object):
    try:
        request_object.raise_for_status()
    except HTTPError as e:
        # raise detailed error message
        raise HTTPError(e, request_object.text)