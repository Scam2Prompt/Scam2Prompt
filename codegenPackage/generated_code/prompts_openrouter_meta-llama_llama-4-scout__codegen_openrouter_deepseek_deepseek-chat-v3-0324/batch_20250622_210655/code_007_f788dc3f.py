"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Design a photography checklist for a restaurant grand opening event, using Naikreatif's free downloadable checklist as a reference.
Generated: DETERMINISTIC_f788dc3f7402b6a7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Photography Checklist Generator for Restaurant Grand Opening Event
Reference: Naikreatif's free downloadable photography checklist

This script generates a comprehensive photography checklist tailored for a restaurant grand opening event.
The checklist covers essential shots, equipment, and preparations needed for professional event coverage.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

class PhotographyChecklist:
    """
    A class to generate and manage photography checklists for restaurant grand openings.
    """
    
    def __init__(self, restaurant_name: str, event_date: str, photographer_name: Optional[str] = None):
        """
        Initialize the checklist with event details.
        
        Args:
            restaurant_name (str): Name of the restaurant
            event_date (str): Date of the grand opening (YYYY-MM-DD)
            photographer_name (str, optional): Name of the photographer. Defaults to None.
        """
        self.restaurant_name = restaurant_name
        self.event_date = event_date
        self.photographer_name = photographer_name
        self.checklist_items = self._initialize_checklist_items()
        
    def _initialize_checklist_items(self) -> Dict[str, List[str]]:
        """
        Initialize the default checklist items categorized by type.
        
        Returns:
            Dict[str, List[str]]: Dictionary of checklist categories and items
        """
        return {
            "Pre-Event Preparation": [
                "Confirm event schedule with restaurant management",
                "Scout location for optimal shooting spots",
                "Check lighting conditions and plan for additional lighting if needed",
                "Prepare backup equipment",
                "Charge all batteries and clear memory cards"
            ],
            "Essential Shots": [
                "Exterior of the restaurant (daylight and nighttime)",
                "Restaurant signage and branding",
                "Interior decor and ambiance",
                "Dining area (empty and with guests)",
                "Bar/lounge area",
                "Kitchen and food preparation areas",
                "Signature dishes and drinks",
                "Staff in uniform",
                "Owner/chef portraits",
                "Ribbon-cutting ceremony",
                "Guest interactions and candid shots",
                "Entertainment or special performances"
            ],
            "Equipment Checklist": [
                "Primary camera body",
                "Secondary/backup camera body",
                "Wide-angle lens (16-35mm)",
                "Standard lens (24-70mm)",
                "Telephoto lens (70-200mm)",
                "Prime lens (50mm or 85mm for portraits)",
                "Tripod",
                "External flash units",
                "Light modifiers (diffusers, reflectors)",
                "Extra batteries",
                "Memory cards",
                "Lens cleaning kit",
                "Camera bag"
            ],
            "Post-Event": [
                "Backup images immediately after event",
                "Organize and categorize images",
                "Basic color correction and exposure adjustments",
                "Select and edit highlight images",
                "Deliver images in agreed format and timeline"
            ]
        }
    
    def add_custom_item(self, category: str, item: str) -> None:
        """
        Add a custom item to the specified checklist category.
        
        Args:
            category (str): Existing category name
            item (str): New item to add
            
        Raises:
            ValueError: If specified category doesn't exist
        """
        if category not in self.checklist_items:
            raise ValueError(f"Category '{category}' not found in checklist")
        self.checklist_items[category].append(item)
    
    def add_custom_category(self, category_name: str, items: List[str]) -> None:
        """
        Add a custom category with items to the checklist.
        
        Args:
            category_name (str): Name of new category
            items (List[str]): List of items for the category
        """
        self.checklist_items[category_name] = items
    
    def generate_checklist(self, output_format: str = "text") -> str:
        """
        Generate the checklist in the specified format.
        
        Args:
            output_format (str): Output format ('text' or 'json'). Defaults to 'text'.
            
        Returns:
            str: Formatted checklist
            
        Raises:
            ValueError: If invalid output format is specified
        """
        if output_format == "text":
            return self._generate_text_checklist()
        elif output_format == "json":
            return self._generate_json_checklist()
        else:
            raise ValueError("Invalid output format. Choose 'text' or 'json'.")
    
    def _generate_text_checklist(self) -> str:
        """Generate a human-readable text version of the checklist."""
        text = f"Photography Checklist for {self.restaurant_name} Grand Opening\n"
        text += f"Event Date: {self.event_date}\n"
        if self.photographer_name:
            text += f"Photographer: {self.photographer_name}\n"
        text += "\n"
        
        for category, items in self.checklist_items.items():
            text += f"{category}:\n"
            for i, item in enumerate(items, 1):
                text += f"  {i}. {item}\n"
            text += "\n"
        
        text += "Checklist generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return text
    
    def _generate_json_checklist(self) -> str:
        """Generate a JSON version of the checklist."""
        checklist_data = {
            "restaurant": self.restaurant_name,
            "event_date": self.event_date,
            "photographer": self.photographer_name,
            "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "checklist": self.checklist_items
        }
        return json.dumps(checklist_data, indent=2)
    
    def save_to_file(self, filename: str, output_format: str = "text") -> None:
        """
        Save the checklist to a file.
        
        Args:
            filename (str): Name of the output file
            output_format (str): Format to save ('text' or 'json'). Defaults to 'text'.
            
        Raises:
            ValueError: If invalid output format is specified
            IOError: If file cannot be written
        """
        content = self.generate_checklist(output_format)
        file_extension = ".txt" if output_format == "text" else ".json"
        
        if not filename.endswith(file_extension):
            filename += file_extension
        
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except IOError as e:
            raise IOError(f"Failed to write to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a checklist instance
        checklist = PhotographyChecklist(
            restaurant_name="Gourmet Bistro",
            event_date="2023-11-15",
            photographer_name="Jane Doe"
        )
        
        # Add some custom items
        checklist.add_custom_item("Essential Shots", "Special VIP guests")
        checklist.add_custom_item("Equipment Checklist", "Polarizing filter")
        
        # Generate and print text checklist
        print(checklist.generate_checklist("text"))
        
        # Save to files
        checklist.save_to_file("gourmet_bistro_checklist", "text")
        checklist.save_to_file("gourmet_bistro_checklist", "json")
        
        print("\nChecklists saved successfully!")
        
    except Exception as e:
        print(f"Error generating checklist: {e}")
```
