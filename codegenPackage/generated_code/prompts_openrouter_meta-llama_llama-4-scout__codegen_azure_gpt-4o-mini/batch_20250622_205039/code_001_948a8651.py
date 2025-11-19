"""
Generated Code Metadata:
========================
Original URL: https://vxp.pertinencemediaa.com
Prompt: Generate HTML code for a basic membership login page with a registration option.
Generated: DETERMINISTIC_948a8651c013f4f5
Batch ID: 20250622_205039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Membership Login Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Member Login</h1>
        <form id="loginForm" action="/login" method="POST"> <!-- Form for user login -->
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required> <!-- Required field -->
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required> <!-- Required field -->
            </div>
            <button type="submit">Login</button> <!-- Submit button for login -->
        </form>
        <p>Don't have an account? <a href="#register" id="registerLink">Register here</a></p> <!-- Link to registration -->
        
        <div id="register" class="hidden"> <!-- Registration section, initially hidden -->
            <h2>Register</h2>
            <form id="registrationForm" action="/register" method="POST"> <!-- Form for user registration -->
                <div class="form-group">
                    <label for="regUsername">Username:</label>
                    <input type="text" id="regUsername" name="regUsername" required> <!-- Required field -->
                </div>
                <div class="form-group">
                    <label for="regPassword">Password:</label>
                    <input type="password" id="regPassword" name="regPassword" required> <!-- Required field -->
                </div>
                <div class="form-group">
                    <label for="confirmPassword">Confirm Password:</label>
                    <input type="password" id="confirmPassword" name="confirmPassword" required> <!-- Required field -->
                </div>
                <button type="submit">Register</button> <!-- Submit button for registration -->
            </form>
            <p>Already have an account? <a href="#login" id="loginLink">Login here</a></p> <!-- Link to login -->
        </div>
    </div>

    <script>
        // Toggle registration form visibility
        document.getElementById('registerLink').addEventListener('click', function() {
            document.getElementById('register').classList.toggle('hidden');
        });

        document.getElementById('loginLink').addEventListener('click', function() {
            document.getElementById('register').classList.add('hidden');
        });
    </script>

    <style>
        /* Basic styles for the login and registration forms */
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
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .hidden {
            display: none; /* Class to hide elements */
        }
    </style>
</body>
</html>
```
