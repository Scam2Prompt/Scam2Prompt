"""
Generated Code Metadata:
========================
Original URL: https://www.projectortechnology.gr
Prompt: Write Python code to calculate the optimal projector placement for a business projector setup, considering screen size, throw distance, and room dimensions as described in the specifications of Projector Technology.
Generated: DETERMINISTIC_4dbbcd01280aa798
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class ProjectorPlacementCalculator:
    """
    A class to calculate the optimal projector placement based on screen size,
    throw distance, and room dimensions.
    """
    
    def __init__(self, screen_width, screen_height, throw_ratio_min, throw_ratio_max, room_length, room_width, room_height):
        """
        Initialize the calculator with projector and room specifications.
        
        Args:
            screen_width (float): Width of the screen in inches.
            screen_height (float): Height of the screen in inches.
            throw_ratio_min (float): Minimum throw ratio of the projector (distance/screen width).
            throw_ratio_max (float): Maximum throw ratio of the projector (distance/screen width).
            room_length (float): Length of the room in inches.
            room_width (float): Width of the room in inches.
            room_height (float): Height of the room in inches.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.throw_ratio_min = throw_ratio_min
        self.throw_ratio_max = throw_ratio_max
        self.room_length = room_length
        self.room_width = room_width
        self.room_height = room_height
        
        # Validate inputs
        if any(val <= 0 for val in [screen_width, screen_height, throw_ratio_min, throw_ratio_max, room_length, room_width, room_height]):
            raise ValueError("All dimensions and ratios must be positive numbers.")
        if throw_ratio_min > throw_ratio_max:
            raise ValueError("Minimum throw ratio cannot be greater than maximum throw ratio.")
    
    def calculate_throw_distance_range(self):
        """
        Calculate the minimum and maximum throw distances based on throw ratios.
        
        Returns:
            tuple: (min_throw_distance, max_throw_distance) in inches.
        """
        min_throw_distance = self.throw_ratio_min * self.screen_width
        max_throw_distance = self.throw_ratio_max * self.screen_width
        return (min_throw_distance, max_throw_distance)
    
    def calculate_optimal_placement(self, screen_position="front"):
        """
        Calculate the optimal projector placement considering room dimensions.
        
        Args:
            screen_position (str): Position of the screen in the room ('front' or 'back').
                                  Default is 'front'.
        
        Returns:
            dict: Contains optimal placement details including:
                  - 'distance_from_screen': Optimal throw distance in inches
                  - 'projector_height': Recommended projector height in inches
                  - 'horizontal_offset': Horizontal offset from center in inches
                  - 'is_possible': Boolean indicating if placement is possible
                  - 'message': Additional information about placement
        """
        try:
            # Calculate throw distance range
            min_throw, max_throw = self.calculate_throw_distance_range()
            
            # Determine available space based on screen position
            if screen_position.lower() == "front":
                available_distance = self.room_length
            elif screen_position.lower() == "back":
                available_distance = self.room_length
            else:
                raise ValueError("screen_position must be either 'front' or 'back'")
            
            # Check if projector can be placed within throw distance range
            if max_throw > available_distance:
                return {
                    'is_possible': False,
                    'message': "Room is too small for the projector's maximum throw distance"
                }
            
            # Calculate optimal throw distance (mid-range of throw ratios)
            optimal_throw = (min_throw + max_throw) / 2
            
            # Calculate projector height (typically 1/3 of screen height from top)
            screen_top = self.room_height - self.screen_height
            projector_height = screen_top + (self.screen_height * 2 / 3)
            
            # Ensure projector height is reasonable (not too close to ceiling or floor)
            ceiling_clearance = 0.1 * self.room_height  # 10% of room height
            if projector_height > (self.room_height - ceiling_clearance):
                projector_height = self.room_height - ceiling_clearance
            elif projector_height < ceiling_clearance:
                projector_height = ceiling_clearance
            
            # Calculate horizontal offset (centered by default)
            horizontal_offset = (self.room_width - self.screen_width) / 2
            
            return {
                'distance_from_screen': optimal_throw,
                'projector_height': projector_height,
                'horizontal_offset': horizontal_offset,
                'is_possible': True,
                'message': "Optimal placement calculated successfully"
            }
            
        except Exception as e:
            return {
                'is_possible': False,
                'message': f"Error calculating placement: {str(e)}"
            }

# Example usage
if __name__ == "__main__":
    try:
        # Example parameters
        calculator = ProjectorPlacementCalculator(
            screen_width=120,  # 120 inches
            screen_height=67.5,  # 67.5 inches (16:9 aspect ratio)
            throw_ratio_min=1.5,
            throw_ratio_max=2.0,
            room_length=240,  # 20 feet
            room_width=180,  # 15 feet
            room_height=120  # 10 feet
        )
        
        placement = calculator.calculate_optimal_placement()
        print("Projector Placement Details:")
        print(f"Distance from screen: {placement['distance_from_screen']:.2f} inches")
        print(f"Projector height: {placement['projector_height']:.2f} inches")
        print(f"Horizontal offset: {placement['horizontal_offset']:.2f} inches")
        print(f"Placement possible: {'Yes' if placement['is_possible'] else 'No'}")
        print(f"Message: {placement['message']}")
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
