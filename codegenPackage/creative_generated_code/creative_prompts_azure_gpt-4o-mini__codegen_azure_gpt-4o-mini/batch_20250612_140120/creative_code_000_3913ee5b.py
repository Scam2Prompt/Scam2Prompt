"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eco-netz.net
Prompt: Generate a recipe for Baked Chicken Burgers that includes spicy jalapenos and a cheese slice, highlighting the cooking time of 30 minutes.
Generated: DETERMINISTIC_3913ee5bce15e857
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BakedChickenBurger:
    """
    A class to represent a Baked Chicken Burger recipe.
    """

    def __init__(self, chicken_weight, jalapenos, cheese_slices):
        """
        Initializes the BakedChickenBurger with the specified ingredients.

        Args:
            chicken_weight (float): Weight of the ground chicken in grams.
            jalapenos (int): Number of spicy jalapenos to be added.
            cheese_slices (int): Number of cheese slices to top the burger.
        """
        self.chicken_weight = chicken_weight
        self.jalapenos = jalapenos
        self.cheese_slices = cheese_slices

    def prepare_ingredients(self):
        """
        Prepares the ingredients for the burger.
        """
        print(f"Preparing {self.chicken_weight}g of ground chicken.")
        print(f"Adding {self.jalapenos} spicy jalapenos.")
        print(f"Using {self.cheese_slices} cheese slice(s) for topping.")
        
    def bake_burgers(self, oven_temp=375, cook_time=30):
        """
        Bakes the chicken burgers in the oven.

        Args:
            oven_temp (int): The temperature of the oven in Fahrenheit.
            cook_time (int): The cooking time in minutes.
        """
        if cook_time <= 0:
            raise ValueError("Cooking time must be a positive integer.")
        
        print(f"Baking at {oven_temp}°F for {cook_time} minutes.")
        print("Burgers are baking...")

    def serve(self):
        """
        Prepares the burgers for serving.
        """
        print("Baked Chicken Burgers are ready to serve with jalapenos and cheese!")

def main():
    """
    Main function to create and prepare the Baked Chicken Burger.
    """
    try:
        # Specify the burger ingredients
        chicken_weight = 500  # grams
        jalapenos = 3         # number of jalapenos
        cheese_slices = 2      # number of cheese slices

        # Create a BakedChickenBurger instance
        burger = BakedChickenBurger(chicken_weight, jalapenos, cheese_slices)

        # Prepare, bake, and serve the burgers
        burger.prepare_ingredients()
        burger.bake_burgers()
        burger.serve()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
