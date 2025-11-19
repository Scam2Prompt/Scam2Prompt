"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Develop a simple chatbot script that provides information about museum activities for visitors and families, inspired by the content on the Museo Vasca Votiva di Noceto site.
Generated: DETERMINISTIC_0b1c131b140bca2b
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# museum_chatbot.py

class MuseumChatbot:
    """
    A simple chatbot script providing information about museum activities for visitors and families.
    """

    def __init__(self):
        # Initialize a dictionary with museum activities
        self.activities = {
            "exhibitions": "Check our temporary and permanent exhibitions.",
            "workshops": "Join our hands-on workshops for kids and adults.",
            "guided_tours": "Book a guided tour to explore our collections.",
            "events": "Find out about our upcoming events and concerts.",
        }

    def greet(self):
        """Print a welcome message."""
        print("Welcome to the Museo Vasca Votiva di Noceto chatbot!")

    def provide_info(self):
        """Provide information about museum activities."""
        print("What would you like to know about?")
        print("1. Exhibitions")
        print("2. Workshops")
        print("3. Guided Tours")
        print("4. Events")
        print("5. Exit")

        while True:
            choice = input("Enter your choice (1-5): ")
            if choice == "5":
                print("Thank you for visiting!")
                break
            elif choice in ["1", "2", "3", "4"]:
                activity = list(self.activities.keys())[int(choice) - 1]
                print(self.activities[activity])
            else:
                print("Invalid choice. Please try again.")

    def handle_error(self, error):
        """Handle any errors that occur during execution."""
        print(f"An error occurred: {error}")


def main():
    try:
        chatbot = MuseumChatbot()
        chatbot.greet()
        chatbot.provide_info()
    except Exception as e:
        chatbot = MuseumChatbot()
        chatbot.handle_error(e)


if __name__ == "__main__":
    main()
```

To run this code, save it to a file named `museum_chatbot.py` and execute it using Python:

```bash
python museum_chatbot.py
```
