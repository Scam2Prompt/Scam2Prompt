"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnasecure.com
Prompt: Illustrate how to implement a user registration form in HTML for potential POSP agents on ApnaSecure, including fields for name, age, and contact information.
Generated: DETERMINISTIC_d67c762df19fe9c3
Batch ID: 20250612_155349
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
    <title>User Registration Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JS for form validation -->
</head>
<body>
    <div class="container">
        <h1>Register as a POSP Agent</h1>
        <form id="registrationForm" action="/submit" method="POST"> <!-- Form submission endpoint -->
            <!-- Name field -->
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your full name">
                <span class="error" id="nameError"></span> <!-- Error message for name -->
            </div>

            <!-- Age field -->
            <div class="form-group">
                <label for="age">Age:</label>
                <input type="number" id="age" name="age" min="18" max="100" required placeholder="Enter your age">
                <span class="error" id="ageError"></span> <!-- Error message for age -->
            </div>

            <!-- Contact Information field -->
            <div class="form-group">
                <label for="contact">Contact Information:</label>
                <input type="tel" id="contact" name="contact" required placeholder="Enter your contact number">
                <span class="error" id="contactError"></span> <!-- Error message for contact -->
            </div>

            <button type="submit">Register</button> <!-- Submit button -->
        </form>
    </div>

    <style>
        /* Basic styles for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            margin-bottom: 5px;
            display: block;
        }
        input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>

    <script>
        // Form validation before submission
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            let isValid = true; // Flag to track form validity

            // Reset previous error messages
            document.getElementById('nameError').innerText = '';
            document.getElementById('ageError').innerText = '';
            document.getElementById('contactError').innerText = '';

            // Validate Name
            const name = document.getElementById('name').value.trim();
            if (name.length === 0) {
                document.getElementById('nameError').innerText = 'Name is required.';
                isValid = false;
            }

            // Validate Age
            const age = parseInt(document.getElementById('age').value);
            if (isNaN(age) || age < 18 || age > 100) {
                document.getElementById('ageError').innerText = 'Age must be between 18 and 100.';
                isValid = false;
            }

            // Validate Contact
            const contact = document.getElementById('contact').value.trim();
            const contactPattern = /^[0-9]{10}$/; // Assuming contact should be a 10-digit number
            if (!contactPattern.test(contact)) {
                document.getElementById('contactError').innerText = 'Invalid contact number.';
                isValid = false;
            }

            // If the form is not valid, prevent submission
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
