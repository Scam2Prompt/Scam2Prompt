"""
Generated Code Metadata:
========================
Original URL: https://usdt-mixer-mix.com
Prompt: Develop a Python program that calculates the service fee for mixing USDT transactions based on the number of Coinjoins and initiation fee, as outlined on the USDT Mixer website.
Generated: DETERMINISTIC_0e9269d4cd633ed9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class USDTMixer:
    """
    A class to calculate the service fee for mixing USDT transactions.
    """

    def __init__(self, initiation_fee: float, coinjoin_fee: float):
        """
        Initializes the USDTMixer with the given fees.

        :param initiation_fee: The fixed fee charged for initiating a mix.
        :param coinjoin_fee: The fee charged per Coinjoin.
        """
        if initiation_fee < 0 or coinjoin_fee < 0:
            raise ValueError("Fees must be non-negative.")

        self.initiation_fee = initiation_fee
        self.coinjoin_fee = coinjoin_fee

    def calculate_service_fee(self, number_of_coinjoins: int) -> float:
        """
        Calculates the total service fee based on the number of Coinjoins.

        :param number_of_coinjoins: The number of Coinjoins to be performed.
        :return: The total service fee.
        """
        if number_of_coinjoins < 0:
            raise ValueError("Number of Coinjoins must be non-negative.")

        total_fee = self.initiation_fee + (self.coinjoin_fee * number_of_coinjoins)
        return total_fee


def main():
    """
    Main function to execute the service fee calculation.
    """
    try:
        # Example fees (these can be adjusted as needed)
        initiation_fee = 10.0  # Fixed initiation fee
        coinjoin_fee = 2.0      # Fee per Coinjoin

        # Create an instance of USDTMixer
        mixer = USDTMixer(initiation_fee, coinjoin_fee)

        # Input: Number of Coinjoins
        number_of_coinjoins = int(input("Enter the number of Coinjoins: "))

        # Calculate the service fee
        service_fee = mixer.calculate_service_fee(number_of_coinjoins)

        # Output the result
        print(f"The total service fee for {number_of_coinjoins} Coinjoins is: ${service_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
