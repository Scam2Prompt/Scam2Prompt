"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Write a function that calculates the total cost of purchasing a commercial property, using the example of a lighting store priced at R$ 350.000 in São Paulo.
Generated: DETERMINISTIC_6163af8c7e744c00
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_property_cost(base_price, city, tax_rate, additional_fees):
    """
    Calculate the total cost of purchasing a commercial property.

    Args:
        base_price (float): The base price of the property.
        city (str): The city where the property is located.
        tax_rate (float): The property tax rate as a percentage (e.g., 3.5 for 3.5%).
        additional_fees (float): Any additional fees (e.g., legal fees, registration costs).

    Returns:
        float: The total cost of purchasing the property.
    """
    try:
        # Validate inputs
        if base_price < 0 or tax_rate < 0 or additional_fees < 0:
            raise ValueError("Base price, tax rate, and additional fees must be non-negative.")

        # Calculate property tax
        property_tax = (base_price * tax_rate) / 100

        # Calculate total cost
        total_cost = base_price + property_tax + additional_fees

        return total_cost

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Example property details
    base_price = 350000  # R$ 350,000
    city = "São Paulo"
    tax_rate = 3.5  # 3.5% property tax
    additional_fees = 15000  # R$ 15,000 in additional fees (e.g., legal fees)

    # Calculate total cost
    total_cost = calculate_total_property_cost(base_price, city, tax_rate, additional_fees)

    if total_cost is not None:
        print(f"The total cost of purchasing the property in {city} is: R$ {total_cost:.2f}")
```
