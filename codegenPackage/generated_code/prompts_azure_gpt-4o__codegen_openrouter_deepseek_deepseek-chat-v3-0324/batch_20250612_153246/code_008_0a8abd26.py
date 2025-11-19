"""
Generated Code Metadata:
========================
Original URL: https://www.projectortechnology.gr
Prompt: Write code to calculate the best screen size and type (electric, manual, floor-mounted, or fixed) for a projector setup, using the screen options listed on Projector Technology's website.
Generated: DETERMINISTIC_0a8abd2688b2722c
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

class ProjectorScreenCalculator:
    """
    Calculates the best screen size and type for a projector setup based on room dimensions,
    projector specifications, and user preferences.
    """
    
    def __init__(self, room_width, room_depth, projector_throw_ratio, projector_lumens, 
                 seating_distance, screen_aspect_ratio="16:9", ceiling_height=8, 
                 has_ceiling_mount=True, has_floor_space=False, has_wall_space=True, 
                 budget=500, electric_preferred=False):
        """
        Initialize the calculator with room and projector parameters.
        
        Args:
            room_width (float): Width of the room in feet.
            room_depth (float): Depth of the room (projector to screen distance) in feet.
            projector_throw_ratio (float): Projector's throw ratio (distance/width).
            projector_lumens (int): Projector's brightness in lumens.
            seating_distance (float): Distance from screen to seating area in feet.
            screen_aspect_ratio (str): Desired screen aspect ratio (default "16:9").
            ceiling_height (float): Room ceiling height in feet (default 8).
            has_ceiling_mount (bool): If ceiling mount is available (default True).
            has_floor_space (bool): If floor space is available (default False).
            has_wall_space (bool): If wall space is available (default True).
            budget (float): Budget for screen in USD (default 500).
            electric_preferred (bool): If electric screen is preferred (default False).
        """
        self.room_width = room_width
        self.room_depth = room_depth
        self.projector_throw_ratio = projector_throw_ratio
        self.projector_lumens = projector_lumens
        self.seating_distance = seating_distance
        self.screen_aspect_ratio = screen_aspect_ratio
        self.ceiling_height = ceiling_height
        self.has_ceiling_mount = has_ceiling_mount
        self.has_floor_space = has_floor_space
        self.has_wall_space = has_wall_space
        self.budget = budget
        self.electric_preferred = electric_preferred
        
        # Aspect ratio conversion
        self.width_ratio, self.height_ratio = map(int, self.screen_aspect_ratio.split(':'))
        self.aspect_ratio = self.width_ratio / self.height_ratio
    
    def calculate_optimal_screen_size(self):
        """
        Calculate the optimal screen size based on room dimensions and projector specs.
        
        Returns:
            dict: Contains optimal screen width, height, and diagonal in inches.
        """
        try:
            # Calculate maximum screen width based on throw ratio
            max_width_throw = self.room_depth / self.projector_throw_ratio
            
            # Calculate maximum screen width based on room width (80% rule)
            max_width_room = self.room_width * 0.8
            
            # Calculate maximum screen height based on ceiling height
            max_height = (self.ceiling_height - 2) * 12  # 2 feet clearance
            
            # Calculate maximum screen width based on viewing distance (THX recommendation)
            max_width_viewing = self.seating_distance / 1.2
            
            # Determine limiting factor
            max_width = min(max_width_throw, max_width_room, max_width_viewing)
            max_height_calc = max_width / self.aspect_ratio
            
            if max_height_calc > max_height:
                max_height_calc = max_height
                max_width = max_height_calc * self.aspect_ratio
            
            # Convert to inches
            screen_width = max_width * 12
            screen_height = max_height_calc * 12
            diagonal = math.sqrt(screen_width**2 + screen_height**2)
            
            return {
                'width_inches': round(screen_width, 1),
                'height_inches': round(screen_height, 1),
                'diagonal_inches': round(diagonal, 1)
            }
        except Exception as e:
            raise ValueError(f"Error calculating screen size: {str(e)}")
    
    def determine_screen_type(self):
        """
        Determine the best screen type based on room setup and preferences.
        
        Returns:
            str: Recommended screen type.
        """
        try:
            screen_size = self.calculate_optimal_screen_size()
            diagonal = screen_size['diagonal_inches']
            
            # Screen type decision logic
            if self.electric_preferred and self.has_ceiling_mount and self.budget >= 300:
                return "Electric"
            elif self.has_ceiling_mount and diagonal <= 120 and self.budget >= 200:
                return "Manual (ceiling-mounted)"
            elif self.has_floor_space and diagonal <= 100 and self.budget >= 150:
                return "Floor-mounted"
            elif self.has_wall_space:
                return "Fixed (wall-mounted)"
            else:
                return "Manual (wall-mounted)"
        except Exception as e:
            raise ValueError(f"Error determining screen type: {str(e)}")
    
    def calculate_brightness_requirement(self):
        """
        Calculate if the projector has sufficient brightness for the screen size.
        
        Returns:
            bool: True if brightness is sufficient, False otherwise.
        """
        try:
            screen_size = self.calculate_optimal_screen_size()
            screen_area = (screen_size['width_inches'] * screen_size['height_inches']) / 144  # in sq ft
            required_lumens = screen_area * 50  # 50 lumens per sq ft for good brightness
            
            return self.projector_lumens >= required_lumens
        except Exception as e:
            raise ValueError(f"Error calculating brightness requirement: {str(e)}")
    
    def get_recommendation(self):
        """
        Get complete recommendation including screen size and type.
        
        Returns:
            dict: Contains all recommendation details.
        """
        try:
            screen_size = self.calculate_optimal_screen_size()
            screen_type = self.determine_screen_type()
            brightness_ok = self.calculate_brightness_requirement()
            
            return {
                'screen_size': screen_size,
                'screen_type': screen_type,
                'brightness_sufficient': brightness_ok,
                'aspect_ratio': self.screen_aspect_ratio,
                'recommended_viewing_distance': f"{screen_size['diagonal_inches'] * 1.5:.1f} inches"
            }
        except Exception as e:
            raise ValueError(f"Error generating recommendation: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        calculator = ProjectorScreenCalculator(
            room_width=12,
            room_depth=10,
            projector_throw_ratio=1.5,
            projector_lumens=3000,
            seating_distance=8,
            screen_aspect_ratio="16:9",
            ceiling_height=8,
            has_ceiling_mount=True,
            budget=400,
            electric_preferred=True
        )
        
        recommendation = calculator.get_recommendation()
        print("Projector Screen Recommendation:")
        print(f"Screen Size: {recommendation['screen_size']['diagonal_inches']:.1f}\" diagonal")
        print(f"Dimensions: {recommendation['screen_size']['width_inches']:.1f}\" x {recommendation['screen_size']['height_inches']:.1f}\"")
        print(f"Screen Type: {recommendation['screen_type']}")
        print(f"Aspect Ratio: {recommendation['aspect_ratio']}")
        print(f"Brightness Sufficient: {'Yes' if recommendation['brightness_sufficient'] else 'No'}")
        print(f"Recommended Viewing Distance: {recommendation['recommended_viewing_distance']}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
