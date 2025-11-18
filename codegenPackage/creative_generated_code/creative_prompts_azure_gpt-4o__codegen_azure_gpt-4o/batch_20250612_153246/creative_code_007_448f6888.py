"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afms.in
Prompt: Create a chatbot script that can answer queries about Ashvi Facility Management's services, such as "What is included in mechanized housekeeping?" or "How can I book pest control services?"
Generated: DETERMINISTIC_448f6888b5ec2b41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class AshviFacilityBot:
    def __init__(self):
        # Initialize bot with a dictionary of services and their descriptions
        self.services = {
            "mechanized housekeeping": (
                "Mechanized housekeeping includes deep cleaning of floors, "
                "walls, windows, and furniture using advanced cleaning equipment."
            ),
            "pest control": (
                "Our pest control services include eco-friendly treatments for "
                "cockroaches, termites, rodents, ants, and other pests."
            ),
            "landscape management": (
                "This service includes lawn care, garden maintenance, and plant health monitoring."
            ),
            "security services": (
                "We provide professional security personnel and advanced monitoring solutions for your premises."
            ),
        }

    def respond_to_query(self, query):
        """
        Processes the user's query and provides an appropriate response.

        Args:
            query (str): User's input question.

        Returns:
            str: Bot's response, or a message if the query cannot be understood.
        """
        # Normalize query text (case-insensitive)
        query = query.lower()

        # Check if the query matches any known service
        for service, description in self.services.items():
            if re.search(service, query):
                return f"{service.capitalize()}: {description}"

        # Provide a fallback response if the query doesn't match any service
        return "I'm sorry, I couldn't understand your query. Please ask about our specific services like 'mechanized housekeeping' or 'pest control'."

    def book_service(self, service_name):
        """
        Handles service booking requests.

        Args:
            service_name (str): Name of the service to book.

        Returns:
            str: Confirmation message for booking, or error if service not found.
        """
        # Normalize service name (case-insensitive)
        service_name = service_name.lower()

        if service_name in self.services:
            return f"{service_name.capitalize()} service has been successfully booked!"
        else:
            return (
                f"Sorry, we don't recognize the service '{service_name}'. Please check the service name and try again."
            )


# Main function to interact with the chatbot
def main():
    print("Welcome to Ashvi Facility Management Chatbot!")
    print("You can ask about our services, e.g., 'What is included in mechanized housekeeping?'")
    print("To book a service, type 'book <service name>'.")

    bot = AshviFacilityBot()

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()

            # Exit condition
            if user_input.lower() in ["exit", "quit"]:
                print("Bot: Thank you for using Ashvi Facility Management Chatbot. Goodbye!")
                break

            # Handle booking requests
            if user_input.lower().startswith("book "):
                service_name = user_input[5:].strip()
                print("Bot:", bot.book_service(service_name))
                continue

            # General queries about services
            print("Bot:", bot.respond_to_query(user_input))

        except Exception as e:
            # Handle unexpected errors gracefully
            print("Bot: Sorry, an error occurred. Please try again later.")
            print(f"Error details: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
