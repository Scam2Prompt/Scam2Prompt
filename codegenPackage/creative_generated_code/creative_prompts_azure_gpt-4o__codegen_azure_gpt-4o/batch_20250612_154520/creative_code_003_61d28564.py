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
# donor_validation.py

class DonorEligibilityValidator:
    """
    A class to validate donor eligibility based on Orlando Plasma Centers criteria.
    """

    def __init__(self, age, weight, health_status, screening_results):
        """
        Initialize donor information.

        :param age: Donor's age as an integer.
        :param weight: Donor's weight in pounds as a float or integer.
        :param health_status: Donor's self-reported health status as a string ("Good", "Fair", "Poor").
        :param screening_results: A dictionary containing medical screening results.
        """
        self.age = age
        self.weight = weight
        self.health_status = health_status
        self.screening_results = screening_results

    def validate_age(self):
        """
        Validate age. Donor must be between 18 and 65 years old.
        :return: True if age is valid, False otherwise.
        """
        return 18 <= self.age <= 65

    def validate_weight(self):
        """
        Validate weight. Donor must weigh at least 110 pounds.
        :return: True if weight is valid, False otherwise.
        """
        return self.weight >= 110

    def validate_health_status(self):
        """
        Validate health status. Donor must report "Good" health.
        :return: True if health status is valid, False otherwise.
        """
        return self.health_status.lower() == "good"

    def validate_screening_results(self):
        """
        Validate medical screening results. Screening criteria may vary; expected to be a dictionary.
        Example structure:
            {
              "blood_pressure_normal": True,
              "negative_for_infectious_disease": True,
              "iron_level_normal": True
            }
        :return: True if all screening results pass, False otherwise.
        """
        if not isinstance(self.screening_results, dict):
            return False  # Screening results must be in dictionary format.

        # Check all screening results are True
        return all(self.screening_results.values())

    def is_eligible(self):
        """
        Check overall donor eligibility based on all criteria.
        :return: True if donor is eligible, False otherwise.
        """
        try:
            return (self.validate_age() and
                    self.validate_weight() and
                    self.validate_health_status() and
                    self.validate_screening_results())
        except Exception as e:
            # Log the error (placeholder for actual logging mechanism)
            print(f"Error during eligibility validation: {e}")
            return False


# Example usage:
if __name__ == "__main__":
    # Sample donor data
    donor_data = {
        "age": 30,
        "weight": 150,
        "health_status": "Good",
        "screening_results": {
            "blood_pressure_normal": True,
            "negative_for_infectious_disease": True,
            "iron_level_normal": True
        }
    }

    # Create validator instance
    validator = DonorEligibilityValidator(
        age=donor_data["age"],
        weight=donor_data["weight"],
        health_status=donor_data["health_status"],
        screening_results=donor_data["screening_results"]
    )

    # Check donor eligibility
    if validator.is_eligible():
        print("Donor is eligible.")
    else:
        print("Donor is not eligible.")
```
