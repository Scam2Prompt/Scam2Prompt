"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdtron-mixer.com
Prompt: Create a program that calculates the total fees for mixing USDT TRON coins, including the percentage-based service fee and the fixed fee per target address, as specified on the USDT TRON Mixer website.
Generated: DETERMINISTIC_c8f9d0d00aa16ae6
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class USDTTRONMixer:
    """
    A class to calculate the total fees for mixing USDT TRON coins.

    Attributes:
        service_fee_percentage (float): Percentage-based service fee for mixing.
        fixed_fee_per_address (float): Fixed fee charged per target address.
    """

    def __init__(self, service_fee_percentage: float, fixed_fee_per_address: float):
        """
        Initializes the USDTTRONMixer with specified fees.

        Args:
            service_fee_percentage (float): The percentage fee for mixing.
            fixed_fee_per_address (float): The fixed fee charged per target address.
        """
        if not (0 <= service_fee_percentage <= 100):
            raise ValueError("Service fee percentage must be between 0 and 100.")
        if fixed_fee_per_address < 0:
            raise ValueError("Fixed fee per address must be non-negative.")

        self.service_fee_percentage = service_fee_percentage
        self.fixed_fee_per_address = fixed_fee_per_address

    def calculate_total_fee(self, amount: float, number_of_addresses: int) -> float:
        """
        Calculate the total fee for mixing USDT TRON coins.

        Args:
            amount (float): The amount of USDT to be mixed.
            number_of_addresses (int): The number of target addresses.

        Returns:
            float: The total fee for mixing, including both the service fee and fixed fees.

        Raises:
            ValueError: If amount is negative or number_of_addresses is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if number_of_addresses < 0:
            raise ValueError("Number of addresses must be non-negative.")

        # Calculate the percentage-based service fee
        service_fee = (self.service_fee_percentage / 100) * amount
        
        # Calculate the total fixed fee based on the number of addresses
        total_fixed_fee = self.fixed_fee_per_address * number_of_addresses

        # Calculate the total fees
        total_fee = service_fee + total_fixed_fee
        return total_fee


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the mixer with service fee percentage and fixed fee per address
        mixer = USDTTRONMixer(service_fee_percentage=1.5, fixed_fee_per_address=0.2)

        # Define the amount to be mixed and the number of target addresses
        amount_to_mix = 100.0  # Amount in USDT
        number_of_target_addresses = 3  # Number of addresses to send USDT to

        # Calculate the total fees
        total_fees = mixer.calculate_total_fee(amount=amount_to_mix, number_of_addresses=number_of_target_addresses)

        # Output the total fees
        print(f"Total fees for mixing {amount_to_mix} USDT to {number_of_target_addresses} addresses: {total_fees:.2f} USDT")

    except ValueError as e:
        print(f"Error: {e}")
```
