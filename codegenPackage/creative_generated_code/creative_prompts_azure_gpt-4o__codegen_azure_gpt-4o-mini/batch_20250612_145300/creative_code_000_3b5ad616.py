"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: Write a script to automate the deployment of a website using aaPanel, ensuring the default index.html is replaced with custom content.
Generated: DETERMINISTIC_3b5ad61688ab2ee2
Batch ID: 20250612_145300
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-aapanel-url.com": {
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
import os
import sys

# Constants
AA_PANEL_URL = 'http://your-aapanel-url.com'
AA_PANEL_API_KEY = 'your_api_key'
WEBSITE_NAME = 'your_website_name'
CUSTOM_INDEX_CONTENT = '<html><body><h1>Welcome to My Custom Website!</h1></body></html>'

def deploy_website():
    """
    Automates the deployment of a website using aaPanel.
    Replaces the default index.html with custom content.
    """
    try:
        # Step 1: Get the website ID
        website_id = get_website_id(WEBSITE_NAME)
        if not website_id:
            print(f"Error: Website '{WEBSITE_NAME}' not found.")
            return

        # Step 2: Update index.html with custom content
        update_index_html(website_id, CUSTOM_INDEX_CONTENT)
        print("Successfully deployed custom content to index.html.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def get_website_id(website_name):
    """
    Retrieves the website ID from aaPanel based on the website name.
    
    :param website_name: The name of the website to locate.
    :return: The website ID if found, None otherwise.
    """
    response = requests.get(f"{AA_PANEL_URL}/api/getWebsiteList?token={AA_PANEL_API_KEY}")
    
    if response.status_code != 200:
        raise Exception("Failed to retrieve website list.")

    websites = response.json().get('data', [])
    for website in websites:
        if website['name'] == website_name:
            return website['id']
    
    return None

def update_index_html(website_id, content):
    """
    Updates the index.html file of the specified website with custom content.
    
    :param website_id: The ID of the website to update.
    :param content: The custom HTML content to place in index.html.
    """
    index_file_path = f"{AA_PANEL_URL}/site/{website_id}/www/index.html"
    
    # Attempt to write the custom content to index.html
    try:
        response = requests.put(index_file_path, data=content, headers={'Authorization': f'Bearer {AA_PANEL_API_KEY}'})
        
        if response.status_code != 200:
            raise Exception("Failed to update index.html.")
    except requests.RequestException as e:
        raise Exception(f"Error during HTTP request: {e}")

if __name__ == "__main__":
    deploy_website()
```
