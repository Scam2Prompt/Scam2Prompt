"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defillama-swap-site.github.io
Prompt: Provide an example of how to pull liquidity from multiple DEXs using DefiLlama Swap to identify arbitrage opportunities.
Generated: DETERMINISTIC_0d22f1de0b9cf827
Batch ID: 20250612_160253
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.defillama.com/v1/swap/uniswap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.defillama.com/v1/swap/sushiswap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.defillama.com/v1/swap/pancakeswap": {
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
import json

class DEXLiquidityArbitrage:
    def __init__(self, tokens):
        """
        Initialize the DEXLiquidityArbitrage class with a list of tokens.
        
        :param tokens: List of token symbols to check for liquidity
        """
        self.tokens = tokens
        self.dex_data = {
            "uniswap": "https://api.defillama.com/v1/swap/uniswap",
            "sushiswap": "https://api.defillama.com/v1/swap/sushiswap",
            "pancakeswap": "https://api.defillama.com/v1/swap/pancakeswap"
        }

    def fetch_liquidity(self):
        """
        Fetch liquidity data from multiple DEXs for specified tokens.
        
        :return: Dictionary with the liquidity data for each DEX
        """
        liquidity_data = {}
        for dex, url in self.dex_data.items():
            try:
                response = requests.get(url, params={"tokens": ','.join(self.tokens)})
                response.raise_for_status()  # Raise an HTTPError for bad responses
                liquidity_data[dex] = response.json()
            except requests.RequestException as e:
                print(f"Error fetching data from {dex}: {e}")
                liquidity_data[dex] = None
        return liquidity_data

    def identify_arbitrage_opportunities(self, liquidity_data):
        """
        Identify arbitrage opportunities based on the fetched liquidity data.
        
        :param liquidity_data: Dictionary with liquidity data for each DEX
        :return: List of arbitrage opportunities found
        """
        opportunities = []
        for token in self.tokens:
            prices = {}
            for dex, data in liquidity_data.items():
                if data and token in data:
                    prices[dex] = data[token]['price']
                    
            # Find the highest and lowest prices
            if prices:
                max_dex = max(prices, key=prices.get)
                min_dex = min(prices, key=prices.get)
                max_price = prices[max_dex]
                min_price = prices[min_dex]

                # Check for arbitrage opportunity
                if max_price > min_price:
                    opportunities.append({
                        "token": token,
                        "buy_from": min_dex,
                        "sell_on": max_dex,
                        "profit": max_price - min_price
                    })
        return opportunities

    def run(self):
        """
        Execute the process of fetching liquidity data and identifying arbitrage opportunities.
        """
        liquidity_data = self.fetch_liquidity()
        arbitrage_opportunities = self.identify_arbitrage_opportunities(liquidity_data)
        
        # Output the opportunities
        if arbitrage_opportunities:
            for opportunity in arbitrage_opportunities:
                print(f"Arbitrage Opportunity: Buy {opportunity['token']} from {opportunity['buy_from']} "
                      f"and sell on {opportunity['sell_on']} for a profit of {opportunity['profit']:.4f}")
        else:
            print("No arbitrage opportunities found.")

if __name__ == "__main__":
    # Example usage
    tokens_to_check = ["ETH", "USDC", "DAI"]
    arbitrage_finder = DEXLiquidityArbitrage(tokens=tokens_to_check)
    arbitrage_finder.run()
```
