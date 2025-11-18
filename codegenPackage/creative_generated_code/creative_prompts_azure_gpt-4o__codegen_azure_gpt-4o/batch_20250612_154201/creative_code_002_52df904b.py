"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webward.app
Prompt: Generate a script to check the availability of domain names through Porkbun.com and automatically purchase one if available.
Generated: DETERMINISTIC_52df904bfe9883ab
Batch ID: 20250612_154201
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.porkbun.com/v3": {
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
import sys

# Constants
API_BASE_URL = "https://api.porkbun.com/v3"
API_KEY = "your_api_key_here"  # Replace with your Porkbun API key
SECRET_KEY = "your_secret_key_here"  # Replace with your Porkbun API secret

def check_domain_availability(domain_name):
    """
    Check if a domain name is available for registration using Porkbun API.
    
    Parameters:
        domain_name (str): The domain name to check.
    
    Returns:
        bool: True if the domain is available, False otherwise.
    """
    url = f"{API_BASE_URL}/check"
    payload = {
        "apikey": API_KEY,
        "secretapikey": SECRET_KEY,
        "domain": domain_name
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx/5xx)
        data = response.json()

        # Ensure API response is parsed correctly
        if data.get("status") == "SUCCESS":
            return data.get("available", "false").lower() == "true"
        else:
            print(f"Error while checking domain availability: {data.get('message')}")
            return False
    except requests.RequestException as e:
        print(f"An error occurred while checking domain availability: {e}")
        return False


def purchase_domain(domain_name):
    """
    Attempt to purchase a domain name through Porkbun API.
    
    Parameters:
        domain_name (str): The domain name to purchase.
    
    Returns:
        bool: True if the domain is successfully purchased, False otherwise.
    """
    url = f"{API_BASE_URL}/register"
    payload = {
        "apikey": API_KEY,
        "secretapikey": SECRET_KEY,
        "domain": domain_name,
        "years": 1,  # Number of years to register the domain
        "contact": {}  # Add proper contact information here if required by Porkbun API
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx/5xx)
        data = response.json()

        # Ensure API response is parsed correctly
        if data.get("status") == "SUCCESS":
            print(f"Domain '{domain_name}' successfully purchased!")
            return True
        else:
            print(f"Error while purchasing domain: {data.get('message')}")
            return False
    except requests.RequestException as e:
        print(f"An error occurred while purchasing domain: {e}")
        return False


def main():
    """
    Main function to interactively check and purchase a domain name.
    """
    # Accept domain name input from the user
    domain_name = input("Enter the domain name to check and purchase: ").strip()

    # Check if the domain is available
    if check_domain_availability(domain_name):
        print(f"Domain '{domain_name}' is available!")
        should_purchase = input("Do you want to purchase this domain? (yes/no): ").strip().lower()

        if should_purchase == "yes":
            # Attempt to purchase the domain
            if purchase_domain(domain_name):
                print(f"Domain '{domain_name}' has been successfully purchased.")
            else:
                print(f"Failed to purchase the domain '{domain_name}'.")
        else:
            print("Purchase canceled.")
    else:
        print(f"Domain '{domain_name}' is not available.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
        sys.exit(0)
```

**Note**: Replace `your_api_key_here` and `your_secret_key_here` with your actual Porkbun API credentials. Also, ensure proper contact information is included in the `contact` field of the `purchase_domain` function payload as required by Porkbun's API documentation. Use this script responsibly and in compliance with Porkbun's terms of service.
