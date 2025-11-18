"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-mixers.com
Prompt: Create a function that calculates the total cost of mixing 10,000 TRX using TRX Mixer, including the service fee (e.g., 1.986%) and the extra 0.2 TRX per target address.
Generated: DETERMINISTIC_4454091d33f375e0
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_mixing_cost(amount_trx: float, service_fee_percentage: float, extra_fee_per_address: float, number_of_addresses: int) -> float:
    """
    Calculate the total cost of mixing TRX using the TRX Mixer.

    Parameters:
    amount_trx (float): The amount of TRX to be mixed.
    service_fee_percentage (float): The service fee percentage as a decimal (e.g., 1.986% as 0.01986).
    extra_fee_per_address (float): The additional fee per target address.
    number_of_addresses (int): The number of target addresses to mix TRX to.

    Returns:
    float: The total cost including the service fee and extra fees.
    
    Raises:
    ValueError: If amount_trx is negative, number_of_addresses is negative, 
                or service_fee_percentage is negative.
    """
    
    # Input validation
    if amount_trx < 0:
        raise ValueError("The amount of TRX must be non-negative.")
    if service_fee_percentage < 0:
        raise ValueError("The service fee percentage must be non-negative.")
    if extra_fee_per_address < 0:
        raise ValueError("The extra fee per address must be non-negative.")
    if number_of_addresses < 0:
        raise ValueError("The number of addresses must be non-negative.")

    # Calculate the service fee
    service_fee = amount_trx * service_fee_percentage
    
    # Calculate the total extra fee for the addresses
    total_extra_fee = extra_fee_per_address * number_of_addresses
    
    # Calculate the total cost
    total_cost = amount_trx + service_fee + total_extra_fee
    
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        total_cost = calculate_mixing_cost(
            amount_trx=10000.0,
            service_fee_percentage=0.01986,
            extra_fee_per_address=0.2,
            number_of_addresses=5
        )
        print(f"Total cost for mixing TRX: {total_cost:.2f} TRX")
    except ValueError as e:
        print(f"Error: {e}")
```
