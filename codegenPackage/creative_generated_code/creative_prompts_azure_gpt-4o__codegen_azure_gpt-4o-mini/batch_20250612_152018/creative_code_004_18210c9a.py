"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Generate code to build a subscription form for receiving updates from Darul Raza, ensuring the form validates input fields like email and phone number.
Generated: DETERMINISTIC_18210c9ad54f5bf9
Batch ID: 20250612_152018
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
    <title>Subscription Form - Darul Raza</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Subscribe for Updates from Darul Raza</h1>
        <form id="subscription-form" novalidate>
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
                <span class="error-message" id="email-error"></span>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}">
                <span class="error-message" id="phone-error"></span>
            </div>
            <button type="submit">Subscribe</button>
        </form>
        <div id="success-message" class="success-message"></div>
    </div>

    <script>
        // Get form elements
        const form = document.getElementById('subscription-form');
        const emailInput = document.getElementById('email');
        const phoneInput = document.getElementById('phone');
        const emailError = document.getElementById('email-error');
        const phoneError = document.getElementById('phone-error');
        const successMessage = document.getElementById('success-message');

        // Function to validate email
        function validateEmail(email) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailPattern.test(email);
        }

        // Function to validate phone
        function validatePhone(phone) {
            return phone.length === 10 && /^\d+$/.test(phone);
        }

        // Handle form submission
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Clear previous error messages
            emailError.innerText = '';
            phoneError.innerText = '';
            successMessage.innerText = '';

            // Validate inputs
            const email = emailInput.value.trim();
            const phone = phoneInput.value.trim();
            let isValid = true;

            if (!validateEmail(email)) {
                emailError.innerText = 'Please enter a valid email address.';
                isValid = false;
            }

            if (!validatePhone(phone)) {
                phoneError.innerText = 'Please enter a valid phone number (10 digits).';
                isValid = false;
            }

            // If all inputs are valid, handle successful submission
            if (isValid) {
                // Simulate a successful subscription (replace with actual API call)
                successMessage.innerText = 'Thank you for subscribing! You will receive updates soon.';
                form.reset(); // Reset form
            }
        });
    </script>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        .error-message {
            color: red;
            font-size: 0.9em;
        }
        .success-message {
            color: green;
            font-size: 1.1em;
            margin-top: 15px;
        }
    </style>
</body>
</html>
```
