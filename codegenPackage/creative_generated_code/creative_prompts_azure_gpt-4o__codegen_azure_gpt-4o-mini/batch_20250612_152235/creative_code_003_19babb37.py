"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plnksale.vercel.app
Prompt: Write a script to calculate the liquidity percentage for a presale, ensuring that less than 51% of raised funds are allocated to liquidity, as described in the Baby Maga project.
Generated: DETERMINISTIC_19babb37067cd10e
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Presale:
    def __init__(self, total_raised: float, liquidity_allocation: float):
        """
        Initialize the Presale object with the total amount raised and the liquidity allocation.

        :param total_raised: Total funds raised in the presale
        :param liquidity_allocation: Amount allocated to liquidity
        """
        if total_raised <= 0:
            raise ValueError("Total raised amount must be greater than zero.")
        if liquidity_allocation < 0:
            raise ValueError("Liquidity allocation cannot be negative.")
        
        self.total_raised = total_raised
        self.liquidity_allocation = liquidity_allocation

    def calculate_liquidity_percentage(self) -> float:
        """
        Calculate the liquidity percentage of the funds raised.

        :return: Liquidity percentage
        """
        liquidity_percentage = (self.liquidity_allocation / self.total_raised) * 100
        return liquidity_percentage

    def is_liquidity_allocation_valid(self) -> bool:
        """
        Check if the liquidity allocation is less than 51% of the total raised funds.

        :return: True if allocation is valid, False otherwise
        """
        liquidity_percentage = self.calculate_liquidity_percentage()
        return liquidity_percentage < 51

def main():
    """
    Main function to run the liquidity allocation check for a presale.
    """
    try:
        total_raised = float(input("Enter the total amount raised in the presale: "))
        liquidity_allocation = float(input("Enter the amount allocated to liquidity: "))

        presale = Presale(total_raised, liquidity_allocation)

        liquidity_percentage = presale.calculate_liquidity_percentage()
        print(f"Liquidity Percentage: {liquidity_percentage:.2f}%")

        if presale.is_liquidity_allocation_valid():
            print("The liquidity allocation is valid.")
        else:
            print("Warning: The liquidity allocation exceeds 51% of the total funds raised.")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
