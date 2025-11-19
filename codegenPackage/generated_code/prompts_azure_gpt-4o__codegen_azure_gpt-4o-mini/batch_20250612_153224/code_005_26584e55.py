"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: Write a script to calculate the service fee for passing prop firm challenges based on account sizes (e.g., $100 for a $10K account, $500 for a $200K account) and simulate refund conditions if the challenge is not passed.
Generated: DETERMINISTIC_26584e557f64787d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropFirmChallenge:
    """
    A class to represent a prop firm challenge and calculate service fees based on account sizes.
    """

    def __init__(self):
        # Define a mapping of account sizes to service fees
        self.fee_structure = {
            10000: 100,
            200000: 500,
            50000: 250,
            100000: 400
        }

    def calculate_service_fee(self, account_size):
        """
        Calculate the service fee based on the provided account size.

        :param account_size: The size of the account (in dollars)
        :return: The service fee (in dollars)
        :raises ValueError: If the account size is not in the fee structure
        """
        if account_size not in self.fee_structure:
            raise ValueError(f"Account size ${account_size} is not supported.")
        return self.fee_structure[account_size]

    def simulate_refund(self, account_size, passed_challenge):
        """
        Simulate the refund conditions based on whether the challenge was passed.

        :param account_size: The size of the account (in dollars)
        :param passed_challenge: Boolean indicating if the challenge was passed
        :return: Refund amount (in dollars) or service fee if not refunded
        """
        try:
            service_fee = self.calculate_service_fee(account_size)
            if passed_challenge:
                return 0  # No refund if the challenge is passed
            else:
                return service_fee  # Refund the service fee if the challenge is not passed
        except ValueError as e:
            print(f"Error: {e}")
            return None  # Return None if there was an error

def main():
    """
    Main function to demonstrate the PropFirmChallenge class functionality.
    """
    challenge = PropFirmChallenge()

    # Example account sizes to test
    account_sizes = [10000, 200000, 50000, 100000]
    results = {}

    for size in account_sizes:
        # Simulate both passing and failing the challenge
        results[size] = {
            "passed": challenge.simulate_refund(size, True),
            "failed": challenge.simulate_refund(size, False)
        }

    # Print the results
    for size, result in results.items():
        print(f"Account Size: ${size}")
        print(f"  Refund if passed: ${result['passed']}")
        print(f"  Refund if failed: ${result['failed']}")
        print()

if __name__ == "__main__":
    main()
```
