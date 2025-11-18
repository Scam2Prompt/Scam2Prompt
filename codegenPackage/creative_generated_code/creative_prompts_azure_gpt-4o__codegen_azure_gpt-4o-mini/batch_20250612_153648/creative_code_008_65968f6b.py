"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Develop a tool to simulate the impact of early access participation on token rewards in Manta CeDeFi, using the APR and TVL data provided.
Generated: DETERMINISTIC_65968f6be60f54b4
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class TokenRewardSimulator:
    """
    A class to simulate the impact of early access participation on token rewards in Manta CeDeFi.
    
    Attributes:
    ----------
    apr : float
        Annual Percentage Rate of the token rewards
    tvl : float
        Total Value Locked in the liquidity pool
    participation_percent : float
        Percentage of early access participation
    """
    
    def __init__(self, apr: float, tvl: float, participation_percent: float):
        """
        Initializes the TokenRewardSimulator with APR, TVL, and participation percentage.

        Parameters:
        ----------
        apr : float
            Annual Percentage Rate (APR) as a decimal (e.g., 0.05 for 5%)
        tvl : float
            Total Value Locked (TVL) in the liquidity pool
        participation_percent : float
            Percentage of early access participation (e.g., 0.1 for 10%)
        """
        self.apr = apr
        self.tvl = tvl
        self.participation_percent = participation_percent

    def calculate_rewards(self) -> float:
        """
        Calculate the estimated token rewards based on the APR, TVL, and participation.

        Returns:
        -------
        float
            Estimated token rewards from early access participation
        """
        # Validate input values
        if not (0 <= self.apr <= 1):
            raise ValueError("APR must be between 0 and 1.")
        if self.tvl < 0:
            raise ValueError("TVL must be a non-negative value.")
        if not (0 <= self.participation_percent <= 1):
            raise ValueError("Participation percentage must be between 0 and 1.")
        
        # Calculate total annual rewards based on TVL and APR
        total_annual_rewards = self.tvl * self.apr
        
        # Calculate rewards based on early access participation
        early_access_rewards = total_annual_rewards * self.participation_percent
        
        return early_access_rewards

def main():
    """
    Main function to demonstrate the TokenRewardSimulator functionality.
    It will prompt user inputs for APR, TVL, and participation percentage, and output the estimated rewards.
    """
    try:
        apr = float(input("Enter the Annual Percentage Rate (APR) as a decimal (e.g., 0.05 for 5%): "))
        tvl = float(input("Enter the Total Value Locked (TVL): "))
        participation_percent = float(input("Enter the early access participation percentage as a decimal (e.g., 0.1 for 10%): "))

        # Create an instance of the simulator
        simulator = TokenRewardSimulator(apr, tvl, participation_percent)

        # Calculate and display rewards
        rewards = simulator.calculate_rewards()
        print(f"Estimated token rewards from early access participation: {rewards:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
