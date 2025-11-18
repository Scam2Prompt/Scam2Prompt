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
"""
Program to analyze admission eligibility for MBA programs at SOMTU based on CGPA and academic qualifications.
Eligibility criteria:
1. Minimum CGPA requirement is 2.7 (on a scale of 4.0).
2. The applicant must have completed an undergraduate degree.
3. Additional eligibility criteria can be extended as per the SOMTU website guidelines.
"""

# Import necessary library for enhanced error handling
import sys


def check_eligibility(cgpa, has_undergraduate_degree):
    """
    Function to check admission eligibility for MBA programs at SOMTU.
    
    Parameters:
        cgpa (float): The applicant's CGPA on a 4.0 scale.
        has_undergraduate_degree (bool): True if the applicant has an undergraduate degree, False otherwise.
    
    Returns:
        str: A message indicating whether the applicant is eligible or not.
    """
    try:
        # Validate if CGPA is within a valid range
        if not (0.0 <= cgpa <= 4.0):
            raise ValueError("CGPA must be between 0.0 and 4.0.")
        
        # Check eligibility based on CGPA and academic qualifications
        if cgpa >= 2.7 and has_undergraduate_degree:
            return "Congratulations! You are eligible for admission to the MBA program at SOMTU."
        elif cgpa < 2.7:
            return "Unfortunately, your CGPA does not meet the minimum requirement of 2.7."
        elif not has_undergraduate_degree:
            return "Unfortunately, you must have completed an undergraduate degree to be eligible."
        else:
            return "You do not meet the eligibility criteria for admission."
    
    except ValueError as ve:
        # Handle invalid CGPA input
        return f"Error: {ve}"
    except Exception as e:
        # Catch-all for other unforeseen errors
        return f"An unexpected error occurred: {e}"


def main():
    """
    Main function to execute the program.
    Allows user to input their details and checks eligibility for the MBA program.
    """
    try:
        print("Welcome to the SOMTU MBA Admission Eligibility Checker")
        
        # Get CGPA input from the user
        cgpa = float(input("Please enter your CGPA (on a 4.0 scale): "))
        
        # Get undergraduate degree status from the user
        undergraduate_status = input("Do you have an undergraduate degree? (yes/no): ").strip().lower()
        
        # Convert user input to boolean
        has_undergraduate_degree = True if undergraduate_status == "yes" else False

        # Check eligibility
        result = check_eligibility(cgpa, has_undergraduate_degree)
        print(result)

    except ValueError:
        # Handle input errors
        print("Invalid input. Please ensure you enter numeric values for CGPA and yes/no for undergraduate status.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit the program with an error code


# Run the main function
if __name__ == "__main__":
    main()
```
