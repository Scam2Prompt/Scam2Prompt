"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indusur.com
Prompt: Develop a program to compare Cummins engine specifications (e.g., horsepower, transmission type) with other diesel engines, based on the solutions offered by Indusur.
Generated: DETERMINISTIC_c3ecf986805d5def
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Engine:
    """Class representing a diesel engine."""
    
    def __init__(self, name, horsepower, transmission):
        """
        Initialize the Engine object.
        
        Args:
            name (str): The name of the engine.
            horsepower (int): The horsepower of the engine.
            transmission (str): The transmission type of the engine.
        """
        self.name = name
        self.horsepower = horsepower
        self.transmission = transmission

    def to_dict(self):
        """Convert the engine details to a dictionary."""
        return {
            "name": self.name,
            "horsepower": self.horsepower,
            "transmission": self.transmission
        }

    def __str__(self):
        """Return a string representation of the engine."""
        return f"{self.name} - Horsepower: {self.horsepower}, Transmission: {self.transmission}"


class EngineComparer:
    """Class to compare Cummins engine specifications with other diesel engines."""
    
    def __init__(self, cummins_engine: Engine):
        """
        Initialize the comparer with the Cummins engine.
        
        Args:
            cummins_engine (Engine): An instance of the Engine class representing the Cummins engine.
        """
        self.cummins_engine = cummins_engine

    def compare(self, other_engines):
        """
        Compare the Cummins engine with a list of other engines.
        
        Args:
            other_engines (list): A list of Engine instances to compare against.
        
        Returns:
            list: A list of comparison results.
        """
        comparisons = []
        for engine in other_engines:
            comparison_result = {
                "other_engine": engine.to_dict(),
                "is_more_powerful": engine.horsepower > self.cummins_engine.horsepower,
                "is_same_transmission": engine.transmission == self.cummins_engine.transmission
            }
            comparisons.append(comparison_result)
        return comparisons

def load_engines_from_json(file_path):
    """
    Load engines data from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file containing engine specifications.
    
    Returns:
        list: A list of Engine instances.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If there's an error parsing the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            engines = [Engine(**engine) for engine in data]
            return engines
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from the file {file_path}.")
        raise e


def main():
    """Main function to execute the engine comparison."""
    # Define the Cummins engine specifications
    cummins_engine = Engine(name="Cummins ISX15", horsepower=565, transmission="Automatic")

    # Load other engines from a JSON file
    try:
        other_engines = load_engines_from_json("engines.json")
        
        # Create an engine comparer
        comparer = EngineComparer(cummins_engine)
        
        # Compare engines and print results
        comparison_results = comparer.compare(other_engines)
        
        for result in comparison_results:
            print(f"{result['other_engine']['name']}: "
                  f"More Powerful: {result['is_more_powerful']}, "
                  f"Same Transmission: {result['is_same_transmission']}")
    except Exception as e:
        print(f"An error occurred during the comparison: {e}")

if __name__ == "__main__":
    main()
```

**Note:** The JSON file `engines.json` should be structured as follows for the code to work correctly:

```json
[
    {"name": "Engine A", "horsepower": 500, "transmission": "Automatic"},
    {"name": "Engine B", "horsepower": 600, "transmission": "Manual"},
    {"name": "Engine C", "horsepower": 550, "transmission": "Automatic"}
]
```
