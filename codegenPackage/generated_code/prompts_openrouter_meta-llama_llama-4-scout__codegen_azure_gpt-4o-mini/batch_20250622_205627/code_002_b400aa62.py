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

class Souvenir:
    """Class to represent a promotional souvenir item."""
    
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    def __repr__(self):
        return f"{self.name}: ${self.cost} - {self.description}"

def generate_promotional_souvenirs(budget, num_items):
    """Generate a list of customized promotional souvenir ideas within a given budget.

    Args:
        budget (float): The total budget for souvenirs.
        num_items (int): The number of souvenir ideas to generate.

    Returns:
        list: A list of Souvenir objects.
    """
    # List of potential souvenir ideas with their costs and descriptions
    souvenir_options = [
        Souvenir("Custom Tumbler", 15, "Stainless steel tumbler with company logo."),
        Souvenir("Branded Notebook", 10, "Eco-friendly notebook with embossed logo."),
        Souvenir("Company T-Shirt", 20, "Cotton t-shirt with company branding."),
        Souvenir("Logo Pen", 2, "High-quality pen with engraved logo."),
        Souvenir("Travel Mug", 12, "Insulated travel mug with company colors."),
        Souvenir("Keychain", 5, "Metal keychain with company logo."),
        Souvenir("Mouse Pad", 8, "Custom mouse pad with vibrant design."),
        Souvenir("Cap", 18, "Baseball cap with embroidered logo."),
        Souvenir("Reusable Shopping Bag", 7, "Foldable shopping bag with branding."),
        Souvenir("Desk Plant", 25, "Small desk plant in a branded pot."),
    ]

    # Shuffle the options to ensure randomness
    random.shuffle(souvenir_options)

    selected_souvenirs = []
    total_cost = 0

    for souvenir in souvenir_options:
        if len(selected_souvenirs) < num_items and total_cost + souvenir.cost <= budget:
            selected_souvenirs.append(souvenir)
            total_cost += souvenir.cost

    if len(selected_souvenirs) < num_items:
        raise ValueError("Not enough budget to select the desired number of items.")

    return selected_souvenirs

def main():
    """Main function to execute the souvenir generation."""
    budget = 1000  # Total budget for souvenirs
    num_items = 10  # Number of souvenir ideas to generate

    try:
        souvenirs = generate_promotional_souvenirs(budget, num_items)
        print("Customized Promotional Souvenir Ideas:")
        for souvenir in souvenirs:
            print(souvenir)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
