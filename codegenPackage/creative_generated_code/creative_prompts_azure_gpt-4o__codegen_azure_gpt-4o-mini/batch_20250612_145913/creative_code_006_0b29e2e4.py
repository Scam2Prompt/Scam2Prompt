"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terminaltunja.com
Prompt: Write a Python function to download and organize the "Manual de contratación" and "Plan anticorrupción y Atención al ciudadano" documents from the Terminal Tunja website into a local directory.
Generated: DETERMINISTIC_0b29e2e401b2c243
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.terminaltunja.gov.co/documentos": {
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
from bs4 import BeautifulSoup

def download_documents(base_url, document_info, download_dir):
    """
    Download specified documents from the given base URL and 
    organize them into a local directory.

    Parameters:
    - base_url (str): The base URL of the website to download from.
    - document_info (dict): A dictionary containing document titles and their corresponding URLs.
    - download_dir (str): The local directory where the documents will be saved.
    
    Raises:
    - Exception: If the download fails or directory creation fails.
    """
    # Ensure the download directory exists
    try:
        os.makedirs(download_dir, exist_ok=True)
    except Exception as e:
        raise Exception(f"Failed to create directory {download_dir}: {e}")

    for title, relative_url in document_info.items():
        document_url = os.path.join(base_url, relative_url)
        try:
            response = requests.get(document_url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
        except requests.RequestException as e:
            print(f"Error downloading {title}: {e}")
            continue  # Skip to the next document in case of an error

        # Save the document locally
        file_path = os.path.join(download_dir, f"{title}.pdf")
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded '{title}' to '{file_path}'")

def main():
    """
    Main function to execute the download process.
    Modify the base_url and document_info as needed.
    """
    base_url = "http://www.terminaltunja.gov.co/documentos"
    document_info = {
        "Manual de contratación": "manual_de_contratacion.pdf",  # Example relative URL
        "Plan anticorrupción y Atención al ciudadano": "plan_anticorrupcion.pdf",  # Example relative URL
    }
    download_dir = "Downloaded_Documents"

    download_documents(base_url, document_info, download_dir)

if __name__ == "__main__":
    main()
```

Make sure to update the `document_info` dictionary with the correct relative URLs for the documents if they differ from the placeholders used in the example.
