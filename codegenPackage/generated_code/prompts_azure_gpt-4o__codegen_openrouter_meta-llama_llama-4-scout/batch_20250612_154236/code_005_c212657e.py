"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Develop a chatbot using Python that can assist users in finding BPL service centers near them and booking repair services for appliances like refrigerators and washing machines.
Generated: DETERMINISTIC_c212657ed9c9f3cc
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import geopy
from geopy.geocoders import Nominatim
import requests
import json

class BPLServiceCenterChatbot:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="bpl_service_center_chatbot")
        self.bpl_service_centers = self.load_bpl_service_centers()

    def load_bpl_service_centers(self):
        # Load BPL service centers data from API or database
        # For demonstration purposes, assume we have a static list
        return [
            {"id": 1, "name": "BPL Service Center 1", "latitude": 12.9716, "longitude": 77.5949, "address": "Bangalore, Karnataka"},
            {"id": 2, "name": "BPL Service Center 2", "latitude": 28.7041, "longitude": 77.1025, "address": "New Delhi, Delhi"},
            # Add more service centers here...
        ]

    def get_user_location(self, user_input):
        try:
            location = self.geolocator.geocode(user_input)
            if location:
                return {"latitude": location.latitude, "longitude": location.longitude}
            else:
                return None
        except Exception as e:
            print(f"Error getting user location: {str(e)}")
            return None

    def find_nearest_service_centers(self, user_location):
        try:
            nearest_centers = []
            for center in self.bpl_service_centers:
                distance = self.calculate_distance(user_location["latitude"], user_location["longitude"], center["latitude"], center["longitude"])
                center["distance"] = distance
                nearest_centers.append(center)
            nearest_centers.sort(key=lambda x: x["distance"])
            return nearest_centers[:5]  # Return top 5 nearest service centers
        except Exception as e:
            print(f"Error finding nearest service centers: {str(e)}")
            return []

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        try:
            # Using Haversine formula to calculate distance between two points
            R = 6371  # Radius of the Earth in kilometers
            dlat = self.deg2rad(lat2 - lat1)
            dlon = self.deg2rad(lon2 - lon1)
            a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(self.deg2rad(lat1)) * math.cos(self.deg2rad(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = R * c
            return distance
        except Exception as e:
            print(f"Error calculating distance: {str(e)}")
            return 0

    def deg2rad(self, deg):
        return deg * (math.pi / 180)

    def book_repair_service(self, service_center_id, appliance_type):
        try:
            # Simulate booking repair service
            service_center = next((center for center in self.bpl_service_centers if center["id"] == service_center_id), None)
            if service_center:
                print(f"Repair service booked for {appliance_type} at {service_center['name']}")
                return True
            else:
                print("Service center not found")
                return False
        except Exception as e:
            print(f"Error booking repair service: {str(e)}")
            return False

def main():
    import math
    chatbot = BPLServiceCenterChatbot()
    while True:
        user_input = input("Welcome to BPL Service Center Chatbot! Type 'find service centers near me' or 'book repair service' or 'exit': ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "find service centers near me":
            location_input = input("Enter your location: ")
            user_location = chatbot.get_user_location(location_input)
            if user_location:
                nearest_centers = chatbot.find_nearest_service_centers(user_location)
                if nearest_centers:
                    print("Nearest BPL Service Centers:")
                    for center in nearest_centers:
                        print(f"{center['name']} - {center['address']} (Distance: {center['distance']:.2f} km)")
                else:
                    print("No service centers found near your location")
        elif user_input.lower() == "book repair service":
            service_center_id = int(input("Enter service center ID: "))
            appliance_type = input("Enter appliance type (e.g., refrigerator, washing machine): ")
            if chatbot.book_repair_service(service_center_id, appliance_type):
                print("Repair service booked successfully")

if __name__ == "__main__":
    main()
```
