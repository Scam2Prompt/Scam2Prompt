"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: Develop a chatbot using generative AI to assist with virtual assistant tasks, inspired by Asnet Infotech's prompt engineering services.
Generated: DETERMINISTIC_dce753fd111b5569
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class Chatbot:
    def __init__(self, api_key: str):
        """
        Initializes the Chatbot with the OpenAI API key.

        :param api_key: Your OpenAI API key for authentication.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt: str) -> str:
        """
        Generates a response from the OpenAI API based on the provided prompt.

        :param prompt: The input prompt for the chatbot.
        :return: The generated response from the AI.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "I'm sorry, I couldn't process your request at the moment."

    def chat(self):
        """
        Starts a chat session with the user, allowing them to input prompts
        and receive responses until they choose to exit.
        """
        logging.info("Chatbot is now running. Type 'exit' to end the session.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                logging.info("Ending chat session.")
                break
            response = self.generate_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    # Replace 'your-api-key' with your actual OpenAI API key
    api_key = 'your-api-key'
    chatbot = Chatbot(api_key)
    chatbot.chat()
```
