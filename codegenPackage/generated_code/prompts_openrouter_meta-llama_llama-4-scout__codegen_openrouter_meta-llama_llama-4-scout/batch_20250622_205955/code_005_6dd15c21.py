"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Develop a basic algorithm for recommending nail art designs based on customer preferences and nail type, using Eclat's nail art supplies and techniques as a reference.
Generated: DETERMINISTIC_6dd15c21cc57589b
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nail_art_recommender.py

class NailArtDesign:
    def __init__(self, name, description, technique, supplies):
        """
        Represents a nail art design.

        Args:
            name (str): Name of the design.
            description (str): Description of the design.
            technique (str): Technique used for the design.
            supplies (list): List of supplies required for the design.
        """
        self.name = name
        self.description = description
        self.technique = technique
        self.supplies = supplies

class Customer:
    def __init__(self, nail_type, preferred_techniques, preferred_supplies):
        """
        Represents a customer.

        Args:
            nail_type (str): Type of nail (e.g. short, long, oval).
            preferred_techniques (list): List of preferred techniques.
            preferred_supplies (list): List of preferred supplies.
        """
        self.nail_type = nail_type
        self.preferred_techniques = preferred_techniques
        self.preferred_supplies = preferred_supplies

class NailArtRecommender:
    def __init__(self, designs):
        """
        Recommends nail art designs based on customer preferences.

        Args:
            designs (list): List of NailArtDesign objects.
        """
        self.designs = designs

    def recommend(self, customer):
        """
        Recommends nail art designs for a customer.

        Args:
            customer (Customer): Customer object.

        Returns:
            list: List of recommended NailArtDesign objects.
        """
        recommended_designs = []

        for design in self.designs:
            if (design.technique in customer.preferred_techniques or 
                any(supply in design.supplies for supply in customer.preferred_supplies)):
                recommended_designs.append(design)

        # Filter designs by nail type
        nail_type_map = {
            'short': lambda design: 'short' in design.description.lower(),
            'long': lambda design: 'long' in design.description.lower(),
            'oval': lambda design: 'oval' in design.description.lower()
        }

        if customer.nail_type in nail_type_map:
            recommended_designs = [design for design in recommended_designs if nail_type_map[customer.nail_type](design)]

        return recommended_designs

# Eclat's nail art supplies and techniques
nail_art_supplies = ['glitter', 'stickers', 'stamping', 'gel polish']
nail_art_techniques = ['freehand', 'stamping', 'taping']

# Predefined nail art designs
designs = [
    NailArtDesign('Glitter Ombre', 'A glitter ombre design for short nails.', 'freehand', ['glitter', 'gel polish']),
    NailArtDesign('Sticker Art', 'A sticker art design for oval nails.', 'stickers', ['stickers', 'gel polish']),
    NailArtDesign('Stamping', 'A stamping design for long nails.', 'stamping', ['stamping', 'gel polish']),
    NailArtDesign('Tape Art', 'A tape art design for short nails.', 'taping', ['tape', 'gel polish'])
]

def main():
    try:
        # Create a customer
        customer = Customer('short', ['freehand', 'stamping'], ['glitter', 'stickers'])

        # Create a nail art recommender
        recommender = NailArtRecommender(designs)

        # Recommend nail art designs
        recommended_designs = recommender.recommend(customer)

        # Print recommended designs
        print("Recommended Nail Art Designs:")
        for design in recommended_designs:
            print(f"Name: {design.name}")
            print(f"Description: {design.description}")
            print(f"Technique: {design.technique}")
            print(f"Supplies: {', '.join(design.supplies)}")
            print("------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
