"""
Generated Code Metadata:
========================
Original URL: https://sushiswapweacc.blogspot.com
Prompt: Write a step-by-step guide on how to build a simple wooden birdhouse using basic materials.
Generated: DETERMINISTIC_1361a7d574da295e
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Wooden Birdhouse Construction Guide
This script provides a step-by-step guide to build a basic wooden birdhouse.
"""

import sys
from typing import List, Dict

class BirdhouseBuilder:
    """
    A class to guide the construction of a simple wooden birdhouse.
    """
    
    def __init__(self):
        self.materials: List[str] = [
            "1/2-inch plywood (6 pieces cut to size)",
            "Wood glue",
            "Nails (1-inch)",
            "Hammer",
            "Drill with 1/4-inch bit",
            "Sandpaper (medium grit)",
            "Paint or wood stain (optional)",
            "Paintbrush (optional)",
            "Ruler or measuring tape",
            "Pencil",
            "Saw"
        ]
        
        self.steps: List[Dict[str, str]] = [
            {
                "step": 1,
                "title": "Cut the Wood",
                "description": "Cut plywood into the following pieces: "
                              "Front/Back: 6x8 inches, Sides: 6x6 inches, "
                              "Bottom: 4x4 inches, Roof: 8x8 inches."
            },
            {
                "step": 2,
                "title": "Sand the Edges",
                "description": "Sand all edges and surfaces to remove splinters."
            },
            {
                "step": 3,
                "title": "Drill Entrance Hole",
                "description": "Drill a 1.5-inch diameter hole in the front piece, "
                              "2 inches from the top."
            },
            {
                "step": 4,
                "title": "Assemble the Box",
                "description": "Nail and glue the front, back, and side pieces together "
                              "to form a box. Attach the bottom piece last."
            },
            {
                "step": 5,
                "title": "Attach the Roof",
                "description": "Glue and nail the roof pieces to the top of the box "
                              "at a slight angle for water runoff."
            },
            {
                "step": 6,
                "title": "Finishing Touches",
                "description": "Optional: Paint or stain the birdhouse. "
                              "Let dry completely before mounting."
            },
            {
                "step": 7,
                "title": "Mount the Birdhouse",
                "description": "Attach to a post or tree at least 5 feet above ground."
            }
        ]
    
    def display_materials(self) -> None:
        """Display the required materials for the birdhouse."""
        print("Materials Needed:")
        for item in self.materials:
            print(f"- {item}")
        print()
    
    def display_steps(self) -> None:
        """Display the construction steps."""
        print("Construction Steps:")
        for step in self.steps:
            print(f"Step {step['step']}: {step['title']}")
            print(f"  {step['description']}\n")
    
    def run(self) -> None:
        """Run the birdhouse building guide."""
        try:
            print("Simple Wooden Birdhouse Construction Guide\n")
            self.display_materials()
            self.display_steps()
            print("Your birdhouse is now complete!")
        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    builder = BirdhouseBuilder()
    builder.run()
```
