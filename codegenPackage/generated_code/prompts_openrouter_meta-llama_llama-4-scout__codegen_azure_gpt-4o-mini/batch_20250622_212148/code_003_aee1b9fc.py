"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Develop a chatbot script that answers common questions about carpet selection, repair, and maintenance, using Perfect Melbourne Carpet's 6-star classification system and room foot traffic ratings.
Generated: DETERMINISTIC_aee1b9fc7fdd735a
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class CarpetChatbot:
    def __init__(self):
        # Initialize the chatbot with common questions and answers
        self.questions_answers = {
            "What is the 6-star classification system?": 
                "The 6-star classification system rates carpets based on durability, comfort, and maintenance. A higher star rating indicates better performance.",
            "How do I choose the right carpet for my room?": 
                "Consider the foot traffic in the room. For high-traffic areas, opt for carpets with a 5 or 6-star rating. For low-traffic areas, a 3 or 4-star rating may suffice.",
            "What is the best way to maintain my carpet?": 
                "Regular vacuuming, immediate stain treatment, and professional cleaning every 12-18 months are recommended for maintaining your carpet's appearance.",
            "How can I repair a damaged carpet?": 
                "For minor damages, you can use a carpet repair kit. For significant damage, consider hiring a professional to ensure a seamless repair.",
            "What are the foot traffic ratings?": 
                "Foot traffic ratings help determine the best carpet for specific areas. Low traffic (1-2 stars), moderate traffic (3-4 stars), and high traffic (5-6 stars)."
        }

    def get_response(self, user_input):
        """
        Get a response based on user input.
        
        :param user_input: str - The question asked by the user.
        :return: str - The response to the user's question.
        """
        # Normalize user input for comparison
        normalized_input = user_input.strip().capitalize()
        
        # Check if the question is in the predefined questions
        response = self.questions_answers.get(normalized_input, "I'm sorry, I don't have an answer for that. Please ask another question.")
        return response

    def start_chat(self):
        """
        Start the chatbot interaction with the user.
        """
        print("Welcome to Perfect Melbourne Carpet Chatbot!")
        print("You can ask me about carpet selection, repair, and maintenance.")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting! Have a great day!")
                break
            
            # Get the response from the chatbot
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        # Create an instance of the chatbot and start the chat
        chatbot = CarpetChatbot()
        chatbot.start_chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
