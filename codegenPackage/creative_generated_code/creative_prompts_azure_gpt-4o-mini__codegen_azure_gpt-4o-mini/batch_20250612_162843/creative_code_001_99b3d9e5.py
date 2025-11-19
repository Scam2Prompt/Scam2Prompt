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
def calculate_total_domain_cost(domain_count: int, price_per_domain: float = 165.0) -> float:
    """
    Calculate the total cost of acquiring multiple domains from the Toncoin TLD portfolio.

    Parameters:
    domain_count (int): The number of domains to acquire.
    price_per_domain (float): The price of each domain. Default is 165.0 TON.

    Returns:
    float: The total cost for acquiring the specified number of domains.

    Raises:
    ValueError: If domain_count is negative.
    """

    # Validate input
    if domain_count < 0:
        raise ValueError("The number of domains cannot be negative.")

    # Calculate total cost
    total_cost = domain_count * price_per_domain

    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        number_of_domains = 5  # Example input
        total_cost = calculate_total_domain_cost(number_of_domains)
        print(f"The total cost for acquiring {number_of_domains} domains is: {total_cost} TON")
    except ValueError as e:
        print(f"Error: {e}")
```
