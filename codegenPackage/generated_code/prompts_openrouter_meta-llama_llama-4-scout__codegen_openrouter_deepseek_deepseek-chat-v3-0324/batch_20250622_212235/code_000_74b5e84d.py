"""
Generated Code Metadata:
========================
Original URL: https://giac1.ma
Prompt: What are the eligibility criteria for a company to benefit from GIAC1's consulting support and financing for strategic studies and training development in Morocco?
Generated: DETERMINISTIC_74b5e84d5e3ef772
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Eligibility criteria checker for GIAC1 consulting support and financing in Morocco

class EligibilityCriteria:
    """
    Class to check if a company meets GIAC1's eligibility criteria for consulting support and financing.
    """
    
    def __init__(self):
        self.criteria = {
            'company_type': ['SME', 'Startup', 'Large Enterprise'],
            'registration': 'Registered in Morocco',
            'sector': ['Industry', 'Services', 'Agriculture', 'Technology'],
            'project_type': ['Strategic Study', 'Training Development'],
            'financial_health': 'Positive financial indicators',
            'commitment': 'Commitment to implement recommendations'
        }
    
    def check_eligibility(self, company_info):
        """
        Check if a company meets all eligibility criteria.
        
        Args:
            company_info (dict): Dictionary containing company information
            
        Returns:
            tuple: (bool, list) - (True if eligible, list of unmet criteria if any)
        """
        unmet_criteria = []
        
        # Check company type
        if company_info.get('company_type') not in self.criteria['company_type']:
            unmet_criteria.append('company_type')
            
        # Check registration status
        if company_info.get('registration') != self.criteria['registration']:
            unmet_criteria.append('registration')
            
        # Check sector
        if company_info.get('sector') not in self.criteria['sector']:
            unmet_criteria.append('sector')
            
        # Check project type
        if company_info.get('project_type') not in self.criteria['project_type']:
            unmet_criteria.append('project_type')
            
        # Check financial health
        if company_info.get('financial_health') != self.criteria['financial_health']:
            unmet_criteria.append('financial_health')
            
        # Check commitment
        if company_info.get('commitment') != self.criteria['commitment']:
            unmet_criteria.append('commitment')
            
        return (len(unmet_criteria) == 0, unmet_criteria)


def main():
    # Example usage
    criteria_checker = EligibilityCriteria()
    
    # Sample company information
    company_data = {
        'company_type': 'SME',
        'registration': 'Registered in Morocco',
        'sector': 'Technology',
        'project_type': 'Strategic Study',
        'financial_health': 'Positive financial indicators',
        'commitment': 'Commitment to implement recommendations'
    }
    
    is_eligible, unmet = criteria_checker.check_eligibility(company_data)
    
    if is_eligible:
        print("Company is eligible for GIAC1 support")
    else:
        print(f"Company is not eligible. Unmet criteria: {unmet}")


if __name__ == "__main__":
    main()
```
