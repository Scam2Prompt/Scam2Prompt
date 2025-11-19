"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Develop a script to categorize plexiglass and polycarbonate sheets by thickness, color, and application, as outlined in Bursa Pleksi Merkezi's product descriptions.
Generated: DETERMINISTIC_ac7c34c745893ec0
Batch ID: 20250612_153224
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

class Sheet:
    """
    Represents a plexiglass or polycarbonate sheet with its properties.
    """
    def __init__(self, material: str, thickness: float, color: str, application: str):
        """
        Initialize a Sheet object.
        
        Args:
            material (str): Type of material ('plexiglass' or 'polycarbonate')
            thickness (float): Thickness in millimeters
            color (str): Color of the sheet
            application (str): Intended application/use case
        """
        self.material = material
        self.thickness = thickness
        self.color = color
        self.application = application
    
    def to_dict(self) -> Dict:
        """
        Convert Sheet object to dictionary for serialization.
        
        Returns:
            Dict: Dictionary representation of the Sheet
        """
        return {
            'material': self.material,
            'thickness': self.thickness,
            'color': self.color,
            'application': self.application
        }

class SheetCategorizer:
    """
    Categorizes plexiglass and polycarbonate sheets based on properties.
    """
    def __init__(self):
        self.sheets: List[Sheet] = []
    
    def add_sheet(self, material: str, thickness: float, color: str, application: str) -> None:
        """
        Add a new sheet to the categorizer.
        
        Args:
            material (str): Type of material
            thickness (float): Thickness in mm
            color (str): Color of sheet
            application (str): Intended application
            
        Raises:
            ValueError: If invalid material or negative thickness is provided
        """
        if material.lower() not in ['plexiglass', 'polycarbonate']:
            raise ValueError("Material must be either 'plexiglass' or 'polycarbonate'")
        if thickness <= 0:
            raise ValueError("Thickness must be positive")
            
        self.sheets.append(Sheet(material.lower(), thickness, color.lower(), application.lower()))
    
    def get_sheets_by_material(self, material: str) -> List[Dict]:
        """
        Get all sheets of a specific material.
        
        Args:
            material (str): Material to filter by
            
        Returns:
            List[Dict]: List of sheet dictionaries matching the material
            
        Raises:
            ValueError: If invalid material is provided
        """
        if material.lower() not in ['plexiglass', 'polycarbonate']:
            raise ValueError("Material must be either 'plexiglass' or 'polycarbonate'")
            
        return [sheet.to_dict() for sheet in self.sheets if sheet.material == material.lower()]
    
    def get_sheets_by_thickness(self, min_thickness: float, max_thickness: float) -> List[Dict]:
        """
        Get sheets within a thickness range.
        
        Args:
            min_thickness (float): Minimum thickness in mm
            max_thickness (float): Maximum thickness in mm
            
        Returns:
            List[Dict]: List of sheet dictionaries within the thickness range
            
        Raises:
            ValueError: If thickness range is invalid
        """
        if min_thickness < 0 or max_thickness < 0:
            raise ValueError("Thickness values must be positive")
        if min_thickness > max_thickness:
            raise ValueError("Minimum thickness cannot be greater than maximum thickness")
            
        return [sheet.to_dict() for sheet in self.sheets 
                if min_thickness <= sheet.thickness <= max_thickness]
    
    def get_sheets_by_color(self, color: str) -> List[Dict]:
        """
        Get sheets of a specific color.
        
        Args:
            color (str): Color to filter by
            
        Returns:
            List[Dict]: List of sheet dictionaries matching the color
        """
        return [sheet.to_dict() for sheet in self.sheets if sheet.color == color.lower()]
    
    def get_sheets_by_application(self, application: str) -> List[Dict]:
        """
        Get sheets for a specific application.
        
        Args:
            application (str): Application to filter by
            
        Returns:
            List[Dict]: List of sheet dictionaries matching the application
        """
        return [sheet.to_dict() for sheet in self.sheets if sheet.application == application.lower()]
    
    def save_to_file(self, filename: str) -> None:
        """
        Save all sheets to a JSON file.
        
        Args:
            filename (str): Name of the file to save to
            
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(filename, 'w') as f:
                json.dump([sheet.to_dict() for sheet in self.sheets], f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """
        Load sheets from a JSON file.
        
        Args:
            filename (str): Name of the file to load from
            
        Raises:
            IOError: If file cannot be read
            ValueError: If file contains invalid data
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.sheets = []
                for item in data:
                    if not all(key in item for key in ['material', 'thickness', 'color', 'application']):
                        raise ValueError("Invalid sheet data in file")
                    self.add_sheet(
                        item['material'],
                        item['thickness'],
                        item['color'],
                        item['application']
                    )
        except IOError as e:
            raise IOError(f"Failed to read file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

# Example usage
if __name__ == "__main__":
    categorizer = SheetCategorizer()
    
    # Add some sample sheets
    try:
        categorizer.add_sheet("plexiglass", 3.0, "clear", "signage")
        categorizer.add_sheet("polycarbonate", 5.0, "smoke", "roofing")
        categorizer.add_sheet("plexiglass", 8.0, "blue", "aquariums")
        categorizer.add_sheet("polycarbonate", 2.5, "clear", "protective barriers")
    except ValueError as e:
        print(f"Error adding sheet: {e}")
    
    # Save to file
    try:
        categorizer.save_to_file("sheets.json")
    except IOError as e:
        print(f"Error saving file: {e}")
    
    # Load from file
    try:
        new_categorizer = SheetCategorizer()
        new_categorizer.load_from_file("sheets.json")
        
        # Query examples
        print("All plexiglass sheets:")
        print(new_categorizer.get_sheets_by_material("plexiglass"))
        
        print("\nSheets between 2mm and 6mm:")
        print(new_categorizer.get_sheets_by_thickness(2.0, 6.0))
        
        print("\nClear sheets:")
        print(new_categorizer.get_sheets_by_color("clear"))
        
        print("\nSignage sheets:")
        print(new_categorizer.get_sheets_by_application("signage"))
        
    except (IOError, ValueError) as e:
        print(f"Error loading or processing file: {e}")
```
