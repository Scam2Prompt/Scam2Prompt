"""
Generated Code Metadata:
========================
Original URL: https://chat.dabaimi.top
Prompt: Generate a Python script that allows for natural conversation with a chatbot, inspired by the features of NextChat.
Generated: DETERMINISTIC_88a73e2f753d6136
Batch ID: 20250612_160133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Dict, List, Optional
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ChatBot:
    """
    A conversational chatbot that maintains conversation history and context.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        """
        Initialize the chatbot with API key and model.
        
        Args:
            api_key: OpenAI API key. If None, will try to get from environment.
            model: The model to use for chat completions.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided and not found in environment variables.")
        
        openai.api_key = self.api_key
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []
        self.system_prompt = "You are a helpful, friendly, and knowledgeable AI assistant."
        
    def add_message(self, role: str, content: str) -> None:
        """
        Add a message to the conversation history.
        
        Args:
            role: 'system', 'user', or 'assistant'
            content: The message content
        """
        if role not in ["system", "user", "assistant"]:
            raise ValueError("Invalid role. Must be 'system', 'user', or 'assistant'.")
        
        self.conversation_history.append({"role": role, "content": content})
    
    def reset_conversation(self) -> None:
        """Reset the conversation history."""
        self.conversation_history = []
        self.add_message("system", self.system_prompt)
    
    def get_response(self, user_input: str) -> str:
        """
        Get a response from the chatbot based on user input.
        
        Args:
            user_input: The user's message
            
        Returns:
            The assistant's response
        """
        try:
            self.add_message("user", user_input)
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=1000
            )
            
            assistant_response = response.choices[0].message['content']
            self.add_message("assistant", assistant_response)
            
            return assistant_response
        
        except openai.error.OpenAIError as e:
            return f"An error occurred: {str(e)}"
        
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    
    def save_conversation(self, file_path: str) -> None:
        """
        Save the conversation history to a JSON file.
        
        Args:
            file_path: Path to save the file
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.conversation_history, f, indent=2)
        except Exception as e:
            raise IOError(f"Failed to save conversation: {str(e)}")
    
    def load_conversation(self, file_path: str) -> None:
        """
        Load a conversation history from a JSON file.
        
        Args:
            file_path: Path to the file to load
        """
        try:
            with open(file_path, 'r') as f:
                self.conversation_history = json.load(f)
        except Exception as e:
            raise IOError(f"Failed to load conversation: {str(e)}")


def main():
    """Main function to run the chatbot interactively."""
    print("Welcome to the ChatBot! Type 'quit' to exit or 'reset' to start a new conversation.")
    
    try:
        bot = ChatBot()
        bot.reset_conversation()
        
        while True:
            user_input = input("\nYou: ")
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
                
            if user_input.lower() == 'reset':
                bot.reset_conversation()
                print("Conversation reset.")
                continue
                
            response = bot.get_response(user_input)
            print(f"\nAssistant: {response}")
            
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
