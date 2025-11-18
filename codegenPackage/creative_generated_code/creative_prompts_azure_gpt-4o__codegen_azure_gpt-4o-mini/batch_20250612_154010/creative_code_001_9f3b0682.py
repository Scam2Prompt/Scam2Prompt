"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tylos.click
Prompt: Generate JavaScript code to implement a booking form for spa treatments, referencing the Energen template's "Book Your Treatment" section.
Generated: DETERMINISTIC_9f3b0682f74ec9da
Batch ID: 20250612_154010
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
    <title>Spa Treatment Booking Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <div class="booking-form">
        <h2>Book Your Treatment</h2>
        <form id="bookingForm">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="treatment">Treatment Type:</label>
            <select id="treatment" name="treatment" required>
                <option value="">Select Treatment</option>
                <option value="massage">Massage</option>
                <option value="facial">Facial</option>
                <option value="manicure">Manicure</option>
                <option value="pedicure">Pedicure</option>
            </select>

            <label for="date">Preferred Date:</label>
            <input type="date" id="date" name="date" required>

            <label for="time">Preferred Time:</label>
            <input type="time" id="time" name="time" required>

            <button type="submit">Book Now</button>
        </form>
        <div id="confirmationMessage" class="hidden"></div>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('bookingForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Collect form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const treatment = document.getElementById('treatment').value;
            const date = document.getElementById('date').value;
            const time = document.getElementById('time').value;

            // Basic validation for email format
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert('Please enter a valid email address.');
                return;
            }

            // Create a booking object
            const bookingDetails = {
                name: name,
                email: email,
                treatment: treatment,
                date: date,
                time: time
            };

            // Simulate sending data to a server (e.g., using fetch)
            try {
                // Normally, you would send this data to the server
                // fetch('/api/bookings', {
                //     method: 'POST',
                //     headers: {
                //         'Content-Type': 'application/json'
                //     },
                //     body: JSON.stringify(bookingDetails)
                // }).then(response => {
                //     if (!response.ok) {
                //         throw new Error('Network response was not ok');
                //     }
                //     return response.json();
                // }).then(data => {
                //     showConfirmation(data);
                // }).catch(error => {
                //     console.error('Error:', error);
                //     alert('There was a problem with your booking. Please try again.');
                // });

                // For demonstration, we will simulate a success response
                showConfirmation(bookingDetails);
            } catch (error) {
                console.error('Error:', error);
                alert('There was a problem with your booking. Please try again.');
            }
        });

        // Function to display confirmation message
        function showConfirmation(booking) {
            const confirmationMessage = document.getElementById('confirmationMessage');
            confirmationMessage.classList.remove('hidden');
            confirmationMessage.innerHTML = `
                <h3>Booking Confirmed!</h3>
                <p>Thank you, ${booking.name}. Your booking for a ${booking.treatment} on ${booking.date} at ${booking.time} has been confirmed.</p>
            `;
        }
    </script>

    <style>
        .hidden {
            display: none;
        }
        .booking-form {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</body>
</html>
```
