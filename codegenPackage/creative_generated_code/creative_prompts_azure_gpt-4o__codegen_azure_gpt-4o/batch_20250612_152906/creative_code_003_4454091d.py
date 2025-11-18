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
def calculate_mixing_cost(base_amount, target_addresses, service_fee_percentage, extra_fee_per_address):
    """
    Calculates the total cost of mixing TRX using a TRX Mixer.
    
    Args:
        base_amount (float): The base amount of TRX to be mixed.
        target_addresses (int): The number of target addresses for mixing.
        service_fee_percentage (float): The service fee percentage (e.g., 1.986% as 1.986).
        extra_fee_per_address (float): The extra fee charged per target address (e.g., 0.2 TRX).
    
    Returns:
        float: The total cost of mixing TRX.
    """
    try:
        # Validate input data
        if base_amount <= 0:
            raise ValueError("Base amount must be greater than zero.")
        if target_addresses <= 0:
            raise ValueError("Target addresses must be a positive integer.")
        if service_fee_percentage < 0:
            raise ValueError("Service fee percentage cannot be negative.")
        if extra_fee_per_address < 0:
            raise ValueError("Extra fee per address cannot be negative.")
        
        # Calculate the service fee based on the base amount
        service_fee = (service_fee_percentage / 100) * base_amount
        
        # Calculate the total extra fee for all target addresses
        total_extra_fee = extra_fee_per_address * target_addresses
        
        # Calculate the total cost
        total_cost = base_amount + service_fee + total_extra_fee
        
        return total_cost
    
    except ValueError as e:
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Parameters
    BASE_AMOUNT = 10000  # Base amount of TRX
    TARGET_ADDRESSES = 5  # Number of target addresses
    SERVICE_FEE_PERCENTAGE = 1.986  # Service fee percentage
    EXTRA_FEE_PER_ADDRESS = 0.2  # Extra fee per target address

    # Calculate the total mixing cost
    total_cost = calculate_mixing_cost(BASE_AMOUNT, TARGET_ADDRESSES, SERVICE_FEE_PERCENTAGE, EXTRA_FEE_PER_ADDRESS)
    
    if total_cost is not None:
        print(f"The total cost of mixing {BASE_AMOUNT} TRX is: {total_cost:.2f} TRX")
```
