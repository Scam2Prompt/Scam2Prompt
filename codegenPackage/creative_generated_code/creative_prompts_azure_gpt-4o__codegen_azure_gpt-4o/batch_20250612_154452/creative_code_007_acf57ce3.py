"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conferencesglobal.org
Prompt: Develop a chatbot using Python that answers FAQs about abstract submission, registration, invitation letters, duplicate payments, and invoice requests based on the information provided on Conferences Global.
Generated: DETERMINISTIC_acf57ce31b59a6e6
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class FAQChatbot:
    def __init__(self):
        # Predefined FAQ responses
        self.faq_responses = {
            "abstract submission": (
                "Abstract submission details:\n"
                "1. Submission deadline is March 15th.\n"
                "2. Submit abstracts via the conference portal.\n"
                "3. Review results will be announced by April 10th."
            ),
            "registration": (
                "Registration details:\n"
                "1. Early bird registration ends on April 1st.\n"
                "2. Use your conference account to register online.\n"
                "3. Onsite registration is available at the venue."
            ),
            "invitation letters": (
                "Invitation letters:\n"
                "1. Invitation letters are provided upon request.\n"
                "2. You must complete registration before requesting an invitation letter.\n"
                "3. Email support@conferencesglobal.com for assistance."
            ),
            "duplicate payments": (
                "Duplicate payment resolution:\n"
                "1. Email proof of duplicate payments to finance@conferencesglobal.com.\n"
                "2. Refunds will be processed within 14 business days."
            ),
            "invoice requests": (
                "Invoice requests:\n"
                "1. Invoices are issued automatically after payment.\n"
                "2. For additional requests, contact finance@conferencesglobal.com."
            )
        }
    
    def get_response(self, query):
        """
        Matches the user's query with predefined FAQ topics and returns a response.
        
        Args:
            query (str): User's input message to the chatbot.
        
        Returns:
            str: The chatbot's response or an error message if no match is found.
        """
        query = query.lower()  # Normalize input query to lowercase for case-insensitive matching
        
        # Check for matching FAQ topic in the predefined responses
        for topic, response in self.faq_responses.items():
            if re.search(topic, query):  # Use regex to check if the query mentions the topic
                return response
        
        # Return a default response if no match is found
        return (
            "I'm sorry, I couldn't find information related to your query.\n"
            "Please email support@conferencesglobal.com for further assistance."
        )

# Main function to interact with the chatbot
def main():
    print("Welcome to Conferences Global FAQ Chatbot!")
    print("Ask about: abstract submission, registration, invitation letters, duplicate payments, or invoice requests.")
    print("Type 'exit' to end the conversation.\n")
    
    chatbot = FAQChatbot()  # Initialize the chatbot instance
    
    while True:
        try:
            # Get user input
            user_query = input("You: ")
            
            # Exit condition
            if user_query.lower() == "exit":
                print("Chatbot: Thank you for using Conferences Global FAQ Chatbot! Goodbye!")
                break
            
            # Get and print the chatbot's response
            response = chatbot.get_response(user_query)
            print(f"Chatbot: {response}\n")
        except KeyboardInterrupt:
            # Handle abrupt termination by user
            print("\nChatbot: Conversation ended. Goodbye!")
            break
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: An error occurred: {e}\nPlease try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
