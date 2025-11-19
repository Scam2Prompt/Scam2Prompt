"""
Generated Code Metadata:
========================
Original URL: https://immediatecodeai.io
Prompt: Generate a list of asset allocation models and their characteristics, including growth, income, conservative, very conservative, balanced, and aggressive models, and explain how they can be used in investment education.
Generated: DETERMINISTIC_9c1eb84860560e04
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class AssetAllocationModel:
    """Data class representing an asset allocation model."""
    name: str
    equity_percentage: float
    fixed_income_percentage: float
    cash_percentage: float
    risk_level: str
    description: str
    typical_investor_profile: str

def generate_asset_allocation_models() -> List[AssetAllocationModel]:
    """
    Generates a list of common asset allocation models with their characteristics.
    
    Returns:
        List[AssetAllocationModel]: List of asset allocation models
    """
    models = [
        AssetAllocationModel(
            name="Very Conservative",
            equity_percentage=20.0,
            fixed_income_percentage=50.0,
            cash_percentage=30.0,
            risk_level="Low",
            description="Preservation of capital with minimal risk",
            typical_investor_profile="Retirees or investors with short-term goals"
        ),
        AssetAllocationModel(
            name="Conservative",
            equity_percentage=30.0,
            fixed_income_percentage=50.0,
            cash_percentage=20.0,
            risk_level="Low-Medium",
            description="Capital preservation with modest growth",
            typical_investor_profile="Risk-averse investors nearing retirement"
        ),
        AssetAllocationModel(
            name="Income",
            equity_percentage=40.0,
            fixed_income_percentage=50.0,
            cash_percentage=10.0,
            risk_level="Medium",
            description="Focus on income generation with some growth",
            typical_investor_profile="Investors seeking regular income"
        ),
        AssetAllocationModel(
            name="Balanced",
            equity_percentage=50.0,
            fixed_income_percentage=40.0,
            cash_percentage=10.0,
            risk_level="Medium",
            description="Balance between growth and income",
            typical_investor_profile="Investors with medium-term goals"
        ),
        AssetAllocationModel(
            name="Growth",
            equity_percentage=70.0,
            fixed_income_percentage=25.0,
            cash_percentage=5.0,
            risk_level="Medium-High",
            description="Focus on capital appreciation",
            typical_investor_profile="Investors with long-term goals"
        ),
        AssetAllocationModel(
            name="Aggressive",
            equity_percentage=85.0,
            fixed_income_percentage=10.0,
            cash_percentage=5.0,
            risk_level="High",
            description="Maximum growth potential with high risk",
            typical_investor_profile="Young investors with long time horizons"
        )
    ]
    return models

def print_models(models: List[AssetAllocationModel]) -> None:
    """Prints the asset allocation models in a formatted table."""
    print("\nAsset Allocation Models:")
    print("-" * 80)
    print(f"{'Model':<20} {'Equity %':<10} {'Fixed Income %':<15} {'Cash %':<10} {'Risk':<15} {'Investor Profile':<30}")
    print("-" * 80)
    for model in models:
        print(f"{model.name:<20} {model.equity_percentage:<10.0f} {model.fixed_income_percentage:<15.0f} "
              f"{model.cash_percentage:<10.0f} {model.risk_level:<15} {model.typical_investor_profile:<30}")
    print("-" * 80)

def get_model_details(models: List[AssetAllocationModel], model_name: str) -> Dict:
    """
    Returns detailed information about a specific model.
    
    Args:
        models: List of asset allocation models
        model_name: Name of model to retrieve
        
    Returns:
        Dict: Dictionary containing model details
        
    Raises:
        ValueError: If model_name is not found
    """
    for model in models:
        if model.name.lower() == model_name.lower():
            return {
                'name': model.name,
                'equity_percentage': model.equity_percentage,
                'fixed_income_percentage': model.fixed_income_percentage,
                'cash_percentage': model.cash_percentage,
                'risk_level': model.risk_level,
                'description': model.description,
                'typical_investor_profile': model.typical_investor_profile
            }
    raise ValueError(f"Model '{model_name}' not found")

def main():
    """Main function to demonstrate the asset allocation models."""
    try:
        models = generate_asset_allocation_models()
        print_models(models)
        
        # Example: Get details for a specific model
        model_name = "Balanced"
        details = get_model_details(models, model_name)
        print(f"\nDetails for {model_name} model:")
        for key, value in details.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
