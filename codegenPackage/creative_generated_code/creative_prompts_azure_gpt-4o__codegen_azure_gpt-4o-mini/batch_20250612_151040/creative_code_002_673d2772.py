"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitebody.com.br
Prompt: Generate HTML and JavaScript code for a contact form that allows users to book electrostimulation training sessions, with validation for email and phone number fields.
Generated: DETERMINISTIC_673d2772b9811d1d
Batch ID: 20250612_151040
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
    <title>Electrostimulation Training Booking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #5cb85c;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
        .error {
            color: red;
            margin-top: -10px;
            margin-bottom: 10px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<h1>Book Your Electrostimulation Training Session</h1>

<!-- Contact form for booking -->
<form id="contactForm" novalidate>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <div id="emailError" class="error"></div>

    <label for="phone">Phone:</label>
    <input type="tel" id="phone" name="phone" pattern="[0-9]{10}" required>
    <div id="phoneError" class="error"></div>

    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4"></textarea>

    <button type="submit">Book Now</button>
</form>

<script>
    // Validate email and phone fields
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission to validate

        // Clear previous error messages
        document.getElementById('emailError').innerText = '';
        document.getElementById('phoneError').innerText = '';

        // Get form fields
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;

        let valid = true;

        // Email validation regex
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(email)) {
            document.getElementById('emailError').innerText = 'Please enter a valid email address.';
            valid = false;
        }

        // Phone number validation (10 digits)
        const phoneRegex = /^[0-9]{10}$/;
        if (!phoneRegex.test(phone)) {
            document.getElementById('phoneError').innerText = 'Please enter a valid 10-digit phone number.';
            valid = false;
        }

        // If all fields are valid, submit the form (or you can implement an AJAX request)
        if (valid) {
            alert('Booking successful! We will contact you soon.');
            // Here you would typically send the form data to the server
            // Example: submitFormData();
        }
    });

    // Example function for form data submission (to be implemented)
    function submitFormData() {
        // Implementation for submitting form data via AJAX or Fetch API
    }
</script>

</body>
</html>
```
