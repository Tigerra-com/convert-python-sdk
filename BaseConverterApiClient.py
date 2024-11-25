import requests

class BaseConverterApiClient:
    API_URL = "https://convert.tigerra.com"

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def send_request(self, method, endpoint, params=None, file_path=None):
        if params is None:
            params = {}

        url = f"{self.API_URL}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }

        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif method.upper() == 'POST':
            if file_path:
                with open(file_path, 'rb') as file:
                    files = {'file': file}
                    response = requests.post(url, headers=headers, files=files, data=params)
            else:
                response = requests.post(url, headers=headers, data=params)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers, data=params)
        else:
            raise ValueError("Unsupported HTTP method")

        if response.status_code != 200:
            response.raise_for_status()

        return response.json()