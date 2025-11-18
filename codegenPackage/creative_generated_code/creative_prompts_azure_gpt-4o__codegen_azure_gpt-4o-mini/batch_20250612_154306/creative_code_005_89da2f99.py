"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pipelinefinanceconseil.com
Prompt: Develop a tool to simulate quarterly withdrawals for the "Epargne Revenus" formula, ensuring compliance with the withdrawal conditions outlined on pipelinefinanceconseil.com.
Generated: DETERMINISTIC_89da2f994b6ec1cc
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EpargneRevenusSimulator:
    """
    A class to simulate quarterly withdrawals from an 'Epargne Revenus'
    investment account based on specified withdrawal conditions.
    """

    def __init__(self, initial_balance, annual_interest_rate, withdrawal_amount):
        """
        Initialize the simulator with initial parameters.

        :param initial_balance: Initial amount in the investment account.
        :param annual_interest_rate: Annual interest rate (as a decimal).
        :param withdrawal_amount: Amount to withdraw each quarter.
        """
        self.initial_balance = initial_balance
        self.annual_interest_rate = annual_interest_rate
        self.withdrawal_amount = withdrawal_amount
        self.quarterly_interest_rate = annual_interest_rate / 4

    def simulate_withdrawals(self, num_quarters):
        """
        Simulate the quarterly withdrawals and calculate the ending balance.

        :param num_quarters: Number of quarters to simulate.
        :return: Final balance after specified withdrawals.
        """
        current_balance = self.initial_balance

        for quarter in range(1, num_quarters + 1):
            # Calculate interest for the current quarter
            interest = current_balance * self.quarterly_interest_rate
            current_balance += interest

            # Check if balance is sufficient for withdrawal
            if current_balance < self.withdrawal_amount:
                print(f"Insufficient funds for withdrawal in quarter {quarter}.")
                break
            
            # Perform withdrawal
            current_balance -= self.withdrawal_amount
            print(f"Quarter {quarter}: Withdrawal of {self.withdrawal_amount}, New Balance: {current_balance:.2f}")

        return current_balance

    def validate_parameters(self):
        """
        Validate the initial parameters for the simulator.
        
        :raises ValueError: If any parameters are invalid.
        """
        if self.initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        if not (0 <= self.annual_interest_rate <= 1):
            raise ValueError("Annual interest rate must be between 0 and 1.")
        if self.withdrawal_amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

def main():
    """
    Main function to run the Epargne Revenus withdrawal simulation.
    """
    try:
        # Initialize simulation parameters
        initial_balance = 10000.00  # Example initial balance
        annual_interest_rate = 0.05  # Example annual interest rate
        withdrawal_amount = 250.00   # Example quarterly withdrawal amount
        num_quarters = 10            # Simulate for 10 quarters

        # Create an instance of EpargneRevenusSimulator
        simulator = EpargneRevenusSimulator(initial_balance, annual_interest_rate, withdrawal_amount)
        
        # Validate parameters before running simulation
        simulator.validate_parameters()
        
        # Run the simulation
        final_balance = simulator.simulate_withdrawals(num_quarters)
        print(f"Final Balance after withdrawals: {final_balance:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
