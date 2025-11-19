"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Construct a web form in HTML that allows users to subscribe for updates on special offers, similar to the subscription feature on Mass Compras.
Generated: DETERMINISTIC_26c8c5175efccf60
Batch ID: 20250612_162753
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
    <title>Special Offers Subscription</title>
    <style>
        /* Simple CSS for styling the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f9f9f9;
        }

        .subscription-form {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 400px;
        }

        .subscription-form h1 {
            font-size: 1.5rem;
            margin-bottom: 15px;
            text-align: center;
        }

        .subscription-form label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        .subscription-form input[type="text"],
        .subscription-form input[type="email"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        .subscription-form button {
            width: 100%;
            padding: 10px;
            font-size: 1rem;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .subscription-form button:hover {
            background-color: #0056b3;
        }

        .subscription-form .error-message {
            color: red;
            font-size: 0.9rem;
            margin-top: -10px;
            margin-bottom: 15px;
        }

        .subscription-form .success-message {
            color: green;
            font-size: 0.9rem;
            text-align: center;
        }
    </style>
</head>
<body>
    <!-- Subscription form container -->
    <form class="subscription-form" id="subscriptionForm">
        <h1>Subscribe for Special Offers</h1>

        <!-- Full Name input -->
        <label for="fullName">Full Name</label>
        <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
        <div class="error-message" id="nameError"></div>

        <!-- Email input -->
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
        <div class="error-message" id="emailError"></div>

        <!-- Submit button -->
        <button type="submit">Subscribe</button>

        <!-- Success message -->
        <div class="success-message" id="successMessage" style="display: none;">
            Thank you for subscribing!
        </div>
    </form>

    <!-- JavaScript for validation and handling the form -->
    <script>
        document.getElementById('subscriptionForm').addEventListener('submit', function (event) {
            // Prevent form submission
            event.preventDefault();

            // Clear any previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('successMessage').style.display = 'none';

            let isValid = true;

            // Validate the full name field
            const fullName = document.getElementById('fullName').value.trim();
            if (fullName === '') {
                document.getElementById('nameError').textContent = 'Please enter your full name.';
                isValid = false;
            }

            // Validate the email field
            const email = document.getElementById('email').value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email format validation
            if (email === '') {
                document.getElementById('emailError').textContent = 'Please enter your email address.';
                isValid = false;
            } else if (!emailRegex.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            // If validation passes, display a success message
            if (isValid) {
                document.getElementById('successMessage').style.display = 'block';
                // Reset the form fields
                document.getElementById('subscriptionForm').reset();
            }
        });
    </script>
</body>
</html>
```
