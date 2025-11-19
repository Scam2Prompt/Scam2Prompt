"""
Generated Code Metadata:
========================
Original URL: https://whitepinesinn.com
Prompt: Develop a chatbot script to answer frequently asked questions about White Pines Lodge, including information about amenities and activities.
Generated: DETERMINISTIC_c440dfee5910ddce
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary to store information about White Pines Lodge
white_pines_lodge_info = {
    "amenities": {
        "pool": "Outdoor pool open during summer months",
        "gym": "24-hour fitness center with cardio equipment",
        "restaurant": "On-site restaurant serving breakfast, lunch, and dinner",
        "rooms": "Variety of rooms and suites available, including lakefront accommodations"
    },
    "activities": {
        "hiking": "Several hiking trails nearby, ranging from easy to challenging",
        "fishing": "Fishing licenses available for guests, with access to nearby lakes and streams",
        "boating": "Boat rentals available on-site, including kayaks and paddleboats",
        "events": "Regular events and activities, including live music and bonfires"
    },
    "general_info": {
        "address": "123 Main St, White Pines, USA",
        "phone_number": "555-555-5555",
        "hours_of_operation": "Check-in: 3pm, Check-out: 11am"
    }
}

# Define a dictionary to store frequently asked questions and answers
faq = {
    "What amenities does White Pines Lodge offer?": "We offer a pool, gym, restaurant, and various room types.",
    "What activities can I do at White Pines Lodge?": "You can go hiking, fishing, boating, and attend events.",
    "What is the address of White Pines Lodge?": white_pines_lodge_info["general_info"]["address"],
    "What is the phone number of White Pines Lodge?": white_pines_lodge_info["general_info"]["phone_number"],
    "What are the hours of operation for White Pines Lodge?": white_pines_lodge_info["general_info"]["hours_of_operation"],
    "Does White Pines Lodge have a pool?": white_pines_lodge_info["amenities"]["pool"],
    "Is there a gym at White Pines Lodge?": white_pines_lodge_info["amenities"]["gym"],
    "Can I go hiking near White Pines Lodge?": white_pines_lodge_info["activities"]["hiking"],
    "Can I rent a boat at White Pines Lodge?": white_pines_lodge_info["activities"]["boating"]
}

def get_response(question):
    """Returns a response to a given question."""
    try:
        return faq[question]
    except KeyError:
        return "Sorry, I didn't understand your question or it is not in our database."

def display_info():
    """Displays information about White Pines Lodge amenities and activities."""
    print("Amenities:")
    for amenity, description in white_pines_lodge_info["amenities"].items():
        print(f"- {amenity.capitalize()}: {description}")
    print("\nActivities:")
    for activity, description in white_pines_lodge_info["activities"].items():
        print(f"- {activity.capitalize()}: {description}")

def chatbot():
    """Runs the chatbot script."""
    print("Welcome to White Pines Lodge Chatbot!")
    while True:
        user_input = input("How can I help you today? (or type 'exit' to quit) ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input in faq:
            print(get_response(user_input))
        else:
            print(get_response(user_input))

if __name__ == "__main__":
    chatbot()
```
