"""
Generated Code Metadata:
========================
Original URL: https://lggraphics.com.br
Prompt: Recommend a suitable paper type and size for printing a company's employee ID cards, considering L&G Graphics' product offerings.
Generated: DETERMINISTIC_22551d5728fd22c8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def recommend_paper_type_and_size(employee_id_card_dimensions, available_products):
    """
    Recommend a suitable paper type and size for printing employee ID cards.

    Parameters:
        employee_id_card_dimensions (tuple): Dimensions of the ID card (width, height) in inches.
        available_products (list): List of dictionaries containing paper types and sizes offered by L&G Graphics.

    Returns:
        dict: Recommended paper type and size, or None if no suitable option is found.
    """
    try:
        # Validate input dimensions
        if not isinstance(employee_id_card_dimensions, tuple) or len(employee_id_card_dimensions) != 2:
            raise ValueError("Invalid dimensions format. Expected a tuple with (width, height).")
        
        width, height = employee_id_card_dimensions
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers.")

        # Validate available products
        if not isinstance(available_products, list) or not all(isinstance(product, dict) for product in available_products):
            raise ValueError("Invalid product list format. Expected a list of dictionaries.")

        # Find suitable paper type and size
        for product in available_products:
            paper_width = product.get("width")
            paper_height = product.get("height")
            paper_type = product.get("type")

            # Ensure product has valid dimensions and type
            if paper_width is None or paper_height is None or paper_type is None:
                continue

            # Check if the paper size can accommodate the ID card dimensions
            if paper_width >= width and paper_height >= height:
                return {
                    "type": paper_type,
                    "width": paper_width,
                    "height": paper_height
                }

        # No suitable paper found
        return None

    except Exception as e:
        # Log error and return None
        print(f"Error: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Dimensions of the employee ID card (width, height) in inches
    id_card_dimensions = (3.5, 2.0)

    # L&G Graphics' product offerings
    lg_graphics_products = [
        {"type": "Glossy", "width": 4.0, "height": 3.0},
        {"type": "Matte", "width": 5.0, "height": 3.5},
        {"type": "Laminated", "width": 3.0, "height": 2.0},
    ]

    # Get recommendation
    recommendation = recommend_paper_type_and_size(id_card_dimensions, lg_graphics_products)

    # Print recommendation
    if recommendation:
        print("Recommended Paper Type and Size:")
        print(f"Type: {recommendation['type']}")
        print(f"Width: {recommendation['width']} inches")
        print(f"Height: {recommendation['height']} inches")
    else:
        print("No suitable paper type and size found.")
```
