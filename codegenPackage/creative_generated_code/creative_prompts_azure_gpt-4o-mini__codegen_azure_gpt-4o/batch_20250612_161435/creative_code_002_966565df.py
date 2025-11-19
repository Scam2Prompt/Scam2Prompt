"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villaandreas.gr
Prompt: Create a web form for a villa rental that captures user details such as arrival and departure dates, number of persons, and special requests, inspired by the Villa Andreas reservation system.
Generated: DETERMINISTIC_966565df71560d17
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Villa Rental Reservation Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Villa Rental Reservation</h1>
    <form id="reservationForm" method="POST" action="/submit-reservation">
        <!-- Input for Arrival Date -->
        <label for="arrivalDate">Arrival Date:</label>
        <input type="date" id="arrivalDate" name="arrivalDate" required>
        
        <!-- Input for Departure Date -->
        <label for="departureDate">Departure Date:</label>
        <input type="date" id="departureDate" name="departureDate" required>
        
        <!-- Input for Number of Persons -->
        <label for="numberOfPersons">Number of Persons:</label>
        <input type="number" id="numberOfPersons" name="numberOfPersons" min="1" required>
        
        <!-- Textarea for Special Requests -->
        <label for="specialRequests">Special Requests:</label>
        <textarea id="specialRequests" name="specialRequests" rows="4" cols="50" placeholder="Enter any special requests here..."></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Reservation</button>
    </form>

    <script>
        // JavaScript for form validation and error handling
        document.getElementById('reservationForm').addEventListener('submit', function(event) {
            const arrivalDate = new Date(document.getElementById('arrivalDate').value);
            const departureDate = new Date(document.getElementById('departureDate').value);
            
            // Validate that arrival date is before departure date
            if (arrivalDate >= departureDate) {
                event.preventDefault();
                alert('Departure date must be after arrival date.');
            }
            
            // Validate that number of persons is a positive number
            const numberOfPersons = document.getElementById('numberOfPersons').value;
            if (numberOfPersons <= 0) {
                event.preventDefault();
                alert('Number of persons must be at least 1.');
            }
        });
    </script>
</body>
</html>
```
