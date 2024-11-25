from BaseConverterApiClient import BaseConverterApiClient

class ConverterDeletePid(BaseConverterApiClient):
    def delete(self, pid):
        return self.send_request('DELETE', f"/delete-pid/{pid}")