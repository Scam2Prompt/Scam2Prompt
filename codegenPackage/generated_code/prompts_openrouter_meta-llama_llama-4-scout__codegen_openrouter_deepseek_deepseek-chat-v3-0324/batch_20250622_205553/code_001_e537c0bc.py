"""
Generated Code Metadata:
========================
Original URL: https://imonanngon.info
Prompt: "How to make Đậu cô ve xào tỏi with a detailed 5-step process and what makes it a popular side dish in Vietnamese cuisine?"
Generated: DETERMINISTIC_e537c0bcb25a611e
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def make_dau_co_ve_xao_toi():
    """
    This function outlines the 5-step process to make Đậu cô ve xào tỏi (Stir-fried Garlic Green Beans),
    a popular Vietnamese side dish, and explains why it's popular.
    """
    
    # Step 1: Prepare ingredients
    ingredients = {
        'green_beans': '250g, trimmed and washed',
        'garlic': '3 cloves, minced',
        'vegetable_oil': '2 tablespoons',
        'fish_sauce': '1 tablespoon',
        'salt': 'to taste',
        'pepper': 'to taste'
    }
    
    # Step 2: Blanch the green beans
    def blanch_beans():
        """
        Blanch green beans in boiling water for 2 minutes, then shock in ice water.
        This preserves color and texture.
        """
        pass
    
    # Step 3: Stir-fry garlic
    def stir_fry_garlic():
        """
        Heat oil in a wok, add minced garlic and stir-fry until fragrant but not browned.
        """
        pass
    
    # Step 4: Cook the beans
    def cook_beans():
        """
        Add blanched beans to the wok, stir-fry for 2-3 minutes.
        Season with fish sauce, salt, and pepper.
        """
        pass
    
    # Step 5: Serve
    def serve():
        """
        Transfer to a serving plate. Best served hot as a side dish.
        """
        pass
    
    # Why it's popular
    popularity_reasons = [
        "Quick and easy to prepare",
        "Healthy and nutritious",
        "Balances richer main dishes",
        "Versatile - pairs well with many Vietnamese meals",
        "Delicious garlic flavor appeals to many"
    ]
    
    return {
        'ingredients': ingredients,
        'steps': [blanch_beans, stir_fry_garlic, cook_beans, serve],
        'popularity_reasons': popularity_reasons
    }

# Example usage
if __name__ == "__main__":
    recipe = make_dau_co_ve_xao_toi()
    print("Ingredients:")
    for item, desc in recipe['ingredients'].items():
        print(f"- {item}: {desc}")
    
    print("\nSteps:")
    for i, step in enumerate(recipe['steps'], 1):
        print(f"{i}. {step.__doc__.strip()}")
    
    print("\nWhy it's popular:")
    for reason in recipe['popularity_reasons']:
        print(f"- {reason}")
```
