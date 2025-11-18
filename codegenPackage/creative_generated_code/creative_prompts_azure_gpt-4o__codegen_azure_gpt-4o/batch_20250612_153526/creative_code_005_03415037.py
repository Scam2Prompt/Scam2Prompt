"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myrolandclaim.org
Prompt: Create a Python function to validate user input against eligibility criteria for a legal claim, using the Roland Consumer Claim's conditions as an example.
Generated: DETERMINISTIC_03415037aa4848f5
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def validate_legal_claim(age: int, residency_status: str, incident_date: str, claim_reason: str) -> dict:
    """
    Validate user input against eligibility criteria for a legal claim.
    
    Eligibility criteria:
    1. Age must be at least 18 years old.
    2. Residency status must be "Citizen" or "Permanent Resident".
    3. Incident date must be within the last 5 years.
    4. Claim reason must be a non-empty string and one of the allowed reasons.
    
    Parameters:
    - age (int): Age of the claimant.
    - residency_status (str): Residency status of the claimant (e.g., "Citizen", "Permanent Resident").
    - incident_date (str): Date of the incident in YYYY-MM-DD format.
    - claim_reason (str): Reason for the legal claim.
    
    Returns:
    - dict: A dictionary containing validation results with keys 'is_eligible' (bool) and 'errors' (list).
    """
    from datetime import datetime
    errors = []

    # Validate age
    if not isinstance(age, int) or age < 18:
        errors.append("Claimant must be at least 18 years old.")

    # Validate residency status
    allowed_residencies = {"Citizen", "Permanent Resident"}
    if residency_status not in allowed_residencies:
        errors.append("Residency status must be 'Citizen' or 'Permanent Resident'.")

    # Validate incident date
    try:
        incident_datetime = datetime.strptime(incident_date, "%Y-%m-%d")
        five_years_ago = datetime.now() - timedelta(days=5 * 365)
        if incident_datetime < five_years_ago:
            errors.append("Incident date must be within the last 5 years.")
    except ValueError:
        errors.append("Incident date must be in YYYY-MM-DD format.")

    # Validate claim reason
    allowed_reasons = {"Product Defect", "Service Issue", "Contract Breach", "Misrepresentation"}
    if not claim_reason or claim_reason not in allowed_reasons:
        errors.append(f"Claim reason must be one of the following: {', '.join(allowed_reasons)}.")

    # Determine eligibility
    is_eligible = len(errors) == 0

    return {
        "is_eligible": is_eligible,
        "errors": errors
    }


# Example usage:
# claim_validation = validate_legal_claim(age=25, residency_status="Citizen", incident_date="2018-09-15", claim_reason="Product Defect")
# print(claim_validation)
```
