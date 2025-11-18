"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.io
Prompt: Create a program that calculates the service fee for mixing Bitcoin using CryptoMixer, including configurable delays and multiple output addresses as described on the website.
Generated: DETERMINISTIC_41c52ca064c39b0e
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class CryptoMixer:
    """
    Class to calculate and simulate Bitcoin mixing service fees and operations.
    """

    def __init__(self, base_fee_percent=0.5, delay_range=(30, 300)):
        """
        Initialize the CryptoMixer instance.
        
        :param base_fee_percent: The base percentage fee for the mixing service.
        :param delay_range: Tuple indicating minimum and maximum delay in seconds for transactions.
        """
        self.base_fee_percent = base_fee_percent
        self.delay_range = delay_range

    def calculate_service_fee(self, amount):
        """
        Calculate the service fee for mixing.

        :param amount: The amount of Bitcoin to be mixed.
        :return: Service fee in Bitcoin.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        # Calculate the fee as a percentage of the amount
        fee = amount * (self.base_fee_percent / 100)
        return fee

    def distribute_funds(self, amount, output_addresses):
        """
        Distribute funds to multiple output addresses after deducting the service fee.
        
        :param amount: Total amount of Bitcoin to be distributed.
        :param output_addresses: List of output Bitcoin addresses.
        :return: Dictionary with output addresses and their respective amounts.
        """
        if not output_addresses:
            raise ValueError("At least one output address must be provided.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Calculate service fee and remaining amount after deduction
        service_fee = self.calculate_service_fee(amount)
        amount_after_fee = amount - service_fee

        if amount_after_fee <= 0:
            raise ValueError("Amount after service fee is insufficient for distribution.")

        # Randomly distribute funds across output addresses
        distribution = {}
        remaining_amount = amount_after_fee

        for i, address in enumerate(output_addresses):
            if i == len(output_addresses) - 1:
                # Allocate remaining amount to the last address
                distribution[address] = round(remaining_amount, 8)  # Bitcoin precision
            else:
                # Randomly allocate a portion of the remaining amount
                max_allocatable = remaining_amount / 2
                allocated_amount = round(random.uniform(0.01, max_allocatable), 8)
                distribution[address] = allocated_amount
                remaining_amount -= allocated_amount

        return distribution

    def simulate_transaction_delay(self):
        """
        Simulate transaction delay based on configured delay range.
        """
        delay = random.randint(self.delay_range[0], self.delay_range[1])
        time.sleep(delay)  # Pause execution to simulate delay

def main():
    # Example usage of CryptoMixer
    
    try:
        mixer = CryptoMixer(base_fee_percent=1.0, delay_range=(60, 120))  # 1% fee with 1-2 min delay
        
        amount_to_mix = 0.5  # Bitcoin amount to mix
        output_addresses = [
            "1BitcoinAddressExample1",
            "1BitcoinAddressExample2",
            "1BitcoinAddressExample3"
        ]

        print("Calculating service fee...")
        service_fee = mixer.calculate_service_fee(amount_to_mix)
        print(f"Service fee: {service_fee:.8f} BTC")

        print("\nDistributing funds to output addresses...")
        distribution = mixer.distribute_funds(amount_to_mix, output_addresses)
        for address, btc in distribution.items():
            print(f"Address: {address} - Amount: {btc:.8f} BTC")

        print("\nSimulating transaction delay...")
        mixer.simulate_transaction_delay()
        print("Transactions completed with delay.")
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
