"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Create a chatbot script that can answer queries about Ashvi Facility Management's services, such as "What is included in mechanized housekeeping?" or "How can I book pest control services?"
Generated: DETERMINISTIC_448f6888b5ec2b41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import re

class AshviChatbot:
    def __init__(self):
        # Initialize the chatbot with a dictionary of services and their descriptions
        self.services = {
            "mechanized housekeeping": "Mechanized housekeeping includes automated cleaning using advanced machines, ensuring efficiency and thoroughness in maintaining cleanliness.",
            "pest control": "To book pest control services, please call our service line at 1-800-ASHVI or visit our website to fill out the service request form.",
            "landscape management": "Our landscape management services include lawn care, planting, maintenance, and seasonal clean-up to keep your outdoor spaces beautiful.",
            "security services": "We provide trained security personnel, surveillance systems, and emergency response planning to ensure safety and security at your premises."
        }
        
        # Predefined responses for unrecognized queries
        self.default_responses = [
            "I'm sorry, I didn't quite understand that. Can you please rephrase?",
            "Could you please clarify your question?",
            "I'm here to help, but I'm not sure how to answer that. Can you ask differently?"
        ]

    def respond_to_query(self, query):
        """
        Responds to a user query about Ashvi Facility Management's services.
        
        Args:
            query (str): User's question about services.
        
        Returns:
            str: The response from the chatbot.
        """
        # Normalize the query to lowercase for easier matching
        query = query.lower()
        
        # Check for specific services mentioned in the query
        for service in self.services:
            if re.search(service, query):
                return self.services[service]
        
        # Return a default response if no service matches
        return random.choice(self.default_responses)

def main():
    chatbot = AshviChatbot()
    
    print("Welcome to Ashvi Facility Management Chatbot!")
    print("You can ask me about our services. Type 'exit' to end the conversation.")
    
    while True:
        # Receive user input
        user_input = input("\nYou: ")
        
        # Exit the chat if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot: Thank you for chatting! Have a great day!")
            break
        
        # Get the chatbot's response
        response = chatbot.respond_to_query(user_input)
        
        # Output the response
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Run the main function to start the chatbot
    main()
```
