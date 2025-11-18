"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fomo-view.web.app
Prompt: Create a function to fetch security audit results for FOMO's portfolio tracker using its API.
Generated: DETERMINISTIC_af61cf69e8fe10b4
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_security_audit_results(api_url: str, api_key: str, portfolio_id: str) -> dict:
    """
    Fetches security audit results for FOMO's portfolio tracker using its API.
    
    Args:
        api_url (str): The base URL for FOMO's API.
        api_key (str): The API key for authentication.
        portfolio_id (str): The ID of the portfolio to fetch security audit results for.

    Returns:
        dict: A dictionary containing the security audit results.
    
    Raises:
        ValueError: If the response status code is not 200.
        Exception: For any network-related errors.
    """
    
    # API endpoint to fetch security audit results
    endpoint = f"{api_url}/portfolios/{portfolio_id}/security-audit"
    
    # Headers for API authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Send API request to fetch security audit results
        response = requests.get(endpoint, headers=headers)
        
        # Check if the response status code is successful
        if response.status_code == 200:
            return response.json()  # Return JSON response as a Python dictionary
        else:
            # Raise an error with the status code and message
            raise ValueError(f"Failed to fetch audit results. Status Code: {response.status_code}, Response: {response.text}")
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise Exception(f"An error occurred while connecting to the API: {e}")
```
