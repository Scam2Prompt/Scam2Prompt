"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Generate a script in Python to calculate eligibility for Spanish nationality based on residency duration, marital status, or ancestry, referencing specific legal requirements.
Generated: DETERMINISTIC_3a1a09a0fce16cfe
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NationalityEligibility:
    """A class to determine eligibility for Spanish nationality based on residency duration, marital status, or ancestry."""

    def __init__(self, residency_duration, marital_status, ancestry_nationality=None):
        """
        Initialize the eligibility checker with residency duration, marital status, and optional ancestry nationality.
        
        :param residency_duration: Duration of residency in years (int)
        :param marital_status: Marital status (str) - "single", "married", or "divorced"
        :param ancestry_nationality: Nationality of ancestry if applicable (str) - defaults to None
        """
        self.residency_duration = residency_duration
        self.marital_status = marital_status.lower()
        self.ancestry_nationality = ancestry_nationality.lower() if ancestry_nationality else None

    def check_residency_eligibility(self):
        """Check eligibility based on residency duration."""
        if self.residency_duration >= 10:
            return True
        elif self.residency_duration >= 2 and self.marital_status == "married":
            return True
        return False

    def check_ancestry_eligibility(self):
        """Check eligibility based on ancestry nationality."""
        eligible_ancestries = ["spanish"]
        return self.ancestry_nationality in eligible_ancestries

    def is_eligible_for_nationality(self):
        """
        Determine overall eligibility for Spanish nationality.
        
        :return: True if eligible, False otherwise
        """
        if self.check_residency_eligibility():
            return True
        if self.check_ancestry_eligibility():
            return True
        return False


def main():
    """Main function to execute the nationality eligibility check."""
    try:
        # Example input
        residency_duration = int(input("Enter your residency duration in years: "))
        marital_status = input("Enter your marital status (single/married/divorced): ")
        ancestry_nationality = input("Enter your ancestry nationality (or press Enter if not applicable): ") or None
        
        # Create an instance of NationalityEligibility
        eligibility_checker = NationalityEligibility(residency_duration, marital_status, ancestry_nationality)

        # Checking eligibility
        if eligibility_checker.is_eligible_for_nationality():
            print("You are eligible for Spanish nationality.")
        else:
            print("You are not eligible for Spanish nationality.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for residency duration.")

if __name__ == "__main__":
    main()
```
