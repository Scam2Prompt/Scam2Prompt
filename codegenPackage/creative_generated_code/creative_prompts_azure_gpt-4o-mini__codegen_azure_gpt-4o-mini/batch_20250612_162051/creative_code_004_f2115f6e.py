"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Design a simple HTML form for user registration that captures username and password, inspired by the login features of the Mambo Wood website.
Generated: DETERMINISTIC_f2115f6e914084c0
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
    <title>User Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript for validation -->
</head>
<body>
    <div class="container">
        <h1>User Registration</h1>
        <form id="registrationForm" action="/submit_registration" method="POST">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required minlength="3" maxlength="20" placeholder="Enter your username" />
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required minlength="6" maxlength="20" placeholder="Enter your password" />
            </div>
            <div class="form-group">
                <button type="submit">Register</button>
            </div>
            <div id="error-message" class="error-message"></div> <!-- Container for error messages -->
        </form>
    </div>

    <style>
        /* Basic styling for the registration form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
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
            display: block;
            margin-bottom: 5px;
        }
        input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error-message {
            color: red;
            margin-top: 10px;
        }
    </style>

    <script>
        // Validate the form before submission
        document.getElementById('registrationForm').addEventListener('submit', function(event) {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = ''; // Clear previous error messages

            // Basic validation
            if (username.length < 3 || username.length > 20) {
                errorMessage.textContent = 'Username must be between 3 and 20 characters.';
                event.preventDefault(); // Prevent form submission
            } else if (password.length < 6 || password.length > 20) {
                errorMessage.textContent = 'Password must be between 6 and 20 characters.';
                event.preventDefault(); // Prevent form submission
            }
            // Additional validation can be added here
        });
    </script>
</body>
</html>
```
