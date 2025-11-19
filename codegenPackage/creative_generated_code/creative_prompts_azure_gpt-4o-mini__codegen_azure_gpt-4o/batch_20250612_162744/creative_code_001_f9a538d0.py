"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msu.best
Prompt: How can I troubleshoot a website that is accessible via HTTPS but lacks an SSL certificate?
Generated: DETERMINISTIC_f9a538d0a5f17bc6
Batch ID: 20250612_162744
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the code written in Python using the `requests` library to troubleshoot a website accessible via HTTPS but lacking an SSL certificate:

```python
import requests
from requests.exceptions import SSLError, ConnectionError

def troubleshoot_https_connection(url):
    """
    Troubleshoots a website that is accessible via HTTPS but lacks an SSL certificate.

    Parameters:
        url (str): The URL of the website to troubleshoot.

    Returns:
        str: A message indicating the troubleshooting status.
    """
    # Ensure the URL starts with 'https'
    if not url.startswith('https://'):
        return "Error: URL must start with 'https://'. Please provide a valid HTTPS URL."

    try:
        # Attempt to connect to the website
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            return f"Success: {url} is accessible over HTTPS with a valid SSL certificate."
        else:
            return f"Warning: Received HTTP status {response.status_code} from {url}. Further investigation needed."

    except SSLError:
        # Handle cases where SSL certificate is invalid or missing
        return f"Error: SSL certificate is invalid or missing for {url}."

    except ConnectionError:
        # Handle cases where the connection fails
        return f"Error: Unable to connect to {url}. Please check the URL or network connection."

    except Exception as e:
        # Handle any other unexpected errors
        return f"Error: An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage
    website_url = input("Enter the HTTPS URL to troubleshoot: ")
    result = troubleshoot_https_connection(website_url)
    print(result)
```

### Key Features of the Code:
1. **Input Validation**: Ensures the URL starts with `https://`.
2. **Error Handling**: Catches `SSLError`, `ConnectionError`, and unexpected exceptions.
3. **Timeout Parameter**: Prevents the code from hanging indefinitely.
4. **Production-Ready**: Includes comments for clarity and follows Python best practices.
