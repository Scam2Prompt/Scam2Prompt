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
SOMTU MBA Admission Eligibility Analyzer

This script analyzes a candidate's eligibility for the MBA program at SOMTU based on:
- CGPA (Cumulative Grade Point Average)
- Academic qualifications (Bachelor's degree or equivalent)

Eligibility Criteria:
1. Minimum CGPA of 2.5 out of 4.0 (or equivalent)
2. Bachelor's degree from a recognized institution
"""

def analyze_admission_eligibility(cgpa: float, has_bachelor_degree: bool) -> dict:
    """
    Analyzes admission eligibility based on CGPA and academic qualifications.
    
    Args:
        cgpa (float): Candidate's CGPA (scale of 4.0)
        has_bachelor_degree (bool): Whether candidate has a bachelor's degree
        
    Returns:
        dict: Analysis result containing:
            - is_eligible (bool): Overall eligibility status
            - reasons (list): List of reasons for ineligibility (empty if eligible)
            - cgpa_requirement_met (bool): Whether CGPA requirement is met
            - degree_requirement_met (bool): Whether degree requirement is met
    """
    
    # Validate input parameters
    if not isinstance(cgpa, (int, float)):
        raise ValueError("CGPA must be a numeric value")
    if not isinstance(has_bachelor_degree, bool):
        raise ValueError("has_bachelor_degree must be a boolean value")
    if cgpa < 0 or cgpa > 4.0:
        raise ValueError("CGPA must be between 0 and 4.0")
    
    result = {
        'is_eligible': True,
        'reasons': [],
        'cgpa_requirement_met': False,
        'degree_requirement_met': False
    }
    
    # Check degree requirement
    if has_bachelor_degree:
        result['degree_requirement_met'] = True
    else:
        result['is_eligible'] = False
        result['reasons'].append("Bachelor's degree from recognized institution required")
    
    # Check CGPA requirement
    if cgpa >= 2.5:
        result['cgpa_requirement_met'] = True
    else:
        result['is_eligible'] = False
        result['reasons'].append(f"Minimum CGPA of 2.5 required (current: {cgpa})")
    
    return result


def get_user_input() -> tuple:
    """
    Gets and validates user input for CGPA and degree status.
    
    Returns:
        tuple: (cgpa, has_bachelor_degree)
    """
    while True:
        try:
            cgpa = float(input("Enter your CGPA (0.0 - 4.0 scale): "))
            if cgpa < 0 or cgpa > 4.0:
                print("CGPA must be between 0.0 and 4.0")
                continue
            
            degree_input = input("Do you have a Bachelor's degree from a recognized institution? (yes/no): ").lower()
            if degree_input not in ['yes', 'no']:
                print("Please enter 'yes' or 'no'")
                continue
            
            has_bachelor_degree = degree_input == 'yes'
            return cgpa, has_bachelor_degree
            
        except ValueError:
            print("Please enter a valid numeric value for CGPA")


def display_results(result: dict) -> None:
    """
    Displays the analysis results in a user-friendly format.
    
    Args:
        result (dict): Analysis result from analyze_admission_eligibility
    """
    print("\n=== Admission Eligibility Analysis ===")
    print(f"Overall Eligibility: {'Eligible' if result['is_eligible'] else 'Not Eligible'}")
    
    if result['is_eligible']:
        print("Congratulations! You meet all the requirements for the MBA program.")
    else:
        print("\nReasons for ineligibility:")
        for reason in result['reasons']:
            print(f"- {reason}")
    
    print("\nDetailed Requirements:")
    print(f"- Bachelor's degree requirement: {'Met' if result['degree_requirement_met'] else 'Not Met'}")
    print(f"- Minimum CGPA (2.5) requirement: {'Met' if result['cgpa_requirement_met'] else 'Not Met'}")


def main():
    """Main function to run the admission eligibility analyzer."""
    print("SOMTU MBA Admission Eligibility Analyzer")
    print("----------------------------------------")
    
    try:
        cgpa, has_bachelor_degree = get_user_input()
        result = analyze_admission_eligibility(cgpa, has_bachelor_degree)
        display_results(result)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
