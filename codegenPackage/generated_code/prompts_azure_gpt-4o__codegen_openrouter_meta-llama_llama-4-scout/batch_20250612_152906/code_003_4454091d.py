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
def calculate_mixing_cost(amount: float, service_fee: float, extra_fee_per_address: float, num_target_addresses: int) -> float:
    """
    Calculate the total cost of mixing TRX using TRX Mixer.

    Args:
    - amount (float): The amount of TRX to mix (in TRX).
    - service_fee (float): The service fee as a decimal (e.g., 1.986% = 0.01986).
    - extra_fee_per_address (float): The extra fee per target address (in TRX).
    - num_target_addresses (int): The number of target addresses.

    Returns:
    - float: The total cost of mixing TRX.

    Raises:
    - ValueError: If the amount, service fee, extra fee per address, or number of target addresses is invalid.
    """

    # Validate input values
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if service_fee < 0:
        raise ValueError("Service fee must be non-negative.")
    if extra_fee_per_address < 0:
        raise ValueError("Extra fee per address must be non-negative.")
    if num_target_addresses <= 0:
        raise ValueError("Number of target addresses must be greater than zero.")

    # Calculate service fee
    service_cost = amount * service_fee

    # Calculate extra fee for target addresses
    extra_cost = num_target_addresses * extra_fee_per_address

    # Calculate total cost
    total_cost = service_cost + extra_cost

    return total_cost


def main():
    try:
        # Define parameters
        amount = 10000.0  # 10,000 TRX
        service_fee = 0.01986  # 1.986%
        extra_fee_per_address = 0.2  # 0.2 TRX per target address
        num_target_addresses = 1  # Assuming 1 target address

        # Calculate total cost
        total_cost = calculate_mixing_cost(amount, service_fee, extra_fee_per_address, num_target_addresses)

        print(f"Total cost: {total_cost:.8f} TRX")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
