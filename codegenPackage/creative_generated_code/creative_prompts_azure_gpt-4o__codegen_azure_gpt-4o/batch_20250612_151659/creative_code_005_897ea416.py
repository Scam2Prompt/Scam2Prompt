"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahopefulme.com
Prompt: Provide code to implement a feature for downloading e-books and magazines from a social network platform, similar to HopefulMe's download options.
Generated: DETERMINISTIC_897ea4160043d202
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://socialnetwork.com/api": {
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
import os
import requests

class ContentDownloader:
    """
    A class to handle downloading of e-books and magazines from a social network platform.
    """

    def __init__(self, base_url, download_directory="downloads"):
        """
        Initializes the downloader with the base URL and download directory.

        :param base_url: The URL of the platform's API or file server.
        :param download_directory: Local directory to save downloaded files.
        """
        self.base_url = base_url
        self.download_directory = download_directory

        # Ensure the download directory exists
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

    def download_content(self, content_id, content_type):
        """
        Downloads a specific e-book or magazine based on its content ID.

        :param content_id: Unique identifier of the content to be downloaded.
        :param content_type: Type of content to download, e.g., 'ebook' or 'magazine'.
        :return: Path to the downloaded file, or None if an error occurred.
        """
        if content_type not in ['ebook', 'magazine']:
            print("Error: Unsupported content type.")
            return None

        try:
            # Build the download URL
            download_url = f"{self.base_url}/{content_type}/{content_id}"

            # Send the request to retrieve the file
            response = requests.get(download_url, stream=True)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Extract the filename from the headers or default to content_id
            filename = response.headers.get('Content-Disposition', f"{content_id}.pdf")
            if 'filename=' in filename:
                filename = filename.split('filename=')[-1].strip('"')

            # Save the file locally
            file_path = os.path.join(self.download_directory, filename)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Download successful: {file_path}")
            return file_path

        except requests.exceptions.RequestException as e:
            print(f"Error downloading content: {e}")
            return None

    def list_downloaded_files(self):
        """
        Lists all files in the download directory.

        :return: List of filenames in the download directory.
        """
        try:
            files = os.listdir(self.download_directory)
            return files
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Initialize the downloader with the platform's base URL
    downloader = ContentDownloader(base_url="https://socialnetwork.com/api")

    # Download an e-book
    downloader.download_content(content_id="12345", content_type="ebook")

    # Download a magazine
    downloader.download_content(content_id="67890", content_type="magazine")

    # List all downloaded files
    downloaded_files = downloader.list_downloaded_files()
    print("Downloaded files:", downloaded_files)
```
