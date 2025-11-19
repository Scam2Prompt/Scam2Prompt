"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.linea.ai
Prompt: Generate a Python function that retrieves instant, cited answers about model features using Disarray's capabilities.
Generated: DETERMINISTIC_1255cd0c11b707b9
Batch ID: 20250612_155235
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.disarray.com/models/{model_name}/features": {
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
import logging

# Configure logging to capture errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DisarrayAPIError(Exception):
    """Custom exception for Disarray API errors."""
    pass

def get_model_features(model_name: str) -> dict:
    """
    Retrieve instant, cited answers about model features using Disarray's capabilities.

    Args:
        model_name (str): The name of the model for which features are to be retrieved.

    Returns:
        dict: A dictionary containing the model features and citations.

    Raises:
        DisarrayAPIError: If the API request fails or returns an error.
        ValueError: If the model_name is empty or invalid.
    """
    # Validate input
    if not model_name or not isinstance(model_name, str):
        raise ValueError("Model name must be a non-empty string.")

    # Define the API endpoint and parameters
    api_url = f"https://api.disarray.com/models/{model_name}/features"
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'ModelFeatureFetcher/1.0'
    }

    try:
        # Make a GET request to the Disarray API
        response = requests.get(api_url, headers=headers)
        
        # Check for a successful response
        response.raise_for_status()

        # Parse the JSON response
        features_data = response.json()
        
        if 'features' not in features_data:
            raise DisarrayAPIError("Unexpected response format: 'features' not found.")

        # Log success and return the features
        logging.info("Successfully retrieved features for model: %s", model_name)
        return features_data['features']

    except requests.exceptions.RequestException as e:
        logging.error("API request failed: %s", e)
        raise DisarrayAPIError(f"API request failed: {e}")
    except ValueError as e:
        logging.error("Error parsing JSON response: %s", e)
        raise DisarrayAPIError("Error parsing the response from Disarray API.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        raise DisarrayAPIError("An unexpected error occurred.")

# Example usage (commented out for production):
# try:
#     features = get_model_features("example_model")
#     print(features)
# except DisarrayAPIError as e:
#     print(f"Error: {e}")
```
