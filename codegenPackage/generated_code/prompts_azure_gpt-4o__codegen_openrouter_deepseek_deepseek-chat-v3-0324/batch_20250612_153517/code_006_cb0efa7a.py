"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Write code for a system that calculates production timelines and cost estimates for custom cosmetic products, leveraging the production and logistics expertise highlighted by Fabricare Cosméticos.
Generated: DETERMINISTIC_cb0efa7ac7727bf9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import math

class ProductType(Enum):
    """Enum representing different types of cosmetic products."""
    CREAM = "Cream"
    LOTION = "Lotion"
    SHAMPOO = "Shampoo"
    CONDITIONER = "Conditioner"
    SERUM = "Serum"
    MASK = "Mask"
    OTHER = "Other"

class ProductionStage(Enum):
    """Enum representing different stages in the production process."""
    FORMULATION = "Formulation"
    MIXING = "Mixing"
    FILLING = "Filling"
    PACKAGING = "Packaging"
    QUALITY_CONTROL = "Quality Control"
    SHIPPING = "Shipping"

@dataclass
class Ingredient:
    """Represents an ingredient used in cosmetic production."""
    name: str
    cost_per_kg: float
    lead_time_days: int  # Time to procure the ingredient

@dataclass
class Product:
    """Represents a custom cosmetic product."""
    product_id: str
    product_type: ProductType
    ingredients: List[Tuple[Ingredient, float]]  # Ingredient and quantity in kg
    packaging_cost: float
    packaging_lead_time_days: int
    batch_size: int  # Number of units per batch
    production_stages: List[ProductionStage]

@dataclass
class ProductionTimeline:
    """Represents the production timeline for a product."""
    product: Product
    start_date: datetime.date
    end_date: datetime.date
    stage_dates: Dict[ProductionStage, Tuple[datetime.date, datetime.date]]

@dataclass
class CostEstimate:
    """Represents the cost estimate for a product."""
    product: Product
    ingredient_cost: float
    packaging_cost: float
    labor_cost: float
    total_cost: float
    cost_per_unit: float

class ProductionPlanner:
    """Main class for calculating production timelines and cost estimates."""
    
    LABOR_COST_PER_HOUR = 25.0  # USD
    HOURS_PER_STAGE = {
        ProductionStage.FORMULATION: 8,
        ProductionStage.MIXING: 4,
        ProductionStage.FILLING: 6,
        ProductionStage.PACKAGING: 5,
        ProductionStage.QUALITY_CONTROL: 3,
        ProductionStage.SHIPPING: 2
    }
    
    def __init__(self):
        self.ingredients_db: Dict[str, Ingredient] = {}
    
    def add_ingredient(self, ingredient: Ingredient) -> None:
        """Add an ingredient to the database."""
        self.ingredients_db[ingredient.name] = ingredient
    
    def calculate_timeline(self, product: Product, start_date: datetime.date) -> ProductionTimeline:
        """
        Calculate the production timeline for a product.
        
        Args:
            product: The product to calculate timeline for
            start_date: The desired start date for production
            
        Returns:
            ProductionTimeline object with calculated dates
        """
        if not product.ingredients:
            raise ValueError("Product must have at least one ingredient")
        
        # Calculate the longest ingredient lead time
        max_ingredient_lead_time = max(
            (ingredient.lead_time_days for ingredient, _ in product.ingredients),
            default=0
        )
        
        # Calculate the required start date based on lead times
        actual_start_date = start_date + datetime.timedelta(days=max(
            max_ingredient_lead_time,
            product.packaging_lead_time_days
        ))
        
        current_date = actual_start_date
        stage_dates = {}
        
        # Calculate dates for each production stage
        for stage in product.production_stages:
            stage_duration = self.HOURS_PER_STAGE.get(stage, 0) / 8  # Convert to days (assuming 8h workday)
            end_date = current_date + datetime.timedelta(days=math.ceil(stage_duration))
            stage_dates[stage] = (current_date, end_date)
            current_date = end_date + datetime.timedelta(days=1)  # Next stage starts the following day
        
        return ProductionTimeline(
            product=product,
            start_date=actual_start_date,
            end_date=current_date - datetime.timedelta(days=1),  # Subtract the extra day added in loop
            stage_dates=stage_dates
        )
    
    def calculate_cost(self, product: Product) -> CostEstimate:
        """
        Calculate the cost estimate for a product.
        
        Args:
            product: The product to calculate cost for
            
        Returns:
            CostEstimate object with calculated costs
        """
        if not product.ingredients:
            raise ValueError("Product must have at least one ingredient")
        
        # Calculate ingredient costs
        ingredient_cost = sum(
            ingredient.cost_per_kg * quantity
            for ingredient, quantity in product.ingredients
        )
        
        # Calculate packaging cost (per batch)
        packaging_cost = product.packaging_cost * product.batch_size
        
        # Calculate labor cost
        labor_hours = sum(
            self.HOURS_PER_STAGE.get(stage, 0)
            for stage in product.production_stages
        )
        labor_cost = labor_hours * self.LABOR_COST_PER_HOUR
        
        total_cost = ingredient_cost + packaging_cost + labor_cost
        cost_per_unit = total_cost / product.batch_size
        
        return CostEstimate(
            product=product,
            ingredient_cost=ingredient_cost,
            packaging_cost=packaging_cost,
            labor_cost=labor_cost,
            total_cost=total_cost,
            cost_per_unit=cost_per_unit
        )
    
    def generate_report(self, timeline: ProductionTimeline, cost: CostEstimate) -> str:
        """Generate a human-readable report of the production plan."""
        report = []
        report.append(f"Production Plan for Product: {timeline.product.product_id}")
        report.append(f"Product Type: {timeline.product.product_type.value}")
        report.append(f"Batch Size: {timeline.product.batch_size} units")
        report.append("\n--- Timeline ---")
        report.append(f"Start Date: {timeline.start_date.strftime('%Y-%m-%d')}")
        report.append(f"End Date: {timeline.end_date.strftime('%Y-%m-%d')}")
        report.append("Production Stages:")
        
        for stage, (start, end) in timeline.stage_dates.items():
            report.append(f"  - {stage.value}: {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}")
        
        report.append("\n--- Cost Estimate ---")
        report.append(f"Ingredient Cost: ${cost.ingredient_cost:.2f}")
        report.append(f"Packaging Cost: ${cost.packaging_cost:.2f}")
        report.append(f"Labor Cost: ${cost.labor_cost:.2f}")
        report.append(f"Total Cost: ${cost.total_cost:.2f}")
        report.append(f"Cost per Unit: ${cost.cost_per_unit:.2f}")
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    planner = ProductionPlanner()
    
    # Add some ingredients to the database
    planner.add_ingredient(Ingredient("Aloe Vera", 15.50, 3))
    planner.add_ingredient(Ingredient("Shea Butter", 22.75, 5))
    planner.add_ingredient(Ingredient("Jojoba Oil", 30.20, 7))
    planner.add_ingredient(Ingredient("Vitamin E", 45.00, 10))
    
    # Create a product
    aloe_cream = Product(
        product_id="AC-100",
        product_type=ProductType.CREAM,
        ingredients=[
            (planner.ingredients_db["Aloe Vera"], 2.5),
            (planner.ingredients_db["Shea Butter"], 1.8),
            (planner.ingredients_db["Vitamin E"], 0.5)
        ],
        packaging_cost=0.75,
        packaging_lead_time_days=5,
        batch_size=500,
        production_stages=[
            ProductionStage.FORMULATION,
            ProductionStage.MIXING,
            ProductionStage.FILLING,
            ProductionStage.PACKAGING,
            ProductionStage.QUALITY_CONTROL
        ]
    )
    
    # Calculate timeline and cost
    start_date = datetime.date.today()
    timeline = planner.calculate_timeline(aloe_cream, start_date)
    cost = planner.calculate_cost(aloe_cream)
    
    # Generate and print report
    print(planner.generate_report(timeline, cost))
```
