"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayonnanft.com
Prompt: Develop a script to calculate secondary sales fees for an NFT collection on RayonnaNFT and display the total earnings for the creator.
Generated: DETERMINISTIC_e3de7d14eebf873c
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_secondary_sales_fees(sales_data, creator_fee_percentage):
    """
    Calculate the total secondary sales fees earned by the creator from an NFT collection.

    Args:
        sales_data (list): A list of dictionaries containing sales information.
                          Each dictionary should have keys 'sale_price' and 'secondary_sales'.
                          Example: [{'sale_price': 1000, 'secondary_sales': True}, ...]
        creator_fee_percentage (float): The percentage of sale price earned by the creator as secondary sales fees.

    Returns:
        float: The total secondary sales earnings for the creator.
    """
    try:
        # Validate inputs
        if not isinstance(sales_data, list):
            raise ValueError("sales_data must be a list of dictionaries.")

        if not isinstance(creator_fee_percentage, (int, float)) or creator_fee_percentage < 0:
            raise ValueError("creator_fee_percentage must be a positive number.")

        total_earnings = 0.0

        for sale in sales_data:
            # Validate individual sale data structure
            if not isinstance(sale, dict):
                raise ValueError("Each sale in sales_data must be a dictionary.")
            
            if 'sale_price' not in sale or 'secondary_sales' not in sale:
                raise ValueError("Sale dictionary must contain 'sale_price' and 'secondary_sales' keys.")

            if not isinstance(sale['sale_price'], (int, float)) or sale['sale_price'] < 0:
                raise ValueError("sale_price must be a positive number.")
            
            if not isinstance(sale['secondary_sales'], bool):
                raise ValueError("secondary_sales must be a boolean value.")

            # Calculate secondary sales fees if applicable
            if sale['secondary_sales']:
                fee = (sale['sale_price'] * creator_fee_percentage) / 100
                total_earnings += fee

        return total_earnings

    except Exception as e:
        # Handle and log errors
        print(f"Error calculating secondary sales fees: {str(e)}")
        return 0.0


def main():
    """
    Main function to calculate and display NFT secondary sales earnings.
    """
    # Example sales data (you can replace this with data from your source)
    sales_data = [
        {"sale_price": 1000, "secondary_sales": True},
        {"sale_price": 500, "secondary_sales": False},
        {"sale_price": 2000, "secondary_sales": True},
        {"sale_price": 1500, "secondary_sales": True}
    ]

    # Creator fee percentage (can be adjusted as needed)
    creator_fee_percentage = 10.0  # Example: 10%

    # Calculate total secondary sales earnings
    total_earnings = calculate_secondary_sales_fees(sales_data, creator_fee_percentage)

    # Display the result
    print(f"Total secondary sales earnings for the creator: ${total_earnings:.2f}")


if __name__ == "__main__":
    main()
```
