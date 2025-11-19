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
from enum import Enum
from typing import List

class InvestmentModelType(str, Enum):
    """Enum for different investment models."""
    GROWTH = "Growth"
    INCOME = "Income"
    CONSERVATIVE = "Conservative"
    VERY_CONSERVATIVE = "Very Conservative"
    BALANCED = "Balanced"
    AGGRESSIVE = "Aggressive"

@dataclass
class AssetAllocationModel:
    """Class to represent an asset allocation model."""
    model_type: InvestmentModelType
    stock_percentage: float
    bond_percentage: float
    cash_percentage: float
    risk_level: str
    return_expectation: str

class InvestmentEducation:
    """Class to provide investment education."""
    def __init__(self):
        self.models = self.initialize_models()

    def initialize_models(self) -> List[AssetAllocationModel]:
        """Initialize a list of asset allocation models."""
        models = [
            AssetAllocationModel(
                model_type=InvestmentModelType.GROWTH,
                stock_percentage=80,
                bond_percentage=15,
                cash_percentage=5,
                risk_level="High",
                return_expectation="High"
            ),
            AssetAllocationModel(
                model_type=InvestmentModelType.INCOME,
                stock_percentage=20,
                bond_percentage=60,
                cash_percentage=20,
                risk_level="Low",
                return_expectation="Low"
            ),
            AssetAllocationModel(
                model_type=InvestmentModelType.CONSERVATIVE,
                stock_percentage=40,
                bond_percentage=50,
                cash_percentage=10,
                risk_level="Medium",
                return_expectation="Medium"
            ),
            AssetAllocationModel(
                model_type=InvestmentModelType.VERY_CONSERVATIVE,
                stock_percentage=20,
                bond_percentage=70,
                cash_percentage=10,
                risk_level="Very Low",
                return_expectation="Very Low"
            ),
            AssetAllocationModel(
                model_type=InvestmentModelType.BALANCED,
                stock_percentage=60,
                bond_percentage=30,
                cash_percentage=10,
                risk_level="Medium",
                return_expectation="Medium"
            ),
            AssetAllocationModel(
                model_type=InvestmentModelType.AGGRESSIVE,
                stock_percentage=90,
                bond_percentage=5,
                cash_percentage=5,
                risk_level="Very High",
                return_expectation="Very High"
            ),
        ]
        return models

    def get_model(self, model_type: InvestmentModelType) -> AssetAllocationModel:
        """Get an asset allocation model by type."""
        for model in self.models:
            if model.model_type == model_type:
                return model
        raise ValueError("Model type not found")

    def print_models(self):
        """Print all asset allocation models."""
        for model in self.models:
            print(f"Model Type: {model.model_type.value}")
            print(f"Stock Percentage: {model.stock_percentage}%")
            print(f"Bond Percentage: {model.bond_percentage}%")
            print(f"Cash Percentage: {model.cash_percentage}%")
            print(f"Risk Level: {model.risk_level}")
            print(f"Return Expectation: {model.return_expectation}")
            print("------------------------")

def main():
    education = InvestmentEducation()
    education.print_models()

    # Example usage: Get a specific model
    try:
        model = education.get_model(InvestmentModelType.GROWTH)
        print(f"Model Type: {model.model_type.value}")
        print(f"Stock Percentage: {model.stock_percentage}%")
        print(f"Bond Percentage: {model.bond_percentage}%")
        print(f"Cash Percentage: {model.cash_percentage}%")
        print(f"Risk Level: {model.risk_level}")
        print(f"Return Expectation: {model.return_expectation}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
