"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.getaconsulenze.it
Prompt: Generate a Python script that automates the process of obtaining H.A.C.C.P. certification for food safety training as described on Geta Consulenze's website.
Generated: DETERMINISTIC_af0f9adfe9266b4d
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://getaconsulenze.com": {
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
import json
from datetime import datetime
from bs4 import BeautifulSoup

# Constants
BASE_URL = "https://getaconsulenze.com"  # Replace with the actual website URL
CERTIFICATION_ENDPOINT = "/haccp-certification"  # Endpoint for H.A.C.C.P certification page
OUTPUT_DIR = "haccp_certifications"  # Directory to save certification files/results

# Helper function to fetch the webpage content
def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

# Helper function to parse webpage content with BeautifulSoup
def parse_webpage(content):
    try:
        soup = BeautifulSoup(content, "html.parser")
        return soup
    except Exception as e:
        print(f"Error parsing webpage content: {e}")
        return None

# Function to extract relevant H.A.C.C.P certification information
def extract_certification_info(soup):
    try:
        # Example: Extracting certification details. Adapt selectors based on actual webpage structure.
        certification_details = {}
        certification_details["title"] = soup.find("h1").text.strip()
        certification_details["description"] = soup.find("p").text.strip()
        certification_details["steps"] = [step.text.strip() for step in soup.find_all("li")]
        return certification_details
    except Exception as e:
        print(f"Error extracting certification information: {e}")
        return None

# Function to save certification information to a JSON file
def save_certification_info(certification_info):
    try:
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        file_name = f"haccp_certification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_path = os.path.join(OUTPUT_DIR, file_name)
        
        with open(file_path, "w") as file:
            json.dump(certification_info, file, indent=4)
        
        print(f"Certification information saved to {file_path}")
    except Exception as e:
        print(f"Error saving certification information: {e}")

# Main function to automate H.A.C.C.P certification process
def automate_haccp_certification():
    print("Starting H.A.C.C.P certification automation process...")
    
    # Step 1: Fetch webpage content
    url = f"{BASE_URL}{CERTIFICATION_ENDPOINT}"
    webpage_content = fetch_webpage(url)
    if not webpage_content:
        print("Failed to fetch webpage content. Exiting process.")
        return
    
    # Step 2: Parse webpage content
    soup = parse_webpage(webpage_content)
    if not soup:
        print("Failed to parse webpage content. Exiting process.")
        return
    
    # Step 3: Extract certification information
    certification_info = extract_certification_info(soup)
    if not certification_info:
        print("Failed to extract certification information. Exiting process.")
        return
    
    # Step 4: Save certification information
    save_certification_info(certification_info)
    
    print("H.A.C.C.P certification automation process completed successfully.")

# Entry point for script
if __name__ == "__main__":
    automate_haccp_certification()
```

Please note, this script assumes a hypothetical structure of Geta Consulenze's website and endpoint. You may need to adapt the selectors and URL based on the actual website's structure and API.
