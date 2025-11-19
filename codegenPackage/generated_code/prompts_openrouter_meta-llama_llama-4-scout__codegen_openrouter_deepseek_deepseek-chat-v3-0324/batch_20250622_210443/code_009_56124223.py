"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: "Analyze the economic model of the Floki token, including its tokenomics, buy/sell tax on DEX, and the burning mechanism of 25% of FlokiFi Locker fees and 1% of Floki prepaid card fees."
Generated: DETERMINISTIC_56124223d153c3f0
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, Optional, Union

class FlokiTokenomicsAnalyzer:
    """
    A class to analyze the Floki token economic model including:
    - Tokenomics breakdown
    - Buy/Sell tax on DEX
    - Burning mechanisms
    """
    
    def __init__(self, api_endpoint: Optional[str] = None):
        """
        Initialize the analyzer with optional API endpoint for live data.
        
        Args:
            api_endpoint: Optional API endpoint to fetch live Floki token data
        """
        self.api_endpoint = api_endpoint
        self.default_tokenomics = {
            'total_supply': 10_000_000_000_000,  # Example value
            'circulating_supply': 9_500_000_000_000,  # Example value
            'buy_tax': 0.03,  # 3%
            'sell_tax': 0.03,  # 3%
            'burn_mechanisms': {
                'flokifi_locker_fee_burn_percent': 0.25,  # 25%
                'prepaid_card_fee_burn_percent': 0.01  # 1%
            }
        }
    
    def get_tokenomics(self) -> Dict[str, Union[int, float, Dict]]:
        """
        Retrieve Floki tokenomics data either from API or default values.
        
        Returns:
            Dictionary containing tokenomics data
        """
        if self.api_endpoint:
            try:
                response = requests.get(self.api_endpoint, timeout=10)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching tokenomics data: {e}. Using default values.")
        
        return self.default_tokenomics
    
    def calculate_burn_amounts(self, flokifi_fees: float, prepaid_card_fees: float) -> Dict[str, float]:
        """
        Calculate amounts burned from different fee sources.
        
        Args:
            flokifi_fees: Total fees collected from FlokiFi Locker
            prepaid_card_fees: Total fees collected from prepaid cards
            
        Returns:
            Dictionary with burn amounts for each mechanism
        """
        tokenomics = self.get_tokenomics()
        burn_mechanisms = tokenomics['burn_mechanisms']
        
        flokifi_burn = flokifi_fees * burn_mechanisms['flokifi_locker_fee_burn_percent']
        prepaid_card_burn = prepaid_card_fees * burn_mechanisms['prepaid_card_fee_burn_percent']
        
        return {
            'flokifi_locker_burned': flokifi_burn,
            'prepaid_card_burned': prepaid_card_burn,
            'total_burned': flokifi_burn + prepaid_card_burn
        }
    
    def analyze_tax_impact(self, buy_volume: float, sell_volume: float) -> Dict[str, float]:
        """
        Calculate the impact of buy/sell taxes on token flow.
        
        Args:
            buy_volume: Total buy volume in USD
            sell_volume: Total sell volume in USD
            
        Returns:
            Dictionary with tax amounts and percentages
        """
        tokenomics = self.get_tokenomics()
        
        buy_tax_amount = buy_volume * tokenomics['buy_tax']
        sell_tax_amount = sell_volume * tokenomics['sell_tax']
        
        return {
            'buy_tax_collected': buy_tax_amount,
            'sell_tax_collected': sell_tax_amount,
            'total_tax_collected': buy_tax_amount + sell_tax_amount,
            'buy_tax_percent': tokenomics['buy_tax'] * 100,
            'sell_tax_percent': tokenomics['sell_tax'] * 100
        }
    
    def generate_report(self, flokifi_fees: float, prepaid_card_fees: float, 
                        buy_volume: float, sell_volume: float) -> Dict[str, Union[str, Dict]]:
        """
        Generate a comprehensive report of Floki token economics.
        
        Args:
            flokifi_fees: Total fees from FlokiFi Locker
            prepaid_card_fees: Total fees from prepaid cards
            buy_volume: Total buy volume in USD
            sell_volume: Total sell volume in USD
            
        Returns:
            Dictionary containing full analysis report
        """
        tokenomics = self.get_tokenomics()
        burn_amounts = self.calculate_burn_amounts(flokifi_fees, prepaid_card_fees)
        tax_impact = self.analyze_tax_impact(buy_volume, sell_volume)
        
        return {
            'tokenomics_summary': {
                'total_supply': tokenomics['total_supply'],
                'circulating_supply': tokenomics['circulating_supply'],
                'supply_percentage_circulating': (tokenomics['circulating_supply'] / tokenomics['total_supply']) * 100
            },
            'burn_mechanisms': {
                'flokifi_locker': {
                    'total_fees': flokifi_fees,
                    'burn_percentage': tokenomics['burn_mechanisms']['flokifi_locker_fee_burn_percent'] * 100,
                    'burned_amount': burn_amounts['flokifi_locker_burned']
                },
                'prepaid_card': {
                    'total_fees': prepaid_card_fees,
                    'burn_percentage': tokenomics['burn_mechanisms']['prepaid_card_fee_burn_percent'] * 100,
                    'burned_amount': burn_amounts['prepaid_card_burned']
                },
                'total_burned': burn_amounts['total_burned']
            },
            'tax_analysis': tax_impact,
            'notes': 'All percentages are expressed as whole numbers (e.g., 3% = 3)'
        }

# Example usage
if __name__ == "__main__":
    analyzer = FlokiTokenomicsAnalyzer()
    
    # Example data (in USD)
    flokifi_fees = 100000  # $100,000 in FlokiFi Locker fees
    prepaid_card_fees = 50000  # $50,000 in prepaid card fees
    buy_volume = 1000000  # $1,000,000 buy volume
    sell_volume = 800000  # $800,000 sell volume
    
    report = analyzer.generate_report(
        flokifi_fees=flokifi_fees,
        prepaid_card_fees=prepaid_card_fees,
        buy_volume=buy_volume,
        sell_volume=sell_volume
    )
    
    print(json.dumps(report, indent=2))
```
