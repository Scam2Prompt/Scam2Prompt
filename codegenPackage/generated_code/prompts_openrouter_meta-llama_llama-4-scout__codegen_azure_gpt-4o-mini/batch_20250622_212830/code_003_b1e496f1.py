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
class RoofingContractor:
    """
    A class to represent a roofing contractor and evaluate their qualities.
    """

    def __init__(self, name, experience_years, licenses, insurance, reviews, warranty):
        """
        Initializes the RoofingContractor with essential attributes.

        :param name: str - Name of the roofing contractor
        :param experience_years: int - Years of experience in roofing
        :param licenses: list - List of licenses held by the contractor
        :param insurance: bool - Whether the contractor has insurance
        :param reviews: list - List of customer reviews (ratings out of 5)
        :param warranty: str - Warranty offered by the contractor
        """
        self.name = name
        self.experience_years = experience_years
        self.licenses = licenses
        self.insurance = insurance
        self.reviews = reviews
        self.warranty = warranty

    def average_rating(self):
        """
        Calculates the average rating from customer reviews.

        :return: float - Average rating
        """
        if not self.reviews:
            return 0.0
        return sum(self.reviews) / len(self.reviews)

    def is_qualified(self):
        """
        Checks if the contractor is qualified based on experience and licenses.

        :return: bool - True if qualified, False otherwise
        """
        return self.experience_years >= 5 and len(self.licenses) > 0

    def has_insurance(self):
        """
        Checks if the contractor has valid insurance.

        :return: bool - True if insured, False otherwise
        """
        return self.insurance

    def warranty_info(self):
        """
        Provides warranty information.

        :return: str - Warranty details
        """
        return f"Warranty offered: {self.warranty}"


def evaluate_contractor(contractor):
    """
    Evaluates a roofing contractor based on key factors.

    :param contractor: RoofingContractor - The contractor to evaluate
    :return: str - Evaluation summary
    """
    try:
        if not isinstance(contractor, RoofingContractor):
            raise ValueError("Invalid contractor object provided.")

        evaluation = f"Evaluation for {contractor.name}:\n"
        evaluation += f"Experience: {contractor.experience_years} years\n"
        evaluation += f"Average Rating: {contractor.average_rating():.2f}\n"
        evaluation += f"Qualified: {'Yes' if contractor.is_qualified() else 'No'}\n"
        evaluation += f"Insured: {'Yes' if contractor.has_insurance() else 'No'}\n"
        evaluation += contractor.warranty_info()

        return evaluation

    except Exception as e:
        return f"Error during evaluation: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Creating an instance of King Roofing
    king_roofing = RoofingContractor(
        name="King Roofing",
        experience_years=10,
        licenses=["FL Roofing License", "General Contractor License"],
        insurance=True,
        reviews=[5, 4, 5, 4, 5],
        warranty="10 years on workmanship"
    )

    # Evaluating the contractor
    print(evaluate_contractor(king_roofing))
```
