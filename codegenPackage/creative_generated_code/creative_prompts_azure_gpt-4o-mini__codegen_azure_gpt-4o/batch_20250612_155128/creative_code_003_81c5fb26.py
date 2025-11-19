"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kleanproutah.com
Prompt: Develop a web form for customer inquiries about graffiti removal services, similar to the contact form used by Klean-Pro Utah.
Generated: DETERMINISTIC_81c5fb260506fc47
Batch ID: 20250612_155128
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
    <title>Graffiti Removal Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #ffffff;
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
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        input, textarea, button {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #0066cc;
            color: #ffffff;
            font-weight: bold;
            cursor: pointer;
        }
        button:hover {
            background-color: #005bb5;
        }
        .error {
            color: red;
            font-size: 12px;
        }
        .success {
            color: green;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Graffiti Removal Inquiry Form</h2>
        <!-- Customer inquiry form -->
        <form id="graffitiForm">
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
                <span class="error" id="nameError"></span>
            </div>
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required>
                <span class="error" id="emailError"></span>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>
                <span class="error" id="phoneError"></span>
            </div>
            <div class="form-group">
                <label for="address">Address of Graffiti:</label>
                <input type="text" id="address" name="address" required>
                <span class="error" id="addressError"></span>
            </div>
            <div class="form-group">
                <label for="message">Additional Details:</label>
                <textarea id="message" name="message" rows="4" placeholder="Describe the graffiti issue..." required></textarea>
                <span class="error" id="messageError"></span>
            </div>
            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="formFeedback" class="success"></div>
    </div>

    <script>
        // JavaScript for form validation and submission
        document.getElementById('graffitiForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form from submitting normally
            
            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('phoneError').textContent = '';
            document.getElementById('addressError').textContent = '';
            document.getElementById('messageError').textContent = '';
            document.getElementById('formFeedback').textContent = '';

            // Collect form data
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const address = document.getElementById('address').value.trim();
            const message = document.getElementById('message').value.trim();

            let hasError = false;

            // Validate form fields
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required.';
                hasError = true;
            }
            if (email === '') {
                document.getElementById('emailError').textContent = 'Email is required.';
                hasError = true;
            } else if (!/\S+@\S+\.\S+/.test(email)) {
                document.getElementById('emailError').textContent = 'Invalid email format.';
                hasError = true;
            }
            if (phone === '') {
                document.getElementById('phoneError').textContent = 'Phone number is required.';
                hasError = true;
            } else if (!/^\d{10}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Phone must be 10 digits.';
                hasError = true;
            }
            if (address === '') {
                document.getElementById('addressError').textContent = 'Address is required.';
                hasError = true;
            }
            if (message === '') {
                document.getElementById('messageError').textContent = 'Details are required.';
                hasError = true;
            }

            // If validation passes, simulate form submission
            if (!hasError) {
                // Simulate a successful submission with feedback
                document.getElementById('formFeedback').textContent = 'Thank you! Your inquiry has been submitted successfully.';
                document.getElementById('graffitiForm').reset(); // Reset the form
            }
        });
    </script>
</body>
</html>
```
