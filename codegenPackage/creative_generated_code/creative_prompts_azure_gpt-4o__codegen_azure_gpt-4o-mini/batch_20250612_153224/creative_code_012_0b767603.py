"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Write code to implement a filter system for Casary decorative panels, allowing users to sort by type (e.g., Nano panels, Lam panels) and model numbers.
Generated: DETERMINISTIC_0b76760339996a0b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DecorativePanel:
    """Class to represent a decorative panel."""
    
    def __init__(self, panel_type, model_number):
        self.panel_type = panel_type
        self.model_number = model_number

    def __repr__(self):
        return f"{self.panel_type} - Model: {self.model_number}"


class PanelFilter:
    """Class to filter decorative panels based on type and model number."""
    
    def __init__(self, panels):
        """
        Initialize the PanelFilter with a list of panels.
        
        Args:
            panels (list): List of DecorativePanel objects.
        """
        if not all(isinstance(panel, DecorativePanel) for panel in panels):
            raise ValueError("All items in the panels list must be of type DecorativePanel.")
        self.panels = panels

    def filter_by_type(self, panel_type):
        """
        Filter panels by type.
        
        Args:
            panel_type (str): The type of the panel to filter by.
        
        Returns:
            list: List of panels that match the specified type.
        """
        filtered_panels = [panel for panel in self.panels if panel.panel_type.lower() == panel_type.lower()]
        return filtered_panels

    def filter_by_model(self, model_number):
        """
        Filter panels by model number.
        
        Args:
            model_number (str): The model number to filter by.
        
        Returns:
            list: List of panels that match the specified model number.
        """
        filtered_panels = [panel for panel in self.panels if panel.model_number.lower() == model_number.lower()]
        return filtered_panels

    def filter_by_type_and_model(self, panel_type, model_number):
        """
        Filter panels by both type and model number.
        
        Args:
            panel_type (str): The type of the panel to filter by.
            model_number (str): The model number to filter by.
        
        Returns:
            list: List of panels that match the specified type and model number.
        """
        filtered_panels = [
            panel for panel in self.panels
            if panel.panel_type.lower() == panel_type.lower() and panel.model_number.lower() == model_number.lower()
        ]
        return filtered_panels


# Example usage:
if __name__ == "__main__":
    try:
        # Create decorative panels
        panels = [
            DecorativePanel("Nano", "NP-001"),
            DecorativePanel("Lam", "LP-002"),
            DecorativePanel("Nano", "NP-003"),
            DecorativePanel("Lam", "LP-004"),
        ]

        # Initialize the filter system
        panel_filter = PanelFilter(panels)

        # Filter by type
        nano_panels = panel_filter.filter_by_type("Nano")
        print("Filtered Nano Panels:", nano_panels)

        # Filter by model
        lp_panels = panel_filter.filter_by_model("LP-002")
        print("Filtered LP-002 Panels:", lp_panels)

        # Filter by type and model
        specific_panel = panel_filter.filter_by_type_and_model("Lam", "LP-004")
        print("Filtered Lam LP-004 Panels:", specific_panel)

    except ValueError as e:
        print(f"Error: {e}")
```
