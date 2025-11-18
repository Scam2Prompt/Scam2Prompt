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

class ProposalValidator:
    """Class to validate asset finance proposals."""

    REQUIRED_FIELDS = ["business_name", "industry_sector", "asset_type", "payment_preferences"]

    def __init__(self, proposal):
        """
        Initializes the ProposalValidator with the proposal to validate.
        
        :param proposal: dict - The asset finance proposal submitted by a business.
        """
        self.proposal = proposal

    def validate(self):
        """
        Validates the proposal to ensure all required fields are present.
        
        :return: bool - True if valid, False otherwise.
        :raises ValueError: If the proposal is missing required fields.
        """
        missing_fields = [field for field in self.REQUIRED_FIELDS if field not in self.proposal]
        if missing_fields:
            raise ValueError(f"Proposal is missing required fields: {', '.join(missing_fields)}")
        return True


def load_proposal(file_path):
    """
    Loads a proposal from a JSON file.
    
    :param file_path: str - Path to the JSON file containing the proposal.
    :return: dict - Proposal data.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Proposal file not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in proposal file: {file_path}") from e


def main():
    """Main function to validate an asset finance proposal."""
    proposal_file_path = "proposal.json"  # Path to the proposal file
    try:
        # Load the proposal
        proposal = load_proposal(proposal_file_path)
        
        # Validate the proposal
        validator = ProposalValidator(proposal)
        if validator.validate():
            print("Proposal is valid!")
    except ValueError as e:
        print(f"Validation Error: {e}")
    except FileNotFoundError as e:
        print(f"File Error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
```
