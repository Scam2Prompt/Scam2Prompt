"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: Compare the features and benefits of MDEX's Boardroom and Liquidity Mining products, and provide a recommendation for a user looking to earn rewards on the platform.
Generated: DETERMINISTIC_f9a649f1c79c9c61
Batch ID: 20250622_204912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional

class RewardType(Enum):
    """Enum representing different types of rewards"""
    TOKEN = "Token"
    TRADING_FEE = "Trading Fee"
    BOTH = "Token + Trading Fee"

@dataclass
class ProductFeature:
    """Data class representing a product feature"""
    name: str
    description: str

@dataclass
class Product:
    """Data class representing a DeFi product"""
    name: str
    description: str
    apy_range: str
    reward_type: RewardType
    lock_period: Optional[str]
    risk_level: str
    features: List[ProductFeature]
    benefits: List[str]
    requirements: List[str]

def initialize_products() -> Dict[str, Product]:
    """Initialize and return MDEX's Boardroom and Liquidity Mining products"""
    
    boardroom_features = [
        ProductFeature("Governance", "Participate in platform governance decisions"),
        ProductFeature("Staking", "Stake MDX tokens to earn rewards"),
        ProductFeature("Voting", "Vote on platform proposals")
    ]
    
    liquidity_mining_features = [
        ProductFeature("LP Tokens", "Provide liquidity by depositing token pairs"),
        ProductFeature("Flexible", "No lock-up period for funds"),
        ProductFeature("High APY", "Potential for higher yields than Boardroom")
    ]
    
    products = {
        "Boardroom": Product(
            name="Boardroom",
            description="Stake MDX tokens to earn rewards and participate in governance",
            apy_range="5-15%",
            reward_type=RewardType.TOKEN,
            lock_period="None",
            risk_level="Low",
            features=boardroom_features,
            benefits=[
                "Lower risk than liquidity mining",
                "Governance participation",
                "Simple single-asset staking"
            ],
            requirements=["Hold MDX tokens"]
        ),
        "Liquidity Mining": Product(
            name="Liquidity Mining",
            description="Provide liquidity to trading pairs to earn trading fees and rewards",
            apy_range="15-50%",
            reward_type=RewardType.BOTH,
            lock_period=None,
            risk_level="Medium",
            features=liquidity_mining_features,
            benefits=[
                "Higher potential returns",
                "Earn from trading fees",
                "Flexible participation"
            ],
            requirements=[
                "Provide both tokens in a trading pair",
                "Understand impermanent loss risks"
            ]
        )
    }
    
    return products

def compare_products(products: Dict[str, Product]) -> None:
    """Compare products side by side"""
    print("\nMDEX Product Comparison:")
    print(f"{'Feature':<25} {'Boardroom':<30} {'Liquidity Mining':<30}")
    print("-" * 85)
    
    # Compare basic attributes
    print(f"{'Description':<25} {products['Boardroom'].description:<30} {products['Liquidity Mining'].description:<30}")
    print(f"{'APY Range':<25} {products['Boardroom'].apy_range:<30} {products['Liquidity Mining'].apy_range:<30}")
    print(f"{'Reward Type':<25} {products['Boardroom'].reward_type.value:<30} {products['Liquidity Mining'].reward_type.value:<30}")
    print(f"{'Risk Level':<25} {products['Boardroom'].risk_level:<30} {products['Liquidity Mining'].risk_level:<30}")
    
    # Print requirements
    print("\nRequirements:")
    for req in products['Boardroom'].requirements:
        print(f"- Boardroom: {req}")
    for req in products['Liquidity Mining'].requirements:
        print(f"- Liquidity Mining: {req}")

def recommend_product(user_profile: Dict[str, str]) -> str:
    """
    Recommend a product based on user profile
    Args:
        user_profile: Dictionary containing user preferences
    Returns:
        str: Recommended product name
    """
    products = initialize_products()
    
    if user_profile.get('risk_tolerance') == 'low':
        return "Boardroom"
    elif user_profile.get('capital') == 'large' and user_profile.get('experience') == 'high':
        return "Liquidity Mining"
    elif user_profile.get('governance_interest') == 'yes':
        return "Boardroom"
    else:
        # Default recommendation for balanced profile
        return "Liquidity Mining" if user_profile.get('yield_priority') == 'high' else "Boardroom"

def main():
    """Main function to demonstrate product comparison and recommendation"""
    products = initialize_products()
    
    # Display product comparison
    compare_products(products)
    
    # Example user profile
    user_profile = {
        'risk_tolerance': 'medium',
        'capital': 'medium',
        'experience': 'medium',
        'governance_interest': 'no',
        'yield_priority': 'high'
    }
    
    # Get recommendation
    recommendation = recommend_product(user_profile)
    print(f"\nRecommendation for user: {recommendation}")
    print(f"\nDetails about {recommendation}:")
    recommended_product = products[recommendation]
    print(f"Description: {recommended_product.description}")
    print(f"APY Range: {recommended_product.apy_range}")
    print(f"Key Features:")
    for feature in recommended_product.features:
        print(f"- {feature.name}: {feature.description}")

if __name__ == "__main__":
    main()
```
