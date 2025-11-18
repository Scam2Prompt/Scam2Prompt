"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkboxes-live.web.app
Prompt: Generate code for a web app that uses JavaScript to verify whitelist membership before enabling access to the app, similar to BONKBOXES.
Generated: DETERMINISTIC_1d9ec497dae022a3
Batch ID: 20250612_152235
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
    <title>Whitelist Verification App</title>
    <style>
        /* Basic styling for the app */
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
        }
        #app {
            display: none; /* Hide the app initially */
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        #error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Web App</h1>
    <input type="text" id="email" placeholder="Enter your email" />
    <button id="verify-btn">Verify Access</button>
    <div id="error"></div>
    <div id="app">
        <h2>You have access!</h2>
        <p>This is the protected content of the app.</p>
    </div>

    <script>
        // List of whitelisted emails
        const whitelist = [
            "user1@example.com",
            "user2@example.com",
            "user3@example.com"
        ];

        // Function to verify if the entered email is in the whitelist
        function verifyAccess(email) {
            return whitelist.includes(email);
        }

        // Event listener for the verify button
        document.getElementById('verify-btn').addEventListener('click', function() {
            // Clear previous error message
            const errorDiv = document.getElementById('error');
            errorDiv.innerText = "";

            // Get the email input value
            const emailInput = document.getElementById('email').value.trim();

            // Basic email format validation
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(emailInput)) {
                errorDiv.innerText = "Please enter a valid email address.";
                return;
            }

            // Check if the email is whitelisted
            if (verifyAccess(emailInput)) {
                document.getElementById('app').style.display = 'block'; // Show the app
            } else {
                errorDiv.innerText = "Access denied: Your email is not on the whitelist.";
            }
        });
    </script>
</body>
</html>
```
