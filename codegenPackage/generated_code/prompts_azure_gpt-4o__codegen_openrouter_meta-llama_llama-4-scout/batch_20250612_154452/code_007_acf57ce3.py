"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Develop a chatbot using Python that answers FAQs about abstract submission, registration, invitation letters, duplicate payments, and invoice requests based on the information provided on Conferences Global.
Generated: DETERMINISTIC_acf57ce31b59a6e6
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re

class ConferenceChatbot:
    def __init__(self):
        # Define FAQs and their corresponding answers
        self.faqs = {
            "abstract submission": {
                "deadline": "The abstract submission deadline is usually 2 weeks before the conference date. Please check our website for the most up-to-date information.",
                "format": "Abstracts should be 200-250 words in length and submitted in PDF format.",
                "guidelines": "Please refer to our website for detailed abstract submission guidelines."
            },
            "registration": {
                "deadline": "The early bird registration deadline is 1 month before the conference date. Please check our website for the most up-to-date information.",
                "fees": "Registration fees vary depending on the conference and membership status. Please check our website for the most up-to-date information."
            },
            "invitation letters": {
                "request": "To request an invitation letter, please contact us at [support@conferencesglobal.org](mailto:support@conferencesglobal.org) with your name, email, and conference name.",
                "processing_time": "Invitation letters are usually processed within 3-5 business days."
            },
            "duplicate payments": {
                "refund_policy": "If you have made a duplicate payment, please contact us at [support@conferencesglobal.org](mailto:support@conferencesglobal.org) and we will assist you with a refund.",
                "processing_time": "Refunds are usually processed within 7-10 business days."
            },
            "invoice requests": {
                "request": "To request an invoice, please contact us at [support@conferencesglobal.org](mailto:support@conferencesglobal.org) with your name, email, and conference name.",
                "processing_time": "Invoices are usually processed within 3-5 business days."
            }
        }

    def process_input(self, user_input):
        user_input = user_input.lower()
        
        if re.search(r"abstract submission", user_input):
            if re.search(r"deadline", user_input):
                return self.faqs["abstract submission"]["deadline"]
            elif re.search(r"format", user_input):
                return self.faqs["abstract submission"]["format"]
            elif re.search(r"guidelines", user_input):
                return self.faqs["abstract submission"]["guidelines"]
            else:
                return "Please be more specific about your abstract submission query."
        
        elif re.search(r"registration", user_input):
            if re.search(r"deadline", user_input):
                return self.faqs["registration"]["deadline"]
            elif re.search(r"fees", user_input):
                return self.faqs["registration"]["fees"]
            else:
                return "Please be more specific about your registration query."
        
        elif re.search(r"invitation letters", user_input):
            if re.search(r"request", user_input):
                return self.faqs["invitation letters"]["request"]
            elif re.search(r"processing time", user_input):
                return self.faqs["invitation letters"]["processing_time"]
            else:
                return "Please be more specific about your invitation letter query."
        
        elif re.search(r"duplicate payments", user_input):
            if re.search(r"refund policy", user_input):
                return self.faqs["duplicate payments"]["refund_policy"]
            elif re.search(r"processing time", user_input):
                return self.faqs["duplicate payments"]["processing_time"]
            else:
                return "Please be more specific about your duplicate payment query."
        
        elif re.search(r"invoice requests", user_input):
            if re.search(r"request", user_input):
                return self.faqs["invoice requests"]["request"]
            elif re.search(r"processing time", user_input):
                return self.faqs["invoice requests"]["processing_time"]
            else:
                return "Please be more specific about your invoice request query."
        
        else:
            return "Sorry, I didn't understand your question. Please try rephrasing it."

def main():
    chatbot = ConferenceChatbot()
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "quit":
            break
        
        response = chatbot.process_input(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    main()
```
