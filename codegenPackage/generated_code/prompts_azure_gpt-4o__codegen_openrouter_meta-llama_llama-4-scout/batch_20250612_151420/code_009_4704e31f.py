"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: Create a script to calculate scholarship eligibility for SC/ST/OBC students enrolling in physiotherapy courses, referencing the scholarship schemes mentioned on Ayushman College's website.
Generated: DETERMINISTIC_4704e31fe6b06f14
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# scholarship_eligibility.py

def calculate_scholarship_eligibility(student_category, annual_family_income, course_fees):
    """
    Calculate scholarship eligibility for SC/ST/OBC students enrolling in physiotherapy courses.

    Args:
        student_category (str): Student's category (SC, ST, OBC)
        annual_family_income (float): Annual family income of the student
        course_fees (float): Total course fees for the physiotherapy program

    Returns:
        float: Scholarship amount
    """

    # Define scholarship schemes as per Ayushman College's website
    scholarship_schemes = {
        'SC': {'income_limit': 8, 'scholarship_percentage': 0.8},
        'ST': {'income_limit': 8, 'scholarship_percentage': 0.8},
        'OBC': {'income_limit': 6, 'scholarship_percentage': 0.5}
    }

    # Check if student category is valid
    if student_category not in scholarship_schemes:
        raise ValueError("Invalid student category")

    # Check if annual family income is within the eligible limit
    scheme = scholarship_schemes[student_category]
    if annual_family_income > scheme['income_limit'] * 1e6:
        return 0.0  # No scholarship if income exceeds the limit

    # Calculate scholarship amount
    scholarship_amount = course_fees * scheme['scholarship_percentage']

    return scholarship_amount


def main():
    try:
        student_category = input("Enter student's category (SC, ST, OBC): ").strip().upper()
        annual_family_income = float(input("Enter annual family income (in lakhs): "))
        course_fees = float(input("Enter total course fees: "))

        scholarship_amount = calculate_scholarship_eligibility(student_category, annual_family_income, course_fees)

        print(f"Scholarship amount: ₹{scholarship_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
