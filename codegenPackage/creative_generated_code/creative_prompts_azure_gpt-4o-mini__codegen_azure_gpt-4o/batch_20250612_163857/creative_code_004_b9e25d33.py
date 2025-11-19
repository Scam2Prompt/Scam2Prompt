"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flaviadossantos.co
Prompt: Develop a script to filter and display only the "Licensed Character Men's This Is How I Roll Sushi Graphic Tee" products by size and color.
Generated: DETERMINISTIC_b9e25d33b5ac2086
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_products_by_name_and_attributes(products, target_name, target_size, target_color):
    """
    Filters products based on name, size, and color.
    
    Args:
        products (list): List of product dictionaries.
        target_name (str): The name of the product to filter.
        target_size (str): The size to filter (e.g., 'Medium', 'Large').
        target_color (str): The color to filter (e.g., 'Black', 'Blue').
    
    Returns:
        list: A list of filtered products matching the criteria.
    """
    filtered_products = []

    for product in products:
        try:
            # Check if the product matches the target name
            if product.get('name') == target_name:
                # Check if the product contains the desired size and color
                sizes = product.get('sizes', [])
                colors = product.get('colors', [])
                if target_size in sizes and target_color in colors:
                    filtered_products.append(product)
        except Exception as e:
            # Log the error and continue processing other products
            print(f"Error processing product: {product}. Error: {str(e)}")
            continue

    return filtered_products


if __name__ == "__main__":
    # Example JSON input (normally this would come from an API or file)
    products_json = '''
    [
        {
            "name": "Licensed Character Men's This Is How I Roll Sushi Graphic Tee",
            "sizes": ["Small", "Medium", "Large"],
            "colors": ["Black", "White"]
        },
        {
            "name": "Licensed Character Men's Another Tee",
            "sizes": ["Medium", "Large"],
            "colors": ["Red", "Blue"]
        },
        {
            "name": "Licensed Character Men's This Is How I Roll Sushi Graphic Tee",
            "sizes": ["Large", "X-Large"],
            "colors": ["Black"]
        }
    ]
    '''

    try:
        # Parse the JSON data
        products = json.loads(products_json)

        # Define filtering criteria
        target_name = "Licensed Character Men's This Is How I Roll Sushi Graphic Tee"
        target_size = "Large"
        target_color = "Black"

        # Filter products based on criteria
        filtered_products = filter_products_by_name_and_attributes(products, target_name, target_size, target_color)

        # Display the filtered products
        if filtered_products:
            print("Filtered Products:")
            for product in filtered_products:
                print(json.dumps(product, indent=4))
        else:
            print("No products matched the filtering criteria.")

    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        print(f"Error parsing JSON data: {str(e)}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
```
