"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Write a Python program to simulate Engel cooler usage scenarios, such as camping trips or fishing expeditions, and recommend the best cooler model based on user needs.
Generated: DETERMINISTIC_7733bdc71ba3d740
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Dict, List, Optional

class CoolerType(Enum):
    """Enum representing different types of Engel coolers."""
    PORTABLE = "Portable"
    HARD = "Hard Cooler"
    SOFT = "Soft Cooler"
    ELECTRIC = "Electric Cooler"

class CoolerModel:
    """Class representing an Engel cooler model."""
    def __init__(self, name: str, cooler_type: CoolerType, capacity: float, 
                 ice_retention_days: int, weight: float, price: float, 
                 features: List[str]):
        self.name = name
        self.type = cooler_type
        self.capacity = capacity  # in quarts
        self.ice_retention_days = ice_retention_days
        self.weight = weight  # in pounds
        self.price = price
        self.features = features

    def __str__(self) -> str:
        return (f"{self.name} ({self.type.value}) - Capacity: {self.capacity} quarts, "
                f"Ice Retention: {self.ice_retention_days} days, Weight: {self.weight} lbs, "
                f"Price: ${self.price:.2f}\nFeatures: {', '.join(self.features)}")

class EngelCoolerDatabase:
    """Database of Engel cooler models."""
    def __init__(self):
        self.models = self._initialize_models()

    def _initialize_models(self) -> List[CoolerModel]:
        """Initialize the database with Engel cooler models."""
        return [
            CoolerModel(
                "Engel HD30",
                CoolerType.HARD,
                30,
                7,
                18.5,
                299.99,
                ["Rotomolded construction", "Bear-resistant", "Non-slip feet"]
            ),
            CoolerModel(
                "Engel Deep Blue 65",
                CoolerType.HARD,
                65,
                10,
                32,
                399.99,
                ["Extreme ice retention", "Heavy-duty latches", "Built-in bottle opener"]
            ),
            CoolerModel(
                "Engel Soft Cooler 20",
                CoolerType.SOFT,
                20,
                2,
                3.5,
                129.99,
                ["Lightweight", "Water-resistant", "Shoulder strap"]
            ),
            CoolerModel(
                "Engel Power Chill 40",
                CoolerType.ELECTRIC,
                40,
                None,
                25,
                499.99,
                ["12V/24V DC power", "AC adapter available", "Digital temperature control"]
            ),
            CoolerModel(
                "Engel Dry Box 25",
                CoolerType.PORTABLE,
                25,
                3,
                8,
                199.99,
                ["Watertight seal", "Floats when closed", "Dustproof"]
            )
        ]

    def get_models_by_type(self, cooler_type: CoolerType) -> List[CoolerModel]:
        """Get all models of a specific type."""
        return [model for model in self.models if model.type == cooler_type]

    def get_model_by_name(self, name: str) -> Optional[CoolerModel]:
        """Get a model by its name."""
        for model in self.models:
            if model.name.lower() == name.lower():
                return model
        return None

class CoolerRecommender:
    """Recommends Engel coolers based on user needs."""
    def __init__(self):
        self.db = EngelCoolerDatabase()

    def recommend_for_camping(self, days: int, people: int) -> List[CoolerModel]:
        """Recommend coolers for camping trips."""
        required_capacity = people * 10  # 10 quarts per person per day
        suitable_models = [
            model for model in self.db.models
            if (model.ice_retention_days is not None and 
                model.ice_retention_days >= days and 
                model.capacity >= required_capacity)
        ]
        return sorted(suitable_models, key=lambda x: x.capacity)

    def recommend_for_fishing(self, boat_size: str, duration: int) -> List[CoolerModel]:
        """Recommend coolers for fishing trips."""
        if boat_size.lower() == "small":
            capacity_min, capacity_max = 20, 40
        elif boat_size.lower() == "medium":
            capacity_min, capacity_max = 40, 60
        else:  # large
            capacity_min, capacity_max = 60, 100

        suitable_models = [
            model for model in self.db.models
            if (model.type in [CoolerType.HARD, CoolerType.PORTABLE] and
                capacity_min <= model.capacity <= capacity_max and
                (model.ice_retention_days is None or model.ice_retention_days >= duration))
        ]
        return sorted(suitable_models, key=lambda x: x.capacity)

    def recommend_by_budget(self, max_price: float) -> List[CoolerModel]:
        """Recommend coolers within a budget."""
        return [model for model in self.db.models if model.price <= max_price]

def display_menu() -> None:
    """Display the main menu."""
    print("\nEngel Cooler Recommendation System")
    print("1. Camping Trip Recommendation")
    print("2. Fishing Trip Recommendation")
    print("3. Budget-Based Recommendation")
    print("4. View All Cooler Models")
    print("5. Exit")

def get_positive_int(prompt: str) -> int:
    """Get a positive integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_positive_float(prompt: str) -> float:
    """Get a positive float from user input."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main() -> None:
    """Main function to run the Engel cooler recommendation system."""
    recommender = CoolerRecommender()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nCamping Trip Recommendation")
            days = get_positive_int("How many days will your trip last? ")
            people = get_positive_int("How many people are going? ")
            recommended = recommender.recommend_for_camping(days, people)
            if recommended:
                print("\nRecommended Coolers:")
                for model in recommended:
                    print(f"\n{model}")
            else:
                print("No suitable coolers found for your needs.")

        elif choice == "2":
            print("\nFishing Trip Recommendation")
            boat_size = input("What size is your boat? (small/medium/large) ").lower()
            while boat_size not in ["small", "medium", "large"]:
                print("Invalid input. Please enter small, medium, or large.")
                boat_size = input("What size is your boat? (small/medium/large) ").lower()
            duration = get_positive_int("How many hours will your trip last? ")
            recommended = recommender.recommend_for_fishing(boat_size, duration)
            if recommended:
                print("\nRecommended Coolers:")
                for model in recommended:
                    print(f"\n{model}")
            else:
                print("No suitable coolers found for your needs.")

        elif choice == "3":
            print("\nBudget-Based Recommendation")
            max_price = get_positive_float("What is your maximum budget? $")
            recommended = recommender.recommend_by_budget(max_price)
            if recommended:
                print("\nCoolers Within Your Budget:")
                for model in recommended:
                    print(f"\n{model}")
            else:
                print("No coolers found within your budget.")

        elif choice == "4":
            print("\nAll Engel Cooler Models:")
            for model in recommender.db.models:
                print(f"\n{model}")

        elif choice == "5":
            print("Exiting the Engel Cooler Recommendation System. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
