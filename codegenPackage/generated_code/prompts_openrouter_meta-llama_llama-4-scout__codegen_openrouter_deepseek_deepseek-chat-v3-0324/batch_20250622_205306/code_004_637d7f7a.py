"""
Generated Code Metadata:
========================
Original URL: https://nextmoney.co.th
Prompt: "Design a chatbot dialogue flow to help customers inquire about Next Money's loan services, including motorcycle and car loans, and provide personalized recommendations."
Generated: DETERMINISTIC_637d7f7a5d752be8
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class LoanChatbot:
    """
    A chatbot to assist customers with Next Money's loan services.
    Handles inquiries about motorcycle and car loans, and provides personalized recommendations.
    """
    
    def __init__(self):
        self.loan_data = self._load_loan_data()
        self.user_context = {}
    
    def _load_loan_data(self) -> Dict:
        """Load loan product data from JSON file"""
        try:
            with open('loan_products.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Warning: loan_products.json not found. Using default data.")
            return {
                "motorcycle": {
                    "interest_rate": "5.9%",
                    "max_term": "60 months",
                    "min_amount": "5000",
                    "max_amount": "50000"
                },
                "car": {
                    "interest_rate": "4.9%",
                    "max_term": "84 months",
                    "min_amount": "10000",
                    "max_amount": "100000"
                }
            }
    
    def start_conversation(self) -> str:
        """Initialize the conversation with greeting and options"""
        self.user_context = {}  # Reset context for new conversation
        return ("Hello! Welcome to Next Money loan services. I can help you with:\n"
                "1. Motorcycle loans\n"
                "2. Car loans\n"
                "3. Personalized recommendations\n"
                "Please enter your choice (1-3): ")
    
    def handle_response(self, user_input: str) -> str:
        """Process user input and return appropriate response"""
        try:
            if not self.user_context.get('loan_type'):
                return self._handle_initial_choice(user_input)
            elif not self.user_context.get('amount'):
                return self._handle_amount_query(user_input)
            elif not self.user_context.get('term'):
                return self._handle_term_query(user_input)
            else:
                return self._provide_final_recommendation()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}. Please try again."
    
    def _handle_initial_choice(self, user_input: str) -> str:
        """Process the user's initial loan type selection"""
        if user_input == '1':
            self.user_context['loan_type'] = 'motorcycle'
            return ("Great! Let's discuss motorcycle loans.\n"
                    "What loan amount are you looking for (between ${min}-${max})? "
                    .format(**self.loan_data['motorcycle']))
        elif user_input == '2':
            self.user_context['loan_type'] = 'car'
            return ("Great! Let's discuss car loans.\n"
                    "What loan amount are you looking for (between ${min}-${max})? "
                    .format(**self.loan_data['car']))
        elif user_input == '3':
            return ("For personalized recommendations, please answer:\n"
                    "Which type of loan are you interested in? (motorcycle/car): ")
        else:
            return "Invalid choice. Please enter 1, 2, or 3."
    
    def _handle_amount_query(self, user_input: str) -> str:
        """Process the user's loan amount input"""
        try:
            amount = float(user_input)
            loan_type = self.user_context['loan_type']
            min_amount = float(self.loan_data[loan_type]['min_amount'])
            max_amount = float(self.loan_data[loan_type]['max_amount'])
            
            if amount < min_amount or amount > max_amount:
                return (f"Amount must be between ${min_amount} and ${max_amount}. "
                       "Please enter a valid amount: ")
            
            self.user_context['amount'] = amount
            max_term = self.loan_data[loan_type]['max_term']
            return (f"Got it. For ${amount:,.2f}, what loan term would you like? "
                   f"(Maximum {max_term}): ")
        except ValueError:
            return "Please enter a valid numeric amount: "
    
    def _handle_term_query(self, user_input: str) -> str:
        """Process the user's loan term input"""
        try:
            term = int(user_input)
            loan_type = self.user_context['loan_type']
            max_term = int(self.loan_data[loan_type]['max_term'].split()[0])
            
            if term <= 0 or term > max_term:
                return f"Term must be between 1 and {max_term} months. Please try again: "
            
            self.user_context['term'] = term
            return self._provide_final_recommendation()
        except ValueError:
            return "Please enter a valid number of months: "
    
    def _provide_final_recommendation(self) -> str:
        """Generate final recommendation based on collected information"""
        loan_type = self.user_context['loan_type']
        amount = self.user_context['amount']
        term = self.user_context['term']
        rate = self.loan_data[loan_type]['interest_rate']
        
        monthly_payment = self._calculate_monthly_payment(amount, term, rate)
        
        return (f"Based on your preferences:\n"
                f"- Loan type: {loan_type}\n"
                f"- Amount: ${amount:,.2f}\n"
                f"- Term: {term} months\n"
                f"- Interest rate: {rate}\n\n"
                f"Your estimated monthly payment would be: ${monthly_payment:,.2f}\n"
                f"Would you like to apply now? (yes/no): ")
    
    def _calculate_monthly_payment(self, amount: float, term: int, rate_str: str) -> float:
        """Calculate monthly payment using simple interest formula"""
        rate = float(rate_str.strip('%')) / 100
        monthly_rate = rate / 12
        principal = amount
        payment = principal * monthly_rate * (1 + monthly_rate)**term / ((1 + monthly_rate)**term - 1)
        return payment
    
    def handle_application_response(self, user_input: str) -> str:
        """Process user's response to application prompt"""
        if user_input.lower() == 'yes':
            return ("Great! Please visit our website at www.nextmoney.com/apply "
                   "to complete your application. Thank you for choosing Next Money!")
        elif user_input.lower() == 'no':
            return "Thank you for your inquiry. Let us know if you need any further assistance!"
        else:
            return "Please answer with 'yes' or 'no': "


# Example usage
if __name__ == "__main__":
    bot = LoanChatbot()
    print(bot.start_conversation())
    
    while True:
        user_input = input("> ").strip()
        response = bot.handle_response(user_input)
        print(response)
        
        if "Would you like to apply now?" in response:
            user_input = input("> ").strip()
            final_response = bot.handle_application_response(user_input)
            print(final_response)
            break
```
