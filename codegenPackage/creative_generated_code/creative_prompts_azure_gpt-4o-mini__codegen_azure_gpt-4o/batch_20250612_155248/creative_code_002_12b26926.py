"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://localtravelcoupons.com
Prompt: Create a sample JSON structure for a travel package that includes flights and hotels, inspired by the travel packages offered by Local Travel Coupons.
Generated: DETERMINISTIC_12b2692631a8df2d
Batch ID: 20250612_155248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "travelPackage": {
    "packageId": "LTC12345",  // Unique identifier for the travel package
    "packageName": "Tropical Getaway - 7 Days", // Name of the travel package
    "description": "A 7-day tropical vacation package including flights and hotel stays.", // Description of the package
    "price": {
      "currency": "USD", // Currency used for pricing
      "amount": 1200.00  // Total price of the package
    },
    "flights": [ // Flight details
      {
        "flightId": "FL123", // Unique identifier for the flight
        "departureAirport": {
          "code": "JFK", // Airport code
          "name": "John F. Kennedy International Airport", // Full name of the airport
          "city": "New York", // City of the airport
          "country": "USA" // Country of the airport
        },
        "arrivalAirport": {
          "code": "HNL", // Airport code
          "name": "Daniel K. Inouye International Airport", // Full name of the airport
          "city": "Honolulu", // City of the airport
          "country": "USA" // Country of the airport
        },
        "departureTime": "2023-12-10T08:00:00Z", // Flight departure time in ISO 8601 format
        "arrivalTime": "2023-12-10T16:00:00Z", // Flight arrival time in ISO 8601 format
        "airline": "Delta Airlines", // Airline providing the flight
        "seatClass": "Economy" // Flight seat class
      }
    ],
    "hotels": [ // Hotel details
      {
        "hotelId": "HT456", // Unique identifier for the hotel
        "name": "Ocean Breeze Resort", // Name of the hotel
        "address": {
          "street": "123 Beachside Ave", // Street address of the hotel
          "city": "Honolulu", // City of the hotel
          "state": "HI", // State of the hotel
          "country": "USA", // Country of the hotel
          "postalCode": "96815" // Postal code of the hotel
        },
        "checkInDate": "2023-12-10", // Check-in date in ISO 8601 format
        "checkOutDate": "2023-12-17", // Check-out date in ISO 8601 format
        "roomType": "Deluxe Ocean View", // Type of room reserved
        "rating": 4.5, // Hotel rating
        "amenities": [ // List of amenities provided by the hotel
          "Free WiFi",
          "Swimming Pool",
          "Breakfast Included",
          "Spa Services"
        ]
      }
    ],
    "termsAndConditions": "All sales are final. No refunds for cancellations. Travelers are responsible for adhering to local travel regulations.", // Terms and conditions for the package
    "contactInfo": {
      "email": "support@localtravelcoupons.com", // Support email address
      "phone": "+1-800-555-1234" // Support phone number
    }
  }
}
```
