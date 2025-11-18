"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://woobridge.net
Prompt: Provide code to calculate and display swap fees for a cross-chain transaction on the WOOFi decentralized exchange, referencing the ETH/USDC trading pair.
Generated: DETERMINISTIC_8d4f02a010b8cb83
Batch ID: 20250612_153925
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.woo.org/v1": {
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

class WOOFiSwapFeeCalculator:
    """
    A class to calculate swap fees for cross-chain transactions on the WOOFi decentralized exchange.
    """

    BASE_URL = "https://api.woo.org/v1"  # Base URL for WOOFi API

    def __init__(self, trading_pair):
        """
        Initializes the calculator with the trading pair.
        
        Parameters:
            trading_pair (str): The trading pair for which to calculate swap fees (e.g., 'ETH/USDC').
        """
        self.trading_pair = trading_pair

    def get_swap_fee(self):
        """
        Fetches the swap fee for the given trading pair from the WOOFi API.

        Returns:
            float: The swap fee percentage.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/swap-fees/{self.trading_pair}")
            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Check if the expected data is in the response
            if 'fee' in data:
                return data['fee']
            else:
                raise ValueError("Unexpected response format; 'fee' not found.")
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching swap fee: {e}")
            return None
        except ValueError as e:
            print(e)
            return None

    def display_swap_fee(self):
        """
        Displays the swap fee for the trading pair.
        """
        fee = self.get_swap_fee()
        if fee is not None:
            print(f"Swap fee for trading pair {self.trading_pair}: {fee:.2f}%")
        else:
            print("Unable to retrieve swap fee.")

if __name__ == "__main__":
    # Define the trading pair for which to calculate the swap fee
    trading_pair = "ETH/USDC"
    
    # Create an instance of the WOOFiSwapFeeCalculator
    fee_calculator = WOOFiSwapFeeCalculator(trading_pair)
    
    # Display the swap fee
    fee_calculator.display_swap_fee()
```
