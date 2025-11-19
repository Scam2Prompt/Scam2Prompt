"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gloclinicaesthetics.com
Prompt: Design a simple HTML form for users to sign up for skincare consultations, incorporating fields for name, email, and skin type, as seen on Glo Clinic Aesthetics.
Generated: DETERMINISTIC_f8d1453af6687bcb
Batch ID: 20250612_162051
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
    <title>Skincare Consultation Signup</title>
    <style>
        /* Style for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        .form-container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .form-container h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input[type="text"],
        input[type="email"],
        select {
            width: calc(100% - 20px);
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        .error-message {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Skincare Consultation Signup</h2>
        <form id="signupForm">
            <!-- Name field -->
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" placeholder="Enter your name" required>
                <span class="error-message" id="nameError"></span>
            </div>

            <!-- Email field -->
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
                <span class="error-message" id="emailError"></span>
            </div>

            <!-- Skin type field -->
            <div class="form-group">
                <label for="skinType">Skin Type:</label>
                <select id="skinType" name="skinType" required>
                    <option value="" disabled selected>Select your skin type</option>
                    <option value="Normal">Normal</option>
                    <option value="Dry">Dry</option>
                    <option value="Oily">Oily</option>
                    <option value="Combination">Combination</option>
                    <option value="Sensitive">Sensitive</option>
                </select>
                <span class="error-message" id="skinTypeError"></span>
            </div>

            <!-- Submit button -->
            <button type="submit">Sign Up</button>
        </form>
    </div>

    <script>
        // JavaScript for form validation and error handling
        const form = document.getElementById('signupForm');

        form.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent form submission for validation

            let isValid = true;

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('skinTypeError').textContent = '';

            // Validate name field
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required.';
                isValid = false;
            }

            // Validate email field
            const email = document.getElementById('email').value.trim();
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address.';
                isValid = false;
            }

            // Validate skin type field
            const skinType = document.getElementById('skinType').value;
            if (!skinType) {
                document.getElementById('skinTypeError').textContent = 'Please select a skin type.';
                isValid = false;
            }

            // If form is valid, submit the data
            if (isValid) {
                alert('Signup successful!');
                form.reset(); // Reset the form fields
            }
        });
    </script>
</body>
</html>
```
