"""
Generated Code Metadata:
========================
Original URL: https://www.dow.spb.ru
Prompt: Generate a list of tools and materials required for replacing a windshield in a heavy-duty truck, and suggest a supplier that offers a comprehensive set of products for this task.
Generated: DETERMINISTIC_8cc2c7b34dade737
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# windshield_replacement.py

class WindshieldReplacementKit:
    def __init__(self):
        self.tools = []
        self.materials = []

    def add_tool(self, tool):
        """Add a tool to the replacement kit."""
        self.tools.append(tool)

    def add_material(self, material):
        """Add a material to the replacement kit."""
        self.materials.append(material)

    def get_tools(self):
        """Get the list of tools required."""
        return self.tools

    def get_materials(self):
        """Get the list of materials required."""
        return self.materials


class Supplier:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def get_products(self):
        """Get the list of products offered by the supplier."""
        return self.products


def generate_replacement_kit():
    """Generate a list of tools and materials required for replacing a windshield in a heavy-duty truck."""
    kit = WindshieldReplacementKit()

    # Tools required
    kit.add_tool("Windshield removal tool")
    kit.add_tool("Glass suction cups")
    kit.add_tool("Rubber mallet")
    kit.add_tool("Putty knife")
    kit.add_tool("Safety glasses")

    # Materials required
    kit.add_material("Windshield glass")
    kit.add_material("Windshield sealant")
    kit.add_material("Adhesive primer")
    kit.add_material("Cleaning solution")
    kit.add_material("Rags")

    return kit


def suggest_supplier():
    """Suggest a supplier that offers a comprehensive set of products for windshield replacement."""
    products = [
        "Windshield glass",
        "Windshield sealant",
        "Adhesive primer",
        "Cleaning solution",
        "Rags",
        "Windshield removal tool",
        "Glass suction cups",
        "Rubber mallet",
        "Putty knife",
        "Safety glasses"
    ]

    supplier = Supplier("Heavy Duty Truck Parts", products)
    return supplier


def main():
    try:
        kit = generate_replacement_kit()
        print("Tools required:")
        for tool in kit.get_tools():
            print(f"- {tool}")

        print("\nMaterials required:")
        for material in kit.get_materials():
            print(f"- {material}")

        supplier = suggest_supplier()
        print(f"\nSupplier: {supplier.name}")
        print("Products offered:")
        for product in supplier.get_products():
            print(f"- {product}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
