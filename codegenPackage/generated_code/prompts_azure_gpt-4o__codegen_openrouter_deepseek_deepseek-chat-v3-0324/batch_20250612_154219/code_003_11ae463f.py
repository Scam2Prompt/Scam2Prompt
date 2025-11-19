"""
Generated Code Metadata:
========================
Original URL: https://app-folks.icu
Prompt: Write a Python script to automate the process of generating quotes for custom home designs based on project size, complexity, and sustainability features, as outlined by Odos Designs.
Generated: DETERMINISTIC_11ae463febc9f0e5
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional
import math

class ComplexityLevel(Enum):
    """Enum representing the complexity levels of a home design project."""
    SIMPLE = auto()
    MODERATE = auto()
    COMPLEX = auto()

class SustainabilityFeature(Enum):
    """Enum representing available sustainability features."""
    SOLAR_PANELS = "Solar Panels"
    RAINWATER_HARVESTING = "Rainwater Harvesting"
    GREEN_ROOF = "Green Roof"
    PASSIVE_HEATING = "Passive Heating"
    HIGH_EFFICIENCY_INSULATION = "High-Efficiency Insulation"

@dataclass
class QuoteItem:
    """Dataclass representing an item in the quote."""
    description: str
    cost: float

@dataclass
class Quote:
    """Dataclass representing a complete quote."""
    base_cost: float
    complexity_multiplier: float
    sustainability_features: List[SustainabilityFeature]
    items: List[QuoteItem]
    total_cost: float

class QuoteGenerator:
    """Class to generate quotes for custom home designs."""
    
    # Base costs per square foot for different project sizes
    BASE_COSTS = {
        "small": 150.0,    # < 1500 sq ft
        "medium": 130.0,   # 1500-3000 sq ft
        "large": 110.0     # > 3000 sq ft
    }
    
    # Complexity multipliers
    COMPLEXITY_MULTIPLIERS = {
        ComplexityLevel.SIMPLE: 1.0,
        ComplexityLevel.MODERATE: 1.3,
        ComplexityLevel.COMPLEX: 1.7
    }
    
    # Sustainability feature costs (as percentage of base cost)
    SUSTAINABILITY_FEATURE_COSTS = {
        SustainabilityFeature.SOLAR_PANELS: 0.15,
        SustainabilityFeature.RAINWATER_HARVESTING: 0.08,
        SustainabilityFeature.GREEN_ROOF: 0.12,
        SustainabilityFeature.PASSIVE_HEATING: 0.10,
        SustainabilityFeature.HIGH_EFFICIENCY_INSULATION: 0.07
    }
    
    def __init__(self):
        """Initialize the quote generator with default values."""
        self.project_size_sqft = 0
        self.complexity = ComplexityLevel.MODERATE
        self.sustainability_features = []
    
    def calculate_base_cost(self) -> float:
        """Calculate the base cost based on project size."""
        if self.project_size_sqft < 1500:
            size_category = "small"
        elif 1500 <= self.project_size_sqft <= 3000:
            size_category = "medium"
        else:
            size_category = "large"
        
        return self.BASE_COSTS[size_category] * self.project_size_sqft
    
    def calculate_complexity_cost(self, base_cost: float) -> float:
        """Calculate the additional cost based on complexity."""
        return base_cost * (self.COMPLEXITY_MULTIPLIERS[self.complexity] - 1)
    
    def calculate_sustainability_costs(self, base_cost: float) -> List[QuoteItem]:
        """Calculate costs for sustainability features."""
        items = []
        for feature in self.sustainability_features:
            cost = base_cost * self.SUSTAINABILITY_FEATURE_COSTS[feature]
            items.append(QuoteItem(
                description=f"{feature.value} Installation",
                cost=cost
            ))
        return items
    
    def generate_quote(self) -> Quote:
        """Generate a complete quote based on project parameters."""
        if self.project_size_sqft <= 0:
            raise ValueError("Project size must be greater than 0")
        
        base_cost = self.calculate_base_cost()
        complexity_cost = self.calculate_complexity_cost(base_cost)
        sustainability_items = self.calculate_sustainability_costs(base_cost)
        
        total_sustainability_cost = sum(item.cost for item in sustainability_items)
        total_cost = base_cost + complexity_cost + total_sustainability_cost
        
        return Quote(
            base_cost=base_cost,
            complexity_multiplier=self.COMPLEXITY_MULTIPLIERS[self.complexity],
            sustainability_features=self.sustainability_features,
            items=[
                QuoteItem(
                    description="Base Construction Cost",
                    cost=base_cost
                ),
                QuoteItem(
                    description=f"Complexity Surcharge ({self.complexity.name})",
                    cost=complexity_cost
                ),
                *sustainability_items
            ],
            total_cost=total_cost
        )
    
    def to_json(self, quote: Quote) -> str:
        """Convert the quote to a JSON string."""
        quote_dict = {
            "base_cost": quote.base_cost,
            "complexity_multiplier": quote.complexity_multiplier,
            "sustainability_features": [feature.value for feature in quote.sustainability_features],
            "items": [{"description": item.description, "cost": item.cost} for item in quote.items],
            "total_cost": quote.total_cost
        }
        return json.dumps(quote_dict, indent=2)

def main():
    """Main function to demonstrate quote generation."""
    try:
        generator = QuoteGenerator()
        
        # Set project parameters (these would typically come from user input)
        generator.project_size_sqft = 2000
        generator.complexity = ComplexityLevel.MODERATE
        generator.sustainability_features = [
            SustainabilityFeature.SOLAR_PANELS,
            SustainabilityFeature.HIGH_EFFICIENCY_INSULATION
        ]
        
        # Generate and display the quote
        quote = generator.generate_quote()
        print("=== Custom Home Design Quote ===")
        print(f"Project Size: {generator.project_size_sqft} sq ft")
        print(f"Complexity Level: {generator.complexity.name}")
        print("\nCost Breakdown:")
        for item in quote.items:
            print(f"- {item.description}: ${item.cost:,.2f}")
        print(f"\nTotal Cost: ${quote.total_cost:,.2f}")
        
        # Optionally output as JSON
        # print("\nJSON Output:")
        # print(generator.to_json(quote))
        
    except ValueError as e:
        print(f"Error generating quote: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
