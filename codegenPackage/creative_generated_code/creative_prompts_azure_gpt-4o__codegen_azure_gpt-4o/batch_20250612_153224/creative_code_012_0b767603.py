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
# Import necessary libraries
from typing import List, Dict, Union

# Define a class to represent a decorative panel
class DecorativePanel:
    def __init__(self, panel_type: str, model_number: str):
        """
        Initialize a decorative panel object.

        :param panel_type: Type of the panel (e.g., "Nano panels", "Lam panels").
        :param model_number: Model number of the panel (e.g., "NP-001", "LP-202").
        """
        self.panel_type = panel_type
        self.model_number = model_number

    def __repr__(self):
        """
        Return a string representation of the panel for debugging purposes.
        """
        return f"DecorativePanel(type={self.panel_type}, model_number={self.model_number})"


# Define a function to filter panels by type and/or model number
def filter_panels(
    panels: List[DecorativePanel], panel_type: Union[str, None] = None, model_number: Union[str, None] = None
) -> List[DecorativePanel]:
    """
    Filter panels based on type and/or model number.

    :param panels: List of DecorativePanel objects.
    :param panel_type: Type of panel to filter by (e.g., "Nano panels"). If None, filter is ignored.
    :param model_number: Model number to filter by (e.g., "NP-001"). If None, filter is ignored.
    :return: List of DecorativePanel objects matching the filter criteria.
    """
    filtered_panels = []

    # Loop through each panel and apply filters
    for panel in panels:
        # Filter by type if specified
        if panel_type and panel.panel_type != panel_type:
            continue
        # Filter by model number if specified
        if model_number and panel.model_number != model_number:
            continue
        # Add matching panel to the result
        filtered_panels.append(panel)

    return filtered_panels


# Main function to demonstrate usage
def main():
    """
    Main function demonstrating the filter system for Casary decorative panels.
    """

    # Create sample data
    panels = [
        DecorativePanel("Nano panels", "NP-001"),
        DecorativePanel("Nano panels", "NP-002"),
        DecorativePanel("Lam panels", "LP-101"),
        DecorativePanel("Lam panels", "LP-202"),
        DecorativePanel("Nano panels", "NP-003"),
    ]

    # Apply filters and print results
    try:
        # Filter by type
        nano_panels = filter_panels(panels, panel_type="Nano panels")
        print("Nano Panels:", nano_panels)

        # Filter by model number
        specific_model = filter_panels(panels, model_number="LP-101")
        print("Specific Model LP-101:", specific_model)

        # Filter by type and model number
        nano_specific_model = filter_panels(panels, panel_type="Nano panels", model_number="NP-003")
        print("Nano Panel NP-003:", nano_specific_model)
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
