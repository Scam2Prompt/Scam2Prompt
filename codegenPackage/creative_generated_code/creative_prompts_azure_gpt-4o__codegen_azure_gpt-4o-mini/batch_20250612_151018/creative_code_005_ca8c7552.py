"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-137--keen-roentgen-cafcb7.netlify.app
Prompt: Create a newsletter signup form in JavaScript that sends user emails to a backend, inspired by Joe Previte's focus on helping others learn to code and his newsletter feature.
Generated: DETERMINISTIC_ca8c75521c46c117
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-backend-api.com/newsletter/signup": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter Signup Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .signup-form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .signup-form h2 {
            margin-bottom: 20px;
        }
        .signup-form input[type="email"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .signup-form button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .signup-form button:hover {
            background-color: #0056b3;
        }
        .message {
            margin-top: 15px;
            font-size: 1.1em;
        }
    </style>
</head>
<body>

<div class="signup-form">
    <h2>Subscribe to our Newsletter</h2>
    <input type="email" id="email" placeholder="Enter your email" required>
    <button id="submit">Sign Up</button>
    <div id="responseMessage" class="message"></div>
</div>

<script>
    // Function to handle form submission
    document.getElementById('submit').addEventListener('click', async function() {
        const emailInput = document.getElementById('email');
        const email = emailInput.value;
        const responseMessage = document.getElementById('responseMessage');

        // Validate email format
        if (!validateEmail(email)) {
            responseMessage.textContent = 'Please enter a valid email address.';
            responseMessage.style.color = 'red';
            return;
        }

        // Prepare data for submission
        const data = { email: email };

        try {
            // Send a POST request to the backend
            const response = await fetch('https://your-backend-api.com/newsletter/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            // Check if the response is successful
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }

            // Parse the JSON response
            const result = await response.json();

            // Display success message
            responseMessage.textContent = 'Thank you for subscribing!';
            responseMessage.style.color = 'green';

            // Clear the input field
            emailInput.value = '';
        } catch (error) {
            // Display error message
            responseMessage.textContent = 'Error: ' + error.message;
            responseMessage.style.color = 'red';
        }
    });

    // Function to validate email format
    function validateEmail(email) {
        // Regular expression for validating an email address
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }
</script>

</body>
</html>
```
