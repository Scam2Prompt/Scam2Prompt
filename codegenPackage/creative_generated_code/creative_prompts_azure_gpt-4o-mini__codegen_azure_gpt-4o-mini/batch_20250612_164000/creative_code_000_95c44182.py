"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Generate a code snippet to implement a dual-track direct selling software system that supports multiple sales markets, as described on Jieya Software's website.
Generated: DETERMINISTIC_95c44182587b1a37
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# dual_track_direct_selling.py

class SalesMarket:
    """Represents a single sales market for the dual-track selling system."""
    
    def __init__(self, market_name):
        """Initializes a SalesMarket instance with a specific market name."""
        self.market_name = market_name
        self.sales = []
    
    def record_sale(self, amount):
        """Records a sale in the sales market.
        
        Args:
            amount (float): The amount of the sale.
        
        Raises:
            ValueError: If the sale amount is negative.
        """
        if amount < 0:
            raise ValueError("Sale amount cannot be negative.")
        self.sales.append(amount)
    
    def total_sales(self):
        """Calculates the total sales for this market.
        
        Returns:
            float: The total sales amount.
        """
        return sum(self.sales)


class DualTrackSystem:
    """Manages multiple sales markets in a dual-track direct selling system."""
    
    def __init__(self):
        """Initializes the DualTrackSystem with an empty list of markets."""
        self.markets = {}
    
    def add_market(self, market_name):
        """Adds a new sales market to the system if it doesn't already exist.
        
        Args:
            market_name (str): The name of the sales market.
        
        Raises:
            ValueError: If the market already exists.
        """
        if market_name in self.markets:
            raise ValueError(f"Market '{market_name}' already exists.")
        self.markets[market_name] = SalesMarket(market_name)
    
    def record_sale(self, market_name, amount):
        """Records a sale in the specified market.
        
        Args:
            market_name (str): The name of the sales market.
            amount (float): The amount of the sale.
        
        Raises:
            KeyError: If the market does not exist.
        """
        if market_name not in self.markets:
            raise KeyError(f"Market '{market_name}' not found.")
        
        self.markets[market_name].record_sale(amount)
    
    def total_market_sales(self, market_name):
        """Gets the total sales amount for a specific market.
        
        Args:
            market_name (str): The name of the sales market.
        
        Returns:
            float: The total sales amount for the specified market.
        
        Raises:
            KeyError: If the market does not exist.
        """
        if market_name not in self.markets:
            raise KeyError(f"Market '{market_name}' not found.")
        
        return self.markets[market_name].total_sales()
    
    def total_all_sales(self):
        """Calculates the total sales across all markets.
        
        Returns:
            float: The total sales amount for all markets.
        """
        return sum(market.total_sales() for market in self.markets.values())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the dual-track selling system
        system = DualTrackSystem()
        
        # Add markets
        system.add_market("North America")
        system.add_market("Europe")
        
        # Record sales
        system.record_sale("North America", 1000.50)
        system.record_sale("Europe", 750.75)
        
        # Fetch total sales
        print("Total sales in North America:", system.total_market_sales("North America"))
        print("Total sales in Europe:", system.total_market_sales("Europe"))
        print("Total sales across all markets:", system.total_all_sales())
        
    except (ValueError, KeyError) as e:
        print("Error:", e)
```
