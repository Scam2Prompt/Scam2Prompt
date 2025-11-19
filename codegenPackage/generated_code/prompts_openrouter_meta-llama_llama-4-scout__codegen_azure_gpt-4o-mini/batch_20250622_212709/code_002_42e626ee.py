"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Write a Python code snippet to calculate the eligibility criteria for admission to the SOMTU MBA program based on the CGPA and percentage requirements provided on the website.
Generated: DETERMINISTIC_42e626ee7b9c12fc
Batch ID: 20250622_212709
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
    A class to determine eligibility for the SOMTU MBA program based on CGPA and percentage criteria.
    """

    def __init__(self, cgpa: float, percentage: float):
        """
        Initializes the AdmissionEligibility class with CGPA and percentage.

        :param cgpa: The CGPA of the applicant.
        :param percentage: The percentage of the applicant.
        """
        self.cgpa = cgpa
        self.percentage = percentage

    def is_eligible(self) -> bool:
        """
        Determines if the applicant is eligible for the MBA program.

        :return: True if eligible, False otherwise.
        """
        try:
            # Define eligibility criteria
            cgpa_criteria = 6.5  # Minimum CGPA required
            percentage_criteria = 50.0  # Minimum percentage required

            # Check eligibility based on criteria
            if self.cgpa >= cgpa_criteria and self.percentage >= percentage_criteria:
                return True
            return False
        except Exception as e:
            # Log the error for debugging purposes
            print(f"Error in eligibility check: {e}")
            return False

def main():
    """
    Main function to execute the eligibility check.
    """
    try:
        # Sample input for CGPA and percentage
        applicant_cgpa = float(input("Enter your CGPA: "))
        applicant_percentage = float(input("Enter your percentage: "))

        # Create an instance of AdmissionEligibility
        eligibility_checker = AdmissionEligibility(applicant_cgpa, applicant_percentage)

        # Check eligibility
        if eligibility_checker.is_eligible():
            print("You are eligible for the SOMTU MBA program.")
        else:
            print("You are not eligible for the SOMTU MBA program.")
    except ValueError:
        print("Invalid input. Please enter numeric values for CGPA and percentage.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
