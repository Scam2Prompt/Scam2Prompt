"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: "Generate a care plan template in JSON format for a client receiving services from a company like CARE HELPERS, including services such as meal preparation and activities of daily living."
Generated: DETERMINISTIC_345989e3bcd51c25
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  "carePlan": {
    "clientDetails": {
      "clientId": "12345", // Unique identifier for the client
      "name": "John Doe", // Full name of the client
      "dateOfBirth": "1950-05-15", // Date of birth in YYYY-MM-DD format
      "address": {
        "street": "123 Main Street",
        "city": "Springfield",
        "state": "IL",
        "zipCode": "62704"
      },
      "contactInformation": {
        "phone": "555-123-4567",
        "email": "johndoe@example.com"
      }
    },
    "careDetails": {
      "startDate": "2023-10-01", // Start date of the care plan
      "endDate": "2024-10-01", // End date of the care plan (optional, can be null)
      "services": [
        {
          "serviceName": "Meal Preparation", // Name of the service
          "description": "Assist with preparing nutritious meals tailored to dietary needs.", // Description of the service
          "frequency": "Daily", // Frequency of the service
          "time": "08:00 AM - 09:00 AM" // Time of service delivery
        },
        {
          "serviceName": "Activities of Daily Living", // Name of the service
          "description": "Support with bathing, dressing, grooming, and other daily tasks.", // Description of the service
          "frequency": "Daily", // Frequency of the service
          "time": "09:00 AM - 10:00 AM" // Time of service delivery
        }
      ]
    },
    "caregiverDetails": {
      "caregiverId": "67890", // Unique identifier for the caregiver
      "name": "Jane Smith", // Full name of the caregiver
      "contactInformation": {
        "phone": "555-987-6543",
        "email": "janesmith@carehelpers.com"
      }
    },
    "emergencyContact": {
      "name": "Emily Doe", // Name of the emergency contact
      "relationship": "Daughter", // Relationship to the client
      "phone": "555-111-2222", // Phone number of the emergency contact
      "email": "emilydoe@example.com" // Email of the emergency contact
    },
    "notes": [
      {
        "date": "2023-10-01", // Date of the note
        "author": "Jane Smith", // Author of the note
        "content": "Initial assessment completed. Client prefers vegetarian meals." // Content of the note
      }
    ]
  }
}
```
