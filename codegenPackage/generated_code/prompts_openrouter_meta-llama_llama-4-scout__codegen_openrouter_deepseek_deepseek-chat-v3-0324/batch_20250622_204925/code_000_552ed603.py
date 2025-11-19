"""
Generated Code Metadata:
========================
Original URL: https://gpt-chat.info
Prompt: Write a Python script using the ChatGPT API to generate conversational responses.
Generated: DETERMINISTIC_552ed603845cc482
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import os
from typing import Optional

class ChatGPTConversation:
    """
    A class to handle conversations with the ChatGPT API.
    
    Attributes:
        api_key (str): The OpenAI API key.
        model (str): The model to use for generating responses.
        temperature (float): Controls randomness in response generation.
        max_tokens (int): Maximum number of tokens in the response.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 150
    ):
        """
        Initializes the ChatGPTConversation with the given parameters.
        
        Args:
            api_key (str, optional): OpenAI API key. If not provided, checks environment variable OPENAI_API_KEY.
            model (str): The model to use. Defaults to "gpt-3.5-turbo".
            temperature (float): Controls randomness. Defaults to 0.7.
            max_tokens (int): Maximum response length. Defaults to 150.
            
        Raises:
            ValueError: If no API key is provided and OPENAI_API_KEY is not set.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in OPENAI_API_KEY environment variable")
        
        openai.api_key = self.api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
    
    def generate_response(self, messages: list) -> str:
        """
        Generates a conversational response based on the given messages.
        
        Args:
            messages (list): A list of message dictionaries with 'role' and 'content' keys.
            
        Returns:
            str: The generated response content.
            
        Raises:
            Exception: If there's an error with the API request.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message['content']
        except Exception as e:
            raise Exception(f"Error generating response: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the conversation
        chat = ChatGPTConversation()
        
        # Start a conversation
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, how are you today?"}
        ]
        
        # Get and print the response
        response = chat.generate_response(messages)
        print("Assistant:", response)
        
        # Continue the conversation
        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": "Tell me a fun fact about space."})
        
        response = chat.generate_response(messages)
        print("Assistant:", response)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
