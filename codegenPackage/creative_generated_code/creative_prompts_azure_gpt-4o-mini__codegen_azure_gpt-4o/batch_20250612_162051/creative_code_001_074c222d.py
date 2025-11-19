"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://antalyasehiricinakliye.com
Prompt: Write a Python script that integrates with an API to provide real-time pricing for moving services in Antalya, focusing on small and large item transportation.
Generated: DETERMINISTIC_074c222dd8fe29a2
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.movingservices.com/v1/pricing": {
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

# Configuration settings
API_BASE_URL = "https://api.movingservices.com/v1/pricing"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

def get_pricing(item_type: str, weight: float, distance: float) -> dict:
    """
    Retrieves real-time pricing for moving services.

    Parameters:
    - item_type (str): Type of item ("small" or "large").
    - weight (float): Weight of the item in kilograms.
    - distance (float): Distance to be covered in kilometers.

    Returns:
    - dict: A dictionary containing the pricing information or an error message.
    """
    try:
        # Validate inputs
        if item_type not in ["small", "large"]:
            raise ValueError("Invalid item type. Valid options are 'small' or 'large'.")
        if weight <= 0 or distance <= 0:
            raise ValueError("Weight and distance must be positive values.")

        # API request payload
        payload = {
            "itemType": item_type,
            "weight": weight,
            "distance": distance
        }

        # Set headers for the API request
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        # Make the API request
        response = requests.post(API_BASE_URL, json=payload, headers=headers)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return {"error": f"API request failed: {str(e)}"}
    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

def main():
    """
    Main function to demonstrate the pricing retrieval functionality.
    """
    print("Welcome to Antalya Moving Services Pricing Tool!")
    
    try:
        # Input details for pricing
        item_type = input("Enter item type ('small' or 'large'): ").strip().lower()
        weight = float(input("Enter item weight in kilograms: ").strip())
        distance = float(input("Enter transportation distance in kilometers: ").strip())

        # Fetch pricing
        pricing_data = get_pricing(item_type, weight, distance)

        # Display results
        if "error" in pricing_data:
            print(f"Error: {pricing_data['error']}")
        else:
            print("Pricing Details:")
            print(f"Base Price: {pricing_data['base_price']} TRY")
            print(f"Distance Fee: {pricing_data['distance_fee']} TRY")
            print(f"Total Price: {pricing_data['total_price']} TRY")

    except Exception as e:
        print(f"An error occurred while processing your request: {str(e)}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
