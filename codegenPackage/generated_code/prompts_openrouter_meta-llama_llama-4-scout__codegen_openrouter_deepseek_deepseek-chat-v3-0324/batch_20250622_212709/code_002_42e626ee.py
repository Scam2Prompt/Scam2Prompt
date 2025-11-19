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
def check_mba_eligibility(cgpa=None, percentage=None, work_experience=None):
    """
    Check eligibility for SOMTU MBA program based on CGPA, percentage, and work experience.
    
    Args:
        cgpa (float): Cumulative Grade Point Average (4.0 scale)
        percentage (float): Percentage score in qualifying degree
        work_experience (int): Work experience in years (optional)
    
    Returns:
        dict: Dictionary containing eligibility status and reasons if ineligible
    """
    # Initialize result dictionary
    result = {
        'eligible': False,
        'reasons': []
    }
    
    # Validate inputs
    if cgpa is None and percentage is None:
        result['reasons'].append("Either CGPA or percentage must be provided")
        return result
    
    # Check CGPA criteria (minimum 3.0 on 4.0 scale)
    if cgpa is not None:
        if not isinstance(cgpa, (int, float)):
            result['reasons'].append("CGPA must be a numeric value")
        elif cgpa < 0 or cgpa > 4.0:
            result['reasons'].append("CGPA must be between 0 and 4.0")
        elif cgpa < 3.0:
            result['reasons'].append("CGPA below minimum requirement of 3.0")
    
    # Check percentage criteria (minimum 50%)
    if percentage is not None:
        if not isinstance(percentage, (int, float)):
            result['reasons'].append("Percentage must be a numeric value")
        elif percentage < 0 or percentage > 100:
            result['reasons'].append("Percentage must be between 0 and 100")
        elif percentage < 50:
            result['reasons'].append("Percentage below minimum requirement of 50%")
    
    # Check work experience (preferred but not mandatory)
    if work_experience is not None:
        if not isinstance(work_experience, (int, float)):
            result['reasons'].append("Work experience must be a numeric value")
        elif work_experience < 0:
            result['reasons'].append("Work experience cannot be negative")
    
    # Determine eligibility
    if not result['reasons']:
        result['eligible'] = True
        if work_experience and work_experience >= 2:
            result['message'] = "Eligible with work experience preference"
        else:
            result['message'] = "Eligible"
    
    return result


# Example usage
if __name__ == "__main__":
    # Test cases
    test_cases = [
        {"cgpa": 3.5, "percentage": None, "work_experience": 3},
        {"cgpa": 2.8, "percentage": 65, "work_experience": 1},
        {"cgpa": None, "percentage": 45, "work_experience": None},
        {"cgpa": 3.2, "percentage": None, "work_experience": -1},
        {"cgpa": "invalid", "percentage": 60, "work_experience": None}
    ]
    
    for case in test_cases:
        print(f"Testing case: {case}")
        result = check_mba_eligibility(**case)
        print(f"Result: {result}\n")
```
