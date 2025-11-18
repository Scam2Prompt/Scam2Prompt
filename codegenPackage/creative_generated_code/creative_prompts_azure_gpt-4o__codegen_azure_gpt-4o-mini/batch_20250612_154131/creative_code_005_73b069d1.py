"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.com
Prompt: Develop a custom strategy for curating vaults on Morpho's platform. Include code for optimizing yield, risk, and liquidity while earning fees.
Generated: DETERMINISTIC_73b069d1728d21d3
Batch ID: 20250612_154131
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

class VaultCurator:
    """
    A class to curate vaults on Morpho's platform, optimizing yield, risk, and liquidity.
    """

    def __init__(self, vault_data):
        """
        Initializes the VaultCurator with vault data.

        Args:
            vault_data (pd.DataFrame): DataFrame containing columns for 'yield', 'risk', 'liquidity', and 'fees'.
        """
        self.vault_data = vault_data

    def optimize_vaults(self):
        """
        Optimizes vaults based on yield, risk, liquidity, and fees.
        Returns a curated list of vaults that meet the optimization criteria.

        Returns:
            pd.DataFrame: A DataFrame of optimized vaults.
        """

        try:
            # Calculate a score based on yield and risk
            self.vault_data['score'] = (
                self.vault_data['yield'] / (1 + self.vault_data['risk'])
            ) * self.vault_data['liquidity'] * (1 - self.vault_data['fees'])
            
            # Filter vaults with a positive score
            curated_vaults = self.vault_data[self.vault_data['score'] > 0]

            # Sort vaults based on the score in descending order
            curated_vaults = curated_vaults.sort_values(by='score', ascending=False)

            return curated_vaults

        except KeyError as e:
            print(f"KeyError: {e}. Please check the input DataFrame columns.")
            return pd.DataFrame()  # Return an empty DataFrame on error
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def display_curated_vaults(self):
        """
        Displays the curated vaults.
        """
        curated_vaults = self.optimize_vaults()
        if not curated_vaults.empty:
            print("Curated Vaults:")
            print(curated_vaults[['yield', 'risk', 'liquidity', 'fees', 'score']])
        else:
            print("No vaults meet the optimization criteria.")

# Example usage:
if __name__ == "__main__":
    # Sample vault data
    data = {
        'yield': [0.05, 0.07, 0.04, 0.06],
        'risk': [0.01, 0.03, 0.02, 0.04],
        'liquidity': [10000, 20000, 15000, 5000],
        'fees': [0.01, 0.005, 0.015, 0.02]
    }
    
    vault_df = pd.DataFrame(data)

    # Create an instance of VaultCurator
    curator = VaultCurator(vault_df)

    # Display curated vaults
    curator.display_curated_vaults()
```
