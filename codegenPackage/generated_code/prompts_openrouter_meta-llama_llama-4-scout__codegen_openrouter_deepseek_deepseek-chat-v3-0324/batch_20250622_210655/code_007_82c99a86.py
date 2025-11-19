"""
Generated Code Metadata:
========================
Original URL: https://ecg-eg.net
Prompt: "Develop a simple chatbot script that provides basic tax consultancy services for Egyptian clients, answering questions about tax regulations, filing procedures, and deadlines."
Generated: DETERMINISTIC_82c99a8601548567
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Dict, List, Optional

class TaxConsultantChatbot:
    """
    A simple chatbot providing basic tax consultancy services for Egyptian clients.
    Handles questions about tax regulations, filing procedures, and deadlines.
    """
    
    def __init__(self):
        self.tax_rates = {
            "individual": {
                "income_tax": {
                    "brackets": [
                        (15000, 0.0),
                        (30000, 0.025),
                        (45000, 0.10),
                        (60000, 0.15),
                        (200000, 0.20),
                        (400000, 0.225),
                        (float('inf'), 0.25)
                    ]
                },
                "vat": 0.14
            },
            "corporate": {
                "income_tax": 0.225,
                "vat": 0.14
            }
        }
        
        self.deadlines = {
            "individual_income_tax": datetime.date(datetime.date.today().year, 4, 30),
            "corporate_income_tax": datetime.date(datetime.date.today().year, 4, 30),
            "vat": datetime.date(datetime.date.today().year + 1, 1, 31)
        }
        
        self.filing_procedures = {
            "individual": "File online through the Egyptian Tax Authority portal or visit a local tax office.",
            "corporate": "File online through the Egyptian Tax Authority portal with digital signature.",
            "vat": "Monthly filing required through the Egyptian Tax Authority portal."
        }
        
        self.greetings = ["hi", "hello", "hey", "greetings"]
        self.goodbyes = ["bye", "goodbye", "exit", "quit"]
    
    def calculate_income_tax(self, income: float, taxpayer_type: str = "individual") -> float:
        """
        Calculate income tax based on income and taxpayer type.
        
        Args:
            income: The taxable income amount
            taxpayer_type: Either 'individual' or 'corporate'
            
        Returns:
            Calculated tax amount
        """
        if taxpayer_type not in self.tax_rates:
            raise ValueError("Invalid taxpayer type. Must be 'individual' or 'corporate'.")
            
        if income < 0:
            raise ValueError("Income cannot be negative.")
            
        if taxpayer_type == "corporate":
            return income * self.tax_rates["corporate"]["income_tax"]
        
        tax = 0.0
        previous_limit = 0
        for bracket in self.tax_rates["individual"]["income_tax"]["brackets"]:
            limit, rate = bracket
            if income > previous_limit:
                taxable_amount = min(income, limit) - previous_limit
                tax += taxable_amount * rate
                previous_limit = limit
                
        return tax
    
    def get_deadline(self, tax_type: str) -> str:
        """
        Get the deadline for a specific tax type.
        
        Args:
            tax_type: The type of tax ('individual_income_tax', 'corporate_income_tax', 'vat')
            
        Returns:
            Formatted deadline information
        """
        if tax_type not in self.deadlines:
            return "Sorry, I don't have information about that tax type."
            
        deadline = self.deadlines[tax_type]
        today = datetime.date.today()
        
        if today > deadline:
            return f"The deadline for {tax_type.replace('_', ' ')} was on {deadline.strftime('%B %d, %Y')} (already passed)."
        else:
            days_remaining = (deadline - today).days
            return f"The deadline for {tax_type.replace('_', ' ')} is on {deadline.strftime('%B %d, %Y')} ({days_remaining} days remaining)."
    
    def get_filing_procedure(self, taxpayer_type: str) -> str:
        """
        Get filing procedure for a taxpayer type.
        
        Args:
            taxpayer_type: Either 'individual', 'corporate', or 'vat'
            
        Returns:
            Filing procedure information
        """
        if taxpayer_type not in self.filing_procedures:
            return "Sorry, I don't have information about that taxpayer type."
            
        return self.filing_procedures[taxpayer_type]
    
    def get_vat_rate(self) -> str:
        """
        Get the current VAT rate in Egypt.
        
        Returns:
            Formatted VAT rate information
        """
        return f"The current VAT rate in Egypt is {self.tax_rates['individual']['vat'] * 100}%."
    
    def process_query(self, query: str) -> str:
        """
        Process user query and generate appropriate response.
        
        Args:
            query: User's input query
            
        Returns:
            Bot's response
        """
        query = query.lower().strip()
        
        # Handle greetings
        if any(greeting in query for greeting in self.greetings):
            return "Hello! I'm your Egyptian tax consultant. How can I help you today?"
        
        # Handle goodbyes
        if any(goodbye in query for goodbye in self.goodbyes):
            return "Goodbye! Feel free to ask if you have more tax questions."
        
        # Handle specific questions
        if "income tax" in query:
            if "calculate" in query or "how much" in query:
                try:
                    if "corporate" in query:
                        return "Please provide your annual income to calculate corporate income tax."
                    else:
                        return "Please provide your annual income to calculate individual income tax."
                except Exception as e:
                    return f"Sorry, I couldn't process your request. Error: {str(e)}"
            
            if "deadline" in query:
                if "corporate" in query:
                    return self.get_deadline("corporate_income_tax")
                else:
                    return self.get_deadline("individual_income_tax")
            
            if "file" in query or "procedure" in query:
                if "corporate" in query:
                    return self.get_filing_procedure("corporate")
                else:
                    return self.get_filing_procedure("individual")
        
        elif "vat" in query:
            if "rate" in query:
                return self.get_vat_rate()
            elif "deadline" in query:
                return self.get_deadline("vat")
            elif "file" in query or "procedure" in query:
                return self.get_filing_procedure("vat")
        
        elif "deadline" in query:
            return "Please specify which tax deadline you're asking about (income tax or VAT)."
        
        elif "file" in query or "procedure" in query:
            return "Please specify which tax filing procedure you're asking about (individual, corporate, or VAT)."
        
        # Default response for unrecognized queries
        return "I'm not sure I understand. I can help with questions about Egyptian tax rates, deadlines, and filing procedures. Please try asking more specifically."

def main():
    """
    Main function to run the chatbot interactively.
    """
    chatbot = TaxConsultantChatbot()
    print("Egyptian Tax Consultant Chatbot")
    print("Type 'exit' to quit the conversation.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in chatbot.goodbyes:
                print("Bot:", chatbot.process_query(user_input))
                break
            
            response = chatbot.process_query(user_input)
            print("Bot:", response)
            
            # Handle income tax calculation follow-up
            if "Please provide your annual income" in response:
                try:
                    income = float(input("You (income amount): "))
                    taxpayer_type = "corporate" if "corporate" in response else "individual"
                    tax = chatbot.calculate_income_tax(income, taxpayer_type)
                    print(f"Bot: The estimated income tax is EGP {tax:,.2f} for an income of EGP {income:,.2f}.")
                except ValueError:
                    print("Bot: Sorry, that doesn't look like a valid income amount. Please enter a number.")
        except KeyboardInterrupt:
            print("\nBot: Goodbye!")
            break
        except Exception as e:
            print(f"Bot: Sorry, something went wrong. Error: {str(e)}")

if __name__ == "__main__":
    main()
```
