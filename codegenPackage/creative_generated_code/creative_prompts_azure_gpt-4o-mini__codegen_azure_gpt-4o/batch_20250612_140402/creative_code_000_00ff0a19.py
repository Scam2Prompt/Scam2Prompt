"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degenz.co
Prompt: Generate a Python script that retrieves and analyzes NFT portfolio data from Degenz.Finance, focusing on multi-chain support for EVM, BTC, and SOL wallets.
Generated: DETERMINISTIC_00ff0a19faa21866
Batch ID: 20250612_140402
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.degenz.finance/v1": {
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

class NFTPortfolioAnalyzer:
    """
    A class to retrieve and analyze NFT portfolio data from Degenz.Finance.
    Supports multi-chain wallets for EVM, BTC, and SOL.
    """

    def __init__(self):
        # Base API endpoint for Degenz.Finance
        self.base_url = "https://api.degenz.finance/v1"
        # Supported chains
        self.supported_chains = ["EVM", "BTC", "SOL"]

    def get_portfolio_data(self, chain, wallet_address):
        """
        Retrieve NFT portfolio data for a given chain and wallet address.

        Args:
            chain (str): The blockchain type ("EVM", "BTC", "SOL").
            wallet_address (str): The wallet address to analyze.

        Returns:
            dict: Parsed JSON response containing portfolio data.
        """
        if chain not in self.supported_chains:
            raise ValueError(f"Unsupported chain: {chain}. Supported chains are {self.supported_chains}.")

        try:
            # Construct the API endpoint URL
            url = f"{self.base_url}/nft/{chain}/{wallet_address}"
            # Make a GET request to the API
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad status codes
            
            # Parse JSON response
            portfolio_data = response.json()
            return portfolio_data
        except requests.exceptions.RequestException as e:
            # Handle connectivity or request-related errors
            print(f"Error retrieving portfolio data: {e}")
            return None
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            print(f"Error decoding JSON response: {e}")
            return None

    def analyze_portfolio(self, portfolio_data):
        """
        Analyze retrieved NFT portfolio data.

        Args:
            portfolio_data (dict): The portfolio data retrieved from the API.

        Returns:
            dict: An analysis dictionary summarizing portfolio data.
        """
        if not portfolio_data:
            return {"error": "No valid portfolio data provided for analysis."}

        try:
            # Extract key metrics (example: total assets, total value)
            total_assets = len(portfolio_data.get("assets", []))
            total_value = sum(asset.get("value", 0) for asset in portfolio_data.get("assets", []))
            
            # Create a summary analysis
            analysis = {
                "total_assets": total_assets,
                "total_value": total_value,
                "average_value_per_asset": total_value / total_assets if total_assets > 0 else 0
            }
            return analysis
        except Exception as e:
            # Handle unexpected errors in analysis
            print(f"Error analyzing portfolio data: {e}")
            return {"error": "An error occurred during portfolio analysis."}

def main():
    """
    Main function to execute NFT portfolio retrieval and analysis.
    """
    # Example user input
    chain = "EVM"  # Supported values: "EVM", "BTC", "SOL"
    wallet_address = "0x123456789abcdef"  # Replace with a real wallet address

    # Initialize the NFTPortfolioAnalyzer
    analyzer = NFTPortfolioAnalyzer()

    # Retrieve portfolio data
    portfolio_data = analyzer.get_portfolio_data(chain, wallet_address)
    if not portfolio_data:
        print("Failed to retrieve portfolio data.")
        return

    # Analyze portfolio data
    analysis = analyzer.analyze_portfolio(portfolio_data)
    print("Portfolio Analysis:", analysis)

if __name__ == "__main__":
    main()
```
