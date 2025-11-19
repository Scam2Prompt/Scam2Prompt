"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqsy4i2xejq5goxyzbuufogxpqgugbowdte35bpuvzrccwy5cnr4.ipfs.dweb.link
Prompt: Generate a code snippet to check eligibility for participating in the Gyroscope Community based on the information provided on the website.
Generated: DETERMINISTIC_e9c770d12139b192
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def check_eligibility(age, residency_status, has_gyroscope_device, has_signed_consent):
    """
    Check eligibility for participating in the Gyroscope Community based on provided criteria.
    
    Args:
        age (int): Age of the applicant.
        residency_status (str): Residency status of the applicant ('resident' or 'non-resident').
        has_gyroscope_device (bool): Whether the applicant has a Gyroscope device.
        has_signed_consent (bool): Whether the applicant has signed the consent form.
    
    Returns:
        dict: Dictionary containing eligibility status and reasons if ineligible.
              Format: {'eligible': bool, 'reasons': list[str]}
    
    Raises:
        ValueError: If input values are invalid.
    """
    # Validate input parameters
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a positive integer")
    if residency_status not in ['resident', 'non-resident']:
        raise ValueError("Residency status must be either 'resident' or 'non-resident'")
    if not isinstance(has_gyroscope_device, bool):
        raise ValueError("has_gyroscope_device must be a boolean value")
    if not isinstance(has_signed_consent, bool):
        raise ValueError("has_signed_consent must be a boolean value")
    
    reasons = []
    eligible = True
    
    # Check eligibility criteria
    if age < 18:
        reasons.append("Must be at least 18 years old")
        eligible = False
    
    if residency_status != 'resident':
        reasons.append("Must be a resident")
        eligible = False
    
    if not has_gyroscope_device:
        reasons.append("Must have a Gyroscope device")
        eligible = False
    
    if not has_signed_consent:
        reasons.append("Must have signed the consent form")
        eligible = False
    
    return {'eligible': eligible, 'reasons': reasons}

# Example usage
if __name__ == "__main__":
    try:
        # Test case 1: Eligible participant
        result1 = check_eligibility(
            age=25,
            residency_status='resident',
            has_gyroscope_device=True,
            has_signed_consent=True
        )
        print("Test Case 1:", result1)
        
        # Test case 2: Ineligible participant
        result2 = check_eligibility(
            age=17,
            residency_status='non-resident',
            has_gyroscope_device=False,
            has_signed_consent=False
        )
        print("Test Case 2:", result2)
        
    except ValueError as e:
        print(f"Error: {e}")
```
