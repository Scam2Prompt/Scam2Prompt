"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staging.artlabs.ai
Prompt: Write Python code to integrate artlabs' AI-powered 3D model creation API into an eCommerce platform for generating scalable AR experiences from product images.
Generated: DETERMINISTIC_6cc172353e197520
Batch ID: 20250612_154302
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.artlabs.com/3d-models": {
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
import json

class ArtLabsAPI:
    """
    A class to interact with the ArtLabs AI-powered 3D model creation API.
    """

    BASE_URL = "https://api.artlabs.com/3d-models"

    def __init__(self, api_key):
        """
        Initialize the ArtLabsAPI with the provided API key.

        :param api_key: str - Your API key for authentication
        """
        self.api_key = api_key

    def create_3d_model(self, image_path, product_name):
        """
        Create a 3D model using an image of the product.

        :param image_path: str - The local path to the product image
        :param product_name: str - The name of the product
        :return: dict - Response from the API containing model details
        """
        try:
            # Read the image file
            with open(image_path, 'rb') as image_file:
                files = {'file': image_file}
                headers = {'Authorization': f'Bearer {self.api_key}'}
                
                # Send a POST request to the API
                response = requests.post(self.BASE_URL, headers=headers, files=files)
                
                # Raise an error if the request was unsuccessful
                response.raise_for_status()

                # Return the JSON response if successful
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return None
        except FileNotFoundError:
            print(f"Error: The file at {image_path} was not found.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def process_model(self, model_data):
        """
        Process the model data returned from the API and prepare it for use.

        :param model_data: dict - The model data returned from the API
        :return: str - URL to the processed 3D model
        """
        try:
            # Assuming the model_data contains a 'model_url' key
            model_url = model_data.get('model_url')
            if model_url is None:
                raise ValueError("Model URL not found in the response.")
            
            # Here you can add any additional processing if necessary
            return model_url
        except Exception as e:
            print(f"Error processing model data: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual API key
    api_key = 'your_api_key'
    artlabs_api = ArtLabsAPI(api_key)

    # Path to the product image
    image_path = 'path/to/product_image.jpg'
    product_name = 'Sample Product'

    # Create a 3D model
    model_data = artlabs_api.create_3d_model(image_path, product_name)
    
    if model_data:
        # Process the model to retrieve the URL
        model_url = artlabs_api.process_model(model_data)
        if model_url:
            print(f"3D Model URL: {model_url}")
        else:
            print("Failed to process the model data.")
    else:
        print("Failed to create 3D model.")
```
