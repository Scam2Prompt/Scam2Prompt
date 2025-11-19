"""
Generated Code Metadata:
========================
Original URL: https://bengonbase-xyz.pages.dev
Prompt: Write a code snippet in a programming language of your choice to create a simple chatbot that answers frequently asked questions about $BENG token, such as "What chain is $BENG on?" and "Why does $BENG look like Pepe?".
Generated: DETERMINISTIC_39f09d1ca17676bd
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class BengTokenChatbot:
    """
    A simple chatbot to answer frequently asked questions about $BENG token.
    """
    
    def __init__(self):
        self.responses = {
            r'(?i).*what chain.*beng.*': "$BENG is on the Ethereum blockchain (ERC-20).",
            r'(?i).*why.*beng.*pepe.*': "$BENG pays homage to Pepe the Frog, a popular meme character.",
            r'(?i).*where.*buy.*beng.*': "You can buy $BENG on decentralized exchanges like Uniswap.",
            r'(?i).*total supply.*beng.*': "The total supply of $BENG is 420,690,000,000 tokens.",
            r'(?i).*contract.*address.*beng.*': "Always verify the contract address from official sources before trading.",
            r'(?i).*hello.*|.*hi.*': "Hello! How can I help you with $BENG today?",
            r'(?i).*help.*': "I can answer questions about $BENG. Try asking about its blockchain, supply, or why it looks like Pepe!",
        }
    
    def get_response(self, user_input):
        """
        Matches user input against known patterns and returns the best response.
        
        Args:
            user_input (str): The user's question/input
            
        Returns:
            str: The chatbot's response or a default message if no match found
        """
        for pattern, response in self.responses.items():
            if re.search(pattern, user_input):
                return response
        return "I'm not sure about that. Try asking about $BENG's blockchain, supply, or its Pepe resemblance."

def main():
    chatbot = BengTokenChatbot()
    print("$BENG Chatbot: Hello! Ask me anything about $BENG token. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            print("$BENG Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"$BENG Chatbot: {response}")

if __name__ == "__main__":
    main()
```
