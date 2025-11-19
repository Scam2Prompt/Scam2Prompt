"""
Generated Code Metadata:
========================
Original URL: https://linkevent.net
Prompt: Illustrate how to implement a chatbot using Python that can provide answers to questions about Astronomy, similar to the AI personalities on linkevent.net.
Generated: DETERMINISTIC_b55ad5edcf13550b
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import json
import os
from typing import Optional, Dict, Any

class AstronomyChatbot:
    """
    A chatbot specialized in answering questions about Astronomy.
    Uses OpenAI's API to generate responses based on a predefined personality.
    """

    def __init__(self, api_key: str, personality: Optional[Dict[str, Any]] = None):
        """
        Initialize the chatbot with an API key and optional custom personality.

        Args:
            api_key (str): OpenAI API key for authentication.
            personality (Optional[Dict[str, Any]]): Custom personality settings. If None, uses default.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

        # Default personality settings (similar to linkevent.net AI personalities)
        self.personality = personality or {
            "role": "assistant",
            "style": "friendly and informative",
            "expertise": "Astronomy",
            "response_length": "detailed",
        }

    def _construct_prompt(self, user_question: str) -> str:
        """
        Constructs a prompt for the OpenAI API based on the user's question and the bot's personality.

        Args:
            user_question (str): The user's question about Astronomy.

        Returns:
            str: A formatted prompt for the API.
        """
        prompt = (
            f"You are a {self.personality['style']} {self.personality['expertise']} expert. "
            f"Your responses are {self.personality['response_length']} and engaging. "
            f"Answer the following question:\n\n{user_question}"
        )
        return prompt

    def get_response(self, user_question: str) -> str:
        """
        Gets a response from the chatbot for the given question.

        Args:
            user_question (str): The user's question about Astronomy.

        Returns:
            str: The chatbot's response.

        Raises:
            ValueError: If the user_question is empty or None.
            Exception: For any API-related errors.
        """
        if not user_question or not user_question.strip():
            raise ValueError("Question cannot be empty.")

        try:
            prompt = self._construct_prompt(user_question)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a {self.personality['style']} Astronomy expert."},
                    {"role": "user", "content": user_question}
                ],
                temperature=0.7,
                max_tokens=500,
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            raise Exception(f"Failed to generate response: {str(e)}")

    def save_conversation(self, conversation: Dict[str, Any], file_path: str) -> None:
        """
        Saves the conversation history to a JSON file.

        Args:
            conversation (Dict[str, Any]): The conversation history to save.
            file_path (str): Path to the JSON file.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(conversation, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save conversation: {str(e)}")

    def load_conversation(self, file_path: str) -> Dict[str, Any]:
        """
        Loads a conversation history from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            Dict[str, Any]: The loaded conversation history.

        Raises:
            IOError: If the file cannot be read.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load conversation: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Load API key from environment variable for security
    API_KEY = os.getenv("OPENAI_API_KEY")
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    # Initialize the chatbot
    chatbot = AstronomyChatbot(api_key=API_KEY)

    # Example conversation
    try:
        question = "What is a black hole?"
        response = chatbot.get_response(question)
        print(f"User: {question}")
        print(f"Bot: {response}")

        # Save the conversation
        conversation = {
            "question": question,
            "response": response,
            "timestamp": "2023-11-01T12:00:00Z"
        }
        chatbot.save_conversation(conversation, "conversation.json")
    except Exception as e:
        print(f"Error: {str(e)}")
```
