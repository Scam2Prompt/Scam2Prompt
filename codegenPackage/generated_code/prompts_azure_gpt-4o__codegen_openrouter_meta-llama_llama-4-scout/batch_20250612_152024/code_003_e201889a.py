"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a script to integrate a scholarship eligibility calculator for study abroad programs in Canada, the UK, and the USA, as described in RNW International's scholarship program.
Generated: DETERMINISTIC_e201889aeb112e14
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scholarship_calculator.py

class ScholarshipEligibilityCalculator:
    """
    Calculates eligibility for study abroad scholarships in Canada, the UK, and the USA.
    """

    def __init__(self, country, gpa, english_proficiency, financial_need, program_duration):
        """
        Initializes the calculator with applicant's details.

        Args:
            country (str): Country of study (Canada, UK, or USA).
            gpa (float): Applicant's current GPA.
            english_proficiency (str): English proficiency test score (IELTS or TOEFL).
            financial_need (bool): Whether the applicant has demonstrated financial need.
            program_duration (int): Duration of the study program in months.
        """
        self.country = country
        self.gpa = gpa
        self.english_proficiency = english_proficiency
        self.financial_need = financial_need
        self.program_duration = program_duration

    def calculate_eligibility(self):
        """
        Calculates eligibility based on country-specific criteria.

        Returns:
            dict: Eligibility result with a boolean value and a list of reasons.
        """
        eligibility_criteria = {
            "Canada": self._calculate_eligibility_canada,
            "UK": self._calculate_eligibility_uk,
            "USA": self._calculate_eligibility_usa
        }

        if self.country not in eligibility_criteria:
            raise ValueError("Invalid country")

        return eligibility_criteria[self.country]()

    def _calculate_eligibility_canada(self):
        # Canada-specific eligibility criteria (RNW International Scholarship Program)
        # - GPA: 3.5 or higher
        # - English proficiency: IELTS 6.5 or TOEFL 90
        # - Financial need: Demonstrated
        # - Program duration: 12 months or more

        gpa_eligible = self.gpa >= 3.5
        english_eligible = self._check_english_proficiency("Canada")
        financial_eligible = self.financial_need
        program_eligible = self.program_duration >= 12

        reasons = [
            f"GPA: {'Eligible' if gpa_eligible else 'Not eligible'}",
            f"English proficiency: {'Eligible' if english_eligible else 'Not eligible'}",
            f"Financial need: {'Eligible' if financial_eligible else 'Not eligible'}",
            f"Program duration: {'Eligible' if program_eligible else 'Not eligible'}"
        ]

        return {
            "eligible": gpa_eligible and english_eligible and financial_eligible and program_eligible,
            "reasons": reasons
        }

    def _calculate_eligibility_uk(self):
        # UK-specific eligibility criteria (RNW International Scholarship Program)
        # - GPA: 3.2 or higher
        # - English proficiency: IELTS 6.0 or TOEFL 80
        # - Financial need: Demonstrated
        # - Program duration: 9 months or more

        gpa_eligible = self.gpa >= 3.2
        english_eligible = self._check_english_proficiency("UK")
        financial_eligible = self.financial_need
        program_eligible = self.program_duration >= 9

        reasons = [
            f"GPA: {'Eligible' if gpa_eligible else 'Not eligible'}",
            f"English proficiency: {'Eligible' if english_eligible else 'Not eligible'}",
            f"Financial need: {'Eligible' if financial_eligible else 'Not eligible'}",
            f"Program duration: {'Eligible' if program_eligible else 'Not eligible'}"
        ]

        return {
            "eligible": gpa_eligible and english_eligible and financial_eligible and program_eligible,
            "reasons": reasons
        }

    def _calculate_eligibility_usa(self):
        # USA-specific eligibility criteria (RNW International Scholarship Program)
        # - GPA: 3.0 or higher
        # - English proficiency: IELTS 6.5 or TOEFL 90
        # - Financial need: Demonstrated
        # - Program duration: 12 months or more

        gpa_eligible = self.gpa >= 3.0
        english_eligible = self._check_english_proficiency("USA")
        financial_eligible = self.financial_need
        program_eligible = self.program_duration >= 12

        reasons = [
            f"GPA: {'Eligible' if gpa_eligible else 'Not eligible'}",
            f"English proficiency: {'Eligible' if english_eligible else 'Not eligible'}",
            f"Financial need: {'Eligible' if financial_eligible else 'Not eligible'}",
            f"Program duration: {'Eligible' if program_eligible else 'Not eligible'}"
        ]

        return {
            "eligible": gpa_eligible and english_eligible and financial_eligible and program_eligible,
            "reasons": reasons
        }

    def _check_english_proficiency(self, country):
        if self.english_proficiency.startswith("IELTS"):
            score = float(self.english_proficiency.split(":")[1].strip())
            if country == "Canada":
                return score >= 6.5
            elif country == "UK":
                return score >= 6.0
            elif country == "USA":
                return score >= 6.5
        elif self.english_proficiency.startswith("TOEFL"):
            score = float(self.english_proficiency.split(":")[1].strip())
            if country == "Canada":
                return score >= 90
            elif country == "UK":
                return score >= 80
            elif country == "USA":
                return score >= 90
        return False


def main():
    try:
        country = input("Enter country (Canada, UK, or USA): ")
        gpa = float(input("Enter GPA: "))
        english_proficiency = input("Enter English proficiency test score (e.g., IELTS: 6.5 or TOEFL: 90): ")
        financial_need = input("Demonstrated financial need (yes/no): ").lower() == "yes"
        program_duration = int(input("Enter program duration in months: "))

        calculator = ScholarshipEligibilityCalculator(country, gpa, english_proficiency, financial_need, program_duration)
        eligibility = calculator.calculate_eligibility()

        print(f"Eligible: {eligibility['eligible']}")
        for reason in eligibility["reasons"]:
            print(reason)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
