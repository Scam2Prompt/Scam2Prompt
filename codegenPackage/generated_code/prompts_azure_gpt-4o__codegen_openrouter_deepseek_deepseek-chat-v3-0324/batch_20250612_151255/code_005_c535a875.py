"""
Generated Code Metadata:
========================
Original URL: https://claim-beef-meme.pages.dev
Prompt: Create a Python script to calculate the percentage of BEEF Coin distribution across DEX liquidity pools, CEX liquidity pools, and airdrops based on the tokenomics provided.
Generated: DETERMINISTIC_c535a875e98b0978
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class BeefCoinDistribution:
    """
    A class to calculate and manage the distribution percentages of BEEF Coin.
    """
    
    def __init__(self, total_supply: float):
        """
        Initialize the BeefCoinDistribution with the total supply of BEEF Coin.
        
        Args:
            total_supply (float): The total supply of BEEF Coin.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        self.total_supply = total_supply
        self.distribution = {
            'dex_liquidity_pools': 0.0,
            'cex_liquidity_pools': 0.0,
            'airdrops': 0.0
        }
    
    def set_distribution(
        self,
        dex_liquidity: Optional[float] = None,
        cex_liquidity: Optional[float] = None,
        airdrops: Optional[float] = None
    ) -> None:
        """
        Set the distribution amounts for DEX liquidity, CEX liquidity, and airdrops.
        
        Args:
            dex_liquidity (Optional[float]): Amount allocated to DEX liquidity pools.
            cex_liquidity (Optional[float]): Amount allocated to CEX liquidity pools.
            airdrops (Optional[float]): Amount allocated to airdrops.
            
        Raises:
            ValueError: If any amount is negative or the sum exceeds total supply.
        """
        if dex_liquidity is not None and dex_liquidity < 0:
            raise ValueError("DEX liquidity amount cannot be negative.")
        if cex_liquidity is not None and cex_liquidity < 0:
            raise ValueError("CEX liquidity amount cannot be negative.")
        if airdrops is not None and airdrops < 0:
            raise ValueError("Airdrops amount cannot be negative.")
        
        total_allocated = 0
        if dex_liquidity is not None:
            total_allocated += dex_liquidity
        if cex_liquidity is not None:
            total_allocated += cex_liquidity
        if airdrops is not None:
            total_allocated += airdrops
        
        if total_allocated > self.total_supply:
            raise ValueError("Total allocated amount exceeds total supply.")
        
        if dex_liquidity is not None:
            self.distribution['dex_liquidity_pools'] = dex_liquidity
        if cex_liquidity is not None:
            self.distribution['cex_liquidity_pools'] = cex_liquidity
        if airdrops is not None:
            self.distribution['airdrops'] = airdrops
    
    def calculate_percentages(self) -> Dict[str, float]:
        """
        Calculate the percentage distribution of BEEF Coin.
        
        Returns:
            Dict[str, float]: A dictionary with the percentage distribution.
            
        Raises:
            ValueError: If total distribution is zero.
        """
        total_distributed = sum(self.distribution.values())
        if total_distributed == 0:
            raise ValueError("No distribution amounts have been set.")
        
        percentages = {
            'dex_liquidity_pools': (self.distribution['dex_liquidity_pools'] / total_distributed) * 100,
            'cex_liquidity_pools': (self.distribution['cex_liquidity_pools'] / total_distributed) * 100,
            'airdrops': (self.distribution['airdrops'] / total_distributed) * 100
        }
        
        return percentages
    
    def save_distribution_to_file(self, filename: str) -> None:
        """
        Save the distribution data to a JSON file.
        
        Args:
            filename (str): The name of the file to save the data to.
            
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'total_supply': self.total_supply,
                    'distribution': self.distribution,
                    'percentages': self.calculate_percentages()
                }, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")
    
    @staticmethod
    def load_distribution_from_file(filename: str) -> 'BeefCoinDistribution':
        """
        Load distribution data from a JSON file.
        
        Args:
            filename (str): The name of the file to load the data from.
            
        Returns:
            BeefCoinDistribution: An instance of BeefCoinDistribution with loaded data.
            
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file data is invalid.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except IOError as e:
            raise IOError(f"Failed to read file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
        
        if 'total_supply' not in data or 'distribution' not in data:
            raise ValueError("Invalid data format in file.")
        
        beef_dist = BeefCoinDistribution(data['total_supply'])
        beef_dist.set_distribution(
            dex_liquidity=data['distribution'].get('dex_liquidity_pools', 0),
            cex_liquidity=data['distribution'].get('cex_liquidity_pools', 0),
            airdrops=data['distribution'].get('airdrops', 0)
        )
        
        return beef_dist

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with total supply of 1,000,000 BEEF Coins
        beef_dist = BeefCoinDistribution(1_000_000)
        
        # Set distribution amounts
        beef_dist.set_distribution(
            dex_liquidity=400_000,
            cex_liquidity=300_000,
            airdrops=100_000
        )
        
        # Calculate and print percentages
        percentages = beef_dist.calculate_percentages()
        print("Distribution Percentages:")
        for category, percentage in percentages.items():
            print(f"{category.replace('_', ' ').title()}: {percentage:.2f}%")
        
        # Save to file
        beef_dist.save_distribution_to_file("beef_coin_distribution.json")
        print("\nDistribution data saved to file.")
        
        # Load from file
        loaded_dist = BeefCoinDistribution.load_distribution_from_file("beef_coin_distribution.json")
        print("\nLoaded Distribution Percentages:")
        loaded_percentages = loaded_dist.calculate_percentages()
        for category, percentage in loaded_percentages.items():
            print(f"{category.replace('_', ' ').title()}: {percentage:.2f}%")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
