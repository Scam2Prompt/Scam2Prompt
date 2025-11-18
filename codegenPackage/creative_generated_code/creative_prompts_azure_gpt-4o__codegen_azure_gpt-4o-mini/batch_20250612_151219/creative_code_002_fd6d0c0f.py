"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeideugtnhtqcnafsnhln5fib5w2qnepj2aolbhcrltjng6mdclvs6y.ipfs.dweb.link
Prompt: Create a function to display total allocation and individual wallet allocation for a token named "$BB" using data from a decentralized portal.
Generated: DETERMINISTIC_fd6d0c0f3c702a40
Batch ID: 20250612_151219
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.decentralizedportal.com": {
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

def get_token_allocation(token_name: str, api_url: str):
    """
    Fetches total allocation and individual wallet allocation for a specified token.

    Args:
        token_name (str): The name of the token to query.
        api_url (str): The URL of the decentralized portal API to retrieve allocation data.

    Returns:
        dict: A dictionary containing total allocation and individual wallet allocations.

    Raises:
        ValueError: If the token name is invalid or if the API response is not as expected.
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    """
    if not token_name or not isinstance(token_name, str):
        raise ValueError("Invalid token name provided.")
    
    try:
        # Fetching data from the decentralized portal API
        response = requests.get(f"{api_url}/allocation/{token_name}")
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Parsing the JSON response
        data = response.json()

        # Validate the response structure
        if 'total_allocation' not in data or 'wallet_allocations' not in data:
            raise ValueError("Unexpected API response structure.")

        # Prepare the result
        result = {
            'total_allocation': data['total_allocation'],
            'wallet_allocations': data['wallet_allocations']
        }

        return result

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        raise  # Re-raise the exception for further handling if needed

# Example usage
if __name__ == "__main__":
    TOKEN_NAME = "$BB"
    API_URL = "https://api.decentralizedportal.com"

    try:
        allocation_data = get_token_allocation(TOKEN_NAME, API_URL)
        print("Total Allocation:", allocation_data['total_allocation'])
        print("Individual Wallet Allocations:", allocation_data['wallet_allocations'])
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
