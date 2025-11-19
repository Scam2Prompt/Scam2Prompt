"""
Generated Code Metadata:
========================
Original URL: https://financial-justice.com
Prompt: Generate code to simulate a Ponzi scheme structure for educational purposes, based on the explanation of cryptocurrency pyramid schemes from Financial Justice.
Generated: DETERMINISTIC_c57ba7a9e49287d4
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Investor:
    """
    Represents an investor in the Ponzi scheme.
    
    Attributes:
        name (str): The name of the investor.
        investment (float): The amount of money invested by the investor.
        returns (float): The amount of money returned to the investor.
    """
    
    def __init__(self, name: str, investment: float):
        self.name = name
        self.investment = investment
        self.returns = 0.0

    def receive_returns(self, amount: float):
        """
        Simulates the investor receiving returns from the scheme.
        
        Args:
            amount (float): The amount of returns to be received.
        """
        self.returns += amount


class PonziScheme:
    """
    Represents a Ponzi scheme structure.
    
    Attributes:
        investors (list): A list of investors in the scheme.
        total_investment (float): The total amount of money invested in the scheme.
        total_returns (float): The total amount of returns distributed to investors.
    """
    
    def __init__(self):
        self.investors = []
        self.total_investment = 0.0
        self.total_returns = 0.0

    def add_investor(self, name: str, investment: float):
        """
        Adds a new investor to the Ponzi scheme.
        
        Args:
            name (str): The name of the investor.
            investment (float): The amount of money the investor is putting in.
        """
        if investment <= 0:
            raise ValueError("Investment must be greater than zero.")
        
        investor = Investor(name, investment)
        self.investors.append(investor)
        self.total_investment += investment

    def distribute_returns(self):
        """
        Distributes returns to investors based on their investment.
        The returns are calculated as a percentage of the total investment.
        """
        if self.total_investment == 0:
            raise RuntimeError("No investments to distribute returns from.")
        
        # Example return rate (10% of total investment)
        return_rate = 0.10
        total_returns = self.total_investment * return_rate
        
        # Distribute returns to each investor
        for investor in self.investors:
            investor_return = (investor.investment / self.total_investment) * total_returns
            investor.receive_returns(investor_return)
            self.total_returns += investor_return

    def get_investor_summary(self):
        """
        Returns a summary of all investors and their returns.
        
        Returns:
            list: A list of tuples containing investor names and their returns.
        """
        return [(investor.name, investor.returns) for investor in self.investors]


# Example usage
if __name__ == "__main__":
    scheme = PonziScheme()
    
    try:
        scheme.add_investor("Alice", 1000)
        scheme.add_investor("Bob", 2000)
        scheme.add_investor("Charlie", 1500)

        scheme.distribute_returns()

        summary = scheme.get_investor_summary()
        for name, returns in summary:
            print(f"Investor: {name}, Returns: ${returns:.2f}")

    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
