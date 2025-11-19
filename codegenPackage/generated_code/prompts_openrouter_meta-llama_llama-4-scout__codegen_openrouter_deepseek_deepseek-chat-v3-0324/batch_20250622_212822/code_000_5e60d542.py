"""
Generated Code Metadata:
========================
Original URL: https://jcijobs.com
Prompt: What are the benefits of working at Johnson Controls, including health and wellbeing programs?
Generated: DETERMINISTIC_5e60d542cd585667
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script provides information about benefits at Johnson Controls including health and wellbeing programs
# It's designed to be a simple informational module that could be integrated into a larger HR system

class JohnsonControlsBenefits:
    """
    A class to represent and provide information about benefits at Johnson Controls.
    Includes details about health and wellbeing programs.
    """
    
    def __init__(self):
        """Initialize the benefits information"""
        self.benefits = {
            'health_programs': [
                'Comprehensive medical, dental, and vision insurance',
                'Health savings accounts (HSA) and flexible spending accounts (FSA)',
                'On-site health centers at select locations',
                'Preventive care and wellness programs',
                'Mental health support and counseling services'
            ],
            'wellbeing_programs': [
                'Employee assistance programs (EAP)',
                'Fitness reimbursement or gym discounts',
                'Nutrition and weight management programs',
                'Stress management resources',
                'Work-life balance initiatives'
            ],
            'other_benefits': [
                'Retirement savings plans with company match',
                'Tuition reimbursement',
                'Career development opportunities',
                'Paid time off and holidays',
                'Parental leave programs'
            ]
        }
    
    def get_health_programs(self):
        """Return a list of health-related benefits"""
        return self.benefits['health_programs']
    
    def get_wellbeing_programs(self):
        """Return a list of wellbeing programs"""
        return self.benefits['wellbeing_programs']
    
    def get_all_benefits(self):
        """Return all benefits categorized by type"""
        return self.benefits
    
    def search_benefits(self, keyword):
        """
        Search benefits by keyword
        Args:
            keyword (str): Term to search in benefits descriptions
        Returns:
            list: Matching benefits containing the keyword
        """
        if not isinstance(keyword, str):
            raise ValueError("Keyword must be a string")
            
        keyword = keyword.lower()
        results = []
        
        for category in self.benefits.values():
            for benefit in category:
                if keyword in benefit.lower():
                    results.append(benefit)
        
        return results

# Example usage
if __name__ == "__main__":
    try:
        jc_benefits = JohnsonControlsBenefits()
        print("Health Programs:")
        for program in jc_benefits.get_health_programs():
            print(f"- {program}")
            
        print("\nWellbeing Programs:")
        for program in jc_benefits.get_wellbeing_programs():
            print(f"- {program}")
            
        print("\nSearch Results for 'mental':")
        for result in jc_benefits.search_benefits("mental"):
            print(f"- {result}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
