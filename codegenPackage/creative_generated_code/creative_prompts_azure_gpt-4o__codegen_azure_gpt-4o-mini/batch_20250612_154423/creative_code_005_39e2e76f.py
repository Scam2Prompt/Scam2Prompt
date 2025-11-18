"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reservation-team.com
Prompt: Develop a chatbot in Python that assists users with booking flights, hotels, and vacation packages, incorporating the personalized approach described on reservation-team.com.
Generated: DETERMINISTIC_39e2e76fc5aa5adb
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
flights_data = [
    {"id": 1, "destination": "New York", "price": 300},
    {"id": 2, "destination": "Los Angeles", "price": 400},
    {"id": 3, "destination": "Miami", "price": 250},
]

hotels_data = [
    {"id": 1, "location": "New York", "price": 200},
    {"id": 2, "location": "Los Angeles", "price": 150},
    {"id": 3, "location": "Miami", "price": 100},
]

packages_data = [
    {"id": 1, "package": "New York Getaway", "price": 500},
    {"id": 2, "package": "Los Angeles Experience", "price": 600},
    {"id": 3, "package": "Miami Adventure", "price": 700},
]

# Function to simulate a personalized greeting
def personalized_greeting(user_name):
    greetings = [
        f"Hello, {user_name}! How can I assist you today?",
        f"Welcome back, {user_name}! Ready to plan your next trip?",
        f"Hi, {user_name}! Let's find you the perfect travel options.",
    ]
    return random.choice(greetings)

# Function to fetch available flights
def get_flights(destination):
    return [flight for flight in flights_data if flight["destination"].lower() == destination.lower()]

# Function to fetch available hotels
def get_hotels(location):
    return [hotel for hotel in hotels_data if hotel["location"].lower() == location.lower()]

# Function to fetch available vacation packages
def get_packages():
    return packages_data

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint to handle user messages and provide responses."""
    try:
        user_input = request.json.get('message')
        user_name = request.json.get('user_name', 'Guest')

        response = {"message": ""}

        # Personalized greeting
        if "hello" in user_input.lower():
            response['message'] = personalized_greeting(user_name)
        
        # Flight booking inquiry
        elif "flight" in user_input.lower():
            destination = user_input.split("to")[-1].strip()
            flights = get_flights(destination)
            if flights:
                flight_options = [f"{flight['destination']} - ${flight['price']}" for flight in flights]
                response['message'] = f"Available flights: {', '.join(flight_options)}"
            else:
                response['message'] = "Sorry, I couldn't find any flights to that destination."

        # Hotel booking inquiry
        elif "hotel" in user_input.lower():
            location = user_input.split("in")[-1].strip()
            hotels = get_hotels(location)
            if hotels:
                hotel_options = [f"{hotel['location']} - ${hotel['price']}" for hotel in hotels]
                response['message'] = f"Available hotels: {', '.join(hotel_options)}"
            else:
                response['message'] = "Sorry, I couldn't find any hotels in that location."

        # Vacation package inquiry
        elif "package" in user_input.lower():
            packages = get_packages()
            package_options = [f"{pkg['package']} - ${pkg['price']}" for pkg in packages]
            response['message'] = f"Available vacation packages: {', '.join(package_options)}"

        else:
            response['message'] = "I'm sorry, I didn't understand that. Can you please specify if you want to book a flight, hotel, or package?"

        return jsonify(response), 200

    except Exception as e:
        # Error handling for unexpected issues
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
