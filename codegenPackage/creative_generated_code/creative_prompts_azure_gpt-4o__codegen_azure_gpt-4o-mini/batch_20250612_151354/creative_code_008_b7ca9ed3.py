"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Create a chatbot using Python that answers questions about Springs International Ministries’ programs, such as “Where was Jesus on Saturday?” or details about Mission 2030.
Generated: DETERMINISTIC_b7ca9ed3814b2009
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Chatbot:
    """
    A simple chatbot that provides information about Springs International Ministries’ programs.
    """

    def __init__(self):
        # A dictionary to hold predefined responses
        self.responses = {
            "Where was Jesus on Saturday?": "Jesus was in the tomb on Saturday after His crucifixion.",
            "What is Mission 2030?": "Mission 2030 is a vision aimed at reaching every nation with the Gospel of Jesus Christ by the year 2030.",
            "What programs does Springs International Ministries offer?": "We offer various programs including community outreach, missionary training, and spiritual growth workshops.",
            "Tell me about volunteer opportunities.": "We have several volunteer opportunities, including local outreach and international mission trips. You can visit our website for more details.",
            "How can I donate?": "You can donate through our website, where we have a dedicated donations page."
        }

    def get_response(self, user_input):
        """
        Returns a response based on the user input.
        
        :param user_input: The user's question as a string.
        :return: A string response to the user's question.
        """
        # Normalize the input to improve matching
        normalized_input = user_input.strip().capitalize()
        
        # Get the response if available; otherwise, return a default response
        return self.responses.get(normalized_input, "I'm sorry, I don't have the information on that. Please ask another question.")

    def start_chat(self):
        """
        Starts the chat session with the user.
        """
        print("Welcome to the Springs International Ministries Chatbot!")
        print("You can ask me about our programs. Type 'exit' to end the conversation.")

        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting! Have a great day!")
                    break

                response = self.get_response(user_input)
                print(f"Chatbot: {response}")

            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()
```
