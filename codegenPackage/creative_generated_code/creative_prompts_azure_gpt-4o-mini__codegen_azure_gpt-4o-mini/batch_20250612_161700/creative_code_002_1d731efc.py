"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wuffis.pages.dev
Prompt: Write a code snippet to prompt users for a password before granting access to a webpage.
Generated: DETERMINISTIC_1d731efc276da22b
Batch ID: 20250612_161700
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
    <title>Password Protected Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        #login-form {
            display: none;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="login-form">
        <h2>Please Enter Your Password</h2>
        <input type="password" id="password" placeholder="Password" required>
        <button onclick="checkPassword()">Submit</button>
        <p id="error-message" style="color:red; display:none;"></p>
    </div>

    <script>
        // Predefined password for access
        const correctPassword = "securePassword123"; // Change this to your desired password

        // Function to prompt for password
        function promptForPassword() {
            document.getElementById('login-form').style.display = 'block';
        }

        // Function to check the entered password
        function checkPassword() {
            const enteredPassword = document.getElementById('password').value;
            const errorMessage = document.getElementById('error-message');

            // Check if the entered password matches the correct password
            if (enteredPassword === correctPassword) {
                // If correct, grant access and redirect to the protected page
                window.location.href = "protected-page.html"; // Change to your protected page URL
            } else {
                // Show error message if password is incorrect
                errorMessage.textContent = "Incorrect password. Please try again.";
                errorMessage.style.display = 'block';
                document.getElementById('password').value = ''; // Clear the input field
            }
        }

        // Call the function to prompt for a password on page load
        window.onload = promptForPassword;
    </script>
</body>
</html>
```
