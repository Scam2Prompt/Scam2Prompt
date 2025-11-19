"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: "What are the different types of knit fabrics used for sportswear and swimwear, and how do they differ in terms of material and application?"
Generated: DETERMINISTIC_985f33e7acaf107d
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a function to retrieve information about knit fabrics used for sportswear and swimwear
def get_knit_fabrics_info():
    """
    Returns a list of knit fabrics commonly used for sportswear and swimwear,
    along with their material composition and applications.
    """
    try:
        # Define a list of knit fabrics with their properties
        knit_fabrics = [
            {
                "name": "Polyester Spandex Blend",
                "material": "Polyester and Spandex",
                "applications": [
                    "Sportswear (e.g., leggings, compression wear)",
                    "Swimwear (e.g., swimsuits)"
                ],
                "properties": [
                    "Stretchable",
                    "Durable",
                    "Quick-drying"
                ]
            },
            {
                "name": "Nylon Spandex Blend",
                "material": "Nylon and Spandex",
                "applications": [
                    "Swimwear (e.g., bikinis, one-piece swimsuits)",
                    "Sportswear (e.g., yoga pants, athletic tops)"
                ],
                "properties": [
                    "High elasticity",
                    "Smooth texture",
                    "Resistant to chlorine"
                ]
            },
            {
                "name": "Mesh Knit Fabric",
                "material": "Polyester or Nylon",
                "applications": [
                    "Sportswear (e.g., breathable jerseys, shorts)",
                    "Swimwear linings"
                ],
                "properties": [
                    "Breathable",
                    "Lightweight",
                    "Moisture-wicking"
                ]
            },
            {
                "name": "Rib Knit Fabric",
                "material": "Cotton, Polyester, or Blends",
                "applications": [
                    "Sportswear (e.g., cuffs, collars, tank tops)"
                ],
                "properties": [
                    "Stretchable",
                    "Comfortable",
                    "Form-fitting"
                ]
            },
            {
                "name": "Tricot Knit Fabric",
                "material": "Nylon or Polyester",
                "applications": [
                    "Swimwear (e.g., linings, outer layers)",
                    "Sportswear (e.g., tracksuits)"
                ],
                "properties": [
                    "Smooth texture",
                    "Durable",
                    "Resistant to runs"
                ]
            }
        ]

        # Return the data as a JSON string for easy readability
        return json.dumps(knit_fabrics, indent=4)

    except Exception as e:
        # Handle any unexpected errors
        return json.dumps({"error": str(e)})

# Main execution block
if __name__ == "__main__":
    # Retrieve and print knit fabrics information
    fabrics_info = get_knit_fabrics_info()
    print(fabrics_info)
```
