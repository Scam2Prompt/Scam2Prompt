"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Generate a list of potential corporate benefits and discounts that could be offered to employees through a portal like Vertiv GmbH's Mitarbeiterangebote.
Generated: DETERMINISTIC_9d0c11658f6c497b
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corporate Benefits and Discounts Generator for Employee Portal

This script generates a list of potential corporate benefits and discounts
that could be offered to employees through a corporate portal.
"""

from typing import List, Dict
import random

class CorporateBenefitsGenerator:
    """
    Generates a comprehensive list of corporate benefits and discounts
    that could be offered to employees.
    """
    
    def __init__(self):
        self.benefit_categories = {
            'health_wellness': [
                'Gym membership discounts',
                'On-site fitness classes',
                'Subsidized health insurance',
                'Mental health support programs',
                'Nutrition counseling discounts',
                'Preventive health screenings',
                'Smoking cessation programs',
                'Ergonomic workstation assessments'
            ],
            'financial': [
                'Retirement plan matching',
                'Stock purchase plans',
                'Financial planning services',
                'Student loan repayment assistance',
                'Credit union membership',
                'Tax preparation services',
                'Mortgage assistance programs',
                'Car lease discounts'
            ],
            'education': [
                'Tuition reimbursement',
                'Professional certification support',
                'Online learning platform subscriptions',
                'Book purchase discounts',
                'Language course subsidies',
                'Conference attendance support',
                'Internal training programs',
                'Education loan assistance'
            ],
            'lifestyle': [
                'Employee assistance programs',
                'Childcare subsidies',
                'Elder care support',
                'Pet insurance discounts',
                'Commuter benefits',
                'Bicycle purchase programs',
                'Travel discounts',
                'Event ticket discounts'
            ],
            'shopping': [
                'Corporate discount programs (e.g., PerkAtWork)',
                'Electronics purchase programs',
                'Mobile phone plan discounts',
                'Home appliance discounts',
                'Furniture discounts',
                'Clothing store discounts',
                'Grocery store discounts',
                'Office supply discounts'
            ],
            'food': [
                'On-site cafeteria subsidies',
                'Meal delivery service discounts',
                'Coffee/tea subscriptions',
                'Local restaurant partnerships',
                'Healthy snack programs',
                'Catering service discounts',
                'Farmers market discounts',
                'Nutrition box subscriptions'
            ],
            'technology': [
                'Software discounts (Microsoft, Adobe, etc.)',
                'Hardware purchase programs',
                'Cloud service credits',
                'Home office equipment stipend',
                'Tech support services',
                'Cybersecurity tools',
                'App subscriptions',
                'Gaming equipment discounts'
            ]
        }
        
        self.vendor_specific_discounts = [
            {'vendor': 'Apple', 'discount': '10% off hardware'},
            {'vendor': 'Samsung', 'discount': '15% off select products'},
            {'vendor': 'Microsoft', 'discount': 'Office 365 at reduced rate'},
            {'vendor': 'Adidas', 'discount': '30% off employee store'},
            {'vendor': 'Deutsche Bahn', 'discount': 'BahnCard 50 at reduced price'},
            {'vendor': 'Sixt', 'discount': 'Corporate car rental rates'},
            {'vendor': 'TUI', 'discount': '5-15% off vacation packages'},
            {'vendor': 'Amazon', 'discount': 'Prime membership discount'}
        ]
    
    def generate_benefits_list(self, include_vendor_discounts: bool = True) -> Dict[str, List[str]]:
        """
        Generates a comprehensive list of corporate benefits organized by category.
        
        Args:
            include_vendor_discounts: Whether to include vendor-specific discounts
            
        Returns:
            Dictionary of benefits organized by category
        """
        benefits = {category: benefits.copy() for category, benefits in self.benefit_categories.items()}
        
        if include_vendor_discounts:
            benefits['vendor_discounts'] = [f"{d['vendor']}: {d['discount']}" for d in self.vendor_specific_discounts]
        
        return benefits
    
    def get_random_benefits(self, count: int = 5) -> List[str]:
        """
        Returns a random selection of benefits from all categories.
        
        Args:
            count: Number of benefits to return
            
        Returns:
            List of randomly selected benefits
        """
        all_benefits = []
        for category in self.benefit_categories.values():
            all_benefits.extend(category)
        
        if count > len(all_benefits):
            count = len(all_benefits)
            
        return random.sample(all_benefits, count)

# Example usage
if __name__ == "__main__":
    generator = CorporateBenefitsGenerator()
    
    # Get all benefits organized by category
    all_benefits = generator.generate_benefits_list()
    
    # Get random selection of benefits
    random_benefits = generator.get_random_benefits(10)
```
