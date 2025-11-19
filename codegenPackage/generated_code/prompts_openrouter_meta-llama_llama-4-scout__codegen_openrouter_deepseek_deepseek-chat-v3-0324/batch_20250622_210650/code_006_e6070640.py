"""
Generated Code Metadata:
========================
Original URL: https://yilgun.com
Prompt: What are the frequently asked questions about Umrah, including restrictions on performing Umrah multiple times?
Generated: DETERMINISTIC_e60706402ca10fa1
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Umrah FAQ Generator
This script provides answers to frequently asked questions about Umrah,
including restrictions on performing Umrah multiple times.
"""

class UmrahFAQ:
    """A class to handle Umrah frequently asked questions."""
    
    def __init__(self):
        """Initialize the FAQ data."""
        self.faq_data = {
            "general": [
                {
                    "question": "What is Umrah?",
                    "answer": "Umrah is a pilgrimage to Mecca that can be undertaken at any time of the year."
                },
                {
                    "question": "What is the difference between Hajj and Umrah?",
                    "answer": "Hajj is obligatory once in a lifetime for Muslims who can afford it, while Umrah is optional."
                },
                {
                    "question": "What are the pillars of Umrah?",
                    "answer": "The pillars are Ihram, Tawaf around the Kaaba, and Sa'i between Safa and Marwah."
                }
            ],
            "restrictions": [
                {
                    "question": "Can I perform Umrah multiple times?",
                    "answer": "Yes, you can perform Umrah multiple times, but there are no restrictions on the number of times."
                },
                {
                    "question": "Is there a waiting period between Umrahs?",
                    "answer": "No, there is no mandatory waiting period between performing Umrahs."
                },
                {
                    "question": "Can I perform Umrah during Hajj season?",
                    "answer": "Yes, but if you intend to perform Hajj, you must enter Ihram with the intention of Hajj."
                }
            ],
            "requirements": [
                {
                    "question": "What are the requirements for Umrah?",
                    "answer": "You must be a Muslim, have a valid visa, and be physically and financially capable."
                },
                {
                    "question": "Do women need a mahram for Umrah?",
                    "answer": "Women below 45 must be accompanied by a mahram. Women 45+ may travel in groups without a mahram."
                }
            ]
        }
    
    def get_faq(self, category=None):
        """
        Retrieve FAQs based on category.
        
        Args:
            category (str, optional): The category of FAQs to retrieve. 
                                     Options: 'general', 'restrictions', 'requirements'.
                                     If None, returns all FAQs.
        
        Returns:
            dict: A dictionary of FAQs for the specified category or all FAQs.
        """
        try:
            if category:
                return {category: self.faq_data.get(category, [])}
            return self.faq_data
        except Exception as e:
            print(f"Error retrieving FAQs: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    faq = UmrahFAQ()
    
    # Get all FAQs
    all_faqs = faq.get_faq()
    print("All FAQs:", all_faqs)
    
    # Get specific category FAQs
    restrictions_faq = faq.get_faq("restrictions")
    print("\nRestrictions FAQs:", restrictions_faq)
```
