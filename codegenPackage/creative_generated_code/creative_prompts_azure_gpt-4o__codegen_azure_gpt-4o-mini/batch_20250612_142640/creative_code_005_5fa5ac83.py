"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Create a Python script to validate asset finance proposals submitted by businesses, ensuring they include required fields like industry sector, asset type, and payment preferences, as outlined by Rhino Asset Finance.
Generated: DETERMINISTIC_5fa5ac83e4d0240f
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any, List

class ProposalValidationError(Exception):
    """Custom exception for proposal validation errors."""
    pass

class AssetFinanceProposalValidator:
    """Validator for asset finance proposals."""

    REQUIRED_FIELDS = {
        "industry_sector": str,
        "asset_type": str,
        "payment_preferences": List[str]
    }

    def __init__(self, proposal: Dict[str, Any]):
        """
        Initialize the validator with a proposal.

        :param proposal: Dictionary containing the asset finance proposal details.
        """
        self.proposal = proposal

    def validate(self) -> None:
        """
        Validate the asset finance proposal against required fields.

        :raises ProposalValidationError: If any required field is missing or invalid.
        """
        for field, field_type in self.REQUIRED_FIELDS.items():
            if field not in self.proposal:
                raise ProposalValidationError(f"Missing required field: {field}")
            if not isinstance(self.proposal[field], field_type):
                raise ProposalValidationError(f"Invalid type for field: {field}. Expected {field_type.__name__}.")

def main():
    """
    Main function to run the asset finance proposal validation.
    It reads a proposal from a JSON file and validates it.
    """
    try:
        # Load proposal from a JSON file
        with open('proposal.json', 'r') as file:
            proposal = json.load(file)

        # Initialize validator
        validator = AssetFinanceProposalValidator(proposal)
        
        # Validate the proposal
        validator.validate()
        
        print("Proposal is valid.")

    except FileNotFoundError:
        print("Error: The proposal file was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the proposal file.")
    except ProposalValidationError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
