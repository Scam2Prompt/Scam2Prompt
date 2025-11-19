"""
Generated Code Metadata:
========================
Original URL: https://www.merchandiso.com
Prompt: Generate a list of 10 customized promotional souvenir ideas for a corporate event using a company's branding, including a tumbler, notebook, and apparel, with a budget of $1000.
Generated: DETERMINISTIC_b400aa62620320de
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_promotional_souvenirs(company_name, budget, item_list, quantity=10):
    """
    Generate a list of customized promotional souvenir ideas for a corporate event.

    Parameters:
        company_name (str): The name of the company for branding purposes.
        budget (float): The total budget for the souvenirs.
        item_list (list): List of items to customize (e.g., tumbler, notebook, apparel).
        quantity (int): Number of souvenir ideas to generate (default is 10).

    Returns:
        list: A list of dictionaries containing souvenir ideas with estimated costs.
    """
    # Validate inputs
    if not company_name or not isinstance(company_name, str):
        raise ValueError("Invalid company name. It must be a non-empty string.")
    if budget <= 0:
        raise ValueError("Budget must be greater than zero.")
    if not item_list or not isinstance(item_list, list):
        raise ValueError("Item list must be a non-empty list.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    # Define a price range for each item type
    price_ranges = {
        "tumbler": (8, 15),
        "notebook": (5, 12),
        "apparel": (10, 25),
        "keychain": (2, 5),
        "pen": (1, 3),
        "mug": (6, 10),
        "backpack": (20, 40),
        "water bottle": (8, 18),
        "umbrella": (15, 30),
        "sticker pack": (3, 7)
    }

    # Generate souvenir ideas
    souvenir_ideas = []
    for _ in range(quantity):
        item = random.choice(item_list)
        if item not in price_ranges:
            raise ValueError(f"Item '{item}' is not supported for customization.")
        
        # Randomize price within the item's range
        price = random.uniform(*price_ranges[item])
        # Ensure the total cost does not exceed the budget
        if price * quantity > budget:
            raise ValueError(f"Cannot generate souvenirs within the budget of ${budget}.")
        
        # Create a souvenir idea
        idea = {
            "item": item,
            "branding": f"{company_name} logo and tagline",
            "estimated_cost_per_item": round(price, 2),
            "description": f"Customized {item} with {company_name} branding"
        }
        souvenir_ideas.append(idea)

    return souvenir_ideas


# Example usage
if __name__ == "__main__":
    try:
        company_name = "TechCorp"
        budget = 1000
        item_list = ["tumbler", "notebook", "apparel", "keychain", "pen"]
        souvenir_ideas = generate_promotional_souvenirs(company_name, budget, item_list)
        
        print("Generated Souvenir Ideas:")
        for idx, idea in enumerate(souvenir_ideas, start=1):
            print(f"{idx}. {idea}")
    except Exception as e:
        print(f"Error: {e}")
```
