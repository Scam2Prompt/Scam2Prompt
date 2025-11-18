"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksynccs.w3spaces.com
Prompt: Generate a contact form with HTML and CSS that can be hosted on W3 Spaces, including validation using JavaScript.
Generated: DETERMINISTIC_185c4d88ebc288d8
Batch ID: 20250612_150440
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
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 500px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            margin-bottom: 5px;
            display: block;
            color: #555;
        }

        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        textarea {
            resize: vertical;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
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
    <div class="container">
        <h2>Contact Us</h2>
        <form id="contactForm">
            <div class="form-group">
                <label for="name">Name <span class="error" id="nameError"></span></label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email <span class="error" id="emailError"></span></label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Message <span class="error" id="messageError"></span></label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
    </div>

    <script>
        // Function to validate the contact form
        function validateForm(event) {
            event.preventDefault(); // Prevent form submission
            let isValid = true; // Flag to track form validity

            // Clear previous error messages
            document.getElementById('nameError').innerText = '';
            document.getElementById('emailError').innerText = '';
            document.getElementById('messageError').innerText = '';

            // Get form fields
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Name validation
            if (name.length < 3) {
                document.getElementById('nameError').innerText = 'Name must be at least 3 characters.';
                isValid = false;
            }

            // Email validation
            const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
            if (!emailPattern.test(email)) {
                document.getElementById('emailError').innerText = 'Please enter a valid email.';
                isValid = false;
            }

            // Message validation
            if (message.length < 10) {
                document.getElementById('messageError').innerText = 'Message must be at least 10 characters.';
                isValid = false;
            }

            // If the form is valid, you can now submit the form or perform other actions
            if (isValid) {
                alert('Form submitted successfully!'); // Placeholder for actual submission logic
                // Here you can add code to send form data to the server
                // e.g., using fetch() or XMLHttpRequest
            }
        }

        // Attach the validateForm function to the form submit event
        document.getElementById('contactForm').addEventListener('submit', validateForm);
    </script>
</body>
</html>
```
