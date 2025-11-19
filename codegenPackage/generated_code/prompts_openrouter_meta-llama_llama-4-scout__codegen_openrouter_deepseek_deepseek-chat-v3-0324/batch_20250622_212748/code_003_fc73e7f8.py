"""
Generated Code Metadata:
========================
Original URL: https://aasterdex.com
Prompt: Design a simple trading strategy using Aster DEX's Simple Mode and write a code snippet to automate it, leveraging the platform's aggregated liquidity and low fees.
Generated: DETERMINISTIC_fc73e7f87535d433
Batch ID: 20250622_212748
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.asterdex.com": {
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
import requests
import time
from typing import Dict, Optional

class AsterDEXSimpleModeTrader:
    """
    A simple trading bot for Aster DEX's Simple Mode.
    Implements a basic mean-reversion strategy using aggregated liquidity.
    """
    
    def __init__(self, api_key: str, api_secret: str, base_url: str = "https://api.asterdex.com"):
        """
        Initialize the trader with API credentials.
        
        Args:
            api_key: Your Aster DEX API key
            api_secret: Your Aster DEX API secret
            base_url: Base URL for the Aster DEX API
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-KEY": self.api_key,
            "X-API-SECRET": self.api_secret
        })
        
    def get_market_data(self, pair: str) -> Optional[Dict]:
        """
        Fetch current market data for a trading pair.
        
        Args:
            pair: Trading pair (e.g., "ETH_USDT")
            
        Returns:
            Dictionary containing market data or None if request fails
        """
        endpoint = f"{self.base_url}/api/v1/simple/market"
        try:
            response = self.session.get(endpoint, params={"pair": pair})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market data: {e}")
            return None
    
    def place_order(self, pair: str, side: str, amount: float) -> Optional[Dict]:
        """
        Place an order on Aster DEX Simple Mode.
        
        Args:
            pair: Trading pair (e.g., "ETH_USDT")
            side: "buy" or "sell"
            amount: Amount to trade
            
        Returns:
            Order response dictionary or None if request fails
        """
        endpoint = f"{self.base_url}/api/v1/simple/order"
        try:
            response = self.session.post(endpoint, json={
                "pair": pair,
                "side": side,
                "amount": str(amount)
            })
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error placing order: {e}")
            return None
    
    def calculate_mean_reversion_signal(self, pair: str, window_size: int = 5) -> Optional[str]:
        """
        Calculate mean reversion trading signal.
        
        Args:
            pair: Trading pair to analyze
            window_size: Number of periods to consider for mean calculation
            
        Returns:
            "buy", "sell", or None if no clear signal
        """
        # In production, you would implement proper historical data collection
        # Here we simulate with recent price samples
        recent_prices = [self.get_market_data(pair)["last_price"] for _ in range(window_size)]
        if not recent_prices:
            return None
            
        current_price = recent_prices[-1]
        mean_price = sum(recent_prices) / len(recent_prices)
        
        # Simple mean reversion thresholds
        if current_price < mean_price * 0.98:
            return "buy"
        elif current_price > mean_price * 1.02:
            return "sell"
        return None
    
    def run_strategy(self, pair: str, trade_amount: float, interval: int = 60):
        """
        Run the trading strategy in a loop.
        
        Args:
            pair: Trading pair to trade
            trade_amount: Amount to trade per signal
            interval: Seconds between strategy checks
        """
        print(f"Starting mean reversion strategy for {pair}")
        
        while True:
            try:
                signal = self.calculate_mean_reversion_signal(pair)
                if signal:
                    print(f"Signal detected: {signal.upper()} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
                    order_result = self.place_order(pair, signal, trade_amount)
                    if order_result:
                        print(f"Order executed: {order_result}")
                    else:
                        print("Order failed")
                else:
                    print(f"No signal - waiting {interval} seconds")
                
                time.sleep(interval)
            except Exception as e:
                print(f"Error in strategy loop: {e}")
                time.sleep(interval * 2)  # Back off on errors
```
