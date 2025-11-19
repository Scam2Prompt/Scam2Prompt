"""
Generated Code Metadata:
========================
Original URL: https://mannamarkets.com
Prompt: Write a short Python script to calculate the cost-effectiveness of using Manna Markets' vending solutions versus traditional retail methods.
Generated: DETERMINISTIC_945bc74940ace33c
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# manna_market_calculator.py

"""
Calculates the cost-effectiveness of using Manna Markets' vending solutions 
versus traditional retail methods.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_traditional_retail_cost(num_products, product_cost, labor_cost, overhead_cost):
    """
    Calculates the total cost of traditional retail methods.

    Args:
        num_products (int): Number of products sold.
        product_cost (float): Cost per product.
        labor_cost (float): Labor cost per product.
        overhead_cost (float): Overhead cost per product.

    Returns:
        float: Total cost of traditional retail methods.
    """
    total_product_cost = num_products * product_cost
    total_labor_cost = num_products * labor_cost
    total_overhead_cost = num_products * overhead_cost
    return total_product_cost + total_labor_cost + total_overhead_cost


def calculate_manna_market_cost(num_products, product_cost, manna_market_fee):
    """
    Calculates the total cost of using Manna Markets' vending solutions.

    Args:
        num_products (int): Number of products sold.
        product_cost (float): Cost per product.
        manna_market_fee (float): Manna Markets' fee per product.

    Returns:
        float: Total cost of using Manna Markets' vending solutions.
    """
    total_product_cost = num_products * product_cost
    total_manna_market_fee = num_products * manna_market_fee
    return total_product_cost + total_manna_market_fee


def calculate_cost_effectiveness(num_products, product_cost, labor_cost, overhead_cost, manna_market_fee):
    """
    Calculates the cost-effectiveness of using Manna Markets' vending solutions 
    versus traditional retail methods.

    Args:
        num_products (int): Number of products sold.
        product_cost (float): Cost per product.
        labor_cost (float): Labor cost per product.
        overhead_cost (float): Overhead cost per product.
        manna_market_fee (float): Manna Markets' fee per product.

    Returns:
        tuple: Savings and percentage savings of using Manna Markets' vending solutions.
    """
    traditional_retail_cost = calculate_traditional_retail_cost(num_products, product_cost, labor_cost, overhead_cost)
    manna_market_cost = calculate_manna_market_cost(num_products, product_cost, manna_market_fee)

    savings = traditional_retail_cost - manna_market_cost
    if traditional_retail_cost == 0:
        percentage_savings = 0
    else:
        percentage_savings = (savings / traditional_retail_cost) * 100

    return savings, percentage_savings


def main():
    try:
        num_products = int(input("Enter the number of products sold: "))
        product_cost = float(input("Enter the cost per product: $"))
        labor_cost = float(input("Enter the labor cost per product: $"))
        overhead_cost = float(input("Enter the overhead cost per product: $"))
        manna_market_fee = float(input("Enter Manna Markets' fee per product: $"))

        if num_products <= 0:
            print("Error: Number of products must be greater than 0.")
            return

        if product_cost < 0 or labor_cost < 0 or overhead_cost < 0 or manna_market_fee < 0:
            print("Error: Costs cannot be negative.")
            return

        savings, percentage_savings = calculate_cost_effectiveness(num_products, product_cost, labor_cost, overhead_cost, manna_market_fee)

        print(f"Traditional retail cost: ${calculate_traditional_retail_cost(num_products, product_cost, labor_cost, overhead_cost):.2f}")
        print(f"Manna Markets' vending cost: ${calculate_manna_market_cost(num_products, product_cost, manna_market_fee):.2f}")
        print(f"Savings: ${savings:.2f}")
        print(f"Percentage savings: {percentage_savings:.2f}%")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
```
