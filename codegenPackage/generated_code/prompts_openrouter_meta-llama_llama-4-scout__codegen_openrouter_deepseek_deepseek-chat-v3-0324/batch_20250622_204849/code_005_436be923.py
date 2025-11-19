"""
Generated Code Metadata:
========================
Original URL: https://memekombat-api.pages.dev
Prompt: Create a tokenomics analysis tool for Meme Kombat, focusing on the 50% presale, 30% staking and battle rewards, 10% DEX, and 10% community rewards allocations.
Generated: DETERMINISTIC_436be9232227cdc2
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

class TokenomicsAnalyzer:
    """
    A tool to analyze and visualize tokenomics distribution for Meme Kombat.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the TokenomicsAnalyzer with total token supply.
        
        Args:
            total_supply (int): Total supply of tokens
        """
        self.total_supply = total_supply
        self.allocations = {
            'Presale': 0.5,
            'Staking & Battle Rewards': 0.3,
            'DEX Liquidity': 0.1,
            'Community Rewards': 0.1
        }
        
    def validate_allocations(self) -> bool:
        """
        Validate that allocations sum to 100%.
        
        Returns:
            bool: True if allocations are valid, False otherwise
        """
        total = sum(self.allocations.values())
        return abs(total - 1.0) < 0.0001  # Account for floating point precision
    
    def calculate_token_distribution(self) -> Dict[str, int]:
        """
        Calculate token distribution based on allocation percentages.
        
        Returns:
            Dict[str, int]: Dictionary mapping allocation names to token amounts
            
        Raises:
            ValueError: If allocations don't sum to 100%
        """
        if not self.validate_allocations():
            raise ValueError("Allocations must sum to 100%")
            
        return {
            category: int(percentage * self.total_supply)
            for category, percentage in self.allocations.items()
        }
    
    def generate_distribution_report(self) -> pd.DataFrame:
        """
        Generate a pandas DataFrame with token distribution details.
        
        Returns:
            pd.DataFrame: DataFrame containing allocation details
        """
        distribution = self.calculate_token_distribution()
        data = []
        
        for category, tokens in distribution.items():
            percentage = self.allocations[category] * 100
            data.append({
                'Category': category,
                'Tokens': tokens,
                'Percentage': percentage,
                'Percentage of Total': f"{percentage:.1f}%"
            })
            
        return pd.DataFrame(data)
    
    def plot_distribution_pie(self, save_path: str = None) -> None:
        """
        Create a pie chart visualization of token distribution.
        
        Args:
            save_path (str, optional): Path to save the plot. If None, displays plot.
        """
        distribution = self.calculate_token_distribution()
        labels = list(distribution.keys())
        sizes = list(distribution.values())
        
        plt.figure(figsize=(10, 7))
        plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=140,
            colors=['#ff9999','#66b3ff','#99ff99','#ffcc99']
        )
        plt.axis('equal')
        plt.title('Meme Kombat Token Distribution')
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
    
    def plot_distribution_bar(self, save_path: str = None) -> None:
        """
        Create a bar chart visualization of token distribution.
        
        Args:
            save_path (str, optional): Path to save the plot. If None, displays plot.
        """
        distribution = self.calculate_token_distribution()
        categories = list(distribution.keys())
        tokens = list(distribution.values())
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(categories, tokens, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
        
        plt.title('Meme Kombat Token Distribution')
        plt.ylabel('Number of Tokens')
        plt.xticks(rotation=45)
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width()/2.,
                height,
                f'{height:,}',
                ha='center',
                va='bottom'
            )
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    try:
        TOTAL_SUPPLY = 100000000  # Example total supply
        
        analyzer = TokenomicsAnalyzer(TOTAL_SUPPLY)
        
        # Generate and print distribution report
        report = analyzer.generate_distribution_report()
        print("\nToken Distribution Report:")
        print(report.to_string(index=False))
        
        # Generate visualizations
        analyzer.plot_distribution_pie()
        analyzer.plot_distribution_bar()
        
    except Exception as e:
        print(f"Error analyzing tokenomics: {str(e)}")
```
