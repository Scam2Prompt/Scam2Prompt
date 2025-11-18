"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Generate a script to calculate savings growth over time, leveraging Genesis Investment Credit Union's savings account features.
Generated: DETERMINISTIC_b17d76065dea7571
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

class SavingsAccount:
    """A class to represent a savings account."""

    def __init__(self, initial_balance, annual_interest_rate):
        """
        Initialize the savings account with an initial balance and annual interest rate.

        Parameters:
        initial_balance (float): The starting balance of the savings account.
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 5 for 5%).
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")

        self.balance = initial_balance
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal

    def calculate_growth(self, years):
        """
        Calculate the growth of savings over a specified number of years.

        Parameters:
        years (int): The number of years to calculate growth for.

        Returns:
        list: A list of balances at the end of each year.
        """
        if years < 0:
            raise ValueError("Number of years cannot be negative.")
        
        balances = []
        for year in range(years + 1):
            balances.append(self.balance)
            self.balance *= (1 + self.annual_interest_rate)  # Compound interest formula
        
        return balances

def plot_growth(years, balances):
    """Plot the growth of savings over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(range(years + 1), balances, marker='o')
    plt.title('Savings Growth Over Time')
    plt.xlabel('Years')
    plt.ylabel('Balance ($)')
    plt.grid()
    plt.xticks(range(0, years + 1))
    plt.yticks([round(b, 2) for b in balances])
    plt.show()

def main():
    """Main function to execute the savings growth calculation."""
    try:
        initial_balance = float(input("Enter the initial balance: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the number of years: "))

        # Initialize savings account
        savings_account = SavingsAccount(initial_balance, annual_interest_rate)

        # Calculate growth
        balances = savings_account.calculate_growth(years)

        # Plot results
        plot_growth(years, balances)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
