"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-portal.firebaseapp.com
Prompt: Create a function to calculate the scarcity factor of the USUAL token over time, using the minting rate and TVL growth data provided by the Usual ecosystem.
Generated: DETERMINISTIC_8b108b1aa6f17076
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class UsualToken:
    def __init__(self, minting_rate, tvl_data):
        """
        Initializes the UsualToken class with minting rate and TVL data.
        
        :param minting_rate: The rate at which new tokens are minted (tokens per time unit)
        :param tvl_data: A pandas DataFrame containing the Time, Total Value Locked (TVL)
        """
        self.minting_rate = minting_rate
        self.tvl_data = tvl_data

    def calculate_scarcity_factor(self):
        """
        Calculates the scarcity factor of the USUAL token over time based on minting rate and TVL growth.
        
        :return: A pandas DataFrame containing Time, TVL, and Scarcity Factor
        """
        if 'Time' not in self.tvl_data.columns or 'TVL' not in self.tvl_data.columns:
            raise ValueError("tvl_data must contain 'Time' and 'TVL' columns.")
        
        # Calculate the total minted tokens over time
        total_minted = self.minting_rate * self.tvl_data['Time']

        # Calculate the scarcity factor as the ratio of TVL to total minted tokens
        scarcity_factor = self.tvl_data['TVL'] / total_minted
        
        # Construct a new DataFrame to hold the results
        result_df = pd.DataFrame({
            'Time': self.tvl_data['Time'],
            'TVL': self.tvl_data['TVL'],
            'Scarcity Factor': scarcity_factor
        })
        
        return result_df

    def plot_scarcity_factor(self, result_df):
        """
        Plots the scarcity factor over time.
        
        :param result_df: A pandas DataFrame with the results containing Time, TVL, and Scarcity Factor
        """
        plt.figure(figsize=(10, 6))
        plt.plot(result_df['Time'], result_df['Scarcity Factor'], marker='o', color='b', label='Scarcity Factor')
        plt.title('Scarcity Factor of USUAL Token Over Time')
        plt.xlabel('Time')
        plt.ylabel('Scarcity Factor')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Sample TVL data for demonstration
    data = {
        'Time': [0, 1, 2, 3, 4, 5],
        'TVL': [1000, 1500, 2000, 2500, 3100, 4000]
    }
    
    tvl_df = pd.DataFrame(data)
    minting_rate = 50  # Example minting rate

    # Create an instance of UsualToken and calculate the scarcity factor
    usual_token = UsualToken(minting_rate, tvl_df)
    scarcity_df = usual_token.calculate_scarcity_factor()
    
    # Plot the results
    usual_token.plot_scarcity_factor(scarcity_df)
```
