"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claiming.website
Prompt: Create an API call to fetch and display a website's privacy policy dynamically.
Generated: DETERMINISTIC_7bc597ede77ce30d
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_privacy_policy(url):
    """
    Fetches the privacy policy from a given website URL.

    Parameters:
        url (str): The URL of the website whose privacy policy we want to fetch.

    Returns:
        str: The privacy policy text if successful, or an appropriate error message.
    """
    try:
        # Perform a GET request to fetch the privacy policy page
        response = requests.get(url, timeout=10)  # Set timeout to avoid hanging
        
        # Raise an HTTPError if the response status is not successful
        response.raise_for_status()  
        
        # Return the content of the privacy policy page
        return response.text
    
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 404, 500)
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        # Handle connection errors (e.g., network problems)
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        # Handle timeout errors
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        # Handle all other request-related errors
        return f"An error occurred while making the request: {req_err}"

def main():
    """
    Main function to execute the script and display the privacy policy.
    """
    print("Enter the URL of the privacy policy page:")
    url = input().strip()  # Read the URL from the user and strip extra spaces
    
    if not url:
        print("Error: URL cannot be empty.")
        return

    # Fetch the privacy policy and display the result
    policy = fetch_privacy_policy(url)
    print("\nPrivacy Policy Content:")
    print(policy)

if __name__ == "__main__":
    main()
```
