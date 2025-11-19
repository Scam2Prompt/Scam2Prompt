"""
Generated Code Metadata:
========================
Original URL: https://www.spanisheyeclinic.com
Prompt: What are the common symptoms and treatment options for blepharitis and eye allergies as per the Spanish Eye Clinic, and how can they be differentiated?
Generated: DETERMINISTIC_e4000f1ea6801b40
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EyeCondition:
    """
    A class to represent an eye condition with symptoms and treatment options.
    """

    def __init__(self, name, symptoms, treatments):
        """
        Initializes the EyeCondition with a name, symptoms, and treatments.

        :param name: str - The name of the eye condition
        :param symptoms: list - A list of common symptoms
        :param treatments: list - A list of treatment options
        """
        self.name = name
        self.symptoms = symptoms
        self.treatments = treatments

    def display_info(self):
        """
        Displays the information about the eye condition.
        """
        print(f"Condition: {self.name}")
        print("Common Symptoms:")
        for symptom in self.symptoms:
            print(f"- {symptom}")
        print("Treatment Options:")
        for treatment in self.treatments:
            print(f"- {treatment}")


def main():
    """
    Main function to create instances of eye conditions and display their information.
    """
    try:
        # Define symptoms and treatments for Blepharitis
        blepharitis_symptoms = [
            "Red, swollen eyelids",
            "Itchy or burning eyes",
            "Crusty eyelashes",
            "Sensitivity to light",
            "Dry eyes"
        ]
        blepharitis_treatments = [
            "Warm compresses",
            "Eyelid scrubs",
            "Antibiotic ointments",
            "Artificial tears"
        ]

        # Define symptoms and treatments for Eye Allergies
        eye_allergies_symptoms = [
            "Itchy eyes",
            "Redness",
            "Watery discharge",
            "Swelling around the eyes",
            "Sensitivity to light"
        ]
        eye_allergies_treatments = [
            "Antihistamine eye drops",
            "Oral antihistamines",
            "Cold compresses",
            "Avoiding allergens"
        ]

        # Create instances of EyeCondition
        blepharitis = EyeCondition("Blepharitis", blepharitis_symptoms, blepharitis_treatments)
        eye_allergies = EyeCondition("Eye Allergies", eye_allergies_symptoms, eye_allergies_treatments)

        # Display information for each condition
        blepharitis.display_info()
        print("\n" + "-"*40 + "\n")
        eye_allergies.display_info()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
