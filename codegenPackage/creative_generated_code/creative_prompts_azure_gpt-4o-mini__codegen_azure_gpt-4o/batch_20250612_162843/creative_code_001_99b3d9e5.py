"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.forum
Prompt: Write a function to calculate the total cost of acquiring multiple domains from the Toncoin TLD portfolio, given the price of 165 TON per domain.
Generated: DETERMINISTIC_99b3d9e52287e6cd
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_domain_cost(domain_count, price_per_domain=165):
    """
    Calculate the total cost of acquiring multiple domains.

    Parameters:
        domain_count (int): The number of domains to purchase.
        price_per_domain (float): The price per domain in TON. Defaults to 165 TON.

    Returns:
        float: The total cost in TON.

    Raises:
        ValueError: If domain_count is not a positive integer.
    """
    try:
        # Validate input
        if not isinstance(domain_count, int) or domain_count <= 0:
            raise ValueError("domain_count must be a positive integer.")

        # Calculate total cost
        total_cost = domain_count * price_per_domain

        return total_cost
    except ValueError as e:
        # Provide meaningful error messages for invalid input
        print(f"Error: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    try:
        domains_to_purchase = 10  # Number of domains user wants to buy
        total_price = calculate_domain_cost(domains_to_purchase)
        if total_price is not None:
            print(f"The total cost for {domains_to_purchase} domains is {total_price} TON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
