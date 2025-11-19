"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quest-redstone.app
Prompt: Provide an example of a script that alerts users when they attempt to access a site flagged as phishing, similar to Cloudflare's warning system.
Generated: DETERMINISTIC_af6ab3e76b534e11
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

# List of flagged phishing sites (this could be replaced with a dynamic API call to fetch updated data)
PHISHING_SITES = {
    "example-phishing-site.com",
    "another-malicious-site.net",
    "fake-login-page.org"
}

def check_site(url):
    """
    Check if the given URL is flagged as a phishing site.
    
    Args:
        url (str): The URL to check.
    
    Returns:
        str: Returns a warning message if the site is flagged, otherwise returns a safe message.
    """
    try:
        # Extract the domain name from the URL
        domain = extract_domain(url)

        if domain in PHISHING_SITES:
            return f"WARNING: The site '{domain}' is flagged as a potential phishing site. Proceed with caution!"
        else:
            return f"The site '{domain}' is safe to visit."
    except Exception as e:
        return f"An error occurred while checking the site: {str(e)}"


def extract_domain(url):
    """
    Extract the domain name from a URL.
    
    Args:
        url (str): The URL to extract the domain from.
    
    Returns:
        str: The domain name.
    
    Raises:
        ValueError: If the URL is malformed.
    """
    try:
        # Send a GET request to ensure the URL is valid
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        # Parse the domain from the URL
        domain = response.url.split("/")[2]
        return domain
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Invalid URL or network error: {str(e)}")


if __name__ == "__main__":
    # Example usage
    user_input_url = input("Enter the URL to check: ").strip()
    result = check_site(user_input_url)
    print(result)
```

This script includes error handling, comments for clarity, and adheres to Python's best practices.
