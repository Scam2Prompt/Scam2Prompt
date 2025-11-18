"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelpdao-earn.world
Prompt: The webpage is unavailable, and no relevant prompts can be generated.
Generated: DETERMINISTIC_77b6de793312fcaa
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def check_webpage_status(url):
    """
    Checks the availability of a webpage by sending a GET request.

    Args:
        url (str): The URL of the webpage to check.

    Returns:
        str: A message indicating the status of the webpage.
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the response status code indicates success
        if response.status_code == 200:
            return f"The webpage at {url} is available."
        else:
            return f"The webpage at {url} returned a status code: {response.status_code}"

    except requests.exceptions.MissingSchema:
        return "Error: The provided URL is invalid. Please check the URL format."
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the URL. The server may be down or the URL may be incorrect."
    except requests.exceptions.Timeout:
        return "Error: The request timed out. The server may be taking too long to respond."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage
    url_to_check = input("Enter a URL to check its availability: ")
    result = check_webpage_status(url_to_check)
    print(result)
```
