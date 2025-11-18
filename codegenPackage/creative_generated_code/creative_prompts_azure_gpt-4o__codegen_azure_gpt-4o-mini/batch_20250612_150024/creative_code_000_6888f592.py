"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-stether.org
Prompt: Write Python code using the Amazon Web Services (AWS) SDK to retrieve product details from the "Electrónica" category on Amazon.es.
Generated: DETERMINISTIC_6888f59282fb3b34
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import botocore
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_amazon_product_details(asin, category='Electrónica'):
    """
    Retrieve product details from Amazon for a given ASIN in the specified category.

    :param asin: The Amazon Standard Identification Number (ASIN) of the product.
    :param category: The category of the product (default is 'Electrónica').
    :return: A dictionary containing product details or None if an error occurs.
    """
    # Initialize a session using your credentials
    session = boto3.Session(
        aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',
        aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
        region_name='us-west-2'  # Change as per your requirements
    )

    # Initialize the Product Advertising API client
    client = session.client('productadvertising')

    try:
        # Call the get_items method with the specified ASIN and category
        response = client.get_items(
            ItemIds=[asin],
            Condition='New',
            Resources=[
                'ItemInfo.Title',
                'ItemInfo.Features',
                'ItemInfo.ContentInfo',
                'Offers.Listings.Price'
            ]
        )
        
        # Check if the response contains items
        if 'ItemsResult' in response and 'Items' in response['ItemsResult']:
            product_details = response['ItemsResult']['Items'][0]
            logging.info("Product details retrieved successfully.")
            return product_details
        else:
            logging.warning("No product found for the given ASIN.")
            return None

    except botocore.exceptions.ClientError as e:
        logging.error(f"Client error: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example ASIN for testing
    test_asin = 'B09168Z8Y6'  # Replace with a valid ASIN
    product_info = get_amazon_product_details(test_asin)

    if product_info:
        print(product_info)
    else:
        print("Failed to retrieve product details.")
```

**Note**: Remember to replace `'YOUR_AWS_ACCESS_KEY_ID'` and `'YOUR_AWS_SECRET_ACCESS_KEY'` with your actual AWS credentials. Ensure that the IAM user has the necessary permissions to access the Product Advertising API.
