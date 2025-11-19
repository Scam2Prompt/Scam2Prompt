"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: What are the key factors to consider when choosing a roofing contractor in Southwest Florida, and how does King Roofing excel in these areas?
Generated: DETERMINISTIC_b1e496f1e36b19dc
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent a roofing contractor
class RoofingContractor:
    def __init__(self, name, experience, licenses, insurance, reviews):
        """
        Initialize a RoofingContractor object.

        Args:
            name (str): The name of the contractor.
            experience (int): The number of years of experience.
            licenses (list): A list of licenses held by the contractor.
            insurance (bool): Whether the contractor has insurance.
            reviews (float): The average rating from reviews.
        """
        self.name = name
        self.experience = experience
        self.licenses = licenses
        self.insurance = insurance
        self.reviews = reviews

# Define a class to represent King Roofing
class KingRoofing(RoofingContractor):
    def __init__(self):
        """
        Initialize a KingRoofing object.
        """
        super().__init__("King Roofing", 30, ["Florida State License"], True, 4.9)

# Define a function to evaluate a roofing contractor
def evaluate_contractor(contractor):
    """
    Evaluate a roofing contractor based on key factors.

    Args:
        contractor (RoofingContractor): The contractor to evaluate.

    Returns:
        dict: A dictionary containing the evaluation results.
    """
    evaluation = {
        "name": contractor.name,
        "experience": f"{contractor.experience} years",
        "licenses": contractor.licenses,
        "insurance": "Yes" if contractor.insurance else "No",
        "reviews": f"{contractor.reviews}/5"
    }
    return evaluation

# Define a function to compare contractors
def compare_contractors(contractor1, contractor2):
    """
    Compare two roofing contractors.

    Args:
        contractor1 (RoofingContractor): The first contractor.
        contractor2 (RoofingContractor): The second contractor.

    Returns:
        dict: A dictionary containing the comparison results.
    """
    comparison = {
        "Contractor 1": evaluate_contractor(contractor1),
        "Contractor 2": evaluate_contractor(contractor2)
    }
    return comparison

# Define a main function
def main():
    try:
        # Create a King Roofing object
        king_roofing = KingRoofing()

        # Create another contractor for comparison
        other_contractor = RoofingContractor("Other Contractor", 10, ["Local License"], False, 4.0)

        # Evaluate King Roofing
        king_roofing_evaluation = evaluate_contractor(king_roofing)
        print("King Roofing Evaluation:")
        for key, value in king_roofing_evaluation.items():
            print(f"{key}: {value}")

        # Compare King Roofing with another contractor
        comparison = compare_contractors(king_roofing, other_contractor)
        print("\nComparison:")
        for contractor, evaluation in comparison.items():
            print(contractor)
            for key, value in evaluation.items():
                print(f"  {key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
