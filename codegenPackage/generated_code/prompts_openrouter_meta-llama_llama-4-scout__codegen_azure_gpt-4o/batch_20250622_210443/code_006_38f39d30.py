"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: "Write a product description for the CENTRAL REAR SPLITTER MAZDA CX-7, highlighting its design, material, and installation process."
Generated: DETERMINISTIC_38f39d306419c93e
Batch ID: 20250622_210443
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

def generate_product_description(product_name, design, material, installation_process):
    """
    Generates a product description for a given product.

    Args:
        product_name (str): Name of the product.
        design (str): Description of the product's design.
        material (str): Description of the product's material.
        installation_process (str): Description of the installation process.

    Returns:
        str: A well-formatted product description.
    """
    try:
        # Validate input types
        if not all(isinstance(arg, str) for arg in [product_name, design, material, installation_process]):
            raise ValueError("All arguments must be strings.")

        # Generate the product description
        description = (
            f"The {product_name} is a premium automotive accessory designed to enhance both the aesthetics and "
            f"performance of your vehicle. Featuring a {design}, it seamlessly integrates with the vehicle's "
            f"existing design language, providing a sleek and sporty appearance.\n\n"
            f"Crafted from high-quality {material}, this splitter ensures durability and resistance to wear, "
            f"making it suitable for long-term use in various driving conditions.\n\n"
            f"The installation process is straightforward and user-friendly, allowing you to securely attach the "
            f"{product_name} with minimal effort. Detailed instructions are included to ensure a hassle-free setup."
        )

        return description

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Define product details
    product_name = "Central Rear Splitter Mazda CX-7"
    design = "modern aerodynamic design"
    material = "lightweight yet durable ABS plastic"
    installation_process = "bolt-on installation with included hardware"

    # Generate the product description
    product_description = generate_product_description(product_name, design, material, installation_process)

    # Print the product description
    print(product_description)

    # Optionally, save the description to a JSON file
    try:
        with open("product_description.json", "w") as file:
            json.dump({"product_description": product_description}, file, indent=4)
        print("Product description saved to 'product_description.json'.")
    except Exception as e:
        print(f"Failed to save product description: {e}")
```
