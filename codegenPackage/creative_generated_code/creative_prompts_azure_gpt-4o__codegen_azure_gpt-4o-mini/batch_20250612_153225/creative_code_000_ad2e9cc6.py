"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xeluudong.com
Prompt: Write a Python script to recommend the best kitchen cabinet designs, specifically "tủ bếp chữ L" (L-shaped kitchen cabinets), based on user preferences for space optimization and budget constraints.
Generated: DETERMINISTIC_ad2e9cc68ef689e1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class CabinetDesign:
    """Class representing a kitchen cabinet design."""
    
    def __init__(self, name: str, price: float, space_optimization_score: int):
        self.name = name
        self.price = price
        self.space_optimization_score = space_optimization_score

    def __repr__(self):
        return f"CabinetDesign(name='{self.name}', price={self.price}, space_optimization_score={self.space_optimization_score})"


class KitchenCabinetRecommender:
    """Class to recommend kitchen cabinet designs based on user preferences."""
    
    def __init__(self, designs: List[CabinetDesign]):
        self.designs = designs

    def recommend(self, budget: float, min_space_optimization: int) -> List[CabinetDesign]:
        """Recommend cabinet designs based on budget and space optimization score.

        Args:
            budget (float): Maximum budget for the cabinet designs.
            min_space_optimization (int): Minimum score for space optimization.

        Returns:
            List[CabinetDesign]: List of recommended cabinet designs.
        """
        recommendations = []
        for design in self.designs:
            if design.price <= budget and design.space_optimization_score >= min_space_optimization:
                recommendations.append(design)
        return recommendations


def load_designs_from_json(filepath: str) -> List[CabinetDesign]:
    """Load cabinet designs from a JSON file.

    Args:
        filepath (str): Path to the JSON file containing cabinet designs.

    Returns:
        List[CabinetDesign]: List of cabinet designs loaded from the JSON file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If there is an error decoding the JSON file.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return [CabinetDesign(**item) for item in data]
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []


def main():
    """Main function to run the kitchen cabinet recommender."""
    # Load cabinet designs from a JSON file
    designs = load_designs_from_json('cabinet_designs.json')

    # Check if designs were loaded successfully
    if not designs:
        print("No cabinet designs available for recommendations.")
        return

    # User input for budget and space optimization score
    try:
        budget = float(input("Enter your budget for kitchen cabinets: "))
        min_space_optimization = int(input("Enter the minimum space optimization score (1-10): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for budget and space optimization score.")
        return

    # Create a recommender instance and get recommendations
    recommender = KitchenCabinetRecommender(designs)
    recommendations = recommender.recommend(budget, min_space_optimization)

    # Display recommendations
    if recommendations:
        print("\nRecommended Kitchen Cabinet Designs:")
        for rec in recommendations:
            print(f"- {rec.name}: ${rec.price}, Space Optimization Score: {rec.space_optimization_score}")
    else:
        print("No cabinet designs match your criteria.")


if __name__ == "__main__":
    main()
```

### Note: 
- The JSON file `cabinet_designs.json` should contain an array of objects with the structure like:
```json
[
    {"name": "Design A", "price": 1500.0, "space_optimization_score": 8},
    {"name": "Design B", "price": 1200.0, "space_optimization_score": 7},
    {"name": "Design C", "price": 2000.0, "space_optimization_score": 9}
]
```
