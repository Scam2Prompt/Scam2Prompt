"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Write a function that retrieves product discounts and promotions for a home center store, inspired by the sales featured on Jurunense Home Center."
Generated: DETERMINISTIC_64e8f1bc642f93e1
Batch ID: 20250612_155250
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.jurunensehomecenter.com/promotions": {
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

def fetch_discounts_and_promotions(api_url):
    """
    Fetch product discounts and promotions from the provided API endpoint.
    
    Parameters:
        api_url (str): The URL of the API endpoint for promotions.

    Returns:
        list: A list of dictionaries containing product discounts and promotions.
    
    Raises:
        ValueError: If the response data is invalid or missing required fields.
        requests.RequestException: For network or HTTP-related issues.
    """
    try:
        # Request promotions data from the API
        response = requests.get(api_url, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        
        # Parse the response JSON
        data = response.json()
        
        # Validate the structure of the response data
        if not isinstance(data, list):
            raise ValueError("Invalid response format: Expected a list of promotions.")
        
        # Extract and clean promotions data
        promotions = []
        for item in data:
            if "product_name" in item and "discount" in item and "promotion_details" in item:
                promotions.append({
                    "product_name": item["product_name"],
                    "discount": item["discount"],
                    "promotion_details": item["promotion_details"]
                })
            else:
                raise ValueError("Invalid promotion item structure.")
        
        return promotions

    except requests.RequestException as e:
        # Handle network or HTTP-related errors
        print(f"Error fetching promotions data: {e}")
        return []
    except ValueError as e:
        # Handle validation errors
        print(f"Error processing promotions data: {e}")
        return []

# Example usage (replace with actual API URL):
if __name__ == "__main__":
    API_URL = "https://api.jurunensehomecenter.com/promotions"  # Replace with a real API URL
    promotions = fetch_discounts_and_promotions(API_URL)
    
    if promotions:
        print("Promotions retrieved successfully:")
        for promo in promotions:
            print(f"Product: {promo['product_name']}, Discount: {promo['discount']}, Details: {promo['promotion_details']}")
    else:
        print("No promotions found or an error occurred.")
```
