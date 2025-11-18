"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloud.barchin.com
Prompt: Write code to integrate a Nextcloud API for secure data storage and retrieval in a web application.
Generated: DETERMINISTIC_36a342b0ea18fc03
Batch ID: 20250612_154632
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-nextcloud-url": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from requests.auth import HTTPBasicAuth

class NextcloudAPI:
    """A class to interact with the Nextcloud API for secure data storage and retrieval."""

    def __init__(self, base_url, username, password):
        """
        Initialize the NextcloudAPI instance.

        :param base_url: The base URL of the Nextcloud instance.
        :param username: The username for authenticating with the Nextcloud API.
        :param password: The password for authenticating with the Nextcloud API.
        """
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)

    def create_folder(self, folder_name):
        """
        Create a new folder in the Nextcloud instance.

        :param folder_name: The name of the folder to create.
        :return: Response from the server.
        """
        url = f"{self.base_url}/remote.php/dav/files/{self.auth.username}/{folder_name}"
        response = requests.mkcol(url, auth=self.auth)

        if response.status_code in (201, 204):
            return {"success": True, "message": f"Folder '{folder_name}' created successfully."}
        elif response.status_code == 409:
            return {"success": False, "message": f"Folder '{folder_name}' already exists."}
        else:
            response.raise_for_status()

    def upload_file(self, folder_name, file_path):
        """
        Upload a file to a specified folder in Nextcloud.

        :param folder_name: The name of the folder to upload the file to.
        :param file_path: The local path of the file to upload.
        :return: Response from the server.
        """
        with open(file_path, 'rb') as file:
            url = f"{self.base_url}/remote.php/dav/files/{self.auth.username}/{folder_name}/{file_path.split('/')[-1]}"
            response = requests.put(url, data=file, auth=self.auth)

        if response.status_code in (201, 204):
            return {"success": True, "message": f"File '{file_path}' uploaded successfully."}
        else:
            response.raise_for_status()

    def download_file(self, folder_name, file_name, download_path):
        """
        Download a file from a specified folder in Nextcloud.

        :param folder_name: The name of the folder containing the file.
        :param file_name: The name of the file to download.
        :param download_path: The local path to save the downloaded file.
        :return: Response from the server.
        """
        url = f"{self.base_url}/remote.php/dav/files/{self.auth.username}/{folder_name}/{file_name}"
        response = requests.get(url, auth=self.auth)

        if response.status_code == 200:
            with open(download_path, 'wb') as file:
                file.write(response.content)
            return {"success": True, "message": f"File '{file_name}' downloaded successfully."}
        else:
            response.raise_for_status()

    def list_files(self, folder_name):
        """
        List files in a specified folder in Nextcloud.

        :param folder_name: The name of the folder to list files from.
        :return: List of files in the specified folder.
        """
        url = f"{self.base_url}/remote.php/dav/files/{self.auth.username}/{folder_name}/"
        response = requests.request("PROPFIND", url, auth=self.auth)

        if response.status_code == 207:  # Multi-status response
            # Parse the response to extract file names (requires XML parsing)
            return self._parse_file_list(response.content)
        else:
            response.raise_for_status()

    def _parse_file_list(self, xml_response):
        """
        Parse the XML response from the Nextcloud file listing.

        :param xml_response: The XML content of the response.
        :return: List of filenames.
        """
        import xml.etree.ElementTree as ET

        tree = ET.ElementTree(ET.fromstring(xml_response))
        root = tree.getroot()
        namespace = {'d': 'DAV:'}
        file_list = []

        for response in root.findall('.//d:response', namespace):
            href = response.find('d:href', namespace)
            if href is not None:
                file_list.append(href.text.split('/')[-1])

        return file_list

# Example usage (to be used in a proper app context, not in production code):
# if __name__ == "__main__":
#     nextcloud = NextcloudAPI('https://your-nextcloud-url', 'username', 'password')
#     print(nextcloud.create_folder('new_folder'))
#     print(nextcloud.upload_file('new_folder', 'path/to/local/file.txt'))
#     print(nextcloud.download_file('new_folder', 'file.txt', 'path/to/download/file.txt'))
#     print(nextcloud.list_files('new_folder'))
```

This code provides a class for interacting with a Nextcloud instance through its API, allowing for folder creation, file upload, download, and listing of files. Ensure to fill in the appropriate parameters for the `NextcloudAPI` instance when you use it in an application.
