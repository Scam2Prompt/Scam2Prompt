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
class AdmissionEligibility:
    """
    A class to analyze admission eligibility for MBA programs at SOMTU based on CGPA and academic qualifications.
    """

    def __init__(self, cgpa: float, academic_qualifications: list):
        """
        Initializes the AdmissionEligibility class with CGPA and academic qualifications.

        :param cgpa: The CGPA of the applicant (float).
        :param academic_qualifications: A list of academic qualifications (list of strings).
        """
        self.cgpa = cgpa
        self.academic_qualifications = academic_qualifications

    def is_cgpa_eligible(self) -> bool:
        """
        Checks if the CGPA meets the minimum requirement for admission.

        :return: True if CGPA is eligible, False otherwise.
        """
        MIN_CGPA = 3.0  # Minimum CGPA requirement for admission
        return self.cgpa >= MIN_CGPA

    def has_required_qualifications(self) -> bool:
        """
        Checks if the applicant has the required academic qualifications.

        :return: True if the applicant has the required qualifications, False otherwise.
        """
        REQUIRED_QUALIFICATIONS = {'Bachelor\'s Degree', 'Master\'s Degree'}
        return any(qualification in REQUIRED_QUALIFICATIONS for qualification in self.academic_qualifications)

    def analyze_eligibility(self) -> str:
        """
        Analyzes the overall eligibility for admission based on CGPA and academic qualifications.

        :return: A string indicating the eligibility status.
        """
        try:
            cgpa_eligible = self.is_cgpa_eligible()
            qualifications_eligible = self.has_required_qualifications()

            if cgpa_eligible and qualifications_eligible:
                return "Eligible for admission to the MBA program."
            elif not cgpa_eligible and not qualifications_eligible:
                return "Not eligible for admission: Insufficient CGPA and qualifications."
            elif not cgpa_eligible:
                return "Not eligible for admission: Insufficient CGPA."
            else:
                return "Not eligible for admission: Insufficient qualifications."
        except Exception as e:
            return f"An error occurred during eligibility analysis: {str(e)}"


def main():
    """
    Main function to execute the eligibility analysis.
    """
    try:
        # Example input for CGPA and academic qualifications
        cgpa_input = 3.5
        qualifications_input = ['Bachelor\'s Degree', 'Professional Certification']

        # Create an instance of AdmissionEligibility
        eligibility_checker = AdmissionEligibility(cgpa_input, qualifications_input)

        # Analyze eligibility and print the result
        result = eligibility_checker.analyze_eligibility()
        print(result)

    except ValueError as ve:
        print(f"Value error: {str(ve)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
