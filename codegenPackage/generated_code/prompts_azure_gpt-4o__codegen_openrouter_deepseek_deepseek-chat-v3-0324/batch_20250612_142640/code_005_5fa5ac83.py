"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Create a Python script to validate asset finance proposals submitted by businesses, ensuring they include required fields like industry sector, asset type, and payment preferences, as outlined by Rhino Asset Finance.
Generated: DETERMINISTIC_5fa5ac83e4d0240f
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any, List, Optional
from enum import Enum

class IndustrySector(Enum):
    AGRICULTURE = "Agriculture"
    CONSTRUCTION = "Construction"
    MANUFACTURING = "Manufacturing"
    TRANSPORT = "Transport"
    HEALTHCARE = "Healthcare"
    TECHNOLOGY = "Technology"
    OTHER = "Other"

class AssetType(Enum):
    VEHICLE = "Vehicle"
    EQUIPMENT = "Equipment"
    MACHINERY = "Machinery"
    PROPERTY = "Property"
    OTHER = "Other"

class PaymentPreference(Enum):
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    ANNUALLY = "Annually"
    BULLET = "Bullet"

REQUIRED_FIELDS = {
    "business_name": str,
    "industry_sector": IndustrySector,
    "asset_type": AssetType,
    "asset_value": (int, float),
    "payment_preference": PaymentPreference,
    "term_length_months": int,
    "contact_email": str
}

class ProposalValidationError(Exception):
    """Custom exception for proposal validation errors."""
    pass

def validate_proposal(proposal_data: Dict[str, Any]) -> List[str]:
    """
    Validate a business asset finance proposal against required fields and types.
    
    Args:
        proposal_data: Dictionary containing the proposal data.
        
    Returns:
        List of error messages if validation fails, empty list if valid.
        
    Raises:
        ProposalValidationError: If proposal_data is not a dictionary.
    """
    errors = []
    
    if not isinstance(proposal_data, dict):
        raise ProposalValidationError("Proposal data must be a dictionary.")
    
    # Check for missing fields
    missing_fields = [field for field in REQUIRED_FIELDS if field not in proposal_data]
    if missing_fields:
        errors.append(f"Missing required fields: {', '.join(missing_fields)}")
    
    # Validate field types and enum values
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in proposal_data:
            continue
            
        value = proposal_data[field]
        
        # Handle enum fields
        if isinstance(expected_type, type) and issubclass(expected_type, Enum):
            try:
                if isinstance(value, str):
                    expected_type(value)  # Try to create enum from string
                elif not isinstance(value, expected_type):
                    errors.append(f"Invalid value for {field}: must be a {expected_type.__name__} enum or valid string")
            except ValueError:
                valid_values = [e.value for e in expected_type]
                errors.append(f"Invalid {field}: must be one of {valid_values}")
        # Handle numeric fields (int or float)
        elif expected_type in ((int, float),):
            if not isinstance(value, (int, float)):
                errors.append(f"Invalid type for {field}: must be a number")
        # Handle other types
        elif not isinstance(value, expected_type):
            errors.append(f"Invalid type for {field}: expected {expected_type.__name__}, got {type(value).__name__}")
    
    # Additional validation for specific fields
    if "asset_value" in proposal_data and proposal_data["asset_value"] <= 0:
        errors.append("Asset value must be greater than 0")
    
    if "term_length_months" in proposal_data and proposal_data["term_length_months"] <= 0:
        errors.append("Term length must be greater than 0 months")
    
    if "contact_email" in proposal_data and "@" not in proposal_data["contact_email"]:
        errors.append("Invalid email format")
    
    return errors

def load_proposal_from_json(json_str: str) -> Optional[Dict[str, Any]]:
    """
    Load proposal data from JSON string.
    
    Args:
        json_str: JSON string containing proposal data.
        
    Returns:
        Parsed dictionary or None if JSON is invalid.
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None

def validate_proposal_from_json(json_str: str) -> List[str]:
    """
    Validate a proposal from JSON string.
    
    Args:
        json_str: JSON string containing proposal data.
        
    Returns:
        List of error messages if validation fails, empty list if valid.
    """
    proposal_data = load_proposal_from_json(json_str)
    if proposal_data is None:
        return ["Invalid JSON format"]
    return validate_proposal(proposal_data)

def main():
    """Example usage of the proposal validation."""
    example_proposal = {
        "business_name": "ABC Construction",
        "industry_sector": "Construction",
        "asset_type": "Equipment",
        "asset_value": 50000,
        "payment_preference": "Monthly",
        "term_length_months": 36,
        "contact_email": "contact@abcconstruction.com"
    }
    
    errors = validate_proposal(example_proposal)
    if errors:
        print("Proposal validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Proposal is valid.")

if __name__ == "__main__":
    main()
```
