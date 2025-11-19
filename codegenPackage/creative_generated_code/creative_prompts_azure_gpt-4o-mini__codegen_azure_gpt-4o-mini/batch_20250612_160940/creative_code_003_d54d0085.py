"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Create a function that simulates the compounding rewards for Sidus staking over a specified lock term on SidusPad.
Generated: DETERMINISTIC_d54d00850cd6af42
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SidusStakingSimulator:
    """
    A class to simulate the compounding rewards for Sidus staking on SidusPad.
    """

    def __init__(self, initial_investment, annual_interest_rate, lock_term_years):
        """
        Initializes the simulator with the provided investment details.

        :param initial_investment: The initial amount invested in Sidus.
        :param annual_interest_rate: The annual interest rate as a decimal (e.g., 0.05 for 5%).
        :param lock_term_years: The duration of the lock term in years.
        """
        # Validate input parameters
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 < annual_interest_rate < 1):
            raise ValueError("Annual interest rate must be between 0 and 1.")
        if lock_term_years <= 0:
            raise ValueError("Lock term must be greater than zero years.")

        self.initial_investment = initial_investment
        self.annual_interest_rate = annual_interest_rate
        self.lock_term_years = lock_term_years

    def calculate_compounded_value(self):
        """
        Calculate the compounded value of the investment after the lock term.

        :return: The total value of the investment after compounding.
        """
        compounded_value = self.initial_investment * (1 + self.annual_interest_rate) ** self.lock_term_years
        return compounded_value

    def simulate(self):
        """
        Simulate the staking rewards and return the results.

        :return: A dictionary containing the initial investment, final value, and total rewards earned.
        """
        final_value = self.calculate_compounded_value()
        total_rewards = final_value - self.initial_investment

        # Prepare the result
        result = {
            "initial_investment": self.initial_investment,
            "final_value": final_value,
            "total_rewards": total_rewards,
            "lock_term_years": self.lock_term_years
        }
        
        return result

# Example execution of the simulator
if __name__ == "__main__":
    try:
        # User-defined parameters
        investment_amount = 1000  # Initial investment in Sidus
        annual_rate = 0.05        # Annual interest rate of 5%
        lock_period = 3           # Lock term of 3 years

        # Create a simulator instance
        simulator = SidusStakingSimulator(investment_amount, annual_rate, lock_period)

        # Run the simulation and print the results
        results = simulator.simulate()
        print(f"Initial Investment: ${results['initial_investment']:.2f}")
        print(f"Final Value after {results['lock_term_years']} years: ${results['final_value']:.2f}")
        print(f"Total Rewards Earned: ${results['total_rewards']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
