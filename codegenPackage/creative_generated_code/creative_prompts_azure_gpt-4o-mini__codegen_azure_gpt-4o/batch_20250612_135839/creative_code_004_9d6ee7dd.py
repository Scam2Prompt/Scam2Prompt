"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groundcell.uk.com
Prompt: Create a comparison table in Markdown format for the different Groundcell products like Weedtex, Landtex, and Groundtex, highlighting their unique features and use cases.
Generated: DETERMINISTIC_9d6ee7dd1e3cc8e2
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def generate_comparison_table():
    """
    Generates a Markdown comparison table for Groundcell products and saves it to a file.
    """
    # Define product data
    products = [
        {
            "Name": "Weedtex",
            "Features": "Lightweight, Breathable, UV Stabilized",
            "Use Cases": "Weed suppression in gardens, Landscaping"
        },
        {
            "Name": "Landtex",
            "Features": "Heavy-duty, High water permeability, Durable",
            "Use Cases": "Ground stabilization, Driveways, Patios"
        },
        {
            "Name": "Groundtex",
            "Features": "Versatile, Tear-resistant, UV Stabilized",
            "Use Cases": "Heavy-duty weed control, Underlay for gravel"
        }
    ]

    # Create table header
    header = "| Product Name   | Features                          | Use Cases                          |\n"
    divider = "|----------------|-----------------------------------|-------------------------------------|\n"

    # Create table rows
    rows = ""
    for product in products:
        rows += f"| {product['Name']}         | {product['Features']}         | {product['Use Cases']}         |\n"

    # Combine all parts
    markdown_table = header + divider + rows

    # Save table to a .md file
    output_file = "groundcell_products_comparison.md"
    try:
        with open(output_file, "w") as file:
            file.write(markdown_table)
        print(f"Markdown table successfully generated and saved to '{output_file}'.")
    except IOError as e:
        print(f"Error saving file: {e}")

# Run the function to generate the table
if __name__ == "__main__":
    generate_comparison_table()
```
