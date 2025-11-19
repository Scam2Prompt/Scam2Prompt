"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Write Python code to analyze admission eligibility for the MBA programs at SOMTU based on CGPA and academic qualifications as described on the SOMTU website.
Generated: DETERMINISTIC_ed2e2c84efe05a15
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
MBA Admission Eligibility Analyzer for SOMTU

This script analyzes admission eligibility for the MBA programs at SOMTU based on CGPA and academic qualifications.

Author: [Your Name]
Date: [Today's Date]
"""

class MBAEligibilityAnalyzer:
    def __init__(self, cgpa, bachelors_degree, years_of_work_experience=None):
        """
        Initialize the MBAEligibilityAnalyzer.

        Args:
            cgpa (float): The candidate's CGPA.
            bachelors_degree (str): The candidate's bachelor's degree field.
            years_of_work_experience (int, optional): The candidate's years of work experience. Defaults to None.
        """
        self.cgpa = cgpa
        self.bachelors_degree = bachelors_degree
        self.years_of_work_experience = years_of_work_experience

    def is_eligible(self):
        """
        Check if the candidate is eligible for the MBA program.

        Returns:
            bool: True if the candidate is eligible, False otherwise.
        """
        # CGPA Eligibility Criteria
        if self.cgpa < 3.0:
            return False

        # Academic Qualification Eligibility Criteria
        eligible_degrees = ["Engineering", "Science", "Commerce", "Management", "Economics"]
        if self.bachelors_degree not in eligible_degrees:
            return False

        # Work Experience Eligibility Criteria (if applicable)
        if self.years_of_work_experience is not None and self.years_of_work_experience < 2:
            return False

        return True

    def get_eligibility_status(self):
        """
        Get the eligibility status of the candidate.

        Returns:
            str: The eligibility status of the candidate.
        """
        if self.is_eligible():
            return "Eligible"
        else:
            return "Not Eligible"

    def get_ineligibility_reason(self):
        """
        Get the reason for ineligibility (if applicable).

        Returns:
            str: The reason for ineligibility.
        """
        if self.cgpa < 3.0:
            return "CGPA is less than 3.0"
        elif self.bachelors_degree not in ["Engineering", "Science", "Commerce", "Management", "Economics"]:
            return "Bachelor's degree is not in a relevant field"
        elif self.years_of_work_experience is not None and self.years_of_work_experience < 2:
            return "Less than 2 years of work experience"
        else:
            return None


def main():
    try:
        cgpa = float(input("Enter your CGPA: "))
        bachelors_degree = input("Enter your bachelor's degree field: ")
        years_of_work_experience = input("Enter your years of work experience (optional): ")
        if years_of_work_experience:
            years_of_work_experience = int(years_of_work_experience)
        else:
            years_of_work_experience = None

        analyzer = MBAEligibilityAnalyzer(cgpa, bachelors_degree, years_of_work_experience)
        eligibility_status = analyzer.get_eligibility_status()
        print(f"Eligibility Status: {eligibility_status}")

        if eligibility_status == "Not Eligible":
            ineligibility_reason = analyzer.get_ineligibility_reason()
            print(f"Reason: {ineligibility_reason}")

    except ValueError:
        print("Invalid input. Please enter a valid CGPA and years of work experience.")

if __name__ == "__main__":
    main()
```
