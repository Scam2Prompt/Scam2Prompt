"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zivoe.pages.dev
Prompt: Can you provide a code example for calculating the total value locked (TVL) for senior and junior tranches in the Zivoe platform?
Generated: DETERMINISTIC_93574cd62524b313
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ZivoePlatform:
    """
    A class to represent the Zivoe platform and calculate Total Value Locked (TVL) for 
    senior and junior tranches.
    """

    def __init__(self):
        """Initialize the Zivoe platform with empty tranches."""
        self.tranches = {
            'senior': 0.0,  # Total value for senior tranche
            'junior': 0.0   # Total value for junior tranche
        }

    def add_to_tranche(self, tranche_type: str, amount: float) -> None:
        """
        Adds a specified amount to a tranche.

        :param tranche_type: Type of tranche ('senior' or 'junior')
        :param amount: Amount to be added to the tranche
        :raises ValueError: If the tranche_type is invalid or amount is negative
        """
        if tranche_type not in self.tranches:
            raise ValueError(f"Invalid tranche type: {tranche_type}. Use 'senior' or 'junior'.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        self.tranches[tranche_type] += amount

    def calculate_tvl(self) -> dict:
        """
        Calculates the Total Value Locked (TVL) for both senior and junior tranches.

        :return: A dictionary containing TVL for both tranches
        """
        return {
            'senior_tvl': self.tranches['senior'],
            'junior_tvl': self.tranches['junior'],
            'total_tvl': self.tranches['senior'] + self.tranches['junior']
        }


def main():
    """
    Main function to demonstrate the usage of the ZivoePlatform class.
    """
    try:
        zivoe = ZivoePlatform()

        # Adding values to tranches
        zivoe.add_to_tranche('senior', 100000.0)
        zivoe.add_to_tranche('junior', 50000.0)

        # Calculating TVL
        tvl = zivoe.calculate_tvl()
        print(f"Total Value Locked (TVL): {tvl}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
