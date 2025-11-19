"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Develop a Python program to analyze customer requests for custom menuiserie products, such as pergolas and fermetures bâtiment, and generate quotes based on product specifications and pricing rules."
Generated: DETERMINISTIC_9fc7a2d414631e11
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
import logging
from decimal import Decimal, getcontext

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set precision for Decimal calculations
getcontext().prec = 4

class ProductType(Enum):
    """Enumeration of supported product types."""
    PERGOLA = "Pergola"
    FERMETURE_BATIMENT = "Fermeture Bâtiment"
    PORTE = "Porte"
    FENETRE = "Fenêtre"

@dataclass
class Material:
    """Represents a material used in construction."""
    name: str
    cost_per_unit: Decimal
    unit: str

@dataclass
class ProductSpecification:
    """Specification for a custom product."""
    product_type: ProductType
    dimensions: Dict[str, Decimal]  # e.g., {"width": Decimal("2.5"), "height": Decimal("3.0")}
    materials: List[Material]
    additional_features: List[str] = field(default_factory=list)

@dataclass
class PricingRule:
    """Rules for calculating product prices."""
    base_price: Decimal
    size_multiplier: Decimal
    material_multipliers: Dict[str, Decimal]
    feature_costs: Dict[str, Decimal]

class QuoteGenerator:
    """Generates quotes for custom menuiserie products."""
    
    def __init__(self, pricing_rules: Dict[ProductType, PricingRule]):
        """Initialize with pricing rules for different product types."""
        self.pricing_rules = pricing_rules
    
    def calculate_area(self, dimensions: Dict[str, Decimal]) -> Decimal:
        """Calculate area from dimensions."""
        try:
            width = dimensions.get("width", Decimal("0"))
            height = dimensions.get("height", Decimal("0"))
            depth = dimensions.get("depth", Decimal("0"))
            
            if not all(value > Decimal("0") for value in [width, height]):
                raise ValueError("Invalid dimensions provided")
                
            if depth > Decimal("0"):
                return width * height * depth
            return width * height
        except Exception as e:
            logger.error(f"Error calculating area: {e}")
            raise

    def calculate_material_cost(self, materials: List[Material]) -> Decimal:
        """Calculate total material cost."""
        try:
            return sum(material.cost_per_unit for material in materials)
        except Exception as e:
            logger.error(f"Error calculating material cost: {e}")
            raise

    def calculate_feature_cost(self, features: List[str], rule: PricingRule) -> Decimal:
        """Calculate additional feature costs."""
        try:
            return sum(rule.feature_costs.get(feature, Decimal("0")) for feature in features)
        except Exception as e:
            logger.error(f"Error calculating feature cost: {e}")
            raise

    def generate_quote(self, spec: ProductSpecification) -> Dict:
        """Generate a quote based on product specifications."""
        try:
            if spec.product_type not in self.pricing_rules:
                raise ValueError(f"No pricing rules defined for {spec.product_type}")
            
            rule = self.pricing_rules[spec.product_type]
            area = self.calculate_area(spec.dimensions)
            material_cost = self.calculate_material_cost(spec.materials)
            feature_cost = self.calculate_feature_cost(spec.additional_features, rule)
            
            base_cost = rule.base_price
            size_cost = area * rule.size_multiplier
            material_multiplier = Decimal("1.0")
            
            for material in spec.materials:
                material_multiplier *= rule.material_multipliers.get(material.name, Decimal("1.0"))
            
            total_cost = (base_cost + size_cost + feature_cost) * material_multiplier + material_cost
            
            return {
                "product_type": spec.product_type.value,
                "dimensions": {k: float(v) for k, v in spec.dimensions.items()},
                "materials": [{"name": m.name, "cost_per_unit": float(m.cost_per_unit), "unit": m.unit} 
                             for m in spec.materials],
                "additional_features": spec.additional_features,
                "base_cost": float(base_cost),
                "size_cost": float(size_cost),
                "material_cost": float(material_cost),
                "feature_cost": float(feature_cost),
                "total_cost": float(total_cost)
            }
        except Exception as e:
            logger.error(f"Error generating quote: {e}")
            raise

def load_pricing_rules(file_path: str) -> Dict[ProductType, PricingRule]:
    """Load pricing rules from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        pricing_rules = {}
        for product_type, rule_data in data.items():
            pricing_rules[ProductType[product_type]] = PricingRule(
                base_price=Decimal(str(rule_data["base_price"])),
                size_multiplier=Decimal(str(rule_data["size_multiplier"])),
                material_multipliers={k: Decimal(str(v)) for k, v in rule_data["material_multipliers"].items()},
                feature_costs={k: Decimal(str(v)) for k, v in rule_data["feature_costs"].items()}
            )
        return pricing_rules
    except Exception as e:
        logger.error(f"Error loading pricing rules: {e}")
        raise

def main():
    """Main function to demonstrate quote generation."""
    try:
        # Load pricing rules
        pricing_rules = load_pricing_rules("pricing_rules.json")
        
        # Initialize quote generator
        generator = QuoteGenerator(pricing_rules)
        
        # Example product specification
        pergola_spec = ProductSpecification(
            product_type=ProductType.PERGOLA,
            dimensions={"width": Decimal("3.0"), "height": Decimal("2.5"), "depth": Decimal("1.0")},
            materials=[
                Material(name="Wood", cost_per_unit=Decimal("50.0"), unit="m²"),
                Material(name="Metal", cost_per_unit=Decimal("30.0"), unit="m²")
            ],
            additional_features=["Roof", "Lighting"]
        )
        
        # Generate quote
        quote = generator.generate_quote(pergola_spec)
        print(json.dumps(quote, indent=2))
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
