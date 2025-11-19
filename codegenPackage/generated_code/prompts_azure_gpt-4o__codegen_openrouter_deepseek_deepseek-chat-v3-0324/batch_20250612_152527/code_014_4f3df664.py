"""
Generated Code Metadata:
========================
Original URL: https://gigachadgpt-en.web.app
Prompt: Write a Python script to simulate the tokenomics distribution of $GIGA, including presale allocation, treasury, liquidity, and team tokens.
Generated: DETERMINISTIC_4f3df6646e55d3c0
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt

class TokenomicsSimulator:
    """
    Simulates the tokenomics distribution of $GIGA token.
    Handles allocations for presale, treasury, liquidity, team, and other categories.
    """
    
    def __init__(self, total_supply):
        """
        Initialize the simulator with total token supply.
        
        Args:
            total_supply (int): Total supply of $GIGA tokens
        """
        self.total_supply = total_supply
        self.allocations = {}
        
    def add_allocation(self, name, percentage, vesting_period=None):
        """
        Add a token allocation category.
        
        Args:
            name (str): Name of allocation category
            percentage (float): Percentage of total supply (0-100)
            vesting_period (int, optional): Vesting period in months. Defaults to None.
        """
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        if sum(self.allocations.values()) + percentage > 100:
            raise ValueError("Total allocations exceed 100%")
            
        self.allocations[name] = {
            'percentage': percentage,
            'tokens': self.total_supply * percentage / 100,
            'vesting_period': vesting_period
        }
    
    def validate_allocations(self):
        """Check if allocations sum to 100%."""
        total = sum(alloc['percentage'] for alloc in self.allocations.values())
        if total != 100:
            raise ValueError(f"Allocations sum to {total}%, must be exactly 100%")
    
    def generate_distribution_report(self):
        """Generate a text report of token distribution."""
        self.validate_allocations()
        
        report = []
        report.append(f"Token Distribution Report for {self.total_supply:,} $GIGA")
        report.append("=" * 50)
        
        for name, data in self.allocations.items():
            vesting_info = f", {data['vesting_period']}mo vesting" if data['vesting_period'] else ""
            report.append(
                f"{name}: {data['percentage']}% ({data['tokens']:,.0f} tokens{vesting_info})"
            )
        
        report.append("=" * 50)
        return "\n".join(report)
    
    def plot_distribution(self, filename=None):
        """Generate a pie chart of token distribution."""
        self.validate_allocations()
        
        labels = []
        sizes = []
        
        for name, data in self.allocations.items():
            labels.append(f"{name}\n{data['percentage']}%")
            sizes.append(data['percentage'])
        
        fig, ax = plt.subplots()
        ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 8}
        )
        ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
        plt.title(f"$GIGA Token Distribution (Total Supply: {self.total_supply:,})")
        
        if filename:
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            plt.close()
        else:
            plt.show()

def main():
    """Main execution function."""
    try:
        # Configuration
        TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
        
        # Initialize simulator
        simulator = TokenomicsSimulator(TOTAL_SUPPLY)
        
        # Add allocations (percentages must sum to 100)
        simulator.add_allocation("Presale", 20)
        simulator.add_allocation("Treasury", 25, vesting_period=12)
        simulator.add_allocation("Liquidity", 15)
        simulator.add_allocation("Team", 10, vesting_period=24)
        simulator.add_allocation("Staking Rewards", 15)
        simulator.add_allocation("Marketing", 10)
        simulator.add_allocation("Advisors", 5, vesting_period=12)
        
        # Generate and print report
        report = simulator.generate_distribution_report()
        print(report)
        
        # Generate distribution chart
        simulator.plot_distribution("giga_token_distribution.png")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
