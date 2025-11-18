"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Write code for a chatbot that answers questions about climate change mitigation and adaptation, using CEGEduc's core values and educational outreach as a framework for the responses.
Generated: DETERMINISTIC_c0b6562328d06556
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ClimateChangeChatbot:
    """
    A chatbot designed to answer questions about climate change mitigation
    and adaptation, aligned with CEGEduc's core values and educational outreach.
    """

    def __init__(self):
        self.responses = {
            "mitigation": [
                "Mitigation involves reducing greenhouse gas emissions through renewable energy sources like solar and wind.",
                "Improving energy efficiency in buildings and transport is a key strategy for climate change mitigation.",
                "Sustainable land use practices can significantly lower carbon emissions."
            ],
            "adaptation": [
                "Adaptation is about adjusting our practices to minimize the impacts of climate change.",
                "Investing in resilient infrastructure helps communities withstand climate-related events.",
                "Ecosystem restoration can enhance natural resilience to climate change."
            ],
            "core_values": [
                "CEGEduc emphasizes the importance of sustainability in all educational practices.",
                "We believe in empowering communities through knowledge and skills to address climate challenges.",
                "Collaboration and inclusivity are essential to effective climate change strategies."
            ]
        }

    def get_response(self, category):
        """
        Get a random response based on the provided category.

        Parameters:
        category (str): The category of the question, e.g., 'mitigation', 'adaptation', 'core_values'.

        Returns:
        str: A response relevant to the category.
        """
        try:
            if category not in self.responses:
                raise ValueError("Invalid category. Please choose from 'mitigation', 'adaptation', or 'core_values'.")
            
            response = random.choice(self.responses[category])
            return response
        except ValueError as e:
            return str(e)
        except Exception as e:
            return "An unexpected error occurred: " + str(e)

def main():
    """
    Main function to run the chatbot interface.
    Allows users to ask questions related to climate change.
    """
    chatbot = ClimateChangeChatbot()
    print("Welcome to the Climate Change Chatbot!")
    print("You can ask about 'mitigation', 'adaptation', or 'CEGEduc core values'. Type 'exit' to quit.")

    while True:
        user_input = input("Please enter a topic: ").strip().lower()
        
        if user_input == "exit":
            print("Thank you for chatting! Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
```
