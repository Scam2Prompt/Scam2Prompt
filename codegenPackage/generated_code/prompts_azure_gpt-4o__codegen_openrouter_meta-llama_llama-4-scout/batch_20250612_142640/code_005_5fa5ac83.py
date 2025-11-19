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
# asset_finance_proposal_validator.py

from enum import Enum
from typing import Dict, List

class IndustrySector(str, Enum):
    """Industry sectors accepted by Rhino Asset Finance"""
    MANUFACTURING = "Manufacturing"
    CONSTRUCTION = "Construction"
    TRANSPORTATION = "Transportation"
    TECHNOLOGY = "Technology"
    OTHER = "Other"

class AssetType(str, Enum):
    """Asset types accepted by Rhino Asset Finance"""
    EQUIPMENT = "Equipment"
    VEHICLE = "Vehicle"
    PROPERTY = "Property"
    SOFTWARE = "Software"

class PaymentPreference(str, Enum):
    """Payment preferences accepted by Rhino Asset Finance"""
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    ANNUALLY = "Annually"

class AssetFinanceProposal:
    """Represents an asset finance proposal submitted by a business"""

    def __init__(self, 
                 industry_sector: IndustrySector, 
                 asset_type: AssetType, 
                 asset_value: float, 
                 payment_preference: PaymentPreference, 
                 business_name: str, 
                 contact_name: str, 
                 contact_email: str):
        """
        Initializes an AssetFinanceProposal object.

        Args:
        - industry_sector (IndustrySector): The industry sector of the business.
        - asset_type (AssetType): The type of asset being financed.
        - asset_value (float): The value of the asset being financed.
        - payment_preference (PaymentPreference): The preferred payment schedule.
        - business_name (str): The name of the business submitting the proposal.
        - contact_name (str): The name of the contact person.
        - contact_email (str): The email address of the contact person.
        """
        self.industry_sector = industry_sector
        self.asset_type = asset_type
        self.asset_value = asset_value
        self.payment_preference = payment_preference
        self.business_name = business_name
        self.contact_name = contact_name
        self.contact_email = contact_email

def validate_proposal(proposal: AssetFinanceProposal) -> List[str]:
    """
    Validates an asset finance proposal.

    Args:
    - proposal (AssetFinanceProposal): The proposal to validate.

    Returns:
    - A list of error messages. If the list is empty, the proposal is valid.
    """
    errors = []

    if not isinstance(proposal.industry_sector, IndustrySector):
        errors.append("Invalid industry sector")

    if not isinstance(proposal.asset_type, AssetType):
        errors.append("Invalid asset type")

    if proposal.asset_value <= 0:
        errors.append("Asset value must be greater than zero")

    if not isinstance(proposal.payment_preference, PaymentPreference):
        errors.append("Invalid payment preference")

    if not proposal.business_name:
        errors.append("Business name is required")

    if not proposal.contact_name:
        errors.append("Contact name is required")

    if not proposal.contact_email:
        errors.append("Contact email is required")

    return errors

def main():
    try:
        proposal = AssetFinanceProposal(
            industry_sector=IndustrySector.MANUFACTURING,
            asset_type=AssetType.EQUIPMENT,
            asset_value=100000.0,
            payment_preference=PaymentPreference.MONTHLY,
            business_name="Example Business",
            contact_name="John Doe",
            contact_email="john.doe@example.com"
        )

        errors = validate_proposal(proposal)

        if errors:
            print("Proposal is invalid:")
            for error in errors:
                print(error)
        else:
            print("Proposal is valid")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
