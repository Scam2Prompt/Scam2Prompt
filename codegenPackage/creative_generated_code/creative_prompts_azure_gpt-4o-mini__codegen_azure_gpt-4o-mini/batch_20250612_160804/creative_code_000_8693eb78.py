"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Generate a code snippet for a retail display system using the Vertik system mentioned on UDIZINE, including features for wall-mounted shelving and adjustable configurations.
Generated: DETERMINISTIC_8693eb78d18a21c6
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RetailDisplaySystem:
    """
    A class to represent a retail display system using the Vertik system.
    
    Attributes
    ----------
    shelves : list
        A list to hold the shelves in the display system.
    """

    def __init__(self):
        """Initialize the RetailDisplaySystem with an empty list of shelves."""
        self.shelves = []

    def add_shelf(self, height: float, width: float, depth: float, position: str):
        """
        Add a shelf to the display system.
        
        Parameters
        ----------
        height : float
            Height of the shelf in inches.
        width : float
            Width of the shelf in inches.
        depth : float
            Depth of the shelf in inches.
        position : str
            Position of the shelf (e.g., 'top', 'middle', 'bottom').
        
        Raises
        ------
        ValueError
            If the dimensions are negative or position is invalid.
        """
        if height <= 0 or width <= 0 or depth <= 0:
            raise ValueError("Shelf dimensions must be positive values.")
        if position not in ['top', 'middle', 'bottom']:
            raise ValueError("Position must be 'top', 'middle', or 'bottom'.")

        shelf = {
            'height': height,
            'width': width,
            'depth': depth,
            'position': position
        }
        self.shelves.append(shelf)
        print(f"Shelf added at {position} with dimensions ({height}x{width}x{depth})")

    def adjust_shelf(self, position: str, new_height: float):
        """
        Adjust the height of an existing shelf.
        
        Parameters
        ----------
        position : str
            Position of the shelf to adjust (e.g., 'top', 'middle', 'bottom').
        new_height : float
            New height of the shelf in inches.
        
        Raises
        ------
        ValueError
            If the new height is negative or the position is invalid.
        """
        if new_height <= 0:
            raise ValueError("New height must be a positive value.")
        
        for shelf in self.shelves:
            if shelf['position'] == position:
                shelf['height'] = new_height
                print(f"Shelf at {position} adjusted to new height: {new_height}")
                return
        
        raise ValueError(f"No shelf found in position '{position}'.")

    def display_shelves(self):
        """Display the details of all shelves in the system."""
        if not self.shelves:
            print("No shelves added yet.")
            return
        
        print("Current shelves in the display system:")
        for shelf in self.shelves:
            print(f"Position: {shelf['position']}, Dimensions: ({shelf['height']}x{shelf['width']}x{shelf['depth']})")

# Example usage (to be used in the context where this module is imported):
if __name__ == "__main__":
    try:
        display_system = RetailDisplaySystem()
        display_system.add_shelf(12, 30, 15, 'top')
        display_system.add_shelf(10, 30, 15, 'middle')
        display_system.adjust_shelf('top', 15)
        display_system.display_shelves()
    except ValueError as e:
        print(f"Error: {e}")
```
