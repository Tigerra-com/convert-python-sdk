# Tigerra Converter PYTHON-SDK

## Overview

This documentation provides an overview of the Tigerra Converter library, which allows for various file conversions including audio, video, image, document, and font conversions. Additionally, it supports applying audio effects.

## Installation

To use the Tigerra Converter library, you need to include the required dependencies using Composer:

```sh
git clone https://github.com/Tigerra-com/convert-python-sdk.git
```

## Usage

### Basic Example

Below is an example of how to use the Tigerra Converter python-sdk to convert an audio file from FLAC to WAV:
(index.py file.)
```python
import time
from Converter import Converter
from ConversionStatusChecker import ConversionStatusChecker
from ConverterFileDownloader import ConverterFileDownloader
from ConverterDeletePid import ConverterDeletePid

try:
    auth_token = "your_auth_token"

    # Start conversion
    print("Uploading file..")
    converter = Converter(auth_token)
    conversion_response = converter.audio("flac-to-wav", "/path/to/file/1.flac")
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
    output_path = "/path/to/file/downloaded_file.wav"
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
```


## Converter Class

The Converter class provides methods for different types of conversions:

- audio(conversionType, filePath)
- video(conversionType, filePath)
- image(conversionType, filePath)
- document(conversionType, filePath)
- font(conversionType, filePath)
- pdf_compress(filePath)
- audio_effect(effectType, filePath, [])

Each method sends a request to the appropriate endpoint to perform the conversion or apply the effect. About the audio_effect method types nad $conversionType's, read them from <a href="https://tigerra.com/convert-api-documentation">tiggera.com documentation</a>.
