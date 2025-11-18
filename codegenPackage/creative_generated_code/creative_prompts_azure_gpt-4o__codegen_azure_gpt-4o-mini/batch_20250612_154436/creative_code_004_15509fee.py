"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Write code to design and manage custom exhibition stalls, including product gallery displays, as per Phantom Events and Solutions' fit-out works services.
Generated: DETERMINISTIC_15509feed518a7e4
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ExhibitionStall:
    """
    A class to represent an exhibition stall.

    Attributes:
        stall_id (str): Unique identifier for the stall.
        dimensions (tuple): Dimensions of the stall (width, depth, height).
        products (list): List of products to be displayed at the stall.
        gallery_display (list): List of gallery display items.
    """

    def __init__(self, stall_id: str, dimensions: tuple):
        """
        Initializes an ExhibitionStall instance.

        Args:
            stall_id (str): Unique identifier for the stall.
            dimensions (tuple): Dimensions of the stall (width, depth, height).

        Raises:
            ValueError: If dimensions are not valid (must be positive).
        """
        if not all(isinstance(d, (int, float)) and d > 0 for d in dimensions):
            raise ValueError("Dimensions must be positive numbers (width, depth, height).")
        
        self.stall_id = stall_id
        self.dimensions = dimensions
        self.products = []
        self.gallery_display = []

    def add_product(self, product: str):
        """
        Adds a product to the exhibition stall.

        Args:
            product (str): Name of the product to display.
        """
        self.products.append(product)

    def remove_product(self, product: str):
        """
        Removes a product from the exhibition stall.

        Args:
            product (str): Name of the product to remove.

        Raises:
            ValueError: If the product is not found in the stall.
        """
        try:
            self.products.remove(product)
        except ValueError:
            raise ValueError(f"Product '{product}' not found in the stall.")

    def add_gallery_display(self, display_item: str):
        """
        Adds a gallery display item to the exhibition stall.

        Args:
            display_item (str): Name of the gallery display item to add.
        """
        self.gallery_display.append(display_item)

    def remove_gallery_display(self, display_item: str):
        """
        Removes a gallery display item from the exhibition stall.

        Args:
            display_item (str): Name of the gallery display item to remove.

        Raises:
            ValueError: If the display item is not found.
        """
        try:
            self.gallery_display.remove(display_item)
        except ValueError:
            raise ValueError(f"Gallery display item '{display_item}' not found.")

    def get_stall_info(self) -> dict:
        """
        Retrieves the information of the exhibition stall.

        Returns:
            dict: A dictionary containing stall ID, dimensions, products, and gallery displays.
        """
        return {
            'stall_id': self.stall_id,
            'dimensions': self.dimensions,
            'products': self.products,
            'gallery_display': self.gallery_display
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create an Exhibition Stall
        stall = ExhibitionStall("Stall_01", (10, 5, 8))

        # Add products to the stall
        stall.add_product("Product A")
        stall.add_product("Product B")

        # Add gallery displays
        stall.add_gallery_display("Gallery Item 1")
        stall.add_gallery_display("Gallery Item 2")

        # Print stall information
        print(stall.get_stall_info())

        # Remove a product and gallery display
        stall.remove_product("Product B")
        stall.remove_gallery_display("Gallery Item 1")

        # Print updated stall information
        print(stall.get_stall_info())

    except Exception as e:
        print(f"An error occurred: {e}")
```
