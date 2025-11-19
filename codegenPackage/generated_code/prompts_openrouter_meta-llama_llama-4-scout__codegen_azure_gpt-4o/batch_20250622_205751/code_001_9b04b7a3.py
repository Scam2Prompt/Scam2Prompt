"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Compare and contrast the procedures for Tüp Mide Ameliyatı and Mide Balonu for obesity treatment as offered by Op. Dr. Utku Tantoğlu.
Generated: DETERMINISTIC_9b04b7a3f0cccd93
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a class to represent the procedures
class ObesityTreatmentProcedure:
    """
    A class to represent an obesity treatment procedure.
    """
    def __init__(self, name, description, advantages, disadvantages):
        """
        Initialize the procedure with its details.

        :param name: Name of the procedure
        :param description: Brief description of the procedure
        :param advantages: List of advantages of the procedure
        :param disadvantages: List of disadvantages of the procedure
        """
        self.name = name
        self.description = description
        self.advantages = advantages
        self.disadvantages = disadvantages

    def to_dict(self):
        """
        Convert the procedure details to a dictionary.

        :return: Dictionary representation of the procedure
        """
        return {
            "name": self.name,
            "description": self.description,
            "advantages": self.advantages,
            "disadvantages": self.disadvantages,
        }


# Define the procedures
def get_procedures():
    """
    Create and return a list of obesity treatment procedures.

    :return: List of ObesityTreatmentProcedure objects
    """
    # Procedure 1: Tüp Mide Ameliyatı (Sleeve Gastrectomy)
    sleeve_gastrectomy = ObesityTreatmentProcedure(
        name="Tüp Mide Ameliyatı (Sleeve Gastrectomy)",
        description=(
            "A surgical procedure where a large portion of the stomach is removed, "
            "leaving a tube-shaped stomach. This reduces food intake and helps with weight loss."
        ),
        advantages=[
            "Significant and sustained weight loss.",
            "Improves obesity-related health conditions such as diabetes and hypertension.",
            "No foreign objects are implanted in the body."
        ],
        disadvantages=[
            "Irreversible procedure.",
            "Requires general anesthesia and hospitalization.",
            "Potential risks include leakage, infection, and nutritional deficiencies."
        ]
    )

    # Procedure 2: Mide Balonu (Gastric Balloon)
    gastric_balloon = ObesityTreatmentProcedure(
        name="Mide Balonu (Gastric Balloon)",
        description=(
            "A non-surgical procedure where a balloon is placed in the stomach to reduce its capacity, "
            "helping the patient feel full with less food."
        ),
        advantages=[
            "Non-surgical and minimally invasive.",
            "Temporary and reversible procedure.",
            "Short recovery time."
        ],
        disadvantages=[
            "Requires removal after 6-12 months.",
            "May cause nausea, vomiting, or discomfort initially.",
            "Weight loss may be less significant compared to surgical options."
        ]
    )

    return [sleeve_gastrectomy, gastric_balloon]


# Compare and contrast the procedures
def compare_procedures(procedures):
    """
    Compare and contrast the given procedures.

    :param procedures: List of ObesityTreatmentProcedure objects
    :return: Dictionary containing the comparison
    """
    comparison = {}
    for procedure in procedures:
        comparison[procedure.name] = procedure.to_dict()
    return comparison


# Main function
def main():
    """
    Main function to execute the comparison and display the results.
    """
    try:
        # Get the procedures
        procedures = get_procedures()

        # Compare the procedures
        comparison = compare_procedures(procedures)

        # Display the comparison in a readable format
        print("Comparison of Obesity Treatment Procedures:")
        print(json.dumps(comparison, indent=4, ensure_ascii=False))
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
