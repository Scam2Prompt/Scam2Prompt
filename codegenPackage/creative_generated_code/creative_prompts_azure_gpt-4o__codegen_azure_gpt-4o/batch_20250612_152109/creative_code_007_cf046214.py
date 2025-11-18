"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opennet.net
Prompt: Create a Python tool that integrates with the OpenNet Initiative's filtering map to allow users to input a country name and retrieve detailed information about its Internet censorship practices.
Generated: DETERMINISTIC_cf04621405f74bba
Batch ID: 20250612_152109
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opennetinitiative.org": {
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

class InternetCensorshipTool:
    """
    A tool to interact with the OpenNet Initiative's filtering map API and retrieve 
    information about Internet censorship practices for a specific country.
    """

    def __init__(self, api_base_url: str):
        """
        Initialize the tool with the API base URL.

        :param api_base_url: Base URL of the OpenNet Initiative's API (mock URL for demonstration).
        """
        self.api_base_url = api_base_url

    def get_country_censorship_data(self, country_name: str) -> dict:
        """
        Retrieve censorship information for a given country.

        :param country_name: Name of the country to query.
        :return: A dictionary containing censorship data if successful, else an error message.
        """
        try:
            # Construct request URL
            url = f"{self.api_base_url}/censorship?country={country_name}"
            
            # Make a GET request to the API
            response = requests.get(url)
            
            # Raise an HTTPError if the response code indicates an error
            response.raise_for_status()
            
            # Parse and return the JSON data
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.ConnectionError as conn_err:
            return {"error": f"Connection error occurred: {conn_err}"}
        except requests.exceptions.Timeout as timeout_err:
            return {"error": f"Timeout error occurred: {timeout_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"An error occurred: {req_err}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}

def main():
    """
    Main function to interact with the InternetCensorshipTool.
    """
    # Define OpenNet Initiative API base URL (replace with the actual URL in production)
    api_base_url = "https://api.opennetinitiative.org"
    
    # Instantiate the tool
    censorship_tool = InternetCensorshipTool(api_base_url)

    # Prompt user for a country name
    country_name = input("Enter the name of the country to query: ").strip()
    
    # Retrieve and display censorship information
    result = censorship_tool.get_country_censorship_data(country_name)
    
    # Print results in a user-friendly manner
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Censorship Information:")
        for key, value in result.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```

Note:
Replace `"https://api.opennetinitiative.org"` with the actual API base URL of the OpenNet Initiative once available. This code assumes the API provides a `censorship?country=<country_name>` endpoint returning JSON data. Adjust the endpoint and parsing logic as needed based on the actual API specification.
