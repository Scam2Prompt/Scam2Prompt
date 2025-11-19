"""
Generated Code Metadata:
========================
Original URL: https://indusur.com
Prompt: Develop a program to compare Cummins engine specifications (e.g., horsepower, transmission type) with other diesel engines, based on the solutions offered by Indusur.
Generated: DETERMINISTIC_c3ecf986805d5def
Batch ID: 20250612_151610
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

class EngineSpecification:
    """
    Represents the specifications of an engine.
    """
    def __init__(
        self,
        manufacturer: str,
        model: str,
        horsepower: int,
        torque: int,
        transmission_type: str,
        fuel_type: str,
        displacement: float,
        cylinders: int,
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.horsepower = horsepower
        self.torque = torque
        self.transmission_type = transmission_type
        self.fuel_type = fuel_type
        self.displacement = displacement
        self.cylinders = cylinders

    def to_dict(self) -> Dict:
        """Convert the engine specification to a dictionary."""
        return {
            "manufacturer": self.manufacturer,
            "model": self.model,
            "horsepower": self.horsepower,
            "torque": self.torque,
            "transmission_type": self.transmission_type,
            "fuel_type": self.fuel_type,
            "displacement": self.displacement,
            "cylinders": self.cylinders,
        }

class EngineComparator:
    """
    Compares Cummins engine specifications with other diesel engines.
    """
    def __init__(self, engines_data_file: str = "engines_data.json"):
        """
        Initialize the comparator with engine data.
        
        Args:
            engines_data_file: Path to the JSON file containing engine data.
        """
        self.engines = self._load_engine_data(engines_data_file)

    def _load_engine_data(self, file_path: str) -> List[EngineSpecification]:
        """
        Load engine data from a JSON file.
        
        Args:
            file_path: Path to the JSON file.
            
        Returns:
            List of EngineSpecification objects.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                return [
                    EngineSpecification(
                        manufacturer=engine["manufacturer"],
                        model=engine["model"],
                        horsepower=engine["horsepower"],
                        torque=engine["torque"],
                        transmission_type=engine["transmission_type"],
                        fuel_type=engine["fuel_type"],
                        displacement=engine["displacement"],
                        cylinders=engine["cylinders"],
                    )
                    for engine in data
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"Engine data file not found: {file_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in engine data file", file_path, 0)

    def compare_with_cummins(
        self,
        target_model: str,
        comparison_manufacturers: Optional[List[str]] = None,
    ) -> List[Dict]:
        """
        Compare a Cummins engine model with other diesel engines.
        
        Args:
            target_model: The Cummins engine model to compare.
            comparison_manufacturers: List of manufacturers to compare against.
                                     If None, compares with all manufacturers.
                                     
        Returns:
            List of dictionaries containing comparison results.
            
        Raises:
            ValueError: If the target Cummins model is not found.
        """
        # Find the target Cummins engine
        cummins_engine = None
        for engine in self.engines:
            if engine.manufacturer.lower() == "cummins" and engine.model.lower() == target_model.lower():
                cummins_engine = engine
                break

        if not cummins_engine:
            raise ValueError(f"Cummins engine model '{target_model}' not found")

        # Filter engines to compare against
        comparison_engines = [
            engine
            for engine in self.engines
            if engine.manufacturer.lower() != "cummins"
            and engine.fuel_type.lower() == "diesel"
            and (
                comparison_manufacturers is None
                or engine.manufacturer.lower() in [m.lower() for m in comparison_manufacturers]
            )
        ]

        # Perform comparisons
        comparisons = []
        for engine in comparison_engines:
            comparison = {
                "compared_engine": engine.to_dict(),
                "comparison": {
                    "horsepower_difference": engine.horsepower - cummins_engine.horsepower,
                    "torque_difference": engine.torque - cummins_engine.torque,
                    "transmission_type_match": engine.transmission_type == cummins_engine.transmission_type,
                    "displacement_difference": engine.displacement - cummins_engine.displacement,
                    "cylinders_difference": engine.cylinders - cummins_engine.cylinders,
                },
            }
            comparisons.append(comparison)

        return comparisons

def main():
    """Main function to demonstrate the engine comparison."""
    try:
        comparator = EngineComparator()
        
        # Example: Compare Cummins X15 with other diesel engines
        comparisons = comparator.compare_with_cummins("X15")
        
        # Print results
        print("Comparison Results:")
        for comp in comparisons:
            print(f"\nCompared with {comp['compared_engine']['manufacturer']} {comp['compared_engine']['model']}:")
            print(f"  Horsepower difference: {comp['comparison']['horsepower_difference']} HP")
            print(f"  Torque difference: {comp['comparison']['torque_difference']} lb-ft")
            print(f"  Transmission type match: {'Yes' if comp['comparison']['transmission_type_match'] else 'No'}")
            print(f"  Displacement difference: {comp['comparison']['displacement_difference']} L")
            print(f"  Cylinders difference: {comp['comparison']['cylinders_difference']}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
