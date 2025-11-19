"""
Generated Code Metadata:
========================
Original URL: https://roc-remi.com
Prompt: Generate a code snippet for a chatbot that provides information about Chalet Roc Remi's amenities, such as its south-facing orientation, private garden, and BBQ facilities.
Generated: DETERMINISTIC_52a2b62f952c8e7e
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ChaletRocRemiChatbot:
    def __init__(self):
        # Initialize chatbot with predefined information about Chalet Roc Remi
        self.amenities = {
            "orientation": "south-facing",
            "garden": "private garden",
            "bbq": "BBQ facilities"
        }

    def get_amenity_info(self, amenity):
        """
        Fetch information about a specific amenity.
        
        :param amenity: The amenity to inquire about (e.g., 'orientation', 'garden', 'bbq').
        :return: A string containing information about the amenity or an error message.
        """
        try:
            # Check if the requested amenity exists in the predefined list
            if amenity in self.amenities:
                return f"Chalet Roc Remi has a {self.amenities[amenity]}."
            else:
                return f"Sorry, information about '{amenity}' is not available."
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An error occurred while fetching amenity information: {str(e)}"

    def handle_user_query(self, user_input):
        """
        Process user input and respond with appropriate information.
        
        :param user_input: The user's query as a string.
        :return: A response string.
        """
        try:
            # Normalize user input to lowercase for case-insensitive matching
            normalized_input = user_input.strip().lower()
            
            # Respond based on user input
            if "orientation" in normalized_input:
                return self.get_amenity_info("orientation")
            elif "garden" in normalized_input:
                return self.get_amenity_info("garden")
            elif "bbq" in normalized_input or "barbecue" in normalized_input:
                return self.get_amenity_info("bbq")
            else:
                return "I'm sorry, I can only provide information about Chalet Roc Remi's orientation, garden, and BBQ facilities."
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An error occurred while processing your query: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Instantiate the chatbot
    chatbot = ChaletRocRemiChatbot()
    
    # Simulate user queries
    user_queries = [
        "Tell me about the orientation.",
        "Does it have a garden?",
        "What BBQ facilities are available?",
        "Do you have a swimming pool?"
    ]
    
    # Process each query and print the response
    for query in user_queries:
        print(f"User: {query}")
        print(f"Chatbot: {chatbot.handle_user_query(query)}\n")
```
