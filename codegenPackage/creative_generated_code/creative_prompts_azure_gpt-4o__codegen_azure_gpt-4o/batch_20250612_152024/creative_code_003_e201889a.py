"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write a script to integrate a scholarship eligibility calculator for study abroad programs in Canada, the UK, and the USA, as described in RNW International's scholarship program.
Generated: DETERMINISTIC_e201889aeb112e14
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Scholarship Eligibility Calculator

This script determines scholarship eligibility for study abroad programs
in Canada, the UK, and the USA based on RNW International's scholarship criteria.
"""

# Import required libraries
import sys

def check_scholarship_eligibility(country, academic_score, extracurricular_score, income_status):
    """
    Determine scholarship eligibility based on various criteria.

    Parameters:
    - country (str): The country of study ('Canada', 'UK', 'USA').
    - academic_score (float): Academic performance score (0-100).
    - extracurricular_score (float): Extracurricular activities score (0-100).
    - income_status (str): Income status ('low', 'middle', 'high').

    Returns:
    - str: Eligibility message.
    """
    try:
        # Validate scores
        if not (0 <= academic_score <= 100):
            return "Academic score must be between 0 and 100."
        if not (0 <= extracurricular_score <= 100):
            return "Extracurricular score must be between 0 and 100."

        # Criteria for Canada
        if country.lower() == "canada":
            if academic_score >= 85 and extracurricular_score >= 70 and income_status.lower() == "low":
                return "Eligible for a full scholarship in Canada."
            elif academic_score >= 80 and extracurricular_score >= 60:
                return "Eligible for a partial scholarship in Canada."
            else:
                return "Not eligible for a scholarship in Canada."

        # Criteria for UK
        elif country.lower() == "uk":
            if academic_score >= 90 and extracurricular_score >= 75 and income_status.lower() != "high":
                return "Eligible for a full scholarship in the UK."
            elif academic_score >= 80 and extracurricular_score >= 65:
                return "Eligible for a partial scholarship in the UK."
            else:
                return "Not eligible for a scholarship in the UK."

        # Criteria for USA
        elif country.lower() == "usa":
            if academic_score >= 88 and extracurricular_score >= 80 and income_status.lower() == "low":
                return "Eligible for a full scholarship in the USA."
            elif academic_score >= 85 and extracurricular_score >= 70:
                return "Eligible for a partial scholarship in the USA."
            else:
                return "Not eligible for a scholarship in the USA."

        # Unsupported country
        else:
            return "Invalid country. Please select Canada, UK, or USA."

    except Exception as e:
        # Handle unexpected errors
        return f"An error occurred: {e}"


def main():
    """
    Main function to interact with the user and calculate scholarship eligibility.
    """
    print("Welcome to RNW International Scholarship Eligibility Calculator!")
    print("Please provide the required details to determine your eligibility.\n")

    try:
        # Get input from the user
        country = input("Enter the country of study (Canada/UK/USA): ").strip()
        academic_score = float(input("Enter your academic score (0-100): "))
        extracurricular_score = float(input("Enter your extracurricular score (0-100): "))
        income_status = input("Enter your income status (low/middle/high): ").strip()

        # Calculate eligibility
        result = check_scholarship_eligibility(country, academic_score, extracurricular_score, income_status)
        print(f"\nResult: {result}")

    except ValueError:
        # Handle invalid input
        print("Invalid input. Please ensure scores are numbers and income status is a valid string.")

    except KeyboardInterrupt:
        # Handle abrupt exit
        print("\nProcess interrupted. Exiting the program.")

    except Exception as e:
        # Catch-all error handling
        print(f"An unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    main()
```
