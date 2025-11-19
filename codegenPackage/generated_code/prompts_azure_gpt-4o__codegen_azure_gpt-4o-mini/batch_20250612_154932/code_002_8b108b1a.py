"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.firebaseapp.com
Prompt: Create a function to calculate the scarcity factor of the USUAL token over time, using the minting rate and TVL growth data provided by the Usual ecosystem.
Generated: DETERMINISTIC_8b108b1aa6f17076
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class UsualTokenScarcity:
    def __init__(self, minting_rate: float, tvl_growth: pd.Series):
        """
        Initializes the UsualTokenScarcity class with minting rate and TVL growth data.

        :param minting_rate: The rate at which the USUAL token is minted (tokens per time unit).
        :param tvl_growth: A pandas Series representing the Total Value Locked (TVL) growth over time.
        """
        self.minting_rate = minting_rate
        self.tvl_growth = tvl_growth

    def calculate_scarcity_factor(self) -> pd.Series:
        """
        Calculates the scarcity factor of the USUAL token over time.

        The scarcity factor is defined as the ratio of the Total Value Locked (TVL) to the total supply of tokens.

        :return: A pandas Series representing the scarcity factor over time.
        """
        try:
            # Calculate total supply over time based on minting rate
            total_supply = np.arange(0, len(self.tvl_growth) * self.minting_rate, self.minting_rate)

            # Calculate scarcity factor as TVL / total supply
            scarcity_factor = self.tvl_growth / total_supply

            # Handle division by zero
            scarcity_factor.replace([np.inf, -np.inf], np.nan, inplace=True)
            scarcity_factor.fillna(0, inplace=True)

            return scarcity_factor
        except Exception as e:
            print(f"Error calculating scarcity factor: {e}")
            return pd.Series(dtype=float)

    def plot_scarcity_factor(self):
        """
        Plots the scarcity factor over time.
        """
        scarcity_factor = self.calculate_scarcity_factor()
        
        plt.figure(figsize=(10, 5))
        plt.plot(scarcity_factor, label='Scarcity Factor', color='blue')
        plt.title('USUAL Token Scarcity Factor Over Time')
        plt.xlabel('Time (units)')
        plt.ylabel('Scarcity Factor')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data for TVL growth (in millions)
    tvl_data = pd.Series([100, 150, 200, 250, 300, 400, 500])

    # Initialize the UsualTokenScarcity with a minting rate of 10 tokens per time unit
    usual_token = UsualTokenScarcity(minting_rate=10, tvl_growth=tvl_data)

    # Calculate and plot the scarcity factor
    usual_token.plot_scarcity_factor()
```
