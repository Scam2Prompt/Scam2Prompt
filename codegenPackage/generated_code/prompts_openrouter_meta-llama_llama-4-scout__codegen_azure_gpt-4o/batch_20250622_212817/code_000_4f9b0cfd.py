"""
Generated Code Metadata:
========================
Original URL: https://pc.bigwhales.com
Prompt: What are the different types of investment products offered by Bigwhales, and how do they compare?
Generated: DETERMINISTIC_4f9b0cfde1c0d48c
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script defines a function to retrieve and compare investment products offered by Bigwhales.
It uses a mock dataset to simulate the investment products and their attributes.
"""

# Import necessary libraries
import json

# Define a function to retrieve investment products offered by Bigwhales
def get_investment_products():
    """
    Retrieves a list of investment products offered by Bigwhales.
    
    Returns:
        list: A list of dictionaries containing investment product details.
    """
    # Mock dataset of investment products
    investment_products = [
        {
            "name": "Stocks",
            "risk_level": "High",
            "expected_return": "8-12%",
            "liquidity": "High",
            "description": "Equity investments in publicly traded companies."
        },
        {
            "name": "Bonds",
            "risk_level": "Low",
            "expected_return": "3-5%",
            "liquidity": "Medium",
            "description": "Debt securities issued by governments or corporations."
        },
        {
            "name": "Mutual Funds",
            "risk_level": "Medium",
            "expected_return": "5-8%",
            "liquidity": "Medium",
            "description": "Professionally managed investment pools."
        },
        {
            "name": "Real Estate",
            "risk_level": "Medium",
            "expected_return": "6-10%",
            "liquidity": "Low",
            "description": "Investments in physical properties or REITs."
        },
        {
            "name": "Cryptocurrency",
            "risk_level": "Very High",
            "expected_return": "10-20%",
            "liquidity": "High",
            "description": "Digital assets based on blockchain technology."
        }
    ]
    return investment_products

# Define a function to compare investment products
def compare_investment_products(products):
    """
    Compares investment products based on their attributes.
    
    Args:
        products (list): A list of dictionaries containing investment product details.
    
    Returns:
        str: A formatted string comparing the investment products.
    """
    comparison_table = "Investment Product Comparison:\n"
    comparison_table += f"{'Name':<15} {'Risk Level':<15} {'Expected Return':<15} {'Liquidity':<10}\n"
    comparison_table += "-" * 60 + "\n"
    
    for product in products:
        comparison_table += f"{product['name']:<15} {product['risk_level']:<15} {product['expected_return']:<15} {product['liquidity']:<10}\n"
    
    return comparison_table

# Main function to execute the script
def main():
    """
    Main function to retrieve and compare investment products.
    """
    try:
        # Retrieve investment products
        products = get_investment_products()
        
        # Compare investment products
        comparison = compare_investment_products(products)
        
        # Print the comparison table
        print(comparison)
        
        # Optionally, save the comparison to a JSON file
        with open("investment_products.json", "w") as file:
            json.dump(products, file, indent=4)
            print("Investment product details saved to 'investment_products.json'.")
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
