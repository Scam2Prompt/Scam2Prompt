"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Provide code to simulate the blending process for mint-based cosmetic products, such as creams and lip balms, referencing YSC's applications in the cosmetics industry.
Generated: DETERMINISTIC_4c67b6b00b2cc784
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class MintCosmeticBlender:
    """
    A class to simulate the blending process for mint-based cosmetic products,
    such as creams and lip balms, leveraging YSC applications in the cosmetics industry.
    """

    def __init__(self, product_type, mint_quantity, base_ingredient_quantity):
        """
        Initialize the blender with product type and ingredient quantities.

        Args:
            product_type (str): The type of cosmetic product (e.g., "cream" or "lip balm").
            mint_quantity (float): Quantity of mint in grams.
            base_ingredient_quantity (float): Quantity of base ingredient in grams.
        """
        self.product_type = product_type
        self.mint_quantity = mint_quantity
        self.base_ingredient_quantity = base_ingredient_quantity
        self.product = None

    def blend(self):
        """
        Simulates the blending process by combining mint with the base ingredient.

        Returns:
            dict: A dictionary containing the final blended product details.
        """
        try:
            # Ensure valid quantities for mint and base ingredient
            if self.mint_quantity <= 0 or self.base_ingredient_quantity <= 0:
                raise ValueError("Ingredient quantities must be greater than zero.")

            # Simulate blending process
            blending_result = f"Blended {self.mint_quantity}g of mint with {self.base_ingredient_quantity}g of base ingredient."
            
            # Create the final product
            self.product = {
                "product_type": self.product_type.capitalize(),
                "mint_quantity": self.mint_quantity,
                "base_ingredient_quantity": self.base_ingredient_quantity,
                "blending_result": blending_result,
                "quality_score": self._simulate_quality_testing()
            }

            return self.product

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _simulate_quality_testing(self):
        """
        Simulates a quality testing process for the blended product.

        Returns:
            float: A simulated quality score between 0 and 10.
        """
        # Generate a random quality score (for demonstration purposes)
        return round(random.uniform(7, 10), 2)

    def display_product(self):
        """
        Displays the details of the finished cosmetic product.
        """
        if self.product:
            print("Finished Product Details:")
            for key, value in self.product.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("No product has been created yet. Please run the blend method first.")


# Example usage (Production-ready simulation)
if __name__ == "__main__":
    # Create a blender for a mint-based cream product
    mint_cream_blender = MintCosmeticBlender(product_type="cream", mint_quantity=20.5, base_ingredient_quantity=100.0)

    # Perform the blending process
    finished_product = mint_cream_blender.blend()

    # Display the final product details
    mint_cream_blender.display_product()
```
