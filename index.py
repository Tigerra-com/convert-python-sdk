import time
from Converter import Converter
from ConversionStatusChecker import ConversionStatusChecker
from ConverterFileDownloader import ConverterFileDownloader
from ConverterDeletePid import ConverterDeletePid

try:
    auth_token = "1|vRUHtpKXq12Rf9Ra1vsBPDLWwIEtZrrWQFYYHoGO14a25d17"

    # Start conversion
    print("Uploading file..")
    converter = Converter(auth_token)
    conversion_response = converter.audio("flac-to-wav", "/Users/kirilkirkov/Downloads/1.flac")
    pid = conversion_response['pid']
    print(f"Conversion started. PID: {pid}")

    # Check status
    status_checker = ConversionStatusChecker(auth_token)
    while True:
        status_response = status_checker.check_status(pid)
        status = status_response['status']
        print(f"Status: {status}")

        if status == ConversionStatusChecker.STATUS_COMPLETED:
            break
        elif status in [
            ConversionStatusChecker.STATUS_UPLOAD_ERROR,
            ConversionStatusChecker.STATUS_PROCESS_ERROR,
            ConversionStatusChecker.STATUS_CONVERT_ERROR
        ]:
            raise Exception(f"Error occurred: {status}")

        time.sleep(2)

    # Download file
    download_url = status_response['data']
    downloader = ConverterFileDownloader(auth_token)
    output_path = "/Users/kirilkirkov/Downloads/downloaded_file.wav"
    downloader.download_file(download_url, output_path)
    print(f"File downloaded to: {output_path}")

    # Delete PID
    delete_pid = ConverterDeletePid(auth_token)
    r = delete_pid.delete(pid)
    if r['success']:
        print("PID deleted successfully.")
    else:
        print(f"Error deleting PID: {r['message']}")

except Exception as e:
    print(f"Error: {e}")