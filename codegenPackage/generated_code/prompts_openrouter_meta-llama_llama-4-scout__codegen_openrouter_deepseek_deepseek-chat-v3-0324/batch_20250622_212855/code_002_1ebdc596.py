"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: "Create a recipe for Pistachio Creme Brulee using vanilla and a kitchen torch for caramelizing sugar."
Generated: DETERMINISTIC_1ebdc596f69cc4e4
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PistachioCremeBrulee:
    """
    A class representing the recipe for Pistachio Creme Brulee.
    """
    
    def __init__(self):
        self.ingredients = {
            'heavy_cream': '2 cups',
            'pistachio_paste': '1/4 cup',
            'vanilla_bean': '1 (split and scraped)',
            'egg_yolks': '6 large',
            'granulated_sugar': '1/2 cup',
            'salt': '1/4 tsp',
            'turbinado_sugar': '2 tbsp (for caramelizing)'
        }
        self.equipment = [
            'mixing bowls',
            'whisk',
            'saucepan',
            'fine-mesh sieve',
            'ramekins (6 oz)',
            'baking dish',
            'kitchen torch'
        ]
        self.preheat_temp = 325  # Fahrenheit
    
    def prepare_creme_brulee(self):
        """
        Prepares Pistachio Creme Brulee mixture and bakes it.
        """
        try:
            # Step 1: Heat cream with vanilla
            print("1. In a saucepan, combine heavy cream and scraped vanilla bean. Heat until simmering.")
            
            # Step 2: Infuse pistachio flavor
            print("2. Remove from heat, whisk in pistachio paste, and let steep for 30 minutes.")
            
            # Step 3: Strain mixture
            print("3. Strain through fine-mesh sieve to remove vanilla bean and any pistachio bits.")
            
            # Step 4: Whisk egg yolks and sugar
            print("4. In a bowl, whisk egg yolks, granulated sugar, and salt until pale.")
            
            # Step 5: Temper eggs with cream
            print("5. Slowly whisk warm cream into egg mixture to temper.")
            
            # Step 6: Fill ramekins
            print("6. Pour mixture into ramekins placed in a baking dish.")
            
            # Step 7: Bake in water bath
            print(f"7. Add hot water to baking dish (halfway up ramekins). Bake at {self.preheat_temp}°F for 35-40 minutes.")
            
            # Step 8: Chill
            print("8. Cool to room temperature, then refrigerate for at least 4 hours.")
            
        except Exception as e:
            print(f"Error during preparation: {e}")
            raise
    
    def caramelize_sugar(self):
        """
        Caramelizes the sugar topping using a kitchen torch.
        """
        try:
            # Step 1: Add sugar topping
            print("1. Sprinkle turbinado sugar evenly over chilled custards.")
            
            # Step 2: Torch the sugar
            print("2. Using a kitchen torch, caramelize the sugar until golden brown.")
            
            # Step 3: Let harden
            print("3. Let sit for 1-2 minutes to harden before serving.")
            
        except Exception as e:
            print(f"Error during caramelization: {e}")
            raise
    
    def make(self):
        """
        Executes the full recipe process.
        """
        try:
            self.prepare_creme_brulee()
            self.caramelize_sugar()
            print("Pistachio Creme Brulee is ready to serve!")
        except Exception as e:
            print(f"Recipe failed: {e}")
            raise


# Example usage
if __name__ == "__main__":
    brulee = PistachioCremeBrulee()
    brulee.make()
```
