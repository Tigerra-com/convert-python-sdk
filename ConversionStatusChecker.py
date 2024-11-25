from BaseConverterApiClient import BaseConverterApiClient

class ConversionStatusChecker(BaseConverterApiClient):
    STATUS_PENDING = 'pending'
    STATUS_COMPLETED = 'completed'
    STATUS_UPLOAD_ERROR = 'upload_error'
    STATUS_PROCESS_ERROR = 'process_error'
    STATUS_CONVERT_ERROR = 'convert_error'

    def check_status(self, pid):
        endpoint = f"/get-status/{pid}"
        return self.send_request('GET', endpoint)