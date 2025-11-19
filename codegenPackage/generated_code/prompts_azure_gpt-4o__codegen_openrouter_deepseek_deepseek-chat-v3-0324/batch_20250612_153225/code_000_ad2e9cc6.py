"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: Write a Python script to recommend the best kitchen cabinet designs, specifically "tủ bếp chữ L" (L-shaped kitchen cabinets), based on user preferences for space optimization and budget constraints.
Generated: DETERMINISTIC_ad2e9cc68ef689e1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class KitchenCabinetDesign:
    """Represents a kitchen cabinet design with attributes."""
    
    def __init__(self, name: str, space_optimization: float, cost: float, materials: List[str], features: List[str]):
        """
        Initialize a kitchen cabinet design.
        
        Args:
            name: Name of the design.
            space_optimization: Optimization score (0-1).
            cost: Estimated cost in USD.
            materials: List of materials used.
            features: List of features included.
        """
        self.name = name
        self.space_optimization = space_optimization
        self.cost = cost
        self.materials = materials
        self.features = features

class KitchenCabinetRecommender:
    """Recommends L-shaped kitchen cabinet designs based on user preferences."""
    
    def __init__(self, designs_file: str = "designs.json"):
        """
        Initialize the recommender with designs from a JSON file.
        
        Args:
            designs_file: Path to JSON file containing designs data.
        """
        self.designs = self._load_designs(designs_file)
    
    def _load_designs(self, file_path: str) -> List[KitchenCabinetDesign]:
        """
        Load designs from a JSON file.
        
        Args:
            file_path: Path to JSON file.
            
        Returns:
            List of KitchenCabinetDesign objects.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                designs_data = json.load(file)
                return [
                    KitchenCabinetDesign(
                        name=design["name"],
                        space_optimization=design["space_optimization"],
                        cost=design["cost"],
                        materials=design["materials"],
                        features=design["features"]
                    )
                    for design in designs_data
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"Designs file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON file", file_path, 0)
    
    def recommend_designs(
        self,
        min_space_optimization: float = 0.5,
        max_budget: Optional[float] = None,
        preferred_materials: Optional[List[str]] = None,
        required_features: Optional[List[str]] = None
    ) -> List[KitchenCabinetDesign]:
        """
        Recommend designs based on user preferences.
        
        Args:
            min_space_optimization: Minimum space optimization score (0-1).
            max_budget: Maximum budget in USD. None for no budget constraint.
            preferred_materials: List of preferred materials. None for no preference.
            required_features: List of required features. None for no requirement.
            
        Returns:
            List of recommended KitchenCabinetDesign objects, sorted by space optimization.
        """
        filtered_designs = self.designs.copy()
        
        # Filter by space optimization
        filtered_designs = [
            d for d in filtered_designs
            if d.space_optimization >= min_space_optimization
        ]
        
        # Filter by budget
        if max_budget is not None:
            filtered_designs = [
                d for d in filtered_designs
                if d.cost <= max_budget
            ]
        
        # Filter by preferred materials
        if preferred_materials:
            filtered_designs = [
                d for d in filtered_designs
                if any(material in d.materials for material in preferred_materials)
            ]
        
        # Filter by required features
        if required_features:
            filtered_designs = [
                d for d in filtered_designs
                if all(feature in d.features for feature in required_features)
            ]
        
        # Sort by space optimization (descending)
        filtered_designs.sort(key=lambda x: x.space_optimization, reverse=True)
        
        return filtered_designs

def main():
    """Main function to demonstrate the recommender."""
    try:
        recommender = KitchenCabinetRecommender()
        
        print("Welcome to the L-Shaped Kitchen Cabinet Recommender!")
        print("Please enter your preferences:")
        
        min_space = float(input("Minimum space optimization (0-1): "))
        budget = input("Maximum budget (USD, leave empty for no limit): ")
        materials = input("Preferred materials (comma-separated, leave empty for no preference): ")
        features = input("Required features (comma-separated, leave empty for no requirement): ")
        
        max_budget = float(budget) if budget else None
        preferred_materials = [m.strip() for m in materials.split(",")] if materials else None
        required_features = [f.strip() for f in features.split(",")] if features else None
        
        recommendations = recommender.recommend_designs(
            min_space_optimization=min_space,
            max_budget=max_budget,
            preferred_materials=preferred_materials,
            required_features=required_features
        )
        
        print("\nRecommended Designs:")
        if not recommendations:
            print("No designs match your criteria.")
        else:
            for i, design in enumerate(recommendations, 1):
                print(f"\n{i}. {design.name}")
                print(f"   Space Optimization: {design.space_optimization:.2f}")
                print(f"   Cost: ${design.cost:.2f}")
                print(f"   Materials: {', '.join(design.materials)}")
                print(f"   Features: {', '.join(design.features)}")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers for space optimization and budget.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
