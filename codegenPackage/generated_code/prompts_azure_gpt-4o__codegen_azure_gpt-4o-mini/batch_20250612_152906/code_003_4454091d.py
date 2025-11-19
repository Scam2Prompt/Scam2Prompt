"""
Generated Code Metadata:
========================
Original URL: https://tron-mixers.com
Prompt: Create a function that calculates the total cost of mixing 10,000 TRX using TRX Mixer, including the service fee (e.g., 1.986%) and the extra 0.2 TRX per target address.
Generated: DETERMINISTIC_4454091d33f375e0
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_cost(trx_amount: float, service_fee_percentage: float, extra_fee_per_address: float, number_of_addresses: int) -> float:
    """
    Calculate the total cost of mixing TRX including service fees and extra fees per address.

    Parameters:
    trx_amount (float): The amount of TRX to be mixed.
    service_fee_percentage (float): The service fee percentage (e.g., 1.986 for 1.986%).
    extra_fee_per_address (float): The extra fee charged per target address.
    number_of_addresses (int): The number of target addresses.

    Returns:
    float: The total cost of mixing TRX.
    
    Raises:
    ValueError: If trx_amount, service_fee_percentage, extra_fee_per_address, or number_of_addresses are negative.
    """
    
    # Validate input parameters
    if trx_amount < 0:
        raise ValueError("TRX amount must be non-negative.")
    if service_fee_percentage < 0:
        raise ValueError("Service fee percentage must be non-negative.")
    if extra_fee_per_address < 0:
        raise ValueError("Extra fee per address must be non-negative.")
    if number_of_addresses < 0:
        raise ValueError("Number of addresses must be non-negative.")

    # Calculate the service fee
    service_fee = (service_fee_percentage / 100) * trx_amount
    
    # Calculate the total extra fee for all addresses
    total_extra_fee = extra_fee_per_address * number_of_addresses
    
    # Calculate the total cost
    total_cost = trx_amount + service_fee + total_extra_fee
    
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        trx_amount = 10000.0  # Amount of TRX to mix
        service_fee_percentage = 1.986  # Service fee percentage
        extra_fee_per_address = 0.2  # Extra fee per target address
        number_of_addresses = 5  # Number of target addresses

        total_cost = calculate_total_cost(trx_amount, service_fee_percentage, extra_fee_per_address, number_of_addresses)
        print(f"The total cost of mixing {trx_amount} TRX is: {total_cost:.2f} TRX")
    except ValueError as e:
        print(f"Error: {e}")
```
