"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-borpatoken.com
Prompt: Write a function to validate the claim status for BorpaToken based on the current phase (Whitelist, Overflow, or Claim) and return the eligibility status.
Generated: DETERMINISTIC_c7e6f18fdad92743
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from enum import Enum
from datetime import datetime

# Enum for different phases
class Phase(Enum):
    WHITELIST = "Whitelist"
    OVERFLOW = "Overflow"
    CLAIM = "Claim"

# Custom exception for invalid phase
class InvalidPhaseError(Exception):
    pass

def validate_borpa_token_claim(user_data, current_phase):
    """
    Validate the claim status for BorpaToken based on the current phase.

    Parameters:
        user_data (dict): Dictionary containing user information. Example:
            {
                "is_whitelisted": bool,
                "has_overflow_contribution": bool,
                "has_claimed": bool
            }
        current_phase (Phase): Current phase of the BorpaToken distribution process.

    Returns:
        dict: Eligibility status with detailed information. Example:
            {
                "is_eligible": bool,
                "reason": str
            }

    Raises:
        InvalidPhaseError: If the current phase is invalid.
    """
    # Ensure the current phase is valid
    if current_phase not in Phase:
        raise InvalidPhaseError(f"Invalid phase: {current_phase}")

    # Phase-specific validation
    if current_phase == Phase.WHITELIST:
        if user_data.get("is_whitelisted"):
            return {"is_eligible": True, "reason": "User is whitelisted."}
        else:
            return {"is_eligible": False, "reason": "User is not whitelisted."}

    elif current_phase == Phase.OVERFLOW:
        if user_data.get("has_overflow_contribution"):
            return {"is_eligible": True, "reason": "User has made an overflow contribution."}
        else:
            return {"is_eligible": False, "reason": "User has not made an overflow contribution."}

    elif current_phase == Phase.CLAIM:
        if not user_data.get("has_claimed"):
            return {"is_eligible": True, "reason": "User has not claimed yet and is eligible to claim."}
        else:
            return {"is_eligible": False, "reason": "User has already claimed."}

    # Catch any unexpected cases (this should not be reached)
    return {"is_eligible": False, "reason": "Unexpected error in phase validation."}

# Example usage
if __name__ == "__main__":
    # Example user data
    user = {
        "is_whitelisted": True,
        "has_overflow_contribution": False,
        "has_claimed": False,
    }

    # Example current phase
    current_phase = Phase.WHITELIST

    try:
        eligibility = validate_borpa_token_claim(user, current_phase)
        print(eligibility)
    except InvalidPhaseError as e:
        print(f"Error: {e}")
```
