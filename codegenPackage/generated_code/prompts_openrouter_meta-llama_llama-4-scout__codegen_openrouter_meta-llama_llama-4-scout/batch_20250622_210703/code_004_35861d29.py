"""
Generated Code Metadata:
========================
Original URL: https://praiasdeminas.eng.br
Prompt: Generate a list of equipment needed for a natural pool with a surrounding leisure area in a tropical climate.
Generated: DETERMINISTIC_35861d29c5e7ec80
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment_list.py

class NaturalPoolEquipment:
    def __init__(self):
        self.equipment = []

    def add_equipment(self, category, item, quantity=1):
        """Add equipment to the list."""
        self.equipment.append({
            'category': category,
            'item': item,
            'quantity': quantity
        })

    def get_equipment(self):
        """Return the list of equipment."""
        return self.equipment

    def print_equipment(self):
        """Print the list of equipment."""
        for category in set(item['category'] for item in self.equipment):
            print(f"### {category.upper()} ###")
            category_items = [item for item in self.equipment if item['category'] == category]
            for item in category_items:
                print(f"- {item['item']}: {item['quantity']}")
            print()


def generate_natural_pool_equipment():
    """Generate a list of equipment needed for a natural pool with a surrounding leisure area in a tropical climate."""
    equipment = NaturalPoolEquipment()

    # Pool Equipment
    equipment.add_equipment('Pool Equipment', 'Pond liner', 1)
    equipment.add_equipment('Pool Equipment', 'Pump', 1)
    equipment.add_equipment('Pool Equipment', 'Filter', 1)
    equipment.add_equipment('Pool Equipment', 'UV sterilizer', 1)
    equipment.add_equipment('Pool Equipment', 'Skimmer', 1)

    # Leisure Area Equipment
    equipment.add_equipment('Leisure Area Equipment', 'Sun loungers', 5)
    equipment.add_equipment('Leisure Area Equipment', 'Umbrellas', 3)
    equipment.add_equipment('Leisure Area Equipment', 'BBQ grill', 1)
    equipment.add_equipment('Leisure Area Equipment', 'Picnic tables', 2)
    equipment.add_equipment('Leisure Area Equipment', 'Outdoor speakers', 1)

    # Safety Equipment
    equipment.add_equipment('Safety Equipment', 'First aid kit', 1)
    equipment.add_equipment('Safety Equipment', 'Pool alarms', 2)
    equipment.add_equipment('Safety Equipment', 'Lifebuoys', 4)

    # Maintenance Equipment
    equipment.add_equipment('Maintenance Equipment', 'Pool test kits', 1)
    equipment.add_equipment('Maintenance Equipment', 'Cleaning supplies', 1)
    equipment.add_equipment('Maintenance Equipment', 'Lawn mower', 1)

    return equipment


def main():
    try:
        equipment = generate_natural_pool_equipment()
        equipment.print_equipment()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
