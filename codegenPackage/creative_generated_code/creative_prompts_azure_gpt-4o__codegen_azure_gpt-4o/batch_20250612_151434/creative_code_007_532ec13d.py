"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedairlines-vn.com
Prompt: Develop a program to assist users in selecting the best United Airlines ticket class (e.g., Economy, Economy Plus, Business First) based on their preferences and the descriptions provided by United Airlines Vietnam.
Generated: DETERMINISTIC_532ec13d8aa18ab5
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to assist users in selecting the best United Airlines ticket class based on their preferences.
The program provides descriptions of ticket classes and asks users for their preferences to recommend the most suitable option.
"""

# Import necessary libraries
import sys

def display_ticket_classes():
    """
    Display descriptions of United Airlines ticket classes.
    """
    ticket_classes = {
        "Economy": "Economy class offers affordable seats with basic amenities for short and long-haul flights.",
        "Economy Plus": "Economy Plus provides extra legroom and better seating comfort compared to Economy class.",
        "Business First": "Business First offers premium service, lie-flat seats, gourmet meals, and priority boarding."
    }

    print("Available Ticket Classes:")
    for ticket_class, description in ticket_classes.items():
        print(f"{ticket_class}: {description}")

    return ticket_classes

def get_user_preferences():
    """
    Get user preferences through input prompts.
    """
    try:
        print("\nPlease answer the following questions to help us recommend the best ticket class.")
        
        # Collect preferences from the user
        budget = input("Do you prefer an affordable ticket option? (yes/no): ").strip().lower()
        extra_legroom = input("Do you need extra legroom and seating comfort? (yes/no): ").strip().lower()
        premium_service = input("Do you want premium service, lie-flat seats, and gourmet meals? (yes/no): ").strip().lower()

        # Validate inputs
        if budget not in {"yes", "no"} or extra_legroom not in {"yes", "no"} or premium_service not in {"yes", "no"}:
            raise ValueError("Invalid input. Please answer with 'yes' or 'no'.")
        
        # Return preferences as a dictionary
        return {
            "budget": budget == "yes",
            "extra_legroom": extra_legroom == "yes",
            "premium_service": premium_service == "yes"
        }
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def recommend_ticket_class(preferences, ticket_classes):
    """
    Recommend the best ticket class based on user preferences.
    """
    if preferences["premium_service"]:
        recommendation = "Business First"
    elif preferences["extra_legroom"]:
        recommendation = "Economy Plus"
    elif preferences["budget"]:
        recommendation = "Economy"
    else:
        recommendation = "Economy (default choice)"
    
    print(f"\nBased on your preferences, we recommend: {recommendation}")
    print(f"Description: {ticket_classes[recommendation]}")

def main():
    """
    Main function to run the ticket class recommendation program.
    """
    print("Welcome to the United Airlines Ticket Class Selector!")

    # Display ticket classes and descriptions
    ticket_classes = display_ticket_classes()

    # Get user preferences
    preferences = get_user_preferences()

    # Recommend the best ticket class
    recommend_ticket_class(preferences, ticket_classes)

# Entry point for the program
if __name__ == "__main__":
    main()
```
