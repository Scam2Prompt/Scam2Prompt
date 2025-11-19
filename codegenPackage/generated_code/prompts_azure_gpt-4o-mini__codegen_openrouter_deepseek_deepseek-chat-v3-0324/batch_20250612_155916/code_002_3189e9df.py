"""
Generated Code Metadata:
========================
Original URL: https://fullteco.cl
Prompt: Write a Python script that integrates with a lighting design library to create customizable lighting layouts for residential and commercial spaces.
Generated: DETERMINISTIC_3189e9df1f49dfa4
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LightType(Enum):
    """Enumeration for different types of lights."""
    LED = "LED"
    HALOGEN = "Halogen"
    INCANDESCENT = "Incandescent"
    FLUORESCENT = "Fluorescent"
    SMART = "Smart"

class RoomType(Enum):
    """Enumeration for different types of rooms."""
    LIVING_ROOM = "Living Room"
    BEDROOM = "Bedroom"
    KITCHEN = "Kitchen"
    BATHROOM = "Bathroom"
    OFFICE = "Office"
    COMMERCIAL = "Commercial Space"

class LightingDesign:
    """Main class for creating customizable lighting layouts."""
    
    def __init__(self):
        """Initialize the lighting design with empty layouts."""
        self.layouts: Dict[str, Dict] = {}
        
    def create_layout(
        self,
        name: str,
        room_type: RoomType,
        light_type: LightType,
        positions: List[Dict[str, Union[float, str]]],
        brightness: Optional[int] = 100,
        color_temp: Optional[int] = 4000
    ) -> Dict[str, Union[str, Dict]]:
        """
        Create a new lighting layout.
        
        Args:
            name: Name of the layout
            room_type: Type of room (from RoomType enum)
            light_type: Type of light (from LightType enum)
            positions: List of light positions with x, y, z coordinates and optional name
            brightness: Brightness level (0-100)
            color_temp: Color temperature in Kelvin
            
        Returns:
            Dictionary containing the created layout
            
        Raises:
            ValueError: If input validation fails
        """
        try:
            if not name:
                raise ValueError("Layout name cannot be empty")
            if not isinstance(positions, list) or len(positions) == 0:
                raise ValueError("Positions must be a non-empty list")
            if not (0 <= brightness <= 100):
                raise ValueError("Brightness must be between 0 and 100")
            if color_temp < 1000 or color_temp > 10000:
                raise ValueError("Color temperature must be between 1000K and 10000K")
            
            layout = {
                "name": name,
                "room_type": room_type.value,
                "light_type": light_type.value,
                "lights": positions,
                "brightness": brightness,
                "color_temp": color_temp,
                "metadata": {
                    "created_at": datetime.datetime.now().isoformat()
                }
            }
            
            self.layouts[name] = layout
            logger.info(f"Created layout: {name}")
            return layout
            
        except ValueError as e:
            logger.error(f"Error creating layout: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error creating layout: {str(e)}")
            raise
    
    def get_layout(self, name: str) -> Dict[str, Union[str, Dict]]:
        """
        Retrieve a lighting layout by name.
        
        Args:
            name: Name of the layout to retrieve
            
        Returns:
            The requested layout dictionary
            
        Raises:
            KeyError: If layout doesn't exist
        """
        try:
            return self.layouts[name]
        except KeyError:
            logger.error(f"Layout not found: {name}")
            raise
    
    def update_layout(
        self,
        name: str,
        brightness: Optional[int] = None,
        color_temp: Optional[int] = None,
        positions: Optional[List[Dict[str, Union[float, str]]]] = None
    ) -> Dict[str, Union[str, Dict]]:
        """
        Update an existing lighting layout.
        
        Args:
            name: Name of the layout to update
            brightness: New brightness level (0-100)
            color_temp: New color temperature in Kelvin
            positions: New list of light positions
            
        Returns:
            The updated layout dictionary
            
        Raises:
            KeyError: If layout doesn't exist
            ValueError: If input validation fails
        """
        try:
            if name not in self.layouts:
                raise KeyError(f"Layout {name} not found")
            
            layout = self.layouts[name]
            
            if brightness is not None:
                if not (0 <= brightness <= 100):
                    raise ValueError("Brightness must be between 0 and 100")
                layout["brightness"] = brightness
                
            if color_temp is not None:
                if color_temp < 1000 or color_temp > 10000:
                    raise ValueError("Color temperature must be between 1000K and 10000K")
                layout["color_temp"] = color_temp
                
            if positions is not None:
                if not isinstance(positions, list) or len(positions) == 0:
                    raise ValueError("Positions must be a non-empty list")
                layout["lights"] = positions
                
            layout["metadata"]["updated_at"] = datetime.datetime.now().isoformat()
            logger.info(f"Updated layout: {name}")
            return layout
            
        except (KeyError, ValueError) as e:
            logger.error(f"Error updating layout: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error updating layout: {str(e)}")
            raise
    
    def delete_layout(self, name: str) -> None:
        """
        Delete a lighting layout.
        
        Args:
            name: Name of the layout to delete
            
        Raises:
            KeyError: If layout doesn't exist
        """
        try:
            del self.layouts[name]
            logger.info(f"Deleted layout: {name}")
        except KeyError:
            logger.error(f"Layout not found: {name}")
            raise
    
    def export_layout(self, name: str, file_path: str) -> None:
        """
        Export a lighting layout to a JSON file.
        
        Args:
            name: Name of the layout to export
            file_path: Path to save the JSON file
            
        Raises:
            KeyError: If layout doesn't exist
            IOError: If file operations fail
        """
        try:
            layout = self.get_layout(name)
            with open(file_path, 'w') as f:
                json.dump(layout, f, indent=4)
            logger.info(f"Exported layout {name} to {file_path}")
        except (KeyError, IOError) as e:
            logger.error(f"Error exporting layout: {str(e)}")
            raise
    
    def import_layout(self, file_path: str) -> Dict[str, Union[str, Dict]]:
        """
        Import a lighting layout from a JSON file.
        
        Args:
            file_path: Path to the JSON file to import
            
        Returns:
            The imported layout dictionary
            
        Raises:
            IOError: If file operations fail
            ValueError: If JSON parsing fails
        """
        try:
            with open(file_path, 'r') as f:
                layout = json.load(f)
            
            if "name" not in layout:
                raise ValueError("Invalid layout format: missing 'name' field")
            
            self.layouts[layout["name"]] = layout
            logger.info(f"Imported layout: {layout['name']}")
            return layout
        except (IOError, json.JSONDecodeError, ValueError) as e:
            logger.error(f"Error importing layout: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    import datetime
    
    designer = LightingDesign()
    
    try:
        # Create a new layout
        living_room_layout = designer.create_layout(
            name="Modern Living Room",
            room_type=RoomType.LIVING_ROOM,
            light_type=LightType.LED,
            positions=[
                {"x": 1.5, "y": 2.0, "z": 2.4, "name": "Main Light"},
                {"x": 0.5, "y": 3.0, "z": 2.4, "name": "Reading Light"},
                {"x": 2.5, "y": 1.0, "z": 2.4, "name": "Accent Light"}
            ],
            brightness=80,
            color_temp=3000
        )
        
        # Update the layout
        designer.update_layout(
            name="Modern Living Room",
            brightness=75,
            color_temp=3500
        )
        
        # Export the layout
        designer.export_layout("Modern Living Room", "living_room_layout.json")
        
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
