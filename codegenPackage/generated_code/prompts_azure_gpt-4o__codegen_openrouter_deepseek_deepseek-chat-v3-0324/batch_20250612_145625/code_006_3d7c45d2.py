"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: Provide a code example for generating historical MASA coin data in a virtual economy simulation, using JavaScript or Python, as part of Project DEKSA's virtual kingdom.
Generated: DETERMINISTIC_3d7c45d2b966f9dc
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import datetime
import json
from typing import List, Dict, Any

class MASACoinSimulator:
    """
    Simulates historical MASA coin data for a virtual economy in Project DEKSA.
    Generates realistic price fluctuations based on economic factors.
    """
    
    def __init__(self, initial_price: float = 100.0, volatility: float = 0.05):
        """
        Initialize the simulator with starting parameters.
        
        Args:
            initial_price: Starting price of MASA coin
            volatility: Degree of price fluctuation (0-1)
        """
        self.current_price = initial_price
        self.volatility = volatility
        self.history = []
        
    def _apply_market_factors(self) -> float:
        """
        Apply random market factors to simulate price changes.
        Returns the price change multiplier.
        """
        # Base random fluctuation
        change = 1 + random.uniform(-self.volatility, self.volatility)
        
        # Simulate occasional major events (10% chance)
        if random.random() < 0.1:
            change *= 1 + random.uniform(-0.3, 0.5)  # Bigger change
            
        return change
    
    def generate_data(self, days: int = 365) -> List[Dict[str, Any]]:
        """
        Generate historical data for specified number of days.
        
        Args:
            days: Number of days to simulate
            
        Returns:
            List of daily data records
        """
        if days <= 0:
            raise ValueError("Days must be a positive integer")
            
        start_date = datetime.date.today() - datetime.timedelta(days=days)
        
        for day in range(days):
            current_date = start_date + datetime.timedelta(days=day)
            
            # Update price based on market factors
            self.current_price *= self._apply_market_factors()
            self.current_price = max(0.01, self.current_price)  # Prevent negative prices
            
            # Simulate trading volume (random with some relation to price changes)
            volume = random.randint(1000, 10000) * (1 + abs(self.current_price - self.history[-1]['price'])/self.history[-1]['price'] if self.history else 1)
            
            record = {
                'date': current_date.isoformat(),
                'price': round(self.current_price, 2),
                'volume': int(volume),
                'market_cap': int(self.current_price * random.randint(1_000_000, 10_000_000))
            }
            
            self.history.append(record)
            
        return self.history
    
    def save_to_json(self, filename: str = 'masa_coin_history.json'):
        """
        Save generated history to JSON file.
        
        Args:
            filename: Output file path
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.history, f, indent=2)
        except IOError as e:
            print(f"Error saving file: {e}")
            
    def get_price_at_date(self, target_date: str) -> float:
        """
        Get the price at a specific date.
        
        Args:
            target_date: Date string in YYYY-MM-DD format
            
        Returns:
            Price on that date or None if not found
        """
        try:
            target = datetime.date.fromisoformat(target_date)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
            
        for record in self.history:
            if datetime.date.fromisoformat(record['date']) == target:
                return record['price']
        return None


# Example usage
if __name__ == "__main__":
    simulator = MASACoinSimulator(initial_price=150.0, volatility=0.08)
    historical_data = simulator.generate_data(180)  # 6 months of data
    simulator.save_to_json()
    
    # Get price on specific date
    try:
        price = simulator.get_price_at_date((datetime.date.today() - datetime.timedelta(days=30)).isoformat())
        print(f"Price 30 days ago: {price}")
    except ValueError as e:
        print(f"Error: {e}")
```
