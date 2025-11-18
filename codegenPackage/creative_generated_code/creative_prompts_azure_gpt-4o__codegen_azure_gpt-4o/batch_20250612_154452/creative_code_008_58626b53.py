"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retinabd.org
Prompt: Create a chatbot using Python that answers FAQs about medical admission coaching programs, referencing Retina's course offerings and success stories.
Generated: DETERMINISTIC_58626b538a1ffedf
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Chatbot:
    def __init__(self):
        """
        Initialize the chatbot with predefined FAQs and responses.
        """
        self.faqs = {
            "What courses do you offer?": "Retina offers comprehensive medical admission coaching programs, including NEET preparation and specialized topic-focused courses.",
            "What is unique about Retina's coaching program?": "Our programs are tailored with expert faculty, state-of-the-art study materials, and regular testing to ensure success.",
            "Do you have success stories?": "Yes, Retina has produced hundreds of top-ranking students in NEET, many of whom are now pursuing MBBS in prestigious medical colleges.",
            "How can I enroll?": "You can enroll by visiting our website or contacting our admissions office for guidance.",
            "What is the fee structure?": "Our fee structure is competitive and varies depending on the program. Please contact us for detailed information.",
        }

    def get_response(self, user_input):
        """
        Fetch the response for the user's query. If the query is not recognized, provide a default response.

        :param user_input: str, the question asked by the user
        :return: str, the response from the chatbot
        """
        user_input = user_input.strip().lower()  # Normalize user input
        for question, answer in self.faqs.items():
            if user_input in question.lower():  # Match user input with predefined questions
                return answer
        return "I'm sorry, I don't have an answer for that. Please contact Retina's support team for more information."

    def save_chat_history(self, chat_history, file_name="chat_history.json"):
        """
        Save chat history to a JSON file.

        :param chat_history: list, a list of dictionaries containing the chat history
        :param file_name: str, the name of the file to save the chat history
        """
        try:
            with open(file_name, "w") as file:
                json.dump(chat_history, file, indent=4)
        except IOError as e:
            print(f"Error saving chat history: {e}")


def main():
    """
    Main function to run the chatbot application.
    """
    chatbot = Chatbot()
    chat_history = []  # To store chat history between user and bot

    print("Welcome to Retina's Medical Admission Coaching Chatbot!")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Thank you for using Retina's chatbot. Goodbye!")
            break

        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

        # Add to chat history
        chat_history.append({"User": user_input, "Chatbot": response})

    # Save chat history to a file
    chatbot.save_chat_history(chat_history)
    print("Chat history saved successfully.")


if __name__ == "__main__":
    main()
```
