"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-en.web.app
Prompt: Develop a chatbot using OpenAI's GPT API that mimics ScottyChat, providing cryptocurrency market insights and answering questions about $SCOTTY tokens.
Generated: DETERMINISTIC_7df2c07ace5a7782
Batch ID: 20250612_151405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import openai
from dotenv import load_dotenv
from typing import Dict, Any, Optional

# Load environment variables
load_dotenv()

class ScottyChat:
    """
    A chatbot that provides cryptocurrency market insights and answers questions about $SCOTTY tokens.
    """
    
    def __init__(self):
        """
        Initialize the chatbot with OpenAI API key and system prompt.
        """
        openai.api_key = os.getenv("OPENAI_API_KEY")
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        self.system_prompt = """
        You are ScottyChat, an AI assistant specialized in cryptocurrency markets 
        and the $SCOTTY token. Your responses should be:
        - Professional yet friendly
        - Focused on cryptocurrency insights
        - Accurate about $SCOTTY token details
        - Clear and concise
        - Helpful for both beginners and experienced traders
        
        If asked about non-crypto topics, politely decline to answer.
        """
    
    def get_response(self, user_message: str) -> Dict[str, Any]:
        """
        Get a response from ScottyChat based on user input.
        
        Args:
            user_message: The user's input message
            
        Returns:
            Dictionary containing the response or error information
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=256
            )
            
            return {
                "success": True,
                "response": response.choices[0].message.content.strip()
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def chat_loop(self):
        """
        Run an interactive chat loop with the user.
        """
        print("ScottyChat: Hi there! I'm ScottyChat, your cryptocurrency assistant. How can I help you today?")
        print("Type 'quit' to exit the chat.\n")
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['quit', 'exit']:
                    print("ScottyChat: Goodbye! Happy trading!")
                    break
                
                response = self.get_response(user_input)
                if response["success"]:
                    print(f"ScottyChat: {response['response']}\n")
                else:
                    print(f"Error: {response['error']}")
                    
            except KeyboardInterrupt:
                print("\nScottyChat: Goodbye! Happy trading!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")
                break

if __name__ == "__main__":
    try:
        chatbot = ScottyChat()
        chatbot.chat_loop()
    except Exception as e:
        print(f"Failed to initialize ScottyChat: {str(e)}")
```
