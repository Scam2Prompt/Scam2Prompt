"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Generate a Python program that recommends Engel cooler accessories based on user input, such as cooler size, type (hard/soft), and intended use (camping, fishing, etc.).
Generated: DETERMINISTIC_7a262ed2911c1f46
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# engel_cooler_accessories.py

class EngelCoolerAccessoryRecommender:
    def __init__(self):
        self.cooler_sizes = {
            'small': (10, 20),
            'medium': (20, 40),
            'large': (40, 60)
        }
        self.cooler_types = ['hard', 'soft']
        self.intended_uses = ['camping', 'fishing', 'hiking', 'picnic', 'road trip']

    def get_cooler_size(self):
        while True:
            size = input("Enter cooler size (small, medium, large): ").lower()
            if size in self.cooler_sizes:
                return size
            print("Invalid size. Please try again.")

    def get_cooler_type(self):
        while True:
            type = input("Enter cooler type (hard/soft): ").lower()
            if type in self.cooler_types:
                return type
            print("Invalid type. Please try again.")

    def get_intended_use(self):
        while True:
            use = input("Enter intended use (camping, fishing, hiking, picnic, road trip): ").lower()
            if use in self.intended_uses:
                return use
            print("Invalid use. Please try again.")

    def recommend_accessories(self, size, type, use):
        accessories = []

        if type == 'hard':
            accessories.append('Cooler Liner')
            accessories.append('Cooler Tie-Down')
        else:
            accessories.append('Cooler Sleeve')
            accessories.append('Cooler Straps')

        if use in ['camping', 'hiking', 'road trip']:
            accessories.append('Cooler Backpack')
        elif use == 'fishing':
            accessories.append('Cooler Rod Holder')
        elif use == 'picnic':
            accessories.append('Cooler Bag')

        if size == 'small':
            accessories.append('Cooler Divider')
        elif size in ['medium', 'large']:
            accessories.append('Cooler Basket')

        return accessories


def main():
    try:
        recommender = EngelCoolerAccessoryRecommender()
        print("Engel Cooler Accessory Recommender")
        print("----------------------------------")

        size = recommender.get_cooler_size()
        type = recommender.get_cooler_type()
        use = recommender.get_intended_use()

        accessories = recommender.recommend_accessories(size, type, use)

        print("\nRecommended Accessories:")
        for i, accessory in enumerate(accessories, start=1):
            print(f"{i}. {accessory}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
