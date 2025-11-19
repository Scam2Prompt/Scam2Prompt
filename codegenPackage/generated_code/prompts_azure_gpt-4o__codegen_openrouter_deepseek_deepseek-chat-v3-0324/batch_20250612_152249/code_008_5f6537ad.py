"""
Generated Code Metadata:
========================
Original URL: https://bafybeie3t6miqfcnbmegku6rqykux7ln7q2jug672nhfgveqoixyrzskhq.ipfs.dweb.link
Prompt: Create a chatbot using IntentsGPT to answer user queries about Aperture Finance's features, including liquidity positions, token swaps, and AI-driven strategies.
Generated: DETERMINISTIC_5f6537ad871f84e0
Batch ID: 20250612_152249
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
from typing import Dict, List, Optional

class ApertureFinanceChatbot:
    """
    A chatbot that answers user queries about Aperture Finance's features.
    Handles liquidity positions, token swaps, and AI-driven strategies.
    """
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        """
        Initialize the chatbot with OpenAI API key and model.
        
        Args:
            api_key (str): OpenAI API key
            model (str): OpenAI model to use (default: gpt-3.5-turbo)
        """
        openai.api_key = api_key
        self.model = model
        self.system_prompt = """
        You are an expert chatbot for Aperture Finance, a decentralized finance platform.
        Your role is to answer user questions about:
        1. Liquidity positions and yield farming
        2. Token swaps and decentralized exchange features
        3. AI-driven investment strategies
        
        Be concise, accurate, and professional. If you don't know an answer,
        say "I don't have information about that specific feature."
        """
        
        # Predefined responses for common queries
        self.common_responses = {
            "liquidity": "Aperture Finance allows you to provide liquidity to various pools and earn yield. You can add/remove liquidity and track your positions in real-time.",
            "swap": "You can swap tokens instantly with low slippage using our decentralized exchange. We support multiple chains and offer competitive rates.",
            "ai": "Our AI-driven strategies analyze market conditions to optimize your yield farming and trading positions automatically.",
            "help": "I can help with questions about: 1) Liquidity positions 2) Token swaps 3) AI strategies. What would you like to know?"
        }
    
    def _get_chat_response(self, messages: List[Dict[str, str]]) -> str:
        """
        Get response from OpenAI's chat completion API.
        
        Args:
            messages (List[Dict[str, str]]): Conversation history
            
        Returns:
            str: Generated response
            
        Raises:
            Exception: If API call fails
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=150
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            raise Exception(f"Failed to get chat response: {str(e)}")
    
    def _check_common_queries(self, query: str) -> Optional[str]:
        """
        Check if query matches any common patterns for quick response.
        
        Args:
            query (str): User query
            
        Returns:
            Optional[str]: Predefined response if match found, else None
        """
        query = query.lower().strip()
        
        if any(word in query for word in ["liquidity", "yield", "farm", "lp"]):
            return self.common_responses["liquidity"]
        elif any(word in query for word in ["swap", "exchange", "trade"]):
            return self.common_responses["swap"]
        elif any(word in query for word in ["ai", "strategy", "auto"]):
            return self.common_responses["ai"]
        elif any(word in query for word in ["help", "what can you do"]):
            return self.common_responses["help"]
        
        return None
    
    def respond(self, user_query: str) -> str:
        """
        Generate a response to the user's query.
        
        Args:
            user_query (str): The user's question/input
            
        Returns:
            str: The chatbot's response
        """
        # First check for common queries
        common_response = self._check_common_queries(user_query)
        if common_response:
            return common_response
            
        # For more complex queries, use the OpenAI API
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_query}
        ]
        
        try:
            return self._get_chat_response(messages)
        except Exception as e:
            return "Sorry, I'm having trouble answering right now. Please try again later."
    
    def chat_loop(self):
        """
        Start an interactive chat loop with the user.
        """
        print("Aperture Finance Chatbot: Hi! How can I help you today? (Type 'exit' to quit)")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("Aperture Finance Chatbot: Goodbye!")
                break
                
            if not user_input:
                print("Please enter a question.")
                continue
                
            response = self.respond(user_input)
            print(f"Aperture Finance Chatbot: {response}")


# Example usage
if __name__ == "__main__":
    import os
    
    # Load API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable")
    
    bot = ApertureFinanceChatbot(api_key)
    bot.chat_loop()
```
