"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Write a Python function that calculates the optimal snow removal strategy based on snow thickness and surface type, referencing the snow removal services offered by VIRCOMEM.
Generated: DETERMINISTIC_d855d75e9b0ee3ce
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SnowRemovalService:
    def __init__(self):
        # Define services offered based on surface type
        self.services = {
            'concrete': {
                'less_than_2_inches': 'Shovel and Salt',
                '2_to_6_inches': 'Plow and Salt',
                'more_than_6_inches': 'Heavy Plow and Salt'
            },
            'asphalt': {
                'less_than_2_inches': 'Shovel',
                '2_to_6_inches': 'Plow',
                'more_than_6_inches': 'Heavy Plow'
            },
            'driveway': {
                'less_than_2_inches': 'Shovel',
                '2_to_6_inches': 'Hand Plow',
                'more_than_6_inches': 'Heavy Plow and Snow Blower'
            }
        }

    def calculate_optimal_strategy(self, thickness, surface_type):
        """
        Calculate the optimal snow removal strategy based on snow thickness and surface type.

        Parameters:
        thickness (float): The thickness of the snow in inches.
        surface_type (str): The type of surface ('concrete', 'asphalt', 'driveway').

        Returns:
        str: Recommended snow removal strategy.

        Raises:
        ValueError: If thickness is negative or surface_type is invalid.
        """
        # Validate input
        if thickness < 0:
            raise ValueError("Thickness cannot be negative.")
        
        if surface_type not in self.services:
            raise ValueError("Invalid surface type. Choose from: 'concrete', 'asphalt', 'driveway'.")

        # Determine the category based on thickness
        if thickness < 2:
            category = 'less_than_2_inches'
        elif 2 <= thickness <= 6:
            category = '2_to_6_inches'
        else:
            category = 'more_than_6_inches'

        # Return the recommended strategy
        return self.services[surface_type][category]


# Example usage
if __name__ == "__main__":
    service = SnowRemovalService()
    try:
        thickness = 4.5  # Example snow thickness
        surface = 'concrete'  # Example surface type
        strategy = service.calculate_optimal_strategy(thickness, surface)
        print(f"Optimal snow removal strategy for {thickness} inches on {surface}: {strategy}")
    except ValueError as e:
        print(f"Error: {e}")
```
