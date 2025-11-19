"""
Generated Code Metadata:
========================
Original URL: https://angelyeban.pages.dev
Prompt: Create a list of FAQs and answers for Guardarian's on-ramp and off-ramp services, including information on fees, verification, and supported currencies.
Generated: DETERMINISTIC_6b511fdc78de307b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, well-structured implementation for a FAQ system in Python using a dictionary-based approach:

```python
# faq_service.py
from typing import Dict, List, Tuple

class GuardarianFAQService:
    """
    A service providing FAQs for Guardarian's on-ramp and off-ramp services.
    Includes information on fees, verification, and supported currencies.
    """
    
    def __init__(self):
        self.faqs: Dict[str, List[Tuple[str, str]]] = {
            'general': [
                (
                    "What is Guardarian's on-ramp service?",
                    "Guardarian's on-ramp service allows users to purchase cryptocurrencies "
                    "using traditional fiat currencies through various payment methods."
                ),
                (
                    "What is Guardarian's off-ramp service?",
                    "Guardarian's off-ramp service enables users to convert their cryptocurrencies "
                    "back to fiat currencies and withdraw to their bank accounts."
                )
            ],
            'fees': [
                (
                    "What are the fees for using Guardarian's services?",
                    "Fees vary depending on the transaction size, payment method, and currency. "
                    "Typical fees range from 0.5% to 2.5%. Always check the current rates "
                    "on our website before making a transaction."
                ),
                (
                    "Are there any hidden fees?",
                    "No, Guardarian is transparent about all fees. The exact amount you'll pay "
                    "is always displayed before you confirm the transaction."
                )
            ],
            'verification': [
                (
                    "Is verification required to use Guardarian?",
                    "Yes, Guardarian requires identity verification (KYC) for all users to comply "
                    "with financial regulations. The process typically takes less than 15 minutes."
                ),
                (
                    "What documents are needed for verification?",
                    "You'll need a government-issued ID (passport, driver's license) and in some cases, "
                    "a proof of address document (utility bill, bank statement)."
                )
            ],
            'currencies': [
                (
                    "Which fiat currencies does Guardarian support?",
                    "Guardarian supports multiple fiat currencies including EUR, USD, GBP, and more. "
                    "The full list is available on our website."
                ),
                (
                    "Which cryptocurrencies does Guardarian support?",
                    "We support major cryptocurrencies like Bitcoin (BTC), Ethereum (ETH), and many others. "
                    "Check our website for the most up-to-date list."
                )
            ]
        }
    
    def get_faqs(self, category: str = None) -> List[Tuple[str, str]]:
        """
        Retrieve FAQs based on category.
        
        Args:
            category (str, optional): FAQ category ('general', 'fees', 'verification', 'currencies'). 
                                    If None, returns all FAQs.
        
        Returns:
            List of tuples containing (question, answer) pairs
            
        Raises:
            ValueError: If invalid category is provided
        """
        if category is None:
            return [item for sublist in self.faqs.values() for item in sublist]
        
        if category not in self.faqs:
            raise ValueError(f"Invalid category. Available categories: {list(self.faqs.keys())}")
            
        return self.faqs[category]
    
    def search_faqs(self, query: str) -> List[Tuple[str, str]]:
        """
        Search FAQs for questions or answers containing the query string.
        
        Args:
            query: Search term to look for in questions and answers
            
        Returns:
            List of matching (question, answer) pairs
        """
        query = query.lower()
        results = []
        
        for category in self.faqs.values():
            for question, answer in category:
                if query in question.lower() or query in answer.lower():
                    results.append((question, answer))
                    
        return results


# Example usage
if __name__ == "__main__":
    faq_service = GuardarianFAQService()
    
    try:
        # Get all FAQs
        print("All FAQs:")
        for q, a in faq_service.get_faqs():
            print(f"Q: {q}\nA: {a}\n")
        
        # Get specific category
        print("\nVerification FAQs:")
        for q, a in faq_service.get_faqs('verification'):
            print(f"Q: {q}\nA: {a}\n")
        
        # Search
        print("\nSearch results for 'fees':")
        for q, a in faq_service.search_faqs('fees'):
            print(f"Q: {q}\nA: {a}\n")
            
    except ValueError as e:
        print(f"Error: {e}")
```
