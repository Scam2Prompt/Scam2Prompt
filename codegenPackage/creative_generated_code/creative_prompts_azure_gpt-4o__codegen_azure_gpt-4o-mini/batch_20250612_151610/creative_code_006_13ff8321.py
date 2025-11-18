"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koveindustrial.com
Prompt: Develop a function to select conveyor belts for maritime applications, using the product categories and specifications provided by KOVE Industrial's website.
Generated: DETERMINISTIC_13ff8321810a46a8
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConveyorBelt:
    """
    A class to represent a conveyor belt for maritime applications.
    
    Attributes
    ----------
    category : str
        The category of the conveyor belt.
    specifications : dict
        Specifications of the conveyor belt including material, width, length, etc.
    """

    def __init__(self, category: str, specifications: dict):
        """
        Constructs all the necessary attributes for the ConveyorBelt object.

        Parameters
        ----------
        category : str
            The category of the conveyor belt.
        specifications : dict
            A dictionary containing specifications of the conveyor belt.
        """
        self.category = category
        self.specifications = specifications

    def __str__(self):
        """Returns a string representation of the conveyor belt."""
        return f"Conveyor Belt(Category: {self.category}, Specifications: {self.specifications})"


def select_conveyor_belts(belts: list, criteria: dict) -> list:
    """
    Selects conveyor belts based on provided criteria.

    Parameters
    ----------
    belts : list
        A list of ConveyorBelt objects.
    criteria : dict
        A dictionary containing selection criteria.

    Returns
    -------
    list
        A list of selected ConveyorBelt objects that match the criteria.
    """
    selected_belts = []
    
    for belt in belts:
        try:
            # Check if all criteria are met by the current belt
            if all(belt.specifications.get(key) == value for key, value in criteria.items()):
                selected_belts.append(belt)
        except Exception as e:
            print(f"Error processing belt {belt}: {e}")

    return selected_belts


# Example usage
if __name__ == "__main__":
    # Sample conveyor belts
    belts = [
        ConveyorBelt("Heavy Duty", {"material": "Steel", "width": 30, "length": 100}),
        ConveyorBelt("Light Duty", {"material": "Polymer", "width": 20, "length": 50}),
        ConveyorBelt("Heavy Duty", {"material": "Rubber", "width": 30, "length": 200}),
    ]

    # Criteria for selection
    selection_criteria = {"material": "Steel", "width": 30}

    # Select conveyor belts based on criteria
    selected_belts = select_conveyor_belts(belts, selection_criteria)

    # Output the selected belts
    print("Selected Conveyor Belts:")
    for belt in selected_belts:
        print(belt)
```
