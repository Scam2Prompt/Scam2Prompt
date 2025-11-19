"""
Generated Code Metadata:
========================
Original URL: https://localtravelcoupons.com
Prompt: Create a sample JSON structure for a travel package that includes flights and hotels, inspired by the travel packages offered by Local Travel Coupons.
Generated: DETERMINISTIC_12b2692631a8df2d
Batch ID: 20250612_155248
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://json-schema.org/draft-07/schema#": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Travel Package",
  "type": "object",
  "properties": {
    "packageId": {
      "type": "string",
      "description": "Unique identifier for the travel package"
    },
    "name": {
      "type": "string",
      "description": "Name of the travel package"
    },
    "description": {
      "type": "string",
      "description": "Brief description of the travel package"
    },
    "flights": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Flight"
      },
      "description": "List of flights included in the package"
    },
    "hotels": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/Hotel"
      },
      "description": "List of hotels included in the package"
    },
    "price": {
      "type": "object",
      "properties": {
        "currency": {
          "type": "string",
          "description": "Currency of the price (e.g. USD, EUR)"
        },
        "amount": {
          "type": "number",
          "description": "Price amount"
        },
        "discount": {
          "type": "number",
          "description": "Discount percentage"
        }
      },
      "required": ["currency", "amount"]
    }
  },
  "required": ["packageId", "name", "description", "flights", "hotels", "price"],
  "definitions": {
    "Flight": {
      "type": "object",
      "properties": {
        "flightId": {
          "type": "string",
          "description": "Unique identifier for the flight"
        },
        "airline": {
          "type": "string",
          "description": "Airline name"
        },
        "departureAirport": {
          "type": "string",
          "description": "Departure airport code"
        },
        "arrivalAirport": {
          "type": "string",
          "description": "Arrival airport code"
        },
        "departureDate": {
          "type": "string",
          "format": "date-time",
          "description": "Departure date and time"
        },
        "returnDate": {
          "type": "string",
          "format": "date-time",
          "description": "Return date and time"
        }
      },
      "required": ["flightId", "airline", "departureAirport", "arrivalAirport", "departureDate", "returnDate"]
    },
    "Hotel": {
      "type": "object",
      "properties": {
        "hotelId": {
          "type": "string",
          "description": "Unique identifier for the hotel"
        },
        "name": {
          "type": "string",
          "description": "Hotel name"
        },
        "location": {
          "type": "string",
          "description": "Hotel location"
        },
        "checkInDate": {
          "type": "string",
          "format": "date-time",
          "description": "Check-in date and time"
        },
        "checkOutDate": {
          "type": "string",
          "format": "date-time",
          "description": "Check-out date and time"
        }
      },
      "required": ["hotelId", "name", "location", "checkInDate", "checkOutDate"]
    }
  }
}
```

```python
import json

class TravelPackage:
    def __init__(self, package_id, name, description, flights, hotels, price):
        self.package_id = package_id
        self.name = name
        self.description = description
        self.flights = flights
        self.hotels = hotels
        self.price = price

    def to_json(self):
        return {
            "packageId": self.package_id,
            "name": self.name,
            "description": self.description,
            "flights": self.flights,
            "hotels": self.hotels,
            "price": self.price
        }

class Flight:
    def __init__(self, flight_id, airline, departure_airport, arrival_airport, departure_date, return_date):
        self.flight_id = flight_id
        self.airline = airline
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_date = departure_date
        self.return_date = return_date

    def to_json(self):
        return {
            "flightId": self.flight_id,
            "airline": self.airline,
            "departureAirport": self.departure_airport,
            "arrivalAirport": self.arrival_airport,
            "departureDate": self.departure_date,
            "returnDate": self.return_date
        }

class Hotel:
    def __init__(self, hotel_id, name, location, check_in_date, check_out_date):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def to_json(self):
        return {
            "hotelId": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "checkInDate": self.check_in_date,
            "checkOutDate": self.check_out_date
        }

def main():
    try:
        flight1 = Flight("FL001", "American Airlines", "JFK", "LAX", "2024-09-20T08:00:00", "2024-09-22T10:00:00")
        flight2 = Flight("FL002", "Delta Air Lines", "LAX", "JFK", "2024-09-24T12:00:00", "2024-09-26T14:00:00")

        hotel1 = Hotel("HT001", "Hotel California", "Los Angeles", "2024-09-20T14:00:00", "2024-09-22T12:00:00")
        hotel2 = Hotel("HT002", "Hotel New York", "New York City", "2024-09-24T16:00:00", "2024-09-26T10:00:00")

        flights = [flight1.to_json(), flight2.to_json()]
        hotels = [hotel1.to_json(), hotel2.to_json()]

        price = {
            "currency": "USD",
            "amount": 1000.0,
            "discount": 10.0
        }

        travel_package = TravelPackage("PKG001", "California Dreaming", "A 5-day trip to California", flights, hotels, price)

        print(json.dumps(travel_package.to_json(), indent=4))

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
