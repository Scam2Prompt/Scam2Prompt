"""
Generated Code Metadata:
========================
Original URL: https://btfd-bonus.ink
Prompt: Compare the tokenomics of BTFD with another meme coin, focusing on liquidity allocation, vesting periods, and community incentives.
Generated: DETERMINISTIC_76226af33552e38c
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class TokenomicsAnalyzer:
    """
    A class to analyze and compare tokenomics of two meme coins.
    Focuses on liquidity allocation, vesting periods, and community incentives.
    """
    
    def __init__(self, coin1_data: Dict[str, Any], coin2_data: Dict[str, Any]):
        """
        Initialize the analyzer with tokenomics data for two coins.
        
        Args:
            coin1_data: Dictionary containing tokenomics data for first coin
            coin2_data: Dictionary containing tokenomics data for second coin
        """
        self.coin1 = coin1_data
        self.coin2 = coin2_data
        
    def compare_liquidity_allocation(self) -> Dict[str, Dict[str, float]]:
        """
        Compare liquidity allocation percentages between the two coins.
        
        Returns:
            Dictionary with comparison results for each coin's liquidity allocation
        """
        comparison = {
            'coin1': {
                'initial_liquidity': self.coin1.get('liquidity_allocation', {}).get('initial', 0),
                'locked_liquidity': self.coin1.get('liquidity_allocation', {}).get('locked', 0),
                'percentage': self._calculate_liquidity_percentage(self.coin1)
            },
            'coin2': {
                'initial_liquidity': self.coin2.get('liquidity_allocation', {}).get('initial', 0),
                'locked_liquidity': self.coin2.get('liquidity_allocation', {}).get('locked', 0),
                'percentage': self._calculate_liquidity_percentage(self.coin2)
            }
        }
        return comparison
    
    def _calculate_liquidity_percentage(self, coin_data: Dict[str, Any]) -> float:
        """
        Calculate total liquidity percentage from allocation data.
        
        Args:
            coin_data: Dictionary containing coin's tokenomics data
            
        Returns:
            Total liquidity percentage
        """
        liquidity = coin_data.get('liquidity_allocation', {})
        return liquidity.get('initial', 0) + liquidity.get('locked', 0)
    
    def compare_vesting_periods(self) -> Dict[str, Dict[str, Any]]:
        """
        Compare vesting periods between the two coins.
        
        Returns:
            Dictionary with comparison results for each coin's vesting schedule
        """
        comparison = {
            'coin1': {
                'team_vesting': self.coin1.get('vesting', {}).get('team', {}),
                'advisors_vesting': self.coin1.get('vesting', {}).get('advisors', {}),
                'total_vesting_duration': self._calculate_total_vesting_duration(self.coin1)
            },
            'coin2': {
                'team_vesting': self.coin2.get('vesting', {}).get('team', {}),
                'advisors_vesting': self.coin2.get('vesting', {}).get('advisors', {}),
                'total_vesting_duration': self._calculate_total_vesting_duration(self.coin2)
            }
        }
        return comparison
    
    def _calculate_total_vesting_duration(self, coin_data: Dict[str, Any]) -> int:
        """
        Calculate longest vesting duration from vesting data.
        
        Args:
            coin_data: Dictionary containing coin's tokenomics data
            
        Returns:
            Longest vesting duration in days
        """
        vesting = coin_data.get('vesting', {})
        max_duration = 0
        for group in vesting.values():
            duration = group.get('duration_days', 0)
            if duration > max_duration:
                max_duration = duration
        return max_duration
    
    def compare_community_incentives(self) -> Dict[str, Dict[str, Any]]:
        """
        Compare community incentives between the two coins.
        
        Returns:
            Dictionary with comparison results for each coin's community incentives
        """
        comparison = {
            'coin1': {
                'reward_programs': self.coin1.get('community_incentives', {}).get('reward_programs', []),
                'allocation_percentage': self.coin1.get('community_incentives', {}).get('allocation', 0),
                'voting_power': self.coin1.get('community_incentives', {}).get('voting_power', 0)
            },
            'coin2': {
                'reward_programs': self.coin2.get('community_incentives', {}).get('reward_programs', []),
                'allocation_percentage': self.coin2.get('community_incentives', {}).get('allocation', 0),
                'voting_power': self.coin2.get('community_incentives', {}).get('voting_power', 0)
            }
        }
        return comparison
    
    def generate_comparison_report(self) -> Dict[str, Any]:
        """
        Generate a comprehensive comparison report of all tokenomics aspects.
        
        Returns:
            Dictionary containing full comparison report
        """
        return {
            'liquidity_allocation': self.compare_liquidity_allocation(),
            'vesting_periods': self.compare_vesting_periods(),
            'community_incentives': self.compare_community_incentives()
        }

def load_tokenomics_data(file_path: str) -> Dict[str, Any]:
    """
    Load tokenomics data from a JSON file.
    
    Args:
        file_path: Path to JSON file containing tokenomics data
        
    Returns:
        Dictionary containing tokenomics data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Tokenomics data file not found at {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format in tokenomics data file", file_path, 0)

# Example usage
if __name__ == "__main__":
    try:
        # Load tokenomics data for both coins
        btfd_data = load_tokenomics_data('btfd_tokenomics.json')
        other_coin_data = load_tokenomics_data('other_coin_tokenomics.json')
        
        # Initialize analyzer and generate report
        analyzer = TokenomicsAnalyzer(btfd_data, other_coin_data)
        report = analyzer.generate_comparison_report()
        
        # Save comparison report
        with open('tokenomics_comparison_report.json', 'w') as f:
            json.dump(report, f, indent=2)
            
        print("Tokenomics comparison report generated successfully.")
        
    except Exception as e:
        print(f"Error generating tokenomics comparison: {str(e)}")
```
