"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Develop a chatbot script that answers common questions about carpet selection, repair, and maintenance, using Perfect Melbourne Carpet's 6-star classification system and room foot traffic ratings.
Generated: DETERMINISTIC_aee1b9fc7fdd735a
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class CarpetChatbot:
    """
    A chatbot to assist with carpet selection, repair, and maintenance
    based on Perfect Melbourne Carpet's 6-star classification system
    and room foot traffic ratings.
    """

    def __init__(self):
        # Initialize chatbot with predefined responses
        self.responses = {
            "selection": self.get_selection_advice,
            "repair": self.get_repair_advice,
            "maintenance": self.get_maintenance_advice,
        }
        self.foot_traffic_ratings = {
            "low": "For low foot traffic areas (e.g., bedrooms), consider carpets with a 3-4 star rating.",
            "medium": "For medium foot traffic areas (e.g., living rooms), consider carpets with a 4-5 star rating.",
            "high": "For high foot traffic areas (e.g., hallways), consider carpets with a 5-6 star rating.",
        }

    def get_selection_advice(self, foot_traffic):
        """
        Provide carpet selection advice based on foot traffic.
        :param foot_traffic: str - 'low', 'medium', or 'high'
        :return: str - Selection advice
        """
        return self.foot_traffic_ratings.get(
            foot_traffic.lower(),
            "Invalid foot traffic rating. Please specify 'low', 'medium', or 'high'.",
        )

    def get_repair_advice(self):
        """
        Provide general advice on carpet repair.
        :return: str - Repair advice
        """
        return (
            "For carpet repair, consider patching small damaged areas or re-stretching "
            "loose carpets. For extensive damage, consult a professional carpet repair service."
        )

    def get_maintenance_advice(self):
        """
        Provide general advice on carpet maintenance.
        :return: str - Maintenance advice
        """
        return (
            "To maintain your carpet, vacuum regularly, clean spills immediately, "
            "and schedule professional deep cleaning every 12-18 months."
        )

    def handle_query(self, query):
        """
        Handle user queries and provide appropriate responses.
        :param query: str - User's query
        :return: str - Chatbot's response
        """
        query = query.lower()

        # Check for selection-related queries
        if "select" in query or "choose" in query or "foot traffic" in query:
            match = re.search(r"(low|medium|high)", query)
            if match:
                foot_traffic = match.group(1)
                return self.get_selection_advice(foot_traffic)
            else:
                return "Please specify the foot traffic level: 'low', 'medium', or 'high'."

        # Check for repair-related queries
        elif "repair" in query or "fix" in query:
            return self.get_repair_advice()

        # Check for maintenance-related queries
        elif "maintain" in query or "clean" in query or "maintenance" in query:
            return self.get_maintenance_advice()

        # Default response for unrecognized queries
        return "I'm sorry, I didn't understand your question. Please ask about carpet selection, repair, or maintenance."

# Main function to interact with the chatbot
def main():
    """
    Main function to run the chatbot in a loop for user interaction.
    """
    print("Welcome to the Perfect Melbourne Carpet Chatbot!")
    print("Ask me about carpet selection, repair, or maintenance.")
    print("Type 'exit' to end the chat.\n")

    chatbot = CarpetChatbot()

    while True:
        # Get user input
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for using the Perfect Melbourne Carpet Chatbot. Goodbye!")
            break

        # Get chatbot response
        response = chatbot.handle_query(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot if this script is executed directly
if __name__ == "__main__":
    main()
```
