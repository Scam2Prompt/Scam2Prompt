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
def calculate_monthly_domain_lease(domain_value: float, monthly_rate: float) -> float:
    """
    Calculate the monthly lease payment for a domain name.

    Parameters:
        domain_value (float): The total value of the domain in USD.
        monthly_rate (float): The monthly lease rate as a percentage of the domain value.

    Returns:
        float: The calculated monthly lease payment in USD.

    Raises:
        ValueError: If domain_value or monthly_rate is negative.
    """
    # Validate input
    if domain_value < 0:
        raise ValueError("Domain value cannot be negative.")
    if monthly_rate < 0:
        raise ValueError("Monthly rate cannot be negative.")

    # Calculate the monthly lease payment
    monthly_payment = domain_value * (monthly_rate / 100)

    return monthly_payment


# Example usage
if __name__ == "__main__":
    try:
        # Example values
        domain_value = 5000.0  # USD
        monthly_rate = 108.34 / domain_value * 100  # Convert $108.34/month to percentage

        # Calculate the monthly payment
        payment = calculate_monthly_domain_lease(domain_value, monthly_rate)
        print(f"Monthly lease payment for a ${domain_value:.2f} domain: ${payment:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
