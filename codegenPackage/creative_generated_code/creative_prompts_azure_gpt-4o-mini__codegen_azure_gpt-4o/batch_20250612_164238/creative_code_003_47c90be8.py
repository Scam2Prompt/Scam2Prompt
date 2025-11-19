"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Develop a sample HTML form for booking a boat rental at Coastal Boat Rentals, ensuring it includes fields for boat selection, rental duration, and customer contact information.
Generated: DETERMINISTIC_47c90be8926fdd7b
Batch ID: 20250612_164238
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
    <title>Boat Rental Booking | Coastal Boat Rentals</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f9;
        }

        h1 {
            color: #2c3e50;
        }

        form {
            max-width: 500px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: #fff;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #2980b9;
        }

        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>Book Your Boat Rental</h1>
    <p>Fill out the form below to reserve a boat at Coastal Boat Rentals:</p>
    <form id="boatRentalForm" method="post" action="/submit-booking">
        <!-- Boat selection dropdown -->
        <label for="boatType">Boat Type</label>
        <select id="boatType" name="boatType" required>
            <option value="">-- Select a Boat --</option>
            <option value="speedboat">Speedboat</option>
            <option value="pontoon">Pontoon</option>
            <option value="kayak">Kayak</option>
            <option value="yacht">Yacht</option>
        </select>

        <!-- Rental duration input -->
        <label for="rentalDuration">Rental Duration (hours)</label>
        <input type="number" id="rentalDuration" name="rentalDuration" min="1" max="12" required>
        <small class="error" id="durationError"></small>

        <!-- Customer contact information -->
        <label for="customerName">Full Name</label>
        <input type="text" id="customerName" name="customerName" maxlength="100" placeholder="John Doe" required>

        <label for="contactEmail">Email Address</label>
        <input type="email" id="contactEmail" name="contactEmail" placeholder="example@domain.com" required>
        
        <label for="contactPhone">Phone Number</label>
        <input type="tel" id="contactPhone" name="contactPhone" pattern="[0-9]{10}" placeholder="1234567890">

        <!-- Submit button -->
        <button type="submit">Submit Booking</button>
    </form>

    <script>
        // Basic validation for rental duration
        document.getElementById('boatRentalForm').addEventListener('submit', function(event) {
            const duration = document.getElementById('rentalDuration').value;
            const durationError = document.getElementById('durationError');
            durationError.textContent = '';

            if (duration <= 0 || duration > 12) {
                event.preventDefault(); // Prevent form submission
                durationError.textContent = 'Please enter a duration between 1 and 12 hours.';
            }
        });
    </script>
</body>
</html>
```
