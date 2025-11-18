"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hidraulicaimperatriz.com.br
Prompt: Write a script to check the status of a HostGator-hosted website and ensure the "Página Fácil" temporary page is live.
Generated: DETERMINISTIC_4ac3d401a0e209a4
Batch ID: 20250612_154631
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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

def check_hostgator_website_status(url):
    """
    Checks the status of a HostGator-hosted website and validates 
    if the "Página Fácil" temporary page is live.

    Args:
        url (str): The URL of the website to check.

    Returns:
        dict: A dictionary containing the status code, 
              a boolean indicating if the "Página Fácil" page is live,
              and an error message (if any).
    """
    result = {
        'status_code': None,
        'pagina_facil_live': False,
        'error': None
    }

    try:
        # Make an HTTP GET request to the provided URL
        response = requests.get(url, timeout=10)

        # Update status code in result
        result['status_code'] = response.status_code

        # Check if the response was successful
        if response.status_code == 200:
            # Search for key text to identify "Página Fácil"
            if "Página Fácil" in response.text:
                result['pagina_facil_live'] = True
            else:
                result['pagina_facil_live'] = False
        else:
            result['pagina_facil_live'] = False

    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, or other exceptions
        result['error'] = str(e)

    return result


if __name__ == "__main__":
    # Replace this with the URL of the HostGator-hosted website
    website_url = "https://example.com"

    # Check the website status
    status = check_hostgator_website_status(website_url)

    # Print the result
    if status['error']:
        print(f"Error: {status['error']}")
    else:
        print(f"Status Code: {status['status_code']}")
        if status['pagina_facil_live']:
            print("The 'Página Fácil' page is live.")
        else:
            print("The 'Página Fácil' page is not live.")
```
