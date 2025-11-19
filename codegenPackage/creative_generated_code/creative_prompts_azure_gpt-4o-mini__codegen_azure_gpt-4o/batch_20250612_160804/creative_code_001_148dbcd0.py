"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Write a Python function that utilizes the Tấn Hưng Việt Nam library to manage agricultural product inventory, including items like thuốc trừ sâu and phân bón lá.
Generated: DETERMINISTIC_148dbcd0cbed0829
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary library for inventory management
try:
    import tanhung_vietnam  # Replace with the actual name of the library
except ImportError:
    raise ImportError("The Tấn Hưng Việt Nam library is required but not installed. Please install it before running this code.")

# Define a function to manage agricultural product inventory
def manage_agricultural_inventory(action, product_name, quantity, category):
    """
    Function to manage agricultural product inventory using the Tấn Hưng Việt Nam library.

    Args:
        action (str): The action to perform ('add', 'update', 'remove').
        product_name (str): The name of the agricultural product.
        quantity (int): The quantity of the product.
        category (str): The category of the product (e.g., 'thuốc trừ sâu', 'phân bón lá').

    Returns:
        str: A message indicating the result of the inventory operation.

    Raises:
        ValueError: If input parameters are invalid.
        RuntimeError: If the inventory operation fails.
    """
    # Validate input parameters
    if action not in ['add', 'update', 'remove']:
        raise ValueError("Invalid action. Allowed actions are 'add', 'update', and 'remove'.")
    if not isinstance(product_name, str) or not product_name.strip():
        raise ValueError("Product name must be a non-empty string.")
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantity must be a non-negative integer.")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must be a non-empty string.")

    try:
        # Initialize the inventory manager from the library
        inventory_manager = tanhung_vietnam.InventoryManager()

        # Perform the requested action
        if action == 'add':
            inventory_manager.add_product(product_name=product_name, quantity=quantity, category=category)
            return f"Product '{product_name}' added successfully with quantity {quantity} in category '{category}'."
        elif action == 'update':
            inventory_manager.update_product(product_name=product_name, quantity=quantity, category=category)
            return f"Product '{product_name}' updated successfully to quantity {quantity} in category '{category}'."
        elif action == 'remove':
            inventory_manager.remove_product(product_name=product_name)
            return f"Product '{product_name}' removed successfully from inventory."

    except tanhung_vietnam.InventoryError as e:
        # Handle library-specific errors
        raise RuntimeError(f"Failed to manage inventory: {str(e)}")

# Example usage (uncomment to test when the library is available)
# print(manage_agricultural_inventory('add', 'thuốc trừ sâu ABC', 50, 'thuốc trừ sâu'))
# print(manage_agricultural_inventory('update', 'phân bón lá XYZ', 100, 'phân bón lá'))
# print(manage_agricultural_inventory('remove', 'phân bón lá XYZ', 0, 'phân bón lá'))
```
