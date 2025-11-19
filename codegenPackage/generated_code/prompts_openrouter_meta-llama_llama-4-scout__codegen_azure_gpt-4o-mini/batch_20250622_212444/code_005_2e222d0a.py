"""
Generated Code Metadata:
========================
Original URL: https://dikmansdeli.ru
Prompt: "Explain the algorithm used by Venus Protocol to determine interest rates for borrowing and lending, and provide a mathematical example of its application."
Generated: DETERMINISTIC_2e222d0a125f865c
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VenusProtocol:
    """
    A class to represent the Venus Protocol for determining interest rates for borrowing and lending.
    """

    def __init__(self, supply_rate: float, borrow_rate: float, utilization_rate: float):
        """
        Initializes the VenusProtocol with supply rate, borrow rate, and utilization rate.

        :param supply_rate: The interest rate for supplying assets.
        :param borrow_rate: The interest rate for borrowing assets.
        :param utilization_rate: The ratio of borrowed assets to supplied assets.
        """
        self.supply_rate = supply_rate
        self.borrow_rate = borrow_rate
        self.utilization_rate = utilization_rate

    def calculate_interest_rates(self):
        """
        Calculates the effective interest rates based on the utilization rate.

        :return: A tuple containing the effective supply rate and borrow rate.
        """
        try:
            # Ensure utilization rate is within valid bounds
            if not (0 <= self.utilization_rate <= 1):
                raise ValueError("Utilization rate must be between 0 and 1.")

            # Calculate effective supply rate
            effective_supply_rate = self.supply_rate * (1 - self.utilization_rate)

            # Calculate effective borrow rate
            effective_borrow_rate = self.borrow_rate * self.utilization_rate

            return effective_supply_rate, effective_borrow_rate

        except Exception as e:
            print(f"Error calculating interest rates: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize the Venus Protocol with example rates
    supply_rate = 0.05  # 5% supply rate
    borrow_rate = 0.1   # 10% borrow rate
    utilization_rate = 0.6  # 60% utilization

    venus = VenusProtocol(supply_rate, borrow_rate, utilization_rate)

    # Calculate and print the interest rates
    interest_rates = venus.calculate_interest_rates()
    if interest_rates:
        effective_supply_rate, effective_borrow_rate = interest_rates
        print(f"Effective Supply Rate: {effective_supply_rate:.2%}")
        print(f"Effective Borrow Rate: {effective_borrow_rate:.2%}")
```
