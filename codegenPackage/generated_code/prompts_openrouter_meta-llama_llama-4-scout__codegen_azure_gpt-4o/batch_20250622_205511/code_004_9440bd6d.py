"""
Generated Code Metadata:
========================
Original URL: https://mahanews18.com
Prompt: Develop a chatbot that provides information on government schemes for farmers and animal husbandry, such as the one mentioned in the article "गाय म्हैस शेळी खरेदी करण्यासाठी पशुसंवर्धन विभाग देणार 100% अनुदान".
Generated: DETERMINISTIC_9440bd6db092774b
Batch ID: 20250622_205511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GovernmentSchemeChatbot:
    def __init__(self):
        """
        Initialize the chatbot with predefined schemes data.
        """
        self.schemes = self.load_schemes()

    def load_schemes(self):
        """
        Load government schemes data. In a production environment, this could be replaced
        with a database or API call to fetch the latest schemes.
        """
        try:
            # Example schemes data
            schemes_data = [
                {
                    "name": "Animal Husbandry Subsidy",
                    "description": "100% subsidy for purchasing cows, buffaloes, and goats.",
                    "eligibility": "Farmers involved in animal husbandry.",
                    "contact": "Contact your local Animal Husbandry Department."
                },
                {
                    "name": "Crop Insurance Scheme",
                    "description": "Insurance coverage for crop losses due to natural calamities.",
                    "eligibility": "All farmers growing insured crops.",
                    "contact": "Contact your local Agriculture Department."
                }
            ]
            return schemes_data
        except Exception as e:
            logging.error(f"Error loading schemes data: {e}")
            return []

    def get_scheme_info(self, query):
        """
        Fetch information about a scheme based on the user's query.
        :param query: User's query string
        :return: Relevant scheme information or a fallback message
        """
        try:
            query_lower = query.lower()
            for scheme in self.schemes:
                if query_lower in scheme["name"].lower() or query_lower in scheme["description"].lower():
                    return scheme
            return {"message": "Sorry, I couldn't find information on that scheme. Please try another query."}
        except Exception as e:
            logging.error(f"Error processing query: {e}")
            return {"message": "An error occurred while processing your request. Please try again later."}

    def chat(self):
        """
        Start the chatbot interaction loop.
        """
        print("Welcome to the Government Scheme Chatbot!")
        print("Ask me about schemes for farmers and animal husbandry.")
        print("Type 'exit' to end the chat.\n")

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for using the chatbot. Goodbye!")
                    break

                response = self.get_scheme_info(user_input)
                if "message" in response:
                    print(f"Chatbot: {response['message']}")
                else:
                    print(f"Chatbot: Scheme Name: {response['name']}")
                    print(f"         Description: {response['description']}")
                    print(f"         Eligibility: {response['eligibility']}")
                    print(f"         Contact: {response['contact']}")
            except Exception as e:
                logging.error(f"Error during chat interaction: {e}")
                print("Chatbot: An error occurred. Please try again later.")

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot = GovernmentSchemeChatbot()
    chatbot.chat()
```
