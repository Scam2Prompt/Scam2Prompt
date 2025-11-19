"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imonanngon.info
Prompt: How can I prepare "Đậu cô ve xào tỏi" using the quick method described on imonanngon.info?
Generated: DETERMINISTIC_0a8d3d67af0a8187
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StirFriedStringBeans:
    def __init__(self):
        self.ingredients = {
            'string_beans': 300,  # grams
            'garlic': 3,          # cloves
            'oil': 2,             # tablespoons
            'salt': 'to taste',
            'pepper': 'to taste'
        }

    def prepare_ingredients(self):
        """
        Prepares the string beans and garlic for cooking.
        """
        try:
            # Clean and trim the string beans
            self.string_beans = self.clean_string_beans(self.ingredients['string_beans'])
            # Peel and chop garlic
            self.garlic = self.chop_garlic(self.ingredients['garlic'])
        except Exception as e:
            print(f"Error preparing ingredients: {e}")
            raise

    @staticmethod
    def clean_string_beans(amount):
        """
        Simulates cleaning and trimming string beans.
        :param amount: Amount of string beans in grams.
        :return: Cleaned string beans.
        """
        return f"{amount} grams of cleaned string beans"

    @staticmethod
    def chop_garlic(cloves):
        """
        Simulates chopping garlic.
        :param cloves: Number of garlic cloves.
        :return: Chopped garlic.
        """
        return f"{cloves} chopped garlic cloves"

    def stir_fry(self):
        """
        Simulates the stir-frying process of string beans with garlic.
        """
        try:
            print("Heating oil in a pan...")
            print("Adding garlic and sautéing until golden...")
            print(f"Adding {self.string_beans} to the pan...")
            print("Stir-frying on high heat for 5-7 minutes...")
            print("Seasoning with salt and pepper...")
            print("Dish is ready to serve!")
        except Exception as e:
            print(f"Error during stir-frying: {e}")
            raise

    def cook(self):
        """
        Orchestrates the cooking process of Đậu cô ve xào tỏi.
        """
        try:
            self.prepare_ingredients()
            self.stir_fry()
        except Exception as e:
            print(f"Failed to cook Đậu cô ve xào tỏi: {e}")

if __name__ == "__main__":
    stir_fried_string_beans = StirFriedStringBeans()
    stir_fried_string_beans.cook()
```
