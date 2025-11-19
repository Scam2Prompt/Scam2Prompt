"""
Generated Code Metadata:
========================
Original URL: https://securedsync.com
Prompt: What are the potential reasons for an account suspension on a secured sync service?
Generated: DETERMINISTIC_7b325c66dfbd7f0f
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum, auto
from typing import List, Optional

class SuspensionReason(Enum):
    """Enumeration of potential reasons for account suspension on a secured sync service."""
    
    MULTIPLE_FAILED_LOGIN_ATTEMPTS = auto()
    """Account was suspended due to multiple failed login attempts."""
    
    SUSPICIOUS_ACTIVITY = auto()
    """Account was suspended due to suspicious activity detected."""
    
    VIOLATION_OF_TERMS = auto()
    """Account was suspended for violating terms of service."""
    
    PAYMENT_ISSUES = auto()
    """Account was suspended due to payment issues (e.g., unpaid invoices)."""
    
    REPORTED_ABUSE = auto()
    """Account was suspended due to being reported for abuse."""
    
    SECURITY_COMPROMISE = auto()
    """Account was suspended due to suspected security compromise."""
    
    INACTIVITY = auto()
    """Account was suspended due to prolonged inactivity."""
    
    ADMIN_DISCRETION = auto()
    """Account was suspended at the discretion of the service administrators."""
    
    LEGAL_REQUIREMENT = auto()
    """Account was suspended due to legal requirements (e.g., court order)."""
    
    SYSTEM_ERROR = auto()
    """Account was suspended due to a system error (temporary)."""

def get_suspension_reasons() -> List[str]:
    """Returns a list of all possible suspension reasons as strings.
    
    Returns:
        List[str]: List of suspension reason descriptions.
    """
    return [reason.name.replace('_', ' ').title() for reason in SuspensionReason]

def get_suspension_details(reason: SuspensionReason) -> Optional[str]:
    """Provides detailed description for a given suspension reason.
    
    Args:
        reason (SuspensionReason): The suspension reason enum value.
        
    Returns:
        Optional[str]: Detailed description if reason is valid, None otherwise.
    """
    if not isinstance(reason, SuspensionReason):
        return None
    
    descriptions = {
        SuspensionReason.MULTIPLE_FAILED_LOGIN_ATTEMPTS: 
            "Account locked after multiple consecutive failed login attempts.",
        SuspensionReason.SUSPICIOUS_ACTIVITY: 
            "Unusual activity patterns detected (e.g., login from unusual locations).",
        SuspensionReason.VIOLATION_OF_TERMS: 
            "Violation of terms of service or acceptable use policy.",
        SuspensionReason.PAYMENT_ISSUES: 
            "Outstanding balance or payment method issues.",
        SuspensionReason.REPORTED_ABUSE: 
            "Account reported for abusive behavior or content.",
        SuspensionReason.SECURITY_COMPROMISE: 
            "Potential unauthorized access detected.",
        SuspensionReason.INACTIVITY: 
            "Account inactive beyond allowed period (e.g., 12 months).",
        SuspensionReason.ADMIN_DISCRETION: 
            "Suspended by administrator for unspecified reasons.",
        SuspensionReason.LEGAL_REQUIREMENT: 
            "Compliance with legal or regulatory requirements.",
        SuspensionReason.SYSTEM_ERROR: 
            "Temporary suspension due to system error (usually auto-resolved)."
    }
    
    return descriptions.get(reason)
```
