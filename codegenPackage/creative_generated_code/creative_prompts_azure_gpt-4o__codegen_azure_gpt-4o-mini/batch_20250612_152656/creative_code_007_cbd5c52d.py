"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-theai-def.web.app
Prompt: Create a chatbot using Python that mimics ScottyChat, offering cryptocurrency market insights and answering questions about $SCOTTY tokens.
Generated: DETERMINISTIC_cbd5c52d87fb42d3
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class ScottyChatBot:
    """
    A chatbot that provides cryptocurrency market insights and answers questions
    about $SCOTTY tokens.
    """

    BASE_URL = "https://api.coingecko.com/api/v3"
    
    def __init__(self):
        """Initialize the ScottyChatBot."""
        self.token_symbol = "SCOTTY"
    
    def get_market_data(self):
        """
        Fetch market data for cryptocurrencies from CoinGecko.

        Returns:
            dict: A dictionary containing market data.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/coins/markets", params={
                'vs_currency': 'usd',
                'order': 'market_cap_desc',
                'per_page': 10,
                'page': 1,
                'sparkline': False
            })
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching market data: {e}")
            return None

    def get_token_info(self):
        """
        Fetch information about the $SCOTTY token.

        Returns:
            dict: A dictionary containing $SCOTTY token information.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/coins/{self.token_symbol.lower()}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching $SCOTTY token information: {e}")
            return None

    def process_query(self, query):
        """
        Process user queries related to cryptocurrency and $SCOTTY tokens.

        Args:
            query (str): The user's query.

        Returns:
            str: A response to the user's query.
        """
        if "market" in query.lower():
            market_data = self.get_market_data()
            if market_data:
                return f"Top cryptocurrencies:\n" + "\n".join(
                    f"{coin['name']} (${coin['symbol'].upper()}): ${coin['current_price']}" for coin in market_data
                )
            else:
                return "I'm sorry, I couldn't retrieve the market data at this moment."
        
        elif "scotty" in query.lower() or "$scotty" in query.lower():
            token_info = self.get_token_info()
            if token_info:
                return (f"{token_info['name']} (${token_info['symbol'].upper()}): "
                        f"Current Price: ${token_info['market_data']['current_price']['usd']}\n"
                        f"Market Cap: ${token_info['market_data']['market_cap']['usd']}")
            else:
                return "I'm sorry, I couldn't retrieve $SCOTTY token information at this moment."

        return "I'm sorry, I can only provide information about the market and $SCOTTY tokens."

def main():
    """
    Main function to run the ScottyChatBot.
    """
    bot = ScottyChatBot()
    print("Welcome to ScottyChat! Ask me about cryptocurrency or $SCOTTY tokens.")

    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("ScottyChat: Goodbye!")
            break
            
        response = bot.process_query(user_query)
        print(f"ScottyChat: {response}")

if __name__ == "__main__":
    main()
```
