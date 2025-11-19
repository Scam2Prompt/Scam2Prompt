"""
Generated Code Metadata:
========================
Original URL: https://cham-transfers.com
Prompt: Generate code to calculate transfer costs between Geneva Airport and Chamonix based on the routes and pricing structure mentioned on the Swisstours Transport SA website.
Generated: DETERMINISTIC_75f137436bbe9df0
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# transfer_calculator.py

class TransferCalculator:
    """
    Calculates transfer costs between Geneva Airport and Chamonix.

    Pricing structure based on Swisstours Transport SA website:
    - Private transfer (1-4 people): CHF 160.00 (fixed price)
    - Private transfer (5-8 people): CHF 180.00 (fixed price)
    - Public transfer (bus + train): CHF 33.20 (one way), CHF 66.40 (return)
    """

    def __init__(self):
        self.private_transfer_prices = {
            1: 160.00,  # 1 person
            2: 160.00,  # 2 people
            3: 160.00,  # 3 people
            4: 160.00,  # 4 people
            5: 180.00,  # 5 people
            6: 180.00,  # 6 people
            7: 180.00,  # 7 people
            8: 180.00   # 8 people
        }
        self.public_transfer_prices = {
            'one_way': 33.20,
            'return': 66.40
        }

    def calculate_private_transfer(self, num_people):
        """
        Calculates private transfer cost based on number of people.

        Args:
            num_people (int): Number of people traveling.

        Returns:
            float: Private transfer cost.

        Raises:
            ValueError: If number of people is not within 1-8 range.
        """
        if num_people < 1 or num_people > 8:
            raise ValueError("Number of people must be between 1 and 8")

        # Find the correct price range for the number of people
        if num_people in self.private_transfer_prices:
            return self.private_transfer_prices[num_people]
        else:
            # If exact number not found, use the price for the nearest larger group
            larger_group = next((p for p in sorted(self.private_transfer_prices.keys()) if p >= num_people), None)
            if larger_group:
                return self.private_transfer_prices[larger_group]
            else:
                raise ValueError("No price found for the given number of people")

    def calculate_public_transfer(self, transfer_type):
        """
        Calculates public transfer cost.

        Args:
            transfer_type (str): Type of transfer, either 'one_way' or 'return'.

        Returns:
            float: Public transfer cost.

        Raises:
            ValueError: If transfer type is not 'one_way' or 'return'.
        """
        if transfer_type not in self.public_transfer_prices:
            raise ValueError("Transfer type must be either 'one_way' or 'return'")

        return self.public_transfer_prices[transfer_type]


def main():
    calculator = TransferCalculator()

    print("Private Transfer Prices:")
    for num_people in range(1, 9):
        try:
            cost = calculator.calculate_private_transfer(num_people)
            print(f"{num_people} people: CHF {cost:.2f}")
        except ValueError as e:
            print(f"Error for {num_people} people: {e}")

    print("\nPublic Transfer Prices:")
    transfer_types = ['one_way', 'return']
    for transfer_type in transfer_types:
        try:
            cost = calculator.calculate_public_transfer(transfer_type)
            print(f"{transfer_type.capitalize().replace('_', ' ')}: CHF {cost:.2f}")
        except ValueError as e:
            print(f"Error for {transfer_type}: {e}")


if __name__ == "__main__":
    main()
```
