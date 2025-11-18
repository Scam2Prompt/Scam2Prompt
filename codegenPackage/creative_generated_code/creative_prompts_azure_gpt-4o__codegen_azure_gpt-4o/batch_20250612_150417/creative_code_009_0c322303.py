"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passiveinvestincome.com
Prompt: Write a program to simulate the reinvestment process through an interest wallet, as mentioned in PassiveInvestIncome's referral program. Include functionality to track reinvestment amounts and calculate updated earnings.
Generated: DETERMINISTIC_0c322303de201aff
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InterestWallet:
    def __init__(self, initial_balance, annual_interest_rate):
        """
        Initializes the Interest Wallet with a starting balance and annual interest rate.
        
        :param initial_balance: Starting balance in the wallet (float)
        :param annual_interest_rate: Annual interest rate as a percentage (float)
        """
        if initial_balance < 0 or annual_interest_rate < 0:
            raise ValueError("Initial balance and annual interest rate must be non-negative.")
        
        self.balance = initial_balance
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.total_reinvested = 0.0  # Tracks total reinvestment amount
    
    def calculate_monthly_earnings(self):
        """
        Calculates monthly earnings based on the current balance and annual interest rate.
        
        :return: Monthly earnings (float)
        """
        return self.balance * (self.annual_interest_rate / 12)
    
    def reinvest_earnings(self):
        """
        Reinvests monthly earnings back into the wallet and updates the total reinvested amount.
        """
        monthly_earnings = self.calculate_monthly_earnings()
        self.balance += monthly_earnings
        self.total_reinvested += monthly_earnings
    
    def get_wallet_summary(self):
        """
        Retrieves the wallet's current balance, total reinvested amount, and monthly earnings.
        
        :return: A dictionary containing wallet summary.
        """
        return {
            "Current Balance": round(self.balance, 2),
            "Total Reinvested": round(self.total_reinvested, 2),
            "Monthly Earnings": round(self.calculate_monthly_earnings(), 2),
        }

def simulate_reinvestment_process(initial_balance, annual_interest_rate, months):
    """
    Simulates the reinvestment process over a number of months.
    
    :param initial_balance: Starting balance for the simulation (float)
    :param annual_interest_rate: Annual interest rate as a percentage (float)
    :param months: Number of months to simulate (int)
    :return: Final wallet summary (dictionary)
    """
    try:
        # Create an instance of InterestWallet
        wallet = InterestWallet(initial_balance, annual_interest_rate)
        
        # Perform reinvestment for the specified number of months
        for month in range(1, months + 1):
            wallet.reinvest_earnings()
        
        # Return wallet summary after simulation
        return wallet.get_wallet_summary()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    try:
        # Input parameters for simulation
        initial_balance = float(input("Enter initial balance: "))
        annual_interest_rate = float(input("Enter annual interest rate (in %): "))
        months = int(input("Enter number of months to simulate: "))
        
        # Run simulation and display results
        final_summary = simulate_reinvestment_process(initial_balance, annual_interest_rate, months)
        print("\nReinvestment Simulation Summary:")
        for key, value in final_summary.items():
            print(f"{key}: ${value}")
    except ValueError:
        print("Invalid input. Please enter numerical values for balance, interest rate, and months.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
