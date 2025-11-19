"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-wuffis.pages.dev
Prompt: How can I implement password protection for a web page using JavaScript?
Generated: DETERMINISTIC_7e36a0c858e86998
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
        /* Basic styling for the page */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        #loginForm {
            display: none; /* Hide form initially */
            border: 1px solid #ccc;
            padding: 20px;
            background-color: white;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="loginForm">
        <h2>Enter Password</h2>
        <input type="password" id="password" placeholder="Password" required>
        <button id="submitPassword">Submit</button>
        <p id="error-message" style="color:red; display:none;"></p>
    </div>

    <script>
        // Constant for the password (should be stored securely in a real application)
        const PASSWORD = 'yourSecurePassword'; // Change this to your desired password

        // Function to show the login form
        function showLoginForm() {
            document.getElementById('loginForm').style.display = 'block';
        }

        // Function to validate the password
        function validatePassword() {
            const inputPassword = document.getElementById('password').value;
            const errorMessage = document.getElementById('error-message');

            // Check if the input matches the stored password
            if (inputPassword === PASSWORD) {
                // Redirect or allow access to protected content
                alert('Access granted!');
                // Here you could redirect to a different page or reveal content
                // window.location.href = 'protected-content.html'; // Example
                errorMessage.style.display = 'none';
            } else {
                // Display error for wrong password
                errorMessage.textContent = 'Incorrect password. Please try again.';
                errorMessage.style.display = 'block';
            }
        }

        // Event listener for when the DOM content is loaded
        document.addEventListener('DOMContentLoaded', () => {
            // Show the login form on page load
            showLoginForm();

            // Event listener for the submit button
            document.getElementById('submitPassword').addEventListener('click', (event) => {
                event.preventDefault(); // Prevent default form submission
                validatePassword(); // Call validate function
            });
        });
    </script>

</body>
</html>
```
