"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enrolling-ordinal.app
Prompt: Write a Python script that checks if a URL is flagged as a phishing site using a web API.
Generated: DETERMINISTIC_456b9a2b78e3db11
Batch ID: 20250612_162716
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://phishing-check-api.example.com/v1/check": {
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

# Constants for the API endpoint and API key
API_BASE_URL = "https://phishing-check-api.example.com/v1/check"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

def check_url_phishing(url):
    """
    Function to check if a URL is flagged as a phishing site using a web API.
    
    Args:
        url (str): The URL to be checked.
    
    Returns:
        dict: A dictionary containing the API response.
    """
    try:
        # Prepare the request headers and payload
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {"url": url}

        # Send the request to the API
        response = requests.post(API_BASE_URL, json=payload, headers=headers)
        
        # Raise an HTTPError if the response status code indicates an error
        response.raise_for_status()
        
        # Return the JSON response from the API
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print(f"An error occurred while checking the URL: {e}")
        return {"error": "Unable to check URL due to an error."}

def main():
    """
    Main function to prompt the user for a URL and check if it's flagged as phishing.
    """
    print("Phishing URL Checker")
    print("=====================")
    
    # Prompt the user for a URL
    url = input("Enter the URL to check: ").strip()
    
    # Validate the input
    if not url:
        print("Error: URL cannot be empty.")
        return
    
    # Check the URL using the phishing-check API
    result = check_url_phishing(url)
    
    # Display the results
    if "error" in result:
        print("Failed to check the URL. Please try again later.")
    else:
        is_phishing = result.get("is_phishing", False)  # Assuming the API response contains a key 'is_phishing'
        if is_phishing:
            print(f"The URL '{url}' is flagged as a phishing site.")
        else:
            print(f"The URL '{url}' is not flagged as a phishing site.")

if __name__ == "__main__":
    main()
```
