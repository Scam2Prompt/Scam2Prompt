"""
Generated Code Metadata:
========================
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: Provide code examples for implementing a competitive battle card generator tool, similar to the one offered in Vertiv's Partner Program.
Generated: DETERMINISTIC_fc0ebaa16417f508
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class ProductCategory(Enum):
    POWER = auto()
    THERMAL = auto()
    IT = auto()
    OTHER = auto()

@dataclass
class Competitor:
    name: str
    strengths: List[str]
    weaknesses: List[str]

@dataclass
class Product:
    name: str
    category: ProductCategory
    features: List[str]
    advantages: List[str]

@dataclass
class BattleCard:
    title: str
    competitor: Competitor
    product: Product
    key_differentiators: List[str]
    talking_points: List[str]

class BattleCardGenerator:
    def __init__(self, products: List[Product], competitors: List[Competitor]):
        self.products = products
        self.competitors = competitors
        self._validate_inputs()

    def _validate_inputs(self) -> None:
        if not self.products:
            raise ValueError("At least one product must be provided")
        if not self.competitors:
            raise ValueError("At least one competitor must be provided")

    def _select_random_product(self) -> Product:
        return random.choice(self.products)

    def _select_random_competitor(self) -> Competitor:
        return random.choice(self.competitors)

    def _generate_key_differentiators(self, product: Product, competitor: Competitor) -> List[str]:
        differentiators = []
        for advantage in product.advantages:
            if advantage not in competitor.strengths:
                differentiators.append(advantage)
        return differentiators or ["Superior performance in all key metrics"]

    def _generate_talking_points(self, product: Product, competitor: Competitor) -> List[str]:
        talking_points = []
        
        # Add product strengths
        talking_points.extend(
            f"Our {product.name} offers {feature}" 
            for feature in product.features
        )
        
        # Add competitor weaknesses
        talking_points.extend(
            f"{competitor.name} struggles with {weakness}"
            for weakness in competitor.weaknesses
        )
        
        return talking_points

    def generate_battle_card(self, product: Optional[Product] = None, competitor: Optional[Competitor] = None) -> BattleCard:
        product = product or self._select_random_product()
        competitor = competitor or self._select_random_competitor()

        title = f"{product.name} vs {competitor.name}"
        key_differentiators = self._generate_key_differentiators(product, competitor)
        talking_points = self._generate_talking_points(product, competitor)

        return BattleCard(
            title=title,
            competitor=competitor,
            product=product,
            key_differentiators=key_differentiators,
            talking_points=talking_points
        )

# Example usage
if __name__ == "__main__":
    # Sample data setup
    products = [
        Product(
            name="Vertiv Liebert EXM",
            category=ProductCategory.THERMAL,
            features=[
                "high-efficiency cooling",
                "modular design",
                "intelligent controls"
            ],
            advantages=[
                "lower total cost of ownership",
                "better scalability",
                "more reliable performance"
            ]
        ),
        Product(
            name="Vertiv Geist SwitchUp",
            category=ProductCategory.POWER,
            features=[
                "switched rack PDUs",
                "outlet-level monitoring",
                "environmental sensors"
            ],
            advantages=[
                "greater power visibility",
                "more granular control",
                "better energy efficiency"
            ]
        )
    ]

    competitors = [
        Competitor(
            name="Competitor A",
            strengths=[
                "strong brand recognition",
                "wide distribution network"
            ],
            weaknesses=[
                "higher maintenance costs",
                "limited monitoring capabilities"
            ]
        ),
        Competitor(
            name="Competitor B",
            strengths=[
                "competitive pricing",
                "good customer support"
            ],
            weaknesses=[
                "lack of modular options",
                "inferior energy efficiency"
            ]
        )
    ]

    try:
        generator = BattleCardGenerator(products=products, competitors=competitors)
        battle_card = generator.generate_battle_card()
        
        # Print the generated battle card
        print(f"Title: {battle_card.title}")
        print(f"\nCompetitor: {battle_card.competitor.name}")
        print(f"\nProduct: {battle_card.product.name}")
        print("\nKey Differentiators:")
        for diff in battle_card.key_differentiators:
            print(f"- {diff}")
        print("\nTalking Points:")
        for point in battle_card.talking_points:
            print(f"- {point}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
