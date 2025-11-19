"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Generate code for a web application that allows users to book transportation services for heavy and light cargo, with options for corporate parcel delivery, refrigerated cargo, and vehicle rental.
Generated: DETERMINISTIC_1b0e6968a50249c4
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**transportation_service.py**
```python
from enum import Enum
from typing import Dict, List

class CargoType(str, Enum):
    """Enum for cargo types"""
    LIGHT = "light"
    HEAVY = "heavy"
    REFRIGERATED = "refrigerated"

class ServiceType(str, Enum):
    """Enum for service types"""
    CORPORATE_PARCEL_DELIVERY = "corporate_parcel_delivery"
    VEHICLE_RENTAL = "vehicle_rental"

class TransportationService:
    """Class for transportation services"""

    def __init__(self):
        self.services: Dict[str, Dict[str, str]] = {}

    def add_service(self, service_id: str, service_type: ServiceType, cargo_type: CargoType, description: str):
        """Add a new transportation service"""
        self.services[service_id] = {
            "service_type": service_type.value,
            "cargo_type": cargo_type.value,
            "description": description
        }

    def get_service(self, service_id: str):
        """Get a transportation service by ID"""
        return self.services.get(service_id)

    def update_service(self, service_id: str, service_type: ServiceType = None, cargo_type: CargoType = None, description: str = None):
        """Update a transportation service"""
        if service_id not in self.services:
            raise ValueError("Service not found")

        if service_type:
            self.services[service_id]["service_type"] = service_type.value
        if cargo_type:
            self.services[service_id]["cargo_type"] = cargo_type.value
        if description:
            self.services[service_id]["description"] = description

    def delete_service(self, service_id: str):
        """Delete a transportation service"""
        if service_id not in self.services:
            raise ValueError("Service not found")
        del self.services[service_id]

class BookingService:
    """Class for booking transportation services"""

    def __init__(self, transportation_service: TransportationService):
        self.transportation_service = transportation_service
        self.bookings: Dict[str, Dict[str, str]] = {}

    def book_service(self, booking_id: str, service_id: str, customer_name: str, pickup_location: str, dropoff_location: str):
        """Book a transportation service"""
        service = self.transportation_service.get_service(service_id)
        if not service:
            raise ValueError("Service not found")

        self.bookings[booking_id] = {
            "service_id": service_id,
            "customer_name": customer_name,
            "pickup_location": pickup_location,
            "dropoff_location": dropoff_location
        }

    def get_booking(self, booking_id: str):
        """Get a booking by ID"""
        return self.bookings.get(booking_id)

    def cancel_booking(self, booking_id: str):
        """Cancel a booking"""
        if booking_id not in self.bookings:
            raise ValueError("Booking not found")
        del self.bookings[booking_id]

def main():
    transportation_service = TransportationService()
    booking_service = BookingService(transportation_service)

    # Add services
    transportation_service.add_service("service1", ServiceType.CORPORATE_PARCEL_DELIVERY, CargoType.LIGHT, "Corporate parcel delivery service")
    transportation_service.add_service("service2", ServiceType.VEHICLE_RENTAL, CargoType.HEAVY, "Vehicle rental service")

    # Book services
    booking_service.book_service("booking1", "service1", "John Doe", "New York", "Los Angeles")
    booking_service.book_service("booking2", "service2", "Jane Doe", "Chicago", "Houston")

    # Print bookings
    print(booking_service.get_booking("booking1"))
    print(booking_service.get_booking("booking2"))

if __name__ == "__main__":
    main()
```

**app.py (Flask App)**
```python
from flask import Flask, request, jsonify
from transportation_service import TransportationService, BookingService, CargoType, ServiceType

app = Flask(__name__)

transportation_service = TransportationService()
booking_service = BookingService(transportation_service)

# Add services
transportation_service.add_service("service1", ServiceType.CORPORATE_PARCEL_DELIVERY, CargoType.LIGHT, "Corporate parcel delivery service")
transportation_service.add_service("service2", ServiceType.VEHICLE_RENTAL, CargoType.HEAVY, "Vehicle rental service")

@app.route("/services", methods=["GET"])
def get_services():
    services = [{"id": id, **service} for id, service in transportation_service.services.items()]
    return jsonify(services)

@app.route("/services", methods=["POST"])
def add_service():
    data = request.json
    transportation_service.add_service(data["service_id"], ServiceType(data["service_type"]), CargoType(data["cargo_type"]), data["description"])
    return jsonify({"message": "Service added successfully"})

@app.route("/bookings", methods=["POST"])
def book_service():
    data = request.json
    booking_service.book_service(data["booking_id"], data["service_id"], data["customer_name"], data["pickup_location"], data["dropoff_location"])
    return jsonify({"message": "Booking created successfully"})

@app.route("/bookings/<booking_id>", methods=["GET"])
def get_booking(booking_id):
    booking = booking_service.get_booking(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify(booking)

@app.route("/bookings/<booking_id>", methods=["DELETE"])
def cancel_booking(booking_id):
    try:
        booking_service.cancel_booking(booking_id)
        return jsonify({"message": "Booking cancelled successfully"})
    except ValueError:
        return jsonify({"error": "Booking not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
```
