"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Write a function that retrieves and displays a list of sports categories such as "Futebol", "Natação", and "Rugby" from an API similar to the one used in the sports equipment blog.
Generated: DETERMINISTIC_d16e2e7846913e2f
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/sports": {
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

def fetch_sports_categories(api_url):
    """
    Fetch and display a list of sports categories from the given API URL.

    Parameters:
        api_url (str): The URL endpoint for the sports categories API.

    Returns:
        None: Prints the list of sports categories to the console.
    """
    try:
        # Make a GET request to the API
        response = requests.get(api_url)
        
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the data contains a list of categories
        if 'categories' in data and isinstance(data['categories'], list):
            print("Sports Categories:")
            for category in data['categories']:
                print(f"- {category}")
        else:
            print("No categories found in the API response.")
    except requests.exceptions.RequestException as e:
        # Handle request errors (network issues, invalid URLs, etc.)
        print(f"Error fetching data from the API: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'https://api.example.com/sports' with the actual API endpoint
    api_url = "https://api.example.com/sports"
    fetch_sports_categories(api_url)
```
