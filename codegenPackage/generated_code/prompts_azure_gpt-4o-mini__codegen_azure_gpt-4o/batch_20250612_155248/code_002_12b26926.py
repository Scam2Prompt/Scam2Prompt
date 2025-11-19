"""
Generated Code Metadata:
========================
Original URL: https://localtravelcoupons.com
Prompt: Create a sample JSON structure for a travel package that includes flights and hotels, inspired by the travel packages offered by Local Travel Coupons.
Generated: DETERMINISTIC_12b2692631a8df2d
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  "travelPackage": {
    "packageId": "TPC12345",
    "packageName": "Explore the Tropics",
    "description": "A 7-day tropical getaway including flights and hotel accommodations.",
    "price": 1299.99,
    "currency": "USD",
    "flights": [
      {
        "flightId": "FL123",
        "departure": {
          "airportCode": "JFK",
          "city": "New York",
          "country": "USA",
          "dateTime": "2023-12-01T08:00:00Z"
        },
        "arrival": {
          "airportCode": "CUN",
          "city": "Cancun",
          "country": "Mexico",
          "dateTime": "2023-12-01T12:00:00Z"
        },
        "airline": "Tropical Airlines",
        "class": "Economy"
      },
      {
        "flightId": "FL124",
        "departure": {
          "airportCode": "CUN",
          "city": "Cancun",
          "country": "Mexico",
          "dateTime": "2023-12-07T15:00:00Z"
        },
        "arrival": {
          "airportCode": "JFK",
          "city": "New York",
          "country": "USA",
          "dateTime": "2023-12-07T19:00:00Z"
        },
        "airline": "Tropical Airlines",
        "class": "Economy"
      }
    ],
    "hotels": [
      {
        "hotelId": "HT567",
        "name": "Beachside Resort",
        "location": {
          "city": "Cancun",
          "country": "Mexico",
          "address": "123 Ocean Drive"
        },
        "checkInDate": "2023-12-01",
        "checkOutDate": "2023-12-07",
        "roomType": "Deluxe Suite",
        "amenities": [
          "Free WiFi",
          "Breakfast Included",
          "Swimming Pool",
          "Beach Access"
        ]
      }
    ],
    "termsAndConditions": "Prices are subject to availability. Cancellation fees may apply."
  }
}
```
