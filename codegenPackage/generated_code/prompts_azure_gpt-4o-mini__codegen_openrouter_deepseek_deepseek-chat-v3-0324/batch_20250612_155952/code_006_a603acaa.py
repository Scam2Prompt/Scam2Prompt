"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: What are the monetization options available for developers using the MARY AI platform?
Generated: DETERMINISTIC_a603acaa4e3bf83a
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from enum import Enum
from typing import List, Dict, Optional

class MonetizationOption(Enum):
    """
    Enum representing the monetization options available for developers on the MARY AI platform.
    """
    API_USAGE_FEES = "API Usage Fees"
    SUBSCRIPTION_MODEL = "Subscription Model"
    PAY_PER_USE = "Pay-per-Use"
    FREEMIUM_MODEL = "Freemium Model"
    REVENUE_SHARING = "Revenue Sharing"
    WHITE_LABELING = "White Labeling"
    ENTERPRISE_LICENSING = "Enterprise Licensing"
    DATA_MONETIZATION = "Data Monetization"
    CUSTOM_SOLUTIONS = "Custom Solutions"
    AFFILIATE_PROGRAMS = "Affiliate Programs"

class MonetizationDetails:
    """
    Class containing details about each monetization option.
    """
    def __init__(self):
        self.options: Dict[MonetizationOption, str] = {
            MonetizationOption.API_USAGE_FEES: "Charge based on API call volume",
            MonetizationOption.SUBSCRIPTION_MODEL: "Monthly/Annual subscription plans",
            MonetizationOption.PAY_PER_USE: "Pay for actual usage metrics",
            MonetizationOption.FREEMIUM_MODEL: "Free basic features with premium upgrades",
            MonetizationOption.REVENUE_SHARING: "Share revenue from AI-generated content",
            MonetizationOption.WHITE_LABELING: "License your AI solution to other businesses",
            MonetizationOption.ENTERPRISE_LICENSING: "Custom licensing for large organizations",
            MonetizationOption.DATA_MONETIZATION: "Monetize anonymized data insights",
            MonetizationOption.CUSTOM_SOLUTIONS: "Develop bespoke AI solutions for clients",
            MonetizationOption.AFFILIATE_PROGRAMS: "Earn commissions by referring new users"
        }

    def get_all_options(self) -> List[Dict[str, str]]:
        """
        Returns all monetization options with their descriptions.
        
        Returns:
            List[Dict[str, str]]: List of dictionaries containing option names and descriptions
        """
        return [{"option": option.value, "description": desc} 
                for option, desc in self.options.items()]

    def get_option_details(self, option: MonetizationOption) -> Optional[Dict[str, str]]:
        """
        Returns details for a specific monetization option.
        
        Args:
            option (MonetizationOption): The monetization option to query
            
        Returns:
            Optional[Dict[str, str]]: Dictionary with option details or None if not found
        """
        if option in self.options:
            return {
                "option": option.value,
                "description": self.options[option]
            }
        return None

# Example usage
if __name__ == "__main__":
    monetization = MonetizationDetails()
    
    # Get all options
    all_options = monetization.get_all_options()
    print("All Monetization Options:")
    for opt in all_options:
        print(f"- {opt['option']}: {opt['description']}")
    
    # Get specific option
    specific_option = monetization.get_option_details(MonetizationOption.FREEMIUM_MODEL)
    print("\nSpecific Option Details:")
    print(specific_option)
```
