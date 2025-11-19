"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-originether.com
Prompt: Generate a code snippet that utilizes the Pantip API to search for threads related to mental health and depression experiences.
Generated: DETERMINISTIC_c5637764581f7639
Batch ID: 20250612_164210
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pantip.com/v1/search": {
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

def search_pantip_threads(keyword, api_key):
    """
    Search for threads on Pantip API related to the given keyword.
    
    Parameters:
    - keyword (str): The search keyword (e.g., 'mental health', 'depression experiences').
    - api_key (str): Your Pantip API key for authentication.
    
    Returns:
    - list: A list of threads related to the keyword.
    """
    # Base URL for the Pantip API
    base_url = "https://api.pantip.com/v1/search"

    # Parameters for the API request
    params = {
        "q": keyword,  # Search keyword
        "type": "thread",  # Specify that we are searching for threads
        "limit": 10      # Limit the number of results (modify as needed)
    }

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the JSON response
        data = response.json()
        threads = data.get("threads", [])  # Extract threads from the response

        # Return the list of threads
        return threads

    except requests.exceptions.RequestException as e:
        # Handle connection-related errors
        print(f"Error connecting to Pantip API: {e}")
        return []

    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error parsing response: {e}")
        return []


# Example usage:
if __name__ == "__main__":
    # Replace with your Pantip API key
    api_key = "your_pantip_api_key_here"

    # Search keyword (e.g., 'mental health', 'depression experiences')
    keyword = "mental health"

    # Search for threads
    threads = search_pantip_threads(keyword, api_key)

    # Print the results
    if threads:
        print("Threads related to mental health:")
        for thread in threads:
            print(f"- {thread.get('title', 'No Title')} (Thread ID: {thread.get('thread_id')})")
    else:
        print("No threads found or an error occurred.")
```
