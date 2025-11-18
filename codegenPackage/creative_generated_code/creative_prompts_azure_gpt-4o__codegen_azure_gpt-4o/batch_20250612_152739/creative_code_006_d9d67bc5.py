"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthwithdiagnostics.com
Prompt: Create a chatbot script that answers questions about ovarian cancer prevention and early detection, referencing the content from "Health With Diagnostics."
Generated: DETERMINISTIC_d9d67bc5518fc6d9
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai

class OvarianCancerChatbot:
    """
    A chatbot that provides information about ovarian cancer prevention and early detection,
    referencing content from "Health With Diagnostics".
    """
    
    def __init__(self, api_key):
        """
        Initialize the chatbot with OpenAI API key.
        
        :param api_key: OpenAI API key for accessing GPT models.
        """
        self.api_key = api_key
        openai.api_key = self.api_key
    
    def get_response(self, query):
        """
        Fetch the response for a user query using GPT.
        
        :param query: User's question or input.
        :return: Response text from the chatbot.
        """
        try:
            # Query OpenAI GPT with the user's input
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"You are a chatbot that provides accurate and reliable information about ovarian cancer prevention and early detection, referencing content from 'Health With Diagnostics'. Answer the question: {query}",
                max_tokens=300,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except openai.error.OpenAIError as e:
            # Handle any API errors gracefully
            return f"An error occurred while fetching the response: {str(e)}"
    
    def run(self):
        """
        Run the chatbot in a simple interactive loop.
        """
        print("Welcome to the Ovarian Cancer Prevention and Early Detection Chatbot!")
        print("Ask me anything about ovarian cancer prevention and early detection.")
        print("Type 'exit' to end the chat.")

        while True:
            user_input = input("\nYour question: ")
            if user_input.lower() == "exit":
                print("Thank you for using the chatbot. Stay healthy!")
                break
            
            # Get the chatbot's response and display it
            response = self.get_response(user_input)
            print(f"\nChatbot Response: {response}")


# Entry point for the script
if __name__ == "__main__":
    # Prompt the user for their OpenAI API key
    user_api_key = input("Enter your OpenAI API key: ").strip()
    
    # Initialize and run the chatbot
    chatbot = OvarianCancerChatbot(api_key=user_api_key)
    chatbot.run()
```
