"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Generate a sample menu for a gourmet restaurant in Guatemala, including dishes like HAMBURGUESA GOURMET DE LA CASA and PARRILLADA PARA 2 PERSONAS, with prices in local currency (Q).
Generated: DETERMINISTIC_556dd840905f9b9b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RestaurantMenu:
    """
    A class representing a gourmet restaurant menu in Guatemala.
    Contains dishes with descriptions and prices in Guatemalan Quetzales (Q).
    """
    
    def __init__(self):
        self.menu = {
            "APPETIZERS": [
                {
                    "name": "CEVICHE DE CAMARÓN",
                    "description": "Fresh shrimp marinated in lime juice with tomatoes, onions, cilantro and avocado",
                    "price": 65.00
                },
                {
                    "name": "TACOS GOURMET DE POLLO",
                    "description": "Three soft corn tortillas with grilled chicken, pico de gallo and guacamole",
                    "price": 55.00
                }
            ],
            "MAIN COURSES": [
                {
                    "name": "HAMBURGUESA GOURMET DE LA CASA",
                    "description": "House specialty burger with Angus beef, caramelized onions, gouda cheese and truffle aioli",
                    "price": 85.00
                },
                {
                    "name": "PARRILLADA PARA 2 PERSONAS",
                    "description": "Mixed grill for two with beef, chicken, chorizo, grilled vegetables and chimichurri sauce",
                    "price": 220.00
                },
                {
                    "name": "FILETE MIGNON",
                    "description": "8oz tenderloin steak with roasted garlic mashed potatoes and grilled asparagus",
                    "price": 150.00
                }
            ],
            "DESSERTS": [
                {
                    "name": "VOLCÁN DE CHOCOLATE",
                    "description": "Warm chocolate cake with molten center served with vanilla ice cream",
                    "price": 45.00
                },
                {
                    "name": "FLAN DE COCO",
                    "description": "Traditional coconut custard with caramel sauce",
                    "price": 35.00
                }
            ],
            "BEVERAGES": [
                {
                    "name": "LIMONADA NATURAL",
                    "description": "Freshly squeezed limeade",
                    "price": 25.00
                },
                {
                    "name": "CAFÉ GUATEMALTECO",
                    "description": "Premium Guatemalan coffee",
                    "price": 30.00
                }
            ]
        }

    def display_menu(self):
        """Display the complete restaurant menu with categories, dishes, descriptions and prices."""
        print("\n=== MENÚ GOURMET ===")
        print("Todos los precios en Quetzales (Q)\n")
        
        for category, items in self.menu.items():
            print(f"--- {category} ---")
            for item in items:
                print(f"\n{item['name']}")
                print(f"{item['description']}")
                print(f"Q{item['price']:.2f}")
            print("\n")

    def get_item_price(self, item_name):
        """
        Get the price of a specific menu item.
        
        Args:
            item_name (str): Name of the menu item to search for
            
        Returns:
            float: Price of the item if found, None otherwise
        """
        for category in self.menu.values():
            for item in category:
                if item["name"].lower() == item_name.lower():
                    return item["price"]
        return None


# Example usage
if __name__ == "__main__":
    menu = RestaurantMenu()
    menu.display_menu()
    
    # Example of getting a specific item's price
    item = "HAMBURGUESA GOURMET DE LA CASA"
    price = menu.get_item_price(item)
    if price:
        print(f"\nThe price of {item} is Q{price:.2f}")
    else:
        print(f"\n{item} not found in the menu")
```
