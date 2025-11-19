"""
Generated Code Metadata:
========================
Original URL: https://immediatefrontier.app
Prompt: "Design a simple investment portfolio tracker using a programming language of your choice, inspired by the investment essentials discussed on Immediate Frontier."
Generated: DETERMINISTIC_3582f0940278afbf
Batch ID: 20250622_211310
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import requests
from requests.exceptions import RequestException

# Constants
API_BASE_URL = "https://api.coingecko.com/api/v3"
DEFAULT_CURRENCY = "usd"

@dataclass
class Asset:
    """Class representing a single asset in the portfolio."""
    symbol: str
    name: str
    amount: float
    purchase_price: float
    purchase_date: str
    
    def current_value(self, current_price: float) -> float:
        """Calculate current value of the asset."""
        return self.amount * current_price
    
    def profit_loss(self, current_price: float) -> float:
        """Calculate profit/loss for the asset."""
        return (current_price - self.purchase_price) * self.amount
    
    def profit_loss_percentage(self, current_price: float) -> float:
        """Calculate profit/loss percentage for the asset."""
        if self.purchase_price == 0:
            return 0.0
        return ((current_price - self.purchase_price) / self.purchase_price) * 100

@dataclass
class Portfolio:
    """Class representing an investment portfolio."""
    name: str
    assets: List[Asset] = field(default_factory=list)
    currency: str = DEFAULT_CURRENCY
    
    def add_asset(self, asset: Asset) -> None:
        """Add an asset to the portfolio."""
        self.assets.append(asset)
    
    def remove_asset(self, symbol: str) -> bool:
        """Remove an asset from the portfolio by symbol."""
        for i, asset in enumerate(self.assets):
            if asset.symbol.lower() == symbol.lower():
                self.assets.pop(i)
                return True
        return False
    
    def get_asset_prices(self) -> Dict[str, float]:
        """Fetch current prices for all assets in the portfolio."""
        symbols = [asset.symbol for asset in self.assets]
        if not symbols:
            return {}
        
        try:
            response = requests.get(
                f"{API_BASE_URL}/simple/price",
                params={
                    "ids": ",".join(symbols),
                    "vs_currencies": self.currency
                }
            )
            response.raise_for_status()
            data = response.json()
            return {symbol: data[symbol][self.currency] for symbol in data}
        except RequestException as e:
            print(f"Error fetching prices: {e}")
            return {}
    
    def total_value(self) -> float:
        """Calculate total current value of the portfolio."""
        prices = self.get_asset_prices()
        return sum(
            asset.current_value(prices.get(asset.symbol, 0))
            for asset in self.assets
        )
    
    def total_investment(self) -> float:
        """Calculate total initial investment in the portfolio."""
        return sum(asset.amount * asset.purchase_price for asset in self.assets)
    
    def total_profit_loss(self) -> float:
        """Calculate total profit/loss for the portfolio."""
        prices = self.get_asset_prices()
        return sum(
            asset.profit_loss(prices.get(asset.symbol, 0))
            for asset in self.assets
        )
    
    def total_profit_loss_percentage(self) -> float:
        """Calculate total profit/loss percentage for the portfolio."""
        total_investment = self.total_investment()
        if total_investment == 0:
            return 0.0
        return (self.total_profit_loss() / total_investment) * 100
    
    def generate_report(self) -> str:
        """Generate a detailed portfolio report."""
        prices = self.get_asset_prices()
        report = []
        report.append(f"Portfolio: {self.name}")
        report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Currency: {self.currency.upper()}")
        report.append("\nAssets:")
        
        for asset in self.assets:
            current_price = prices.get(asset.symbol, 0)
            report.append(
                f"{asset.name} ({asset.symbol.upper()}): "
                f"Amount: {asset.amount:.4f}, "
                f"Current Price: {current_price:.2f} {self.currency.upper()}, "
                f"Value: {asset.current_value(current_price):.2f} {self.currency.upper()}, "
                f"P/L: {asset.profit_loss(current_price):.2f} {self.currency.upper()} "
                f"({asset.profit_loss_percentage(current_price):.2f}%)"
            )
        
        report.append("\nSummary:")
        report.append(f"Total Investment: {self.total_investment():.2f} {self.currency.upper()}")
        report.append(f"Total Value: {self.total_value():.2f} {self.currency.upper()}")
        report.append(f"Total P/L: {self.total_profit_loss():.2f} {self.currency.upper()} "
                     f"({self.total_profit_loss_percentage():.2f}%)")
        
        return "\n".join(report)
    
    def save_to_file(self, filename: str) -> bool:
        """Save portfolio to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "name": self.name,
                    "currency": self.currency,
                    "assets": [
                        {
                            "symbol": asset.symbol,
                            "name": asset.name,
                            "amount": asset.amount,
                            "purchase_price": asset.purchase_price,
                            "purchase_date": asset.purchase_date
                        }
                        for asset in self.assets
                    ]
                }, f, indent=2)
            return True
        except IOError as e:
            print(f"Error saving portfolio: {e}")
            return False
    
    @classmethod
    def load_from_file(cls, filename: str) -> Optional['Portfolio']:
        """Load portfolio from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                portfolio = cls(data["name"], currency=data.get("currency", DEFAULT_CURRENCY))
                for asset_data in data["assets"]:
                    portfolio.add_asset(Asset(
                        symbol=asset_data["symbol"],
                        name=asset_data["name"],
                        amount=asset_data["amount"],
                        purchase_price=asset_data["purchase_price"],
                        purchase_date=asset_data["purchase_date"]
                    ))
                return portfolio
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading portfolio: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create a new portfolio
    my_portfolio = Portfolio("My Crypto Portfolio")
    
    # Add some assets
    my_portfolio.add_asset(Asset(
        symbol="bitcoin",
        name="Bitcoin",
        amount=0.5,
        purchase_price=40000.00,
        purchase_date="2023-01-15"
    ))
    
    my_portfolio.add_asset(Asset(
        symbol="ethereum",
        name="Ethereum",
        amount=5.0,
        purchase_price=2500.00,
        purchase_date="2023-02-20"
    ))
    
    # Generate and print report
    print(my_portfolio.generate_report())
    
    # Save portfolio to file
    my_portfolio.save_to_file("my_portfolio.json")
    
    # Load portfolio from file
    loaded_portfolio = Portfolio.load_from_file("my_portfolio.json")
    if loaded_portfolio:
        print("\nLoaded Portfolio Report:")
        print(loaded_portfolio.generate_report())
```
