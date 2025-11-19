"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeousgetaways.com
Prompt: Construct a form validation script in HTML and JavaScript to ensure all necessary fields are completed for booking a cosmetic surgery holiday with Gorgeous Getaways.
Generated: DETERMINISTIC_feda7abf3aff83eb
Batch ID: 20250612_155417
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
    <title>Cosmetic Surgery Holiday Booking</title>
    <style>
        /* Simple styles for better user experience */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
            margin-top: 5px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        input, select {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
        }
    </style>
</head>
<body>

<h2>Book Your Cosmetic Surgery Holiday</h2>

<form id="bookingForm">
    <label for="name">Full Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="phone">Phone Number:</label>
    <input type="tel" id="phone" name="phone" required>

    <label for="destination">Destination:</label>
    <select id="destination" name="destination" required>
        <option value="">Select a destination...</option>
        <option value="Thailand">Thailand</option>
        <option value="Turkey">Turkey</option>
        <option value="Mexico">Mexico</option>
        <option value="Spain">Spain</option>
    </select>

    <label for="date">Preferred Date:</label>
    <input type="date" id="date" name="date" required>

    <button type="submit">Submit Booking</button>
</form>

<div id="errorMessages" class="error"></div>

<script>
    // Function to validate form inputs
    function validateForm(event) {
        event.preventDefault(); // Prevent the default form submission

        // Clear previous error messages
        const errorMessagesDiv = document.getElementById('errorMessages');
        errorMessagesDiv.innerHTML = '';

        // Get form values
        const name = document.getElementById('name').value.trim();
        const email = document.getElementById('email').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const destination = document.getElementById('destination').value;
        const date = document.getElementById('date').value;

        // Initialize an array to hold error messages
        let errors = [];

        // Validate required fields
        if (!name) {
            errors.push('Name is required.');
        }
        if (!email) {
            errors.push('Email is required.');
        }
        if (!phone) {
            errors.push('Phone number is required.');
        }
        if (!destination) {
            errors.push('Please select a destination.');
        }
        if (!date) {
            errors.push('Preferred date is required.');
        }

        // If there are errors, display them
        if (errors.length > 0) {
            errorMessagesDiv.innerHTML = errors.join('<br>');
            return; // Stop execution if there are errors
        }

        // If all validations pass, submit the form data (here we just log to console)
        console.log('Form submitted successfully!');
        console.log({ name, email, phone, destination, date });
        alert('Your booking has been submitted.'); // Simulate a successful submission
    }

    // Attach the validation function to the form's submit event
    document.getElementById('bookingForm').addEventListener('submit', validateForm);
</script>

</body>
</html>
```
