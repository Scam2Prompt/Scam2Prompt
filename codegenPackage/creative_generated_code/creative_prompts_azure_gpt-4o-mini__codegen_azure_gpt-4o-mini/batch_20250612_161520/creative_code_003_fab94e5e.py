"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mollinari.com.pl
Prompt: Develop a simple HTML form that collects user data for reservations at Mollinari, ensuring it includes fields for date, time, and number of guests.
Generated: DETERMINISTIC_fab94e5ea86a96c0
Batch ID: 20250612_161520
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
    <title>Mollinari Reservation Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            margin-top: 20px;
            padding: 10px 15px;
            border: none;
            background-color: #28a745;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<h1>Mollinari Reservation Form</h1>
<form id="reservationForm">
    <label for="date">Reservation Date:</label>
    <input type="date" id="date" name="date" required>

    <label for="time">Reservation Time:</label>
    <input type="time" id="time" name="time" required>

    <label for="guests">Number of Guests:</label>
    <input type="number" id="guests" name="guests" min="1" required>

    <button type="submit">Submit Reservation</button>
    <div id="errorMessage" class="error"></div>
</form>

<script>
    // Handle form submission
    document.getElementById('reservationForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Validate input values
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;
        const guests = document.getElementById('guests').value;
        const errorMessage = document.getElementById('errorMessage');

        // Clear previous error messages
        errorMessage.textContent = '';

        // Check for valid inputs
        if (!date || !time || guests < 1) {
            errorMessage.textContent = 'Please fill out all fields correctly.';
            return;
        }

        // Prepare data for submission (e.g., to an API)
        const reservationData = {
            date: date,
            time: time,
            guests: guests
        };

        // Simulate a successful submission (replace with actual API call)
        console.log('Reservation Data:', reservationData);
        alert('Reservation successfully submitted!');

        // Optionally, reset the form after submission
        this.reset();
    });
</script>

</body>
</html>
```
