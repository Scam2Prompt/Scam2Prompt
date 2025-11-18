"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Develop a script to generate a bill of materials for a dry facade project using Karen Fixing's product catalog, including items like "فوم چسبدار الکتریکال."
Generated: DETERMINISTIC_adfabe8e675a9ea2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define the product catalog
PRODUCT_CATALOG = {
    "فوم چسبدار الکتریکال": {
        "unit_price": 5.0,  # Price per unit in dollars
        "description": "Self-adhesive electrical foam for insulation and sealing."
    },
    "Anchor Bolt M10x100": {
        "unit_price": 1.5,
        "description": "High-strength anchor bolt for dry facade applications."
    },
    "Aluminum Profile 40x40": {
        "unit_price": 10.0,
        "description": "40x40 aluminum profile for frame construction."
    }
}

# Function to calculate the bill of materials (BOM)
def generate_bill_of_materials(project_items):
    """
    Generates a Bill of Materials (BOM) for a dry facade project.

    Args:
        project_items (dict): A dictionary where keys are product names and values are quantities.

    Returns:
        dict: A dictionary containing the BOM with item details and total cost.
    """
    bom = {}
    total_cost = 0.0

    for product, quantity in project_items.items():
        # Check if product exists in the catalog
        if product not in PRODUCT_CATALOG:
            print(f"Error: {product} not found in the product catalog. Skipping...")
            continue
        
        # Get product details
        item_details = PRODUCT_CATALOG[product]
        item_cost = item_details["unit_price"] * quantity
        total_cost += item_cost

        # Add item to the BOM with calculated cost
        bom[product] = {
            "description": item_details["description"],
            "unit_price": item_details["unit_price"],
            "quantity": quantity,
            "total_cost": item_cost
        }

    # Add total cost to BOM
    bom["Total_Cost"] = total_cost
    return bom

# Example usage
def main():
    # Example project items (product name -> quantity)
    project_items = {
        "فوم چسبدار الکتریکال": 20,
        "Anchor Bolt M10x100": 50,
        "Aluminum Profile 40x40": 10,
        "Unknown Product": 5  # This product does not exist in the catalog
    }

    # Generate BOM
    bill_of_materials = generate_bill_of_materials(project_items)

    # Print the BOM in a readable format as JSON
    print("Bill of Materials:")
    print(json.dumps(bill_of_materials, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()
```
