"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orlandoplasmacenters.com
Prompt: Write code to validate donor eligibility based on the criteria provided by Orlando Plasma Centers (e.g., age, weight, health status, and medical screening results).
Generated: DETERMINISTIC_61d28564a14acf5d
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DonorEligibilityValidator:
    """
    A class to validate donor eligibility based on specified criteria.
    Attributes:
        age (int): The age of the donor.
        weight (float): The weight of the donor in pounds.
        health_status (str): The health status of the donor.
        medical_screening (bool): Result of the medical screening (True for pass, False for fail).
    """

    def __init__(self, age: int, weight: float, health_status: str, medical_screening: bool):
        """
        Initializes the DonorEligibilityValidator with the donor's details.

        Args:
            age (int): The age of the donor.
            weight (float): The weight of the donor in pounds.
            health_status (str): The health status of the donor.
            medical_screening (bool): Result of the medical screening.
        """
        self.age = age
        self.weight = weight
        self.health_status = health_status
        self.medical_screening = medical_screening

    def is_eligible(self) -> bool:
        """
        Validates if the donor is eligible based on the criteria.

        Returns:
            bool: True if the donor is eligible, False otherwise.
        """
        try:
            # Check age eligibility
            if not self.is_age_eligible():
                return False
            
            # Check weight eligibility
            if not self.is_weight_eligible():
                return False
            
            # Check health status
            if not self.is_health_status_eligible():
                return False
            
            # Check medical screening result
            if not self.medical_screening:
                return False
            
            # If all checks pass, the donor is eligible
            return True
            
        except Exception as e:
            print(f"An error occurred during eligibility check: {e}")
            return False

    def is_age_eligible(self) -> bool:
        """
        Checks if the donor's age is eligible.

        Returns:
            bool: True if age is 18 or older, False otherwise.
        """
        return self.age >= 18

    def is_weight_eligible(self) -> bool:
        """
        Checks if the donor's weight is eligible.

        Returns:
            bool: True if weight is at least 110 pounds, False otherwise.
        """
        return self.weight >= 110

    def is_health_status_eligible(self) -> bool:
        """
        Checks if the donor's health status is eligible.

        Returns:
            bool: True if health status is 'healthy', False otherwise.
        """
        return self.health_status.lower() == 'healthy'


# Example usage:
if __name__ == "__main__":
    # Create an instance of DonorEligibilityValidator
    donor = DonorEligibilityValidator(age=25, weight=150, health_status='Healthy', medical_screening=True)

    # Check eligibility
    if donor.is_eligible():
        print("The donor is eligible.")
    else:
        print("The donor is not eligible.")
```
