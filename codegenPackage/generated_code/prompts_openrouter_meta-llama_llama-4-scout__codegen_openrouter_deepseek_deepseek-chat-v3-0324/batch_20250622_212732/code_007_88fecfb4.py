"""
Generated Code Metadata:
========================
Original URL: https://hometymex.co.za
Prompt: Generate a list of frequently asked questions (FAQs) for a home loan application platform, covering topics such as application process, credit checks, affordability, and costs associated with home loans.
Generated: DETERMINISTIC_88fecfb497397c40
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Home Loan FAQ Generator
This script generates a structured list of FAQs for a home loan application platform.
"""

class FAQGenerator:
    def __init__(self):
        self.faqs = []

    def generate_faqs(self):
        """Generate and return a list of FAQs for home loan applications."""
        self._add_general_application_faqs()
        self._add_credit_check_faqs()
        self._add_affordability_faqs()
        self._add_costs_faqs()
        return self.faqs

    def _add_general_application_faqs(self):
        """Add FAQs related to the general application process."""
        self.faqs.extend([
            {
                "question": "What documents do I need to apply for a home loan?",
                "answer": "Typically, you'll need proof of identity, income documents (payslips/tax returns), bank statements, and details of the property you wish to purchase."
            },
            {
                "question": "How long does the home loan application process take?",
                "answer": "The process usually takes between 2-6 weeks, depending on the complexity of your application and the lender's processes."
            },
            {
                "question": "Can I apply for a home loan online?",
                "answer": "Yes, most lenders allow you to start the application process online, though some steps may require in-person verification."
            }
        ])

    def _add_credit_check_faqs(self):
        """Add FAQs related to credit checks and credit scores."""
        self.faqs.extend([
            {
                "question": "Will applying for a home loan affect my credit score?",
                "answer": "Yes, lenders will perform a credit check which may temporarily affect your score. Multiple applications in a short period can have a greater impact."
            },
            {
                "question": "What credit score do I need to qualify for a home loan?",
                "answer": "Requirements vary by lender, but generally a score of 620 or higher is preferred for conventional loans. Some government-backed loans may accept lower scores."
            },
            {
                "question": "Can I get a home loan with bad credit?",
                "answer": "It may be possible, but you'll likely face higher interest rates or need a larger down payment. Some lenders specialize in bad credit loans."
            }
        ])

    def _add_affordability_faqs(self):
        """Add FAQs related to loan affordability and repayment calculations."""
        self.faqs.extend([
            {
                "question": "How much can I borrow for a home loan?",
                "answer": "This depends on your income, expenses, credit score, and the lender's criteria. Most lenders use debt-to-income ratios to determine borrowing capacity."
            },
            {
                "question": "What is the typical down payment required?",
                "answer": "Conventional loans often require 20%, but some programs (like FHA loans) may allow as little as 3.5%. First-time buyers may qualify for lower down payments."
            },
            {
                "question": "How do lenders assess my ability to repay the loan?",
                "answer": "Lenders evaluate your income stability, existing debts, credit history, and living expenses to determine if you can comfortably make repayments."
            }
        ])

    def _add_costs_faqs(self):
        """Add FAQs related to costs associated with home loans."""
        self.faqs.extend([
            {
                "question": "What costs are involved in getting a home loan?",
                "answer": "Besides the loan amount, you may need to pay application fees, valuation fees, legal fees, stamp duty, and lender's mortgage insurance (if applicable)."
            },
            {
                "question": "What is lender's mortgage insurance (LMI)?",
                "answer": "LMI protects the lender if you default on your loan. It's typically required when your down payment is less than 20% of the property value."
            },
            {
                "question": "Are there ongoing fees with a home loan?",
                "answer": "Some loans have annual fees, account-keeping fees, or redraw fees. Always check the loan terms for ongoing cost information."
            }
        ])

    def format_faqs(self, faqs=None):
        """Format FAQs for display or export."""
        if faqs is None:
            faqs = self.faqs
        formatted = []
        for i, faq in enumerate(faqs, 1):
            formatted.append(f"Q{i}: {faq['question']}")
            formatted.append(f"A{i}: {faq['answer']}\n")
        return "\n".join(formatted)

# Example usage
if __name__ == "__main__":
    generator = FAQGenerator()
    faqs = generator.generate_faqs()
    print(generator.format_faqs(faqs))
```
