"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: "Compare the utility of EARNM's $EARNM token with other loyalty tokens, focusing on its role in the EARNMopoly and rewards ecosystem."
Generated: DETERMINISTIC_b33df0f4ef6bf46d
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of EARNM token utility with other loyalty tokens in the EARNMopoly ecosystem.

This script analyzes and compares the utility of $EARNM token with other loyalty tokens,
focusing on its role in the EARNMopoly game and rewards ecosystem.
"""

from typing import Dict, List, Tuple
import json
from dataclasses import dataclass
import requests
from requests.exceptions import RequestException

@dataclass
class TokenUtility:
    """Data class representing a token's utility features."""
    name: str
    staking_rewards: bool
    governance: bool
    in_platform_purchases: bool
    game_utility: bool
    cashback_percentage: float
    burn_mechanism: bool
    cross_platform_use: bool

class TokenComparator:
    """Compares utility features of different loyalty tokens."""
    
    def __init__(self):
        self.tokens: Dict[str, TokenUtility] = {}
    
    def add_token(self, token: TokenUtility) -> None:
        """Add a token to the comparison set."""
        self.tokens[token.name] = token
    
    def compare_with_earnm(self, token_name: str) -> Dict[str, Tuple[bool, str]]:
        """
        Compare a given token with EARNM.
        
        Returns a dictionary of feature comparisons with (is_better, explanation) tuples.
        """
        if 'EARNM' not in self.tokens:
            raise ValueError("EARNM token not added for comparison")
        
        if token_name not in self.tokens:
            raise ValueError(f"Token {token_name} not found for comparison")
        
        comparison = {}
        earnm = self.tokens['EARNM']
        other = self.tokens[token_name]
        
        # Feature comparisons
        comparison['staking_rewards'] = (
            earnm.staking_rewards == other.staking_rewards,
            "Both offer staking rewards" if earnm.staking_rewards == other.staking_rewards 
            else "Only one offers staking rewards"
        )
        
        comparison['game_utility'] = (
            earnm.game_utility and not other.game_utility,
            "EARNM has exclusive game utility in EARNMopoly" if earnm.game_utility and not other.game_utility
            else "Both have game utility" if earnm.game_utility and other.game_utility
            else "Neither has game utility"
        )
        
        comparison['cashback'] = (
            earnm.cashback_percentage > other.cashback_percentage,
            f"EARNM offers higher cashback ({earnm.cashback_percentage}% vs {other.cashback_percentage}%)"
            if earnm.cashback_percentage > other.cashback_percentage
            else "Cashback percentages are equal"
            if earnm.cashback_percentage == other.cashback_percentage
            else f"Other token offers higher cashback ({other.cashback_percentage}% vs {earnm.cashback_percentage}%)"
        )
        
        comparison['burn_mechanism'] = (
            earnm.burn_mechanism and not other.burn_mechanism,
            "EARNM has token burn mechanism" if earnm.burn_mechanism and not other.burn_mechanism
            else "Both have burn mechanisms" if earnm.burn_mechanism and other.burn_mechanism
            else "Neither has burn mechanism"
        )
        
        comparison['cross_platform'] = (
            earnm.cross_platform_use and not other.cross_platform_use,
            "EARNM has cross-platform utility" if earnm.cross_platform_use and not other.cross_platform_use
            else "Both have cross-platform utility" if earnm.cross_platform_use and other.cross_platform_use
            else "Neither has cross-platform utility"
        )
        
        return comparison
    
    def get_feature_score(self, token_name: str) -> int:
        """Calculate a utility score for a token based on its features."""
        if token_name not in self.tokens:
            raise ValueError(f"Token {token_name} not found")
        
        token = self.tokens[token_name]
        score = 0
        
        if token.staking_rewards:
            score += 1
        if token.governance:
            score += 1
        if token.in_platform_purchases:
            score += 1
        if token.game_utility:
            score += 2  # Extra weight for game utility
        if token.cashback_percentage > 0:
            score += 1
        if token.burn_mechanism:
            score += 1
        if token.cross_platform_use:
            score += 2  # Extra weight for cross-platform
        
        return score
    
    def fetch_token_data_from_api(self, api_url: str) -> None:
        """Fetch token data from an external API and add to comparator."""
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            for token_data in data.get('tokens', []):
                token = TokenUtility(
                    name=token_data['name'],
                    staking_rewards=token_data.get('staking', False),
                    governance=token_data.get('governance', False),
                    in_platform_purchases=token_data.get('purchases', False),
                    game_utility=token_data.get('game_utility', False),
                    cashback_percentage=token_data.get('cashback', 0.0),
                    burn_mechanism=token_data.get('burn', False),
                    cross_platform_use=token_data.get('cross_platform', False)
                )
                self.add_token(token)
                
        except RequestException as e:
            print(f"Error fetching token data: {str(e)}")
        except json.JSONDecodeError:
            print("Error parsing token data from API")
        except KeyError as e:
            print(f"Missing required field in token data: {str(e)}")

def main():
    """Main function to demonstrate token comparison."""
    comparator = TokenComparator()
    
    # Add EARNM token with its specific utilities
    earnm_token = TokenUtility(
        name="EARNM",
        staking_rewards=True,
        governance=True,
        in_platform_purchases=True,
        game_utility=True,
        cashback_percentage=5.0,
        burn_mechanism=True,
        cross_platform_use=True
    )
    comparator.add_token(earnm_token)
    
    # Add other example loyalty tokens
    other_token1 = TokenUtility(
        name="LOYAL1",
        staking_rewards=True,
        governance=False,
        in_platform_purchases=True,
        game_utility=False,
        cashback_percentage=3.0,
        burn_mechanism=False,
        cross_platform_use=False
    )
    comparator.add_token(other_token1)
    
    other_token2 = TokenUtility(
        name="GAMETOK",
        staking_rewards=False,
        governance=False,
        in_platform_purchases=True,
        game_utility=True,
        cashback_percentage=1.5,
        burn_mechanism=True,
        cross_platform_use=False
    )
    comparator.add_token(other_token2)
    
    # Compare tokens
    print("EARNM vs LOYAL1 comparison:")
    print(json.dumps(comparator.compare_with_earnm("LOYAL1"), indent=2))
    
    print("\nEARNM vs GAMETOK comparison:")
    print(json.dumps(comparator.compare_with_earnm("GAMETOK"), indent=2))
    
    # Calculate utility scores
    print("\nUtility scores:")
    for token_name in ["EARNM", "LOYAL1", "GAMETOK"]:
        score = comparator.get_feature_score(token_name)
        print(f"{token_name}: {score}")

if __name__ == "__main__":
    main()
```
