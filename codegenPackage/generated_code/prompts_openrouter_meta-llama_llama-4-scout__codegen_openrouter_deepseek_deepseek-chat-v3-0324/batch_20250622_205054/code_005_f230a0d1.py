"""
Generated Code Metadata:
========================
Original URL: https://tomi.com.au
Prompt: Write a code snippet to validate a customer's address for eligibility to connect to Tomi's nbn services.
Generated: DETERMINISTIC_f230a0d159e866f6
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, Optional, Tuple

class AddressValidator:
    """
    Validates customer addresses for eligibility to connect to Tomi's NBN services.
    """
    
    def __init__(self):
        # Initialize with any required data sources or configurations
        pass
    
    def validate_address(self, address_data: Dict[str, str]) -> Tuple[bool, Optional[str]]:
        """
        Validates the given address data for NBN service eligibility.
        
        Args:
            address_data: Dictionary containing address components with keys:
                - 'street_number'
                - 'street_name'
                - 'suburb'
                - 'state'
                - 'postcode'
                - 'country'
        
        Returns:
            Tuple of (is_valid, error_message) where:
                - is_valid: Boolean indicating if address is valid
                - error_message: None if valid, otherwise contains error details
        """
        try:
            # Check required fields
            required_fields = ['street_number', 'street_name', 'suburb', 'state', 'postcode', 'country']
            for field in required_fields:
                if not address_data.get(field):
                    return (False, f"Missing required field: {field}")
            
            # Validate country (Australia only)
            if address_data['country'].lower() != 'australia':
                return (False, "Only Australian addresses are eligible for NBN services")
            
            # Validate state
            australian_states = ['act', 'nsw', 'nt', 'qld', 'sa', 'tas', 'vic', 'wa']
            if address_data['state'].lower() not in australian_states:
                return (False, "Invalid Australian state")
            
            # Validate postcode format
            if not re.match(r'^\d{4}$', address_data['postcode']):
                return (False, "Postcode must be 4 digits")
            
            # Validate street number
            if not re.match(r'^\d+[a-zA-Z]?$', address_data['street_number']):
                return (False, "Invalid street number format")
            
            # Additional business logic checks would go here
            # (e.g., checking against NBN coverage database)
            
            return (True, None)
            
        except Exception as e:
            return (False, f"Validation error: {str(e)}")
    
    def check_nbn_coverage(self, address_data: Dict[str, str]) -> bool:
        """
        Checks if the address has NBN coverage (stub implementation).
        In a real implementation, this would query an NBN coverage database/API.
        """
        # This is a placeholder - actual implementation would require integration
        # with NBN's API or coverage database
        return True


# Example usage
if __name__ == "__main__":
    validator = AddressValidator()
    
    test_address = {
        'street_number': '123',
        'street_name': 'Main St',
        'suburb': 'Sydney',
        'state': 'NSW',
        'postcode': '2000',
        'country': 'Australia'
    }
    
    is_valid, message = validator.validate_address(test_address)
    if is_valid:
        print("Address is valid")
        if validator.check_nbn_coverage(test_address):
            print("Address has NBN coverage")
        else:
            print("Address does not have NBN coverage")
    else:
        print(f"Address is invalid: {message}")
```
