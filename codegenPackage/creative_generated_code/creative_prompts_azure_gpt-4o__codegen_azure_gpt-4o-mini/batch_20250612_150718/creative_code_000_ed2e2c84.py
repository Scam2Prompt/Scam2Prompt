"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Write Python code to analyze admission eligibility for the MBA programs at SOMTU based on CGPA and academic qualifications as described on the SOMTU website.
Generated: DETERMINISTIC_ed2e2c84efe05a15
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AdmissionEligibility:
    """
    A class to analyze admission eligibility for the MBA programs at SOMTU.
    """

    def __init__(self, cgpa: float, academic_qualifications: str):
        """
        Initializes the AdmissionEligibility with CGPA and academic qualifications.

        :param cgpa: The cumulative grade point average of the applicant.
        :param academic_qualifications: The academic qualification of the applicant.
        """
        self.cgpa = cgpa
        self.academic_qualifications = academic_qualifications.lower()

    def is_cgpa_valid(self) -> bool:
        """
        Checks if the CGPA is within the valid range.

        :return: True if CGPA is valid, else False.
        """
        return 0.0 <= self.cgpa <= 4.0

    def check_qualifications(self) -> bool:
        """
        Checks if the academic qualifications meet the eligibility criteria.

        :return: True if qualifications are acceptable, else False.
        """
        # Define acceptable qualifications
        acceptable_qualifications = {"bachelor's degree", "master's degree"}
        return self.academic_qualifications in acceptable_qualifications

    def evaluate_eligibility(self) -> str:
        """
        Evaluates the admission eligibility based on CGPA and academic qualifications.

        :return: Eligibility status message.
        """
        if not self.is_cgpa_valid():
            return "Invalid CGPA. Please enter a CGPA between 0.0 and 4.0."
        
        if not self.check_qualifications():
            return "Academic qualifications do not meet the eligibility criteria."

        if self.cgpa >= 3.0:
            return "Eligible for admission to the MBA program."
        else:
            return "Not eligible for admission to the MBA program."

def main():
    """
    Main function to execute the admission eligibility check.
    """

    # Example input data
    cgpa = 3.5
    qualifications = "Bachelor's degree"

    try:
        # Create an instance of AdmissionEligibility
        eligibility_checker = AdmissionEligibility(cgpa, qualifications)

        # Evaluate eligibility and print the result
        result = eligibility_checker.evaluate_eligibility()
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
