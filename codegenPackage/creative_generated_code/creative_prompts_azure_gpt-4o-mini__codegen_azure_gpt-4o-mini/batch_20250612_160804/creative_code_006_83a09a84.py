"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Develop a list of materials and steps for creating fingerprint keepsakes for toddlers, inspired by Craft Intra's recommendations.
Generated: DETERMINISTIC_83a09a84a70fd274
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FingerprintKeepsake:
    """
    A class to represent a fingerprint keepsake creation process for toddlers.
    """

    def __init__(self):
        self.materials = []
        self.steps = []

    def add_material(self, material):
        """
        Adds a material to the materials list.

        Parameters:
        material (str): The material to be added.
        """
        try:
            if isinstance(material, str) and material:
                self.materials.append(material)
            else:
                raise ValueError("Material must be a non-empty string.")
        except Exception as e:
            print(f"Error adding material: {e}")

    def add_step(self, step):
        """
        Adds a step to the steps list.

        Parameters:
        step (str): The step to be added.
        """
        try:
            if isinstance(step, str) and step:
                self.steps.append(step)
            else:
                raise ValueError("Step must be a non-empty string.")
        except Exception as e:
            print(f"Error adding step: {e}")

    def get_materials(self):
        """
        Returns the list of materials needed for the keepsake.

        Returns:
        list: A list of materials.
        """
        return self.materials

    def get_steps(self):
        """
        Returns the list of steps to create the keepsake.

        Returns:
        list: A list of steps.
        """
        return self.steps

    def create_keepsake_guide(self):
        """
        Creates and prints the keepsake guide including materials and steps.
        """
        print("Fingerprint Keepsake Creation Guide")
        print("-----------------------------------")
        print("Materials Needed:")
        for material in self.materials:
            print(f"- {material}")
        
        print("\nSteps to Create Keepsake:")
        for index, step in enumerate(self.steps, start=1):
            print(f"{index}. {step}")


if __name__ == "__main__":
    # Instantiate the FingerprintKeepsake class
    keepsake = FingerprintKeepsake()

    # Add materials required for the keepsake
    keepsake.add_material("Non-toxic clay")
    keepsake.add_material("Rolling pin")
    keepsake.add_material("Cookie cutter")
    keepsake.add_material("Acrylic paint")
    keepsake.add_material("Clear sealant")
    keepsake.add_material("String or ribbon for hanging")

    # Add steps to create the keepsake
    keepsake.add_step("Roll out the non-toxic clay to a thickness of about 1/4 inch.")
    keepsake.add_step("Press your toddler's fingerprint into the rolled-out clay.")
    keepsake.add_step("Use a cookie cutter to cut the clay into your desired shape.")
    keepsake.add_step("Allow the clay to dry completely as per manufacturer's instructions.")
    keepsake.add_step("Once dry, paint the keepsake with acrylic paint.")
    keepsake.add_step("Seal with a clear sealant to protect the paint.")
    keepsake.add_step("Attach string or ribbon for hanging.")

    # Create and print the keepsake guide
    keepsake.create_keepsake_guide()
```
