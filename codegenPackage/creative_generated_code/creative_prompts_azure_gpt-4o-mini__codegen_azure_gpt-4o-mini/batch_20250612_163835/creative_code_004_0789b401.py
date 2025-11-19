"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iwslink.com
Prompt: Develop a mobile app feature that enhances customer experience by providing predictive safety content related to the product currently in use.
Generated: DETERMINISTIC_0789b4013118692e
Batch ID: 20250612_163835
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com": {
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
import json
import requests

class SafetyContentPredictor:
    """
    A class to predict and fetch safety content related to the product in use.
    """

    def __init__(self, product_id, api_endpoint):
        """
        Initializes the SafetyContentPredictor with a product ID and API endpoint.
        
        Args:
            product_id (str): The ID of the product currently in use.
            api_endpoint (str): The API endpoint to fetch safety content.
        """
        self.product_id = product_id
        self.api_endpoint = api_endpoint

    def fetch_safety_content(self):
        """
        Fetches safety content from the API based on the product ID.
        
        Returns:
            dict: A dictionary containing safety content, or an error message.
        """
        try:
            # Making a GET request to the API to fetch safety content
            response = requests.get(f"{self.api_endpoint}/safety-content/{self.product_id}")

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse JSON response
            safety_content = response.json()

            if not safety_content:
                return {"error": "No safety content found for this product."}

            return safety_content
            
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON response."}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}

    def display_safety_content(self):
        """
        Displays the fetched safety content in a user-friendly format.

        Returns:
            None
        """
        safety_content = self.fetch_safety_content()

        if "error" in safety_content:
            # Log the error (could be expanded to use a logging framework)
            print(safety_content["error"])
        else:
            # Display the safety content
            print("Safety Content for Product ID:", self.product_id)
            print(json.dumps(safety_content, indent=4))


# Sample usage of the SafetyContentPredictor class
if __name__ == "__main__":
    # Configuration settings
    PRODUCT_ID = "12345"
    API_ENDPOINT = "https://api.example.com"

    # Create an instance of the SafetyContentPredictor
    predictor = SafetyContentPredictor(PRODUCT_ID, API_ENDPOINT)

    # Display the safety content
    predictor.display_safety_content()
```
