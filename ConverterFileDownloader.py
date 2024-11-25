import requests
from BaseConverterApiClient import BaseConverterApiClient

class ConverterFileDownloader(BaseConverterApiClient):
    def download_file(self, download_url, output_path):
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }

        response = requests.get(download_url, headers=headers, stream=True)
        if response.status_code != 200:
            raise Exception("Failed to download file.")

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return output_path