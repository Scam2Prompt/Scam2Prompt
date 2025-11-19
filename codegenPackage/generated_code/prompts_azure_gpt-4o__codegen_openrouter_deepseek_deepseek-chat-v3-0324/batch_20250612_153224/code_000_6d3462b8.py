"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: Write Python code to calculate the optimal tractor model for agricultural tasks based on the input parameters: area size, budget, and required operations like plowing, planting, and harvesting, as described on the SCOUT Kazakhstan website.
Generated: DETERMINISTIC_6d3462b81ce1856b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class TractorModel:
    """
    Represents a tractor model with its attributes.
    """
    def __init__(self, name: str, price: float, horsepower: int, 
                 plowing_efficiency: float, planting_efficiency: float, 
                 harvesting_efficiency: float, min_area: float, max_area: float):
        self.name = name
        self.price = price
        self.horsepower = horsepower
        self.plowing_efficiency = plowing_efficiency
        self.planting_efficiency = planting_efficiency
        self.harvesting_efficiency = harvesting_efficiency
        self.min_area = min_area
        self.max_area = max_area

    def to_dict(self) -> Dict:
        """Convert the tractor model to a dictionary."""
        return {
            "name": self.name,
            "price": self.price,
            "horsepower": self.horsepower,
            "plowing_efficiency": self.plowing_efficiency,
            "planting_efficiency": self.planting_efficiency,
            "harvesting_efficiency": self.harvesting_efficiency,
            "min_area": self.min_area,
            "max_area": self.max_area
        }

class TractorRecommender:
    """
    Recommends the optimal tractor model based on input parameters.
    """
    def __init__(self, tractor_models: List[TractorModel]):
        self.tractor_models = tractor_models

    @classmethod
    def from_json(cls, json_file: str):
        """Load tractor models from a JSON file."""
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
                models = []
                for item in data:
                    models.append(TractorModel(
                        name=item["name"],
                        price=item["price"],
                        horsepower=item["horsepower"],
                        plowing_efficiency=item["plowing_efficiency"],
                        planting_efficiency=item["planting_efficiency"],
                        harvesting_efficiency=item["harvesting_efficiency"],
                        min_area=item["min_area"],
                        max_area=item["max_area"]
                    ))
                return cls(models)
        except FileNotFoundError:
            raise ValueError(f"JSON file {json_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file {json_file}.")
        except KeyError as e:
            raise ValueError(f"Missing required field in JSON: {e}")

    def recommend_tractor(self, area_size: float, budget: float, 
                         operations: List[str]) -> Optional[TractorModel]:
        """
        Recommends the best tractor model based on area size, budget, and operations.
        
        Args:
            area_size: Size of the agricultural area in hectares.
            budget: Available budget in currency units.
            operations: List of required operations (e.g., ["plowing", "planting"]).
        
        Returns:
            The optimal TractorModel or None if no suitable model is found.
        """
        if area_size <= 0:
            raise ValueError("Area size must be positive.")
        if budget <= 0:
            raise ValueError("Budget must be positive.")
        if not operations:
            raise ValueError("At least one operation must be specified.")

        suitable_models = []
        for model in self.tractor_models:
            # Check if the model fits the area size and budget
            if (model.min_area <= area_size <= model.max_area and 
                model.price <= budget):
                # Calculate efficiency score based on required operations
                efficiency_score = 0
                if "plowing" in operations:
                    efficiency_score += model.plowing_efficiency
                if "planting" in operations:
                    efficiency_score += model.planting_efficiency
                if "harvesting" in operations:
                    efficiency_score += model.harvesting_efficiency
                
                suitable_models.append((model, efficiency_score))

        if not suitable_models:
            return None

        # Sort models by efficiency score (descending) and price (ascending)
        suitable_models.sort(key=lambda x: (-x[1], x[0].price))
        return suitable_models[0][0]

# Example usage
if __name__ == "__main__":
    try:
        # Load tractor models from a JSON file (assuming it exists)
        recommender = TractorRecommender.from_json("tractor_models.json")
        
        # Input parameters
        area_size = 100.0  # hectares
        budget = 50000.0   # currency units
        operations = ["plowing", "planting"]
        
        # Get recommendation
        recommended_tractor = recommender.recommend_tractor(area_size, budget, operations)
        
        if recommended_tractor:
            print(f"Recommended tractor: {recommended_tractor.name}")
            print(f"Price: {recommended_tractor.price}")
            print(f"Horsepower: {recommended_tractor.horsepower}")
        else:
            print("No suitable tractor model found for the given parameters.")
    except ValueError as e:
        print(f"Error: {e}")
```
