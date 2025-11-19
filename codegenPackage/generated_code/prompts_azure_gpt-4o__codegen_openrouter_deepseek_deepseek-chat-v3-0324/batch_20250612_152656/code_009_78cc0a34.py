"""
Generated Code Metadata:
========================
Original URL: https://gratisbitcoin-no.pages.dev
Prompt: Generate code in Python to validate user eligibility for free Bitcoin offers from the platforms mentioned, ensuring compliance with their terms.
Generated: DETERMINISTIC_78cc0a34eaca80aa
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from datetime import datetime, timedelta
from typing import Dict, Optional, List

class BitcoinOfferValidator:
    """
    Validates user eligibility for free Bitcoin offers from various platforms.
    Handles platform-specific terms and conditions.
    """
    
    def __init__(self):
        self.platform_terms = {
            'coinbase': {
                'min_age': 18,
                'country_restrictions': ['US', 'CA', 'UK', 'EU'],
                'kyc_required': True,
                'min_account_age_days': 30
            },
            'binance': {
                'min_age': 18,
                'country_restrictions': [],
                'kyc_required': True,
                'min_account_age_days': 0
            },
            'blockchain_com': {
                'min_age': 18,
                'country_restrictions': ['US'],
                'kyc_required': False,
                'min_account_age_days': 7
            }
        }
    
    def validate_user_eligibility(
        self,
        platform: str,
        user_age: int,
        user_country: str,
        has_kyc: bool,
        account_creation_date: Optional[datetime] = None
    ) -> Dict[str, bool]:
        """
        Validates if a user is eligible for free Bitcoin offers on a given platform.
        
        Args:
            platform: Name of the platform (e.g., 'coinbase', 'binance')
            user_age: Age of the user in years
            user_country: Country code of the user (e.g., 'US', 'CA')
            has_kyc: Whether user has completed KYC verification
            account_creation_date: Date when user account was created
            
        Returns:
            Dictionary with 'eligible' (bool) and 'reasons' (list of strings if not eligible)
        """
        if platform not in self.platform_terms:
            raise ValueError(f"Unknown platform: {platform}")
        
        terms = self.platform_terms[platform]
        reasons = []
        
        # Age validation
        if user_age < terms['min_age']:
            reasons.append(f"User must be at least {terms['min_age']} years old")
        
        # Country restrictions
        if terms['country_restrictions'] and user_country not in terms['country_restrictions']:
            reasons.append(f"Not available in {user_country}")
        
        # KYC requirement
        if terms['kyc_required'] and not has_kyc:
            reasons.append("KYC verification required")
        
        # Account age requirement
        if terms['min_account_age_days'] > 0:
            if not account_creation_date:
                reasons.append("Account creation date required for validation")
            else:
                account_age = (datetime.now() - account_creation_date).days
                if account_age < terms['min_account_age_days']:
                    reasons.append(
                        f"Account must be at least {terms['min_account_age_days']} days old"
                    )
        
        return {
            'eligible': len(reasons) == 0,
            'reasons': reasons if reasons else None
        }
    
    def get_supported_platforms(self) -> List[str]:
        """Returns list of supported platforms for validation."""
        return list(self.platform_terms.keys())
    
    def get_platform_terms(self, platform: str) -> Dict:
        """
        Returns the terms and conditions for a specific platform.
        
        Args:
            platform: Name of the platform
            
        Returns:
            Dictionary containing platform terms
            
        Raises:
            ValueError: If platform is not supported
        """
        if platform not in self.platform_terms:
            raise ValueError(f"Platform {platform} not supported")
        return self.platform_terms[platform]


# Example usage
if __name__ == "__main__":
    validator = BitcoinOfferValidator()
    
    # Example user data
    user_data = {
        'platform': 'coinbase',
        'user_age': 25,
        'user_country': 'US',
        'has_kyc': True,
        'account_creation_date': datetime.now() - timedelta(days=45)
    }
    
    # Validate eligibility
    result = validator.validate_user_eligibility(**user_data)
    print(f"Eligibility Result: {result}")
```
