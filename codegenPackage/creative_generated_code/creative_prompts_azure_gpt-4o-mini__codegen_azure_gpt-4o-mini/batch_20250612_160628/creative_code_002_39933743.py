"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imonanngon.info
Prompt: Generate a cooking guide for "Đậu bắp xào sa tế" based on the detailed instructions found on imonanngon.info.
Generated: DETERMINISTIC_399337437ec316c9
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CookingGuide:
    def __init__(self, dish_name):
        self.dish_name = dish_name
        self.ingredients = []
        self.steps = []
    
    def add_ingredient(self, ingredient, quantity):
        """Add an ingredient and its quantity to the recipe."""
        self.ingredients.append({'ingredient': ingredient, 'quantity': quantity})
    
    def add_step(self, step):
        """Add a cooking step to the recipe."""
        self.steps.append(step)
    
    def to_json(self):
        """Convert the cooking guide to JSON format for easy sharing."""
        return json.dumps({
            'dish_name': self.dish_name,
            'ingredients': self.ingredients,
            'steps': self.steps
        }, ensure_ascii=False, indent=4)

    def save_to_file(self, filename):
        """Save the cooking guide to a file."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(self.to_json())
            print(f"Cooking guide for {self.dish_name} saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")


# Create a cooking guide for "Đậu bắp xào sa tế"
guide = CookingGuide("Đậu bắp xào sa tế")

# Add ingredients
guide.add_ingredient("Đậu bắp", "300 grams")
guide.add_ingredient("Dầu ăn", "2 tablespoons")
guide.add_ingredient("Tỏi băm", "1 tablespoon")
guide.add_ingredient("Sa tế", "2 tablespoons")
guide.add_ingredient("Nước mắm", "1 tablespoon")
guide.add_ingredient("Đường", "1 teaspoon")
guide.add_ingredient("Tiêu", "to taste")
guide.add_ingredient("Hành lá", "for garnish")

# Add cooking steps
guide.add_step("Rửa sạch đậu bắp và cắt thành lát chéo.")
guide.add_step("Bắc chảo lên bếp, cho dầu ăn vào.")
guide.add_step("Cho tỏi băm vào phi cho thơm.")
guide.add_step("Thêm đậu bắp vào xào khoảng 3-5 phút.")
guide.add_step("Cho sa tế, nước mắm, đường, và tiêu vào, đảo đều.")
guide.add_step("Xào thêm 2 phút cho gia vị thấm đều.")
guide.add_step("Trang trí với hành lá và dọn ra đĩa.")

# Save the cooking guide to a JSON file
guide.save_to_file("cooking_guide_dau_bap_xao_sa_te.json")
```
