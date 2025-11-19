"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: "Generate a list of materials and tools required to assemble a Cilindro Asador Inoxidable Meat Master Mediano, as per the product specifications on the Meat Master website."
Generated: DETERMINISTIC_fd06d5477ffd090c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# materials_and_tools.py
"""
This script generates a list of materials and tools required to assemble
the Cilindro Asador Inoxidable Meat Master Mediano based on product specifications.
"""

def get_materials_and_tools():
    """
    Returns a dictionary containing lists of materials and tools needed for assembly.
    Based on Meat Master product specifications for the medium stainless steel grill cylinder.
    """
    materials = [
        "Stainless steel cylinder body",
        "Stainless steel grill grate",
        "Stainless steel charcoal tray",
        "Stainless steel lid",
        "Stainless steel legs (4)",
        "Stainless steel screws and bolts",
        "Heat-resistant handles",
        "Adjustable air vents"
    ]
    
    tools = [
        "Phillips head screwdriver",
        "Adjustable wrench",
        "Rubber mallet (for assembly assistance)",
        "Protective gloves",
        "Safety glasses"
    ]
    
    return {
        "materials": materials,
        "tools": tools,
        "notes": [
            "All materials are included in the package",
            "Tools are not included and must be provided by the user",
            "Assembly requires 2 people for safety"
        ]
    }

def print_materials_and_tools():
    """Prints the materials and tools in a user-friendly format."""
    data = get_materials_and_tools()
    
    print("Materials Required:")
    for item in data["materials"]:
        print(f"- {item}")
    
    print("\nTools Required:")
    for tool in data["tools"]:
        print(f"- {tool}")
    
    print("\nNotes:")
    for note in data["notes"]:
        print(f"- {note}")

if __name__ == "__main__":
    print_materials_and_tools()
```
