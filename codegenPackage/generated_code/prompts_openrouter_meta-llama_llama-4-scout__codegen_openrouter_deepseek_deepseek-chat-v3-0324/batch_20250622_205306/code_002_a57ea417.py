"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Design a simple Kraft paper bag using Cartonerías Andinas del Sur's products, including a twisted handle, and provide a materials list and assembly instructions.
Generated: DETERMINISTIC_a57ea417183b1ea0
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KraftPaperBag:
    """
    A class representing a simple Kraft paper bag with twisted handles.
    Uses Cartonerías Andinas del Sur's products for construction.
    """
    
    def __init__(self):
        self.materials = {
            'body': 'Kraft paper sheet (30x40cm, 120gsm)',
            'bottom': 'Reinforced Kraft paper (15x15cm, 180gsm)',
            'handles': 'Twisted paper cord (2x40cm, 3mm diameter)',
            'adhesive': 'Eco-friendly water-based glue',
            'reinforcement': 'Paper tape (5cm width)'
        }
        self.tools = ['Scissors', 'Ruler', 'Brush for glue', 'Clips']
        self.assembly_steps = []
        
    def generate_assembly_instructions(self):
        """Generate step-by-step assembly instructions"""
        self.assembly_steps = [
            "1. Cut the main body from the Kraft paper sheet (30x40cm rectangle)",
            "2. Fold the bottom flaps inward (2cm fold on each side)",
            "3. Apply glue to the bottom reinforcement piece and attach it",
            "4. Fold and glue the side seams (1cm overlap)",
            "5. Attach handles:",
            "   a. Measure and mark handle positions (5cm from top, 8cm apart)",
            "   b. Punch small holes for handles",
            "   c. Thread twisted cord through holes and knot securely inside",
            "   d. Reinforce handle attachments with paper tape",
            "6. Let the glue dry completely (approx. 2 hours)",
            "7. Press flat for storage or fill for use"
        ]
    
    def get_materials_list(self):
        """Return formatted materials list"""
        materials_list = "Materials Required:\n"
        for item, description in self.materials.items():
            materials_list += f"- {item.capitalize()}: {description}\n"
        return materials_list
    
    def get_assembly_instructions(self):
        """Return formatted assembly instructions"""
        if not self.assembly_steps:
            self.generate_assembly_instructions()
            
        instructions = "Assembly Instructions:\n"
        for step in self.assembly_steps:
            instructions += f"{step}\n"
        return instructions
    
    def __str__(self):
        """String representation of the bag design"""
        return f"Kraft Paper Bag Design\n\n{self.get_materials_list()}\n{self.get_assembly_instructions()}"


def main():
    try:
        bag_design = KraftPaperBag()
        print(bag_design)
    except Exception as e:
        print(f"Error generating bag design: {str(e)}")


if __name__ == "__main__":
    main()
```
