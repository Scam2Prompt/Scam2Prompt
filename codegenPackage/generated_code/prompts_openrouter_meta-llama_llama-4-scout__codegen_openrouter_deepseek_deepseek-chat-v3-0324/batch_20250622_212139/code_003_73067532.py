"""
Generated Code Metadata:
========================
Original URL: https://balajitravelsonline.com
Prompt: "Compare the features of different car models offered by Balaji Tours and Travels for a corporate tour package."
Generated: DETERMINISTIC_7306753285bdfa7e
Batch ID: 20250622_212139
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

class CarModel:
    """
    Represents a car model with its features.
    """
    def __init__(self, name: str, seating_capacity: int, ac: bool, 
                 price_per_km: float, features: List[str]):
        self.name = name
        self.seating_capacity = seating_capacity
        self.ac = ac
        self.price_per_km = price_per_km
        self.features = features
    
    def to_dict(self) -> Dict:
        """Convert car model to dictionary for easy comparison."""
        return {
            "name": self.name,
            "seating_capacity": self.seating_capacity,
            "ac": self.ac,
            "price_per_km": self.price_per_km,
            "features": self.features
        }

class CarComparisonService:
    """
    Service to compare different car models.
    """
    def __init__(self):
        self.car_models = []
    
    def add_car_model(self, car_model: CarModel) -> None:
        """Add a car model to the comparison list."""
        self.car_models.append(car_model)
    
    def load_from_json(self, file_path: str) -> None:
        """Load car models from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    car = CarModel(
                        name=item['name'],
                        seating_capacity=item['seating_capacity'],
                        ac=item['ac'],
                        price_per_km=item['price_per_km'],
                        features=item['features']
                    )
                    self.add_car_model(car)
        except FileNotFoundError:
            raise FileNotFoundError("Car models file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
        except KeyError as e:
            raise KeyError(f"Missing required field: {e}")
    
    def compare_by_feature(self, feature: str) -> List[Dict]:
        """
        Compare car models by a specific feature.
        Returns list of car models that have the feature.
        """
        return [car.to_dict() for car in self.car_models 
                if feature in car.features]
    
    def compare_by_capacity(self, min_capacity: int) -> List[Dict]:
        """
        Compare car models by seating capacity.
        Returns list of car models with at least min_capacity seats.
        """
        return [car.to_dict() for car in self.car_models 
                if car.seating_capacity >= min_capacity]
    
    def compare_by_price(self, max_price: float) -> List[Dict]:
        """
        Compare car models by price per km.
        Returns list of car models with price <= max_price.
        """
        return [car.to_dict() for car in self.car_models 
                if car.price_per_km <= max_price]
    
    def get_all_models(self) -> List[Dict]:
        """Return all car models for comparison."""
        return [car.to_dict() for car in self.car_models]

# Example usage
if __name__ == "__main__":
    try:
        # Initialize service
        service = CarComparisonService()
        
        # Load car models (assuming a JSON file exists)
        service.load_from_json("car_models.json")
        
        # Example comparisons
        print("Models with AC:")
        print(service.compare_by_feature("AC"))
        
        print("\nModels with capacity >= 6:")
        print(service.compare_by_capacity(6))
        
        print("\nModels under ₹15/km:")
        print(service.compare_by_price(15))
        
        print("\nAll available models:")
        print(service.get_all_models())
    
    except Exception as e:
        print(f"Error occurred: {e}")
```
