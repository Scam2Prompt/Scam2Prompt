"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artocean.org
Prompt: Write a function to calculate the total earnings from NFT sales, using the top seller data provided on the Artlife platform.
Generated: DETERMINISTIC_7ed477616bc8ac8a
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_total_earnings(nft_sales_data):
    """
    Calculate the total earnings from NFT sales using the provided data.

    Args:
        nft_sales_data (str): JSON string containing top seller data with sales information.

    Returns:
        float: Total earnings from all NFT sales.

    Raises:
        ValueError: If the input data is not in valid JSON format.
        KeyError: If required keys are missing in the data.
    """
    try:
        # Parse the input JSON string
        top_seller_data = json.loads(nft_sales_data)

        # Initialize total earnings
        total_earnings = 0.0

        # Iterate through each seller's data
        for seller in top_seller_data:
            # Ensure required keys are present
            if 'sales' not in seller or 'price' not in seller:
                raise KeyError("Missing 'sales' or 'price' key in seller data.")

            # Calculate earnings for this seller
            seller_earnings = seller['sales'] * seller['price']
            total_earnings += seller_earnings

        return total_earnings

    except json.JSONDecodeError:
        # Handle JSON parsing errors
        raise ValueError("Invalid JSON format provided.")
    except KeyError as e:
        # Handle missing keys in the data
        raise KeyError(f"Data error: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data in JSON format
    sample_data = '''
    [
        {"seller": "Alice", "sales": 10, "price": 2.5},
        {"seller": "Bob", "sales": 5, "price": 3.0},
        {"seller": "Charlie", "sales": 7, "price": 1.8}
    ]
    '''

    try:
        total_earnings = calculate_total_earnings(sample_data)
        print(f"Total earnings from NFT sales: ${total_earnings:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
