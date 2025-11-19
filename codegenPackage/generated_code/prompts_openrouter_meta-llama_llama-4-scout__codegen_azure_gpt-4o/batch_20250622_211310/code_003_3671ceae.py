"""
Generated Code Metadata:
========================
Original URL: https://immediate-smarter.com
Prompt: Design a conversational flowchart for an educational conversation between a user and a seasoned investment professional, addressing the user's interests and questions about investments.
Generated: DETERMINISTIC_3671ceaedc33db24
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def main():
    """
    Main function to run the conversational flowchart.
    """
    print("Welcome to the Investment Conversation Assistant!")
    print("I am here to help you learn about investments.")
    print("Type 'exit' at any time to end the conversation.\n")

    # Load the flowchart
    flowchart = load_flowchart()

    # Start the conversation
    start_conversation(flowchart)


def load_flowchart():
    """
    Load the conversational flowchart from a predefined structure.
    Returns:
        dict: The flowchart structure.
    """
    # Define the flowchart structure
    flowchart = {
        "start": {
            "message": "What would you like to learn about investments?",
            "options": {
                "1": "Types of investments",
                "2": "Risk management",
                "3": "How to start investing",
                "4": "Exit"
            }
        },
        "1": {
            "message": "There are various types of investments, such as stocks, bonds, mutual funds, real estate, and more. Which one interests you?",
            "options": {
                "1": "Stocks",
                "2": "Bonds",
                "3": "Mutual Funds",
                "4": "Real Estate",
                "5": "Go back"
            }
        },
        "2": {
            "message": "Risk management is crucial in investing. Would you like to learn about diversification, risk tolerance, or market volatility?",
            "options": {
                "1": "Diversification",
                "2": "Risk tolerance",
                "3": "Market volatility",
                "4": "Go back"
            }
        },
        "3": {
            "message": "Starting to invest involves setting financial goals, understanding your risk tolerance, and choosing a platform. Would you like to learn more about any of these?",
            "options": {
                "1": "Setting financial goals",
                "2": "Understanding risk tolerance",
                "3": "Choosing a platform",
                "4": "Go back"
            }
        },
        "exit": {
            "message": "Thank you for using the Investment Conversation Assistant. Have a great day!"
        }
    }
    return flowchart


def start_conversation(flowchart):
    """
    Start the conversation based on the flowchart.
    Args:
        flowchart (dict): The conversational flowchart structure.
    """
    current_node = "start"

    while current_node != "exit":
        node = flowchart.get(current_node)
        if not node:
            print("Invalid option. Please try again.")
            current_node = "start"
            continue

        # Display the message
        print("\n" + node["message"])

        # Check if the node has options
        if "options" in node:
            for key, value in node["options"].items():
                print(f"{key}. {value}")

            # Get user input
            user_input = input("Enter your choice: ").strip()

            # Handle exit condition
            if user_input.lower() == "exit":
                current_node = "exit"
                continue

            # Validate user input
            if user_input in node["options"]:
                if node["options"][user_input] == "Exit" or node["options"][user_input] == "Go back":
                    current_node = "start"
                else:
                    current_node = user_input
            else:
                print("Invalid choice. Please try again.")
        else:
            # If no options, end the conversation
            current_node = "exit"

    # Display exit message
    print("\n" + flowchart["exit"]["message"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
