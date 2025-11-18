"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flash-stake.pages.dev
Prompt: Generate code to simulate a "max-yield degen strategy" using Flashstake and YamaFinance APIs, including leveraging upfront yield to buy more GLP tokens.
Generated: DETERMINISTIC_c532e32daa07eb81
Batch ID: 20250612_152441
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.yam.finance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.flashstake.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import time

class FlashstakeAPI:
    BASE_URL = "https://api.flashstake.com"

    @staticmethod
    def get_yield(token: str) -> float:
        """Fetch the yield for a given token."""
        try:
            response = requests.get(f"{FlashstakeAPI.BASE_URL}/yield/{token}")
            response.raise_for_status()
            return response.json()['yield']
        except requests.RequestException as e:
            print(f"Error fetching yield data: {e}")
            return 0.0

class YamaFinanceAPI:
    BASE_URL = "https://api.yam.finance"

    @staticmethod
    def buy_glp(amount: float) -> bool:
        """Purchase GLP tokens with the given amount."""
        try:
            response = requests.post(f"{YamaFinanceAPI.BASE_URL}/buy_glp", json={"amount": amount})
            response.raise_for_status()
            return response.json().get('success', False)
        except requests.RequestException as e:
            print(f"Error buying GLP: {e}")
            return False

class MaxYieldDegenStrategy:
    def __init__(self, initial_investment: float, token: str):
        """Initialize the strategy with an investment amount and token."""
        self.investment = initial_investment
        self.token = token

    def execute_strategy(self):
        """Execute the max-yield degen strategy."""
        while True:
            # Fetch the current yield
            yield_amount = FlashstakeAPI.get_yield(self.token)
            if yield_amount <= 0:
                print("Yield is 0 or less, exiting the strategy.")
                break
            
            # Calculate amount to reinvest
            yield_to_reinvest = self.investment * yield_amount
            print(f"Yield to reinvest: {yield_to_reinvest}")

            # Buy GLP tokens with the yield
            if YamaFinanceAPI.buy_glp(yield_to_reinvest):
                print(f"Successfully bought GLP tokens worth: {yield_to_reinvest}")
                # Increase investment by re-investing the yield
                self.investment += yield_to_reinvest
            else:
                print("Failed to buy GLP tokens, exiting the strategy.")
                break
            
            # Sleep for a specified time before the next iteration
            time.sleep(60)  # Sleep for 1 minute

# Example usage
if __name__ == "__main__":
    # Set your initial investment and token you wish to track
    initial_investment = 1000.0  # Example investment in USD or token
    token = "ETH"  # Example token

    strategy = MaxYieldDegenStrategy(initial_investment, token)
    strategy.execute_strategy()
```
