"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amici.nz
Prompt: Construct a simple HTML form that enables customers to submit inquiries to Amici Italian Cafe, ensuring it captures all necessary contact information.
Generated: DETERMINISTIC_a52db2d17d8371e5
Batch ID: 20250612_155233
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
    <title>Contact Us - Amici Italian Cafe</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }

        .form-container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }

        h2 {
            text-align: center;
            color: #333;
        }

        label {
            display: block;
            margin: 10px 0 5px;
            font-weight: bold;
        }

        input, textarea, button {
            width: 100%;
            padding: 10px;
            margin: 5px 0 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        button {
            background-color: #28a745;
            color: white;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background-color: #218838;
        }

        .error-message {
            color: red;
            font-size: 0.9em;
        }
    </style>
    <script>
        // Client-side validation of the form inputs
        function validateForm(event) {
            const name = document.forms["contactForm"]["name"].value;
            const email = document.forms["contactForm"]["email"].value;
            const message = document.forms["contactForm"]["message"].value;

            const errorDiv = document.getElementById("error-message");
            errorDiv.innerHTML = ""; // Clear previous errors

            if (!name || !email || !message) {
                errorDiv.innerHTML = "Please fill out all fields.";
                event.preventDefault();
                return false;
            }

            // Basic email format validation
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                errorDiv.innerHTML = "Please enter a valid email address.";
                event.preventDefault();
                return false;
            }

            return true;
        }
    </script>
</head>
<body>
    <div class="form-container">
        <h2>Contact Amici Italian Cafe</h2>
        <form name="contactForm" action="/submit_inquiry" method="POST" onsubmit="return validateForm(event)">
            <!-- Name field -->
            <label for="name">Full Name</label>
            <input type="text" id="name" name="name" placeholder="Your full name" required>

            <!-- Email field -->
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" placeholder="Your email address" required>

            <!-- Phone field -->
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" placeholder="Your phone number (optional)">

            <!-- Inquiry field -->
            <label for="message">Your Inquiry</label>
            <textarea id="message" name="message" rows="5" placeholder="Write your inquiry here..." required></textarea>

            <!-- Error message display -->
            <div id="error-message" class="error-message"></div>

            <!-- Submit button -->
            <button type="submit">Send Inquiry</button>
        </form>
    </div>
</body>
</html>
```
