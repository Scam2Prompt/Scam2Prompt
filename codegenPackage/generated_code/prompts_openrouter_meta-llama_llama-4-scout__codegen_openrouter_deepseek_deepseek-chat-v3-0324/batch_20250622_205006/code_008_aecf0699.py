"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-ca.web.app
Prompt: Analyze the tokenomics of Mpeppe ($MPEPE) and provide insights on how the distribution of tokens among different stakeholders (e.g., presale, agents, treasury) may impact the project's success.
Generated: DETERMINISTIC_aecf069984f81088
Batch ID: 20250622_205006
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
import seaborn as sns
from typing import Dict, List, Tuple

class TokenomicsAnalyzer:
    """
    Analyzes token distribution and its impact on project success.
    """
    
    def __init__(self, token_name: str, total_supply: float):
        """
        Initialize analyzer with token details.
        
        Args:
            token_name: Name of the token (e.g., "MPEPE")
            total_supply: Total token supply
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.distribution = {}
        
    def add_distribution_category(self, category: str, percentage: float) -> None:
        """
        Add a token distribution category with its percentage allocation.
        
        Args:
            category: Distribution category (e.g., "Presale", "Team")
            percentage: Percentage allocation (0-100)
            
        Raises:
            ValueError: If percentage is invalid or total exceeds 100%
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        if sum(self.distribution.values()) + percentage > 100:
            raise ValueError("Total distribution cannot exceed 100%")
            
        self.distribution[category] = percentage
        
    def calculate_token_amounts(self) -> Dict[str, float]:
        """
        Calculate actual token amounts for each distribution category.
        
        Returns:
            Dictionary mapping categories to token amounts
        """
        return {k: (v/100) * self.total_supply for k, v in self.distribution.items()}
    
    def analyze_vesting(self, vesting_schedule: Dict[str, List[Tuple[int, float]]]) -> pd.DataFrame:
        """
        Analyze vesting schedules for different categories.
        
        Args:
            vesting_schedule: Dict with category as key and list of (month, percentage) tuples
            
        Returns:
            DataFrame showing monthly token releases
        """
        data = []
        for category, schedule in vesting_schedule.items():
            for month, percent in schedule:
                tokens = (percent/100) * self.distribution.get(category, 0)/100 * self.total_supply
                data.append({
                    'Category': category,
                    'Month': month,
                    'Percentage': percent,
                    'Tokens': tokens
                })
                
        df = pd.DataFrame(data)
        return df.sort_values(['Category', 'Month'])
    
    def plot_distribution(self) -> None:
        """
        Generate pie chart showing token distribution.
        """
        if not self.distribution:
            raise ValueError("No distribution data available")
            
        labels = list(self.distribution.keys())
        sizes = list(self.distribution.values())
        
        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(f'{self.token_name} Token Distribution')
        plt.axis('equal')
        plt.show()
        
    def plot_vesting(self, vesting_df: pd.DataFrame) -> None:
        """
        Generate line plot showing vesting schedules.
        
        Args:
            vesting_df: DataFrame from analyze_vesting method
        """
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            data=vesting_df,
            x='Month',
            y='Tokens',
            hue='Category',
            marker='o'
        )
        plt.title(f'{self.token_name} Vesting Schedule')
        plt.xlabel('Months')
        plt.ylabel('Tokens Released')
        plt.grid(True)
        plt.show()
        
    def assess_risk(self) -> Dict[str, str]:
        """
        Assess potential risks based on token distribution.
        
        Returns:
            Dictionary of risk assessments
        """
        risks = {}
        token_amounts = self.calculate_token_amounts()
        
        # Check for excessive team/insider allocation
        insider_categories = ['Team', 'Advisors', 'Founders']
        insider_allocation = sum(self.distribution.get(cat, 0) for cat in insider_categories)
        if insider_allocation > 20:
            risks['InsiderConcentration'] = f"High insider allocation ({insider_allocation}%) may lead to centralization risks"
            
        # Check for sufficient liquidity allocation
        if self.distribution.get('Liquidity', 0) < 15:
            risks['LiquidityRisk'] = "Low liquidity allocation may impact market stability"
            
        # Check for large presale allocations
        if self.distribution.get('Presale', 0) > 40:
            risks['PresaleRisk'] = "Large presale allocation may lead to early sell pressure"
            
        return risks

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer
        analyzer = TokenomicsAnalyzer("MPEPE", 1_000_000_000)
        
        # Add distribution categories
        analyzer.add_distribution_category("Presale", 30)
        analyzer.add_distribution_category("Team", 15)
        analyzer.add_distribution_category("Liquidity", 20)
        analyzer.add_distribution_category("Treasury", 15)
        analyzer.add_distribution_category("Ecosystem", 20)
        
        # Plot distribution
        analyzer.plot_distribution()
        
        # Define vesting schedules
        vesting = {
            "Team": [(0, 10), (6, 20), (12, 30), (24, 40)],
            "Advisors": [(0, 20), (12, 30), (24, 50)],
            "Treasury": [(0, 100)]
        }
        
        # Analyze vesting
        vesting_df = analyzer.analyze_vesting(vesting)
        analyzer.plot_vesting(vesting_df)
        
        # Assess risks
        risks = analyzer.assess_risk()
        for risk, message in risks.items():
            print(f"[{risk}]: {message}")
            
    except Exception as e:
        print(f"Error analyzing tokenomics: {str(e)}")
```
