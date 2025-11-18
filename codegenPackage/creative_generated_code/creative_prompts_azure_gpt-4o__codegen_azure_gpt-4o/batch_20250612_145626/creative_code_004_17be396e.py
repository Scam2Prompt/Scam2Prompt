"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://makerfinance.org
Prompt: Create a function to search for products under AED 100 on Amazon.ae and display their names, prices, and categories using the Amazon API.
Generated: DETERMINISTIC_17be396ef159c83b
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Function to search for products under AED 100 on Amazon.ae
def search_products_under_aed_100(access_key, secret_key, associate_tag, keyword=""):
    """
    Searches for products under AED 100 on Amazon.ae using the Amazon Product Advertising API.

    Args:
        access_key (str): Your Amazon Product Advertising API access key.
        secret_key (str): Your Amazon Product Advertising API secret key.
        associate_tag (str): Your Amazon affiliate associate tag.
        keyword (str): The search keyword for products (default is an empty string for generic search).

    Returns:
        list: A list of dictionaries containing product names, prices, and categories.
    """
    try:
        # Initialize the Amazon Product Advertising API client
        client = boto3.client(
            'productadvertisingapi',
            region_name='us-east-1',  # Adjust as needed
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        
        # Request parameters
        request_params = {
            'Service': 'AWSECommerceService',
            'Operation': 'ItemSearch',
            'SearchIndex': 'All',  # Search across all categories
            'Keywords': keyword,
            'ResponseGroup': 'ItemAttributes,Offers',
            'Sort': 'price'  # Sort by price (ascending)
        }
        
        # Execute the API call
        response = client.get_item_search(**request_params)
        
        products = []
        
        # Parse the response
        for item in response.get('Items', {}).get('Item', []):
            try:
                # Extract product details
                title = item.get('ItemAttributes', {}).get('Title', 'Unknown Title')
                price = item.get('OfferSummary', {}).get('LowestNewPrice', {}).get('Amount', None)
                category = item.get('ItemAttributes', {}).get('ProductGroup', 'Unknown Category')

                # Convert price to AED and filter products under AED 100
                if price is not None and float(price) / 100.0 < 100:  # Assuming price is in cents
                    products.append({
                        'name': title,
                        'price': float(price) / 100.0,  # Convert cents to AED
                        'category': category
                    })
            except Exception as e:
                # Log parsing errors but continue processing
                print(f"Error parsing item: {e}")

        return products

    except (BotoCoreError, ClientError) as e:
        # Handle API errors
        print(f"API error: {e}")
        return []
    except Exception as e:
        # Handle other unexpected errors
        print(f"Unexpected error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Replace with your credentials and associate tag
    ACCESS_KEY = "your_access_key"
    SECRET_KEY = "your_secret_key"
    ASSOCIATE_TAG = "your_associate_tag"

    # Call the function to search for products
    results = search_products_under_aed_100(ACCESS_KEY, SECRET_KEY, ASSOCIATE_TAG, keyword="electronics")
    
    # Display the results
    for product in results:
        print(f"Name: {product['name']}, Price: AED {product['price']}, Category: {product['category']}")
```

**Note**: Replace placeholders (`your_access_key`, `your_secret_key`, `your_associate_tag`) with your actual Amazon Product Advertising API credentials. As of the current Amazon Product Advertising API (v5), you need to use their official SDK or perform signed requests with the correct API endpoints. Ensure you comply with their usage terms and conditions.
