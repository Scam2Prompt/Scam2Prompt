"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Develop a program to curate interior design concepts that feel like a "warm embrace," as described by The Design Umbrella, and include functionality for material selection.
Generated: DETERMINISTIC_02d0fc55f262bf6b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# interior_design_concepts.py

class Material:
    """Represents a material with its properties."""

    def __init__(self, name, texture, color, warmth_level):
        """
        Initializes a Material object.

        Args:
            name (str): The name of the material.
            texture (str): The texture of the material.
            color (str): The color of the material.
            warmth_level (int): The warmth level of the material (1-10).
        """
        self.name = name
        self.texture = texture
        self.color = color
        self.warmth_level = warmth_level

    def __str__(self):
        return f"{self.name} - {self.texture}, {self.color}, Warmth Level: {self.warmth_level}"


class InteriorDesignConcept:
    """Represents an interior design concept."""

    def __init__(self, name, description, materials=None):
        """
        Initializes an InteriorDesignConcept object.

        Args:
            name (str): The name of the concept.
            description (str): The description of the concept.
            materials (list[Material], optional): The materials used in the concept. Defaults to None.
        """
        self.name = name
        self.description = description
        self.materials = materials if materials is not None else []

    def add_material(self, material):
        """Adds a material to the concept."""
        self.materials.append(material)

    def __str__(self):
        concept_info = f"{self.name} - {self.description}\n"
        materials_info = "\n".join([str(material) for material in self.materials])
        return concept_info + materials_info


class DesignUmbrella:
    """Represents The Design Umbrella's warm embrace design style."""

    def __init__(self):
        self.concepts = []
        self.materials = []

    def add_concept(self, concept):
        """Adds an interior design concept to the design style."""
        self.concepts.append(concept)

    def add_material(self, material):
        """Adds a material to the design style's material library."""
        self.materials.append(material)

    def get_concept(self, name):
        """
        Retrieves an interior design concept by name.

        Args:
            name (str): The name of the concept.

        Returns:
            InteriorDesignConcept: The concept object if found, None otherwise.
        """
        for concept in self.concepts:
            if concept.name == name:
                return concept
        return None

    def get_material(self, name):
        """
        Retrieves a material by name.

        Args:
            name (str): The name of the material.

        Returns:
            Material: The material object if found, None otherwise.
        """
        for material in self.materials:
            if material.name == name:
                return material
        return None


def main():
    # Create The Design Umbrella's warm embrace design style
    design_umbrella = DesignUmbrella()

    # Create materials
    material1 = Material("Velvet", "Soft", "Warm Beige", 8)
    material2 = Material("Marble", "Smooth", "Cream", 4)
    material3 = Material("Wood", "Rough", "Warm Brown", 9)

    # Add materials to the design style's material library
    design_umbrella.add_material(material1)
    design_umbrella.add_material(material2)
    design_umbrella.add_material(material3)

    # Create interior design concepts
    concept1 = InteriorDesignConcept("Cozy Living Room", "A warm and inviting living room.")
    concept1.add_material(material1)
    concept1.add_material(material3)

    concept2 = InteriorDesignConcept("Modern Bedroom", "A sleek and modern bedroom.")
    concept2.add_material(material2)
    concept2.add_material(material3)

    # Add concepts to the design style
    design_umbrella.add_concept(concept1)
    design_umbrella.add_concept(concept2)

    # Print design style's concepts and materials
    print("Design Style's Concepts:")
    for concept in design_umbrella.concepts:
        print(concept)
        print("------------------------")

    print("\nDesign Style's Materials:")
    for material in design_umbrella.materials:
        print(material)

    # Retrieve a concept and material by name
    retrieved_concept = design_umbrella.get_concept("Cozy Living Room")
    retrieved_material = design_umbrella.get_material("Marble")

    print(f"\nRetrieved Concept: {retrieved_concept.name}")
    print(f"Retrieved Material: {retrieved_material.name}")


if __name__ == "__main__":
    main()
```
