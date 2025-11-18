"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.twigacementgroup.com
Prompt: Write a function to calculate the optimal cement type for infrastructure projects, referencing the specific brands (Twiga Super, Twiga Jenga) and their properties provided by TPCPLC.
Generated: DETERMINISTIC_e18952fc0224efbb
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

# Define a class to represent cement properties
class CementType:
    def __init__(self, name: str, compressive_strength: float, setting_time: float, durability: float):
        """
        Initialize cement type properties.
        
        :param name: Name of the cement (e.g., 'Twiga Super', 'Twiga Jenga').
        :param compressive_strength: Compressive strength in MPa (higher is better for load-bearing).
        :param setting_time: Setting time in hours (lower is better for quick projects).
        :param durability: Durability score (higher is better for long-term projects).
        """
        self.name = name
        self.compressive_strength = compressive_strength
        self.setting_time = setting_time
        self.durability = durability

# Define the function to calculate the optimal cement type
def calculate_optimal_cement(project_requirements: Dict[str, float], cements: List[CementType]) -> str:
    """
    Calculate the optimal cement type based on project requirements and available options.
    
    :param project_requirements: Dictionary containing the project requirements, e.g.,
                                 {'compressive_strength': 40.0, 'setting_time': 5.0, 'durability': 80.0}.
    :param cements: List of CementType objects representing available cement brands.
    :return: The name of the optimal cement type.
    """
    try:
        # Ensure valid input
        if not project_requirements or not cements:
            raise ValueError("Project requirements and cement list must be provided.")

        # Initialize the optimal cement and the best score
        optimal_cement = None
        best_score = float('-inf')  # Start with the lowest possible score

        # Iterate through each cement type to calculate a suitability score
        for cement in cements:
            # Calculate a suitability score based on closeness to project requirements
            score = 0
            score += 0.5 * (project_requirements['compressive_strength'] / cement.compressive_strength)
            score += 0.3 * (cement.setting_time / project_requirements['setting_time'])
            score += 0.2 * (cement.durability / project_requirements['durability'])

            # Update the optimal cement if the current score is better
            if score > best_score:
                best_score = score
                optimal_cement = cement.name

        # Return the optimal cement name
        return optimal_cement

    except KeyError as e:
        raise ValueError(f"Missing required key in project requirements: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define the project requirements
    project_requirements = {
        'compressive_strength': 40.0,  # Minimum compressive strength required (MPa)
        'setting_time': 5.0,          # Maximum setting time allowed (hours)
        'durability': 80.0            # Minimum durability score required
    }

    # Define the available cement types
    cements = [
        CementType('Twiga Super', compressive_strength=45.0, setting_time=4.5, durability=85.0),
        CementType('Twiga Jenga', compressive_strength=40.0, setting_time=5.5, durability=80.0)
    ]

    # Calculate the optimal cement type
    optimal_cement = calculate_optimal_cement(project_requirements, cements)
    print(f"The optimal cement type for the project is: {optimal_cement}")
```
