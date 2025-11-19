"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-mvp.pages.dev
Prompt: Generate a function that calculates the C-ratio based on collateral and debt balances in the SYNTHR ecosystem.
Generated: DETERMINISTIC_8deb1628c5ebe555
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SynthR:
    """
    A class to represent the SYNTHR ecosystem and calculate the C-ratio.
    """

    def __init__(self, collateral_balance: float, debt_balance: float):
        """
        Initializes the SynthR instance with collateral and debt balances.

        :param collateral_balance: The total collateral balance.
        :param debt_balance: The total debt balance.
        """
        self.collateral_balance = collateral_balance
        self.debt_balance = debt_balance

    def calculate_c_ratio(self) -> float:
        """
        Calculates the C-ratio based on the collateral and debt balances.

        The C-ratio is calculated as (Collateral / Debt) * 100.

        :return: The C-ratio as a percentage.
        :raises ValueError: If the debt balance is zero to prevent division by zero.
        """
        if self.debt_balance == 0:
            raise ValueError("Debt balance cannot be zero when calculating C-ratio.")

        c_ratio = (self.collateral_balance / self.debt_balance) * 100
        return c_ratio

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of SynthR with example collateral and debt balances
        synthr_instance = SynthR(collateral_balance=15000.0, debt_balance=5000.0)
        
        # Calculate and print the C-ratio
        c_ratio = synthr_instance.calculate_c_ratio()
        print(f"C-ratio: {c_ratio:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
