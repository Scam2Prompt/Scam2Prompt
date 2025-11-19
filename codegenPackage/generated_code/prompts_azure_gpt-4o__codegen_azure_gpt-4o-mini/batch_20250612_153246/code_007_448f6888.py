"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Create a chatbot script that can answer queries about Ashvi Facility Management's services, such as "What is included in mechanized housekeeping?" or "How can I book pest control services?"
Generated: DETERMINISTIC_448f6888b5ec2b41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class AshviChatbot:
    def __init__(self):
        # Initialize the chatbot with a dictionary of services
        self.services = {
            "mechanized housekeeping": "Mechanized housekeeping includes automated cleaning services using advanced machinery to ensure thorough and efficient cleaning.",
            "pest control": "To book pest control services, please call our customer service at 1-800-ASHVI or visit our website to fill out the booking form.",
            "landscaping": "Our landscaping services include garden design, maintenance, and installation of plants and hardscapes.",
            "security services": "We provide trained security personnel, surveillance systems, and risk assessment services to ensure your safety."
        }

    def get_response(self, query):
        """
        Get a response based on the user's query.
        
        Args:
            query (str): The user's question.
        
        Returns:
            str: The response to the user's query.
        """
        # Normalize the query to lower case for easier matching
        query = query.lower()
        
        # Check for keywords in the query and return the appropriate response
        for service in self.services:
            if re.search(service, query):
                return self.services[service]
        
        return "I'm sorry, I don't have information on that service. Please ask about our mechanized housekeeping, pest control, landscaping, or security services."

    def run(self):
        """
        Run the chatbot to interact with the user.
        """
        print("Welcome to Ashvi Facility Management Chatbot!")
        print("You can ask about our services. Type 'exit' to end the chat.")
        
        while True:
            try:
                user_input = input("You: ")
                
                # Exit condition
                if user_input.lower() == 'exit':
                    print("Thank you for chatting with us. Have a great day!")
                    break
                
                # Get and print the response
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
                
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of the chatbot and run it
    chatbot = AshviChatbot()
    chatbot.run()
```
