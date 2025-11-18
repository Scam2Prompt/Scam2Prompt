"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocula.gob.mx
Prompt: Develop a web-based form for submitting public comments or inquiries, referencing the structure of the Cocula government site’s communication features.
Generated: DETERMINISTIC_a32e95dc90d0e0f2
Batch ID: 20250612_152410
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
    <title>Public Comments Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
        }
        .form-container {
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        input, textarea, button {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        textarea {
            resize: vertical;
            min-height: 120px;
        }
        button {
            background-color: #007bff;
            color: #fff;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        .success-message {
            color: green;
            font-size: 1em;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Contact Us</h1>
        <form id="commentsForm">
            <!-- Name Field -->
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <p class="error" id="nameError"></p>
            </div>
            <!-- Email Field -->
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <p class="error" id="emailError"></p>
            </div>
            <!-- Message Field -->
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                <p class="error" id="messageError"></p>
            </div>
            <!-- Submit Button -->
            <button type="submit">Submit</button>
        </form>
        <p class="success-message" id="successMessage"></p>
    </div>

    <script>
        // JavaScript for handling form submission
        document.getElementById('commentsForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission behavior

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('messageError').textContent = '';
            document.getElementById('successMessage').textContent = '';

            // Collect form data
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            let hasError = false;

            // Validate name
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required.';
                hasError = true;
            }

            // Validate email
            if (email === '') {
                document.getElementById('emailError').textContent = 'Email is required.';
                hasError = true;
            } else if (!validateEmail(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address.';
                hasError = true;
            }

            // Validate message
            if (message === '') {
                document.getElementById('messageError').textContent = 'Message is required.';
                hasError = true;
            }

            // If no errors, show success message
            if (!hasError) {
                document.getElementById('successMessage').textContent = 'Thank you for your message! We will get back to you shortly.';
                
                // Clear the form fields after submission
                document.getElementById('commentsForm').reset();
            }
        });

        // Helper function to validate email format
        function validateEmail(email) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return emailRegex.test(email);
        }
    </script>
</body>
</html>
```
