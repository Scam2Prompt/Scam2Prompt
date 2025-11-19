"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blast-drop.world
Prompt: How can I troubleshoot a website that is accessible via HTTPS but lacks an SSL certificate, based on the information from FASTPANEL?
Generated: DETERMINISTIC_500a026288eb16e2
Batch ID: 20250612_162605
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://fastpanel.domain/api/ssl-status/{domain}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fastpanel.domain/api/ssl-status/{domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a Python script to troubleshoot a website accessible via HTTPS but lacking an SSL certificate, using the FASTPANEL API (assuming FASTPANEL provides an API for SSL-related information). The script checks SSL status, identifies issues, and provides actionable suggestions.

```python
import requests

def check_ssl_status(domain, fastpanel_api_key):
    """
    Check the SSL status of a domain using FASTPANEL API.

    Parameters:
    - domain: The domain name to check.
    - fastpanel_api_key: API key for FASTPANEL authentication.

    Returns:
    - None. Prints the SSL status and recommendations.
    """

    # Define the FASTPANEL API endpoint
    api_url = f"https://fastpanel.domain/api/ssl-status/{domain}"

    # Set the headers for authorization
    headers = {
        "Authorization": f"Bearer {fastpanel_api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send the API request
        response = requests.get(api_url, headers=headers)
        
        # Check if the response was successful
        if response.status_code == 200:
            ssl_data = response.json()

            # Check overall SSL status
            if ssl_data.get("ssl_enabled"):
                print(f"✅ SSL is enabled for {domain}.")
                
                # Check for other issues (e.g., expiration, mismatched domain)
                if ssl_data.get("ssl_valid"):
                    print("✅ SSL certificate is valid.")
                else:
                    print("⚠️ SSL certificate is invalid. Please check the following:")
                    if ssl_data.get("reason"):
                        print(f"- Reason: {ssl_data['reason']}")
                    
            else:
                print(f"❌ SSL is not enabled for {domain}.")
                print("Suggestions:")
                print("- Ensure the SSL certificate is installed on the server.")
                print("- Confirm that the web server (e.g., Apache, Nginx) is properly configured for HTTPS.")
                print("- Use FASTPANEL to generate and install an SSL certificate if needed.")
        elif response.status_code == 404:
            print("❌ Domain not found in FASTPANEL. Please check the domain name or ensure it is added to FASTPANEL.")
        else:
            print(f"❌ Failed to retrieve SSL status. HTTP Status Code: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred while connecting to the FASTPANEL API: {e}")
        print("Suggestions:")
        print("- Verify your internet connection.")
        print("- Ensure the FASTPANEL API URL is correct.")
        print("- Check if the API key is valid.")

if __name__ == "__main__":
    # Input domain and FASTPANEL API key
    domain = input("Enter the domain name (e.g., example.com): ").strip()
    fastpanel_api_key = input("Enter your FASTPANEL API key: ").strip()

    # Perform the SSL status check
    check_ssl_status(domain, fastpanel_api_key)
```

### Notes:
- Replace `https://fastpanel.domain/api/ssl-status/{domain}` with the actual FASTPANEL API endpoint for SSL checks.
- Ensure you have a valid FASTPANEL API key for authentication.
- Install the `requests` library if it's not already installed (`pip install requests`).
