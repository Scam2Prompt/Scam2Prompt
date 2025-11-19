"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caldrera.xyz
Prompt: Write a Python function to calculate the monthly lease payment for a domain name, using the example of $108.34/month for a $5,000 domain.
Generated: DETERMINISTIC_89ccc2f3132aaeaa
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_monthly_lease_payment(domain_value: float, lease_rate: float) -> float:
    """
    Calculate the monthly lease payment for a domain name.

    :param domain_value: The total value of the domain in dollars.
    :param lease_rate: The monthly lease rate as a percentage of the domain value.
    :return: The calculated monthly lease payment.
    :raises ValueError: If the domain_value or lease_rate is negative.
    """

    # Validate input parameters
    if domain_value < 0:
        raise ValueError("Domain value must be a non-negative number.")
    if lease_rate < 0:
        raise ValueError("Lease rate must be a non-negative number.")

    # Calculate the monthly lease payment
    monthly_payment = (domain_value * lease_rate) / 100

    return monthly_payment

# Example usage
if __name__ == "__main__":
    try:
        domain_value = 5000  # Example domain value in dollars
        lease_rate = 2.6     # Monthly lease rate as a percentage (e.g., 2.6% for $108.34/month)
        
        monthly_payment = calculate_monthly_lease_payment(domain_value, lease_rate)
        print(f"The monthly lease payment for the domain is: ${monthly_payment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
