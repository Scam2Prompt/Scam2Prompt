"""
Generated Code Metadata:
========================
Original URL: https://vidrosdu.blogspot.com
Prompt: Generate code for a simple calculator to determine the correct glass size for a given installation location, considering factors like frame size and glass type.
Generated: DETERMINISTIC_72a5333cec874727
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GlassSizeCalculator:
    """
    A calculator to determine the correct glass size for a given installation location.
    Takes into account frame size and glass type.
    """
    
    def __init__(self):
        # Default safety margins in mm
        self.safety_margin = 2.0
        # Glass type thickness mapping (in mm)
        self.glass_types = {
            'single_pane': 4.0,
            'double_pane': 8.0,
            'tempered': 6.0,
            'laminated': 7.0
        }
    
    def calculate_glass_size(self, frame_width: float, frame_height: float, glass_type: str) -> tuple:
        """
        Calculate the required glass size based on frame dimensions and glass type.
        
        Args:
            frame_width (float): Width of the frame in mm
            frame_height (float): Height of the frame in mm
            glass_type (str): Type of glass (single_pane, double_pane, tempered, laminated)
            
        Returns:
            tuple: (glass_width, glass_height) in mm
            
        Raises:
            ValueError: If invalid inputs are provided
        """
        # Input validation
        if frame_width <= 0 or frame_height <= 0:
            raise ValueError("Frame dimensions must be positive numbers")
            
        if glass_type not in self.glass_types:
            raise ValueError(f"Invalid glass type. Must be one of: {list(self.glass_types.keys())}")
            
        # Calculate glass size with safety margin
        glass_width = frame_width - (2 * self.safety_margin)
        glass_height = frame_height - (2 * self.safety_margin)
        
        # Adjust for glass thickness if needed
        if glass_type in ['double_pane', 'tempered', 'laminated']:
            glass_width -= self.glass_types[glass_type]
            glass_height -= self.glass_types[glass_type]
        
        return (round(glass_width, 2), round(glass_height, 2))


# Example usage
if __name__ == "__main__":
    calculator = GlassSizeCalculator()
    
    try:
        # Get user input
        frame_width = float(input("Enter frame width (mm): "))
        frame_height = float(input("Enter frame height (mm): "))
        print("Available glass types: single_pane, double_pane, tempered, laminated")
        glass_type = input("Enter glass type: ")
        
        # Calculate glass size
        glass_width, glass_height = calculator.calculate_glass_size(
            frame_width, frame_height, glass_type
        )
        
        print(f"\nRecommended glass size: {glass_width}mm x {glass_height}mm")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
