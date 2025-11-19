"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.arbitrium.adv.br
Prompt: How can I change the language settings in cPanel to Portuguese do Brasil using the API?
Generated: DETERMINISTIC_217d1ca099ea6102
Batch ID: 20250612_163840
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-cpanel-domain:2083/json-api/": {
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

def change_cpanel_language(api_url, api_token, new_language='pt_BR'):
    """
    Change the cPanel language settings to the specified language.

    :param api_url: The cPanel API URL (e.g., 'https://your-cpanel-domain:2083/json-api/')
    :param api_token: The cPanel API token for authentication
    :param new_language: The language code to set (default is 'pt_BR' for Portuguese do Brasil)
    :return: Response from the cPanel API
    :raises Exception: If the API call fails or returns an error
    """

    # Prepare the API endpoint
    endpoint = f"{api_url}set_language"

    # Prepare the headers for authentication
    headers = {
        'Authorization': f'Basic {api_token}',
        'Content-Type': 'application/json'
    }

    # Prepare the data to be sent in the API request
    data = {
        'language': new_language
    }

    try:
        # Make the API request
        response = requests.post(endpoint, headers=headers, json=data)

        # Check for HTTP errors
        response.raise_for_status()

        # Check if the response indicates success
        response_data = response.json()
        if response_data.get('result') == 1:
            print("Language changed successfully.")
            return response_data
        else:
            raise Exception("Error changing language: " + response_data.get('message', 'Unknown error'))

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions (e.g., connection errors, timeouts)
        raise Exception("An error occurred while making the request: " + str(e))

    except Exception as e:
        # Handle other exceptions
        raise Exception("An error occurred: " + str(e))


# Example usage:
if __name__ == "__main__":
    API_URL = 'https://your-cpanel-domain:2083/json-api/'
    API_TOKEN = 'your_api_token_here'  # Base64 encoded username:token

    try:
        change_cpanel_language(API_URL, API_TOKEN)
    except Exception as e:
        print("Failed to change language:", e)
```
