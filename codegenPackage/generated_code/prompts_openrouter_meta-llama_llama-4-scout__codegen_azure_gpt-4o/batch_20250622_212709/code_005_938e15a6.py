"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Generate a sample admission notice for the SOMTU MBA program using a template, incorporating details such as program name, admission dates, and eligibility criteria.
Generated: DETERMINISTIC_938e15a6a5512fc8
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from datetime import datetime

# Function to generate an admission notice
def generate_admission_notice(program_name, admission_start_date, admission_end_date, eligibility_criteria):
    """
    Generates an admission notice for a given program.

    Args:
        program_name (str): Name of the program.
        admission_start_date (str): Admission start date in 'YYYY-MM-DD' format.
        admission_end_date (str): Admission end date in 'YYYY-MM-DD' format.
        eligibility_criteria (str): Eligibility criteria for the program.

    Returns:
        str: Formatted admission notice.
    """
    try:
        # Validate and parse dates
        start_date = datetime.strptime(admission_start_date, '%Y-%m-%d')
        end_date = datetime.strptime(admission_end_date, '%Y-%m-%d')

        # Ensure the start date is before the end date
        if start_date >= end_date:
            raise ValueError("Admission start date must be earlier than the end date.")

        # Template for the admission notice
        notice_template = f"""
        -----------------------------------------------
        SOMTU MBA Program Admission Notice
        -----------------------------------------------

        Program Name: {program_name}

        Admission Start Date: {start_date.strftime('%B %d, %Y')}
        Admission End Date: {end_date.strftime('%B %d, %Y')}

        Eligibility Criteria:
        {eligibility_criteria}

        We invite all eligible candidates to apply for the prestigious SOMTU MBA program.
        For more details, please visit our official website.

        -----------------------------------------------
        """

        return notice_template

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Define program details
    program_name = "Master of Business Administration (MBA)"
    admission_start_date = "2023-11-01"
    admission_end_date = "2023-12-15"
    eligibility_criteria = (
        "1. Bachelor's degree from a recognized university.\n"
        "2. Minimum 50% aggregate marks.\n"
        "3. Valid GMAT or GRE score."
    )

    # Generate and print the admission notice
    admission_notice = generate_admission_notice(
        program_name, admission_start_date, admission_end_date, eligibility_criteria
    )
    print(admission_notice)
```
