"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: Provide code for a web application that includes a login form with fields for username and password, and a registration feature, styled similarly to the VIP Membership website.
Generated: DETERMINISTIC_aeb7817a281daa9d
Batch ID: 20250612_150119
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
    <title>VIP Membership Login</title>
    <link rel="stylesheet" href="styles.css"> <!-- External CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>VIP Membership Login</h1>
        
        <!-- Login Form -->
        <form id="login-form" onsubmit="return handleLogin(event)">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
            <p>Don't have an account? <a href="#register" onclick="toggleForms()">Register</a></p>
        </form>

        <!-- Registration Form -->
        <form id="registration-form" onsubmit="return handleRegistration(event)" style="display: none;">
            <div class="form-group">
                <label for="reg-username">Username</label>
                <input type="text" id="reg-username" name="reg-username" required>
            </div>
            <div class="form-group">
                <label for="reg-password">Password</label>
                <input type="password" id="reg-password" name="reg-password" required>
            </div>
            <div class="form-group">
                <label for="confirm-password">Confirm Password</label>
                <input type="password" id="confirm-password" name="confirm-password" required>
            </div>
            <button type="submit">Register</button>
            <p>Already have an account? <a href="#login" onclick="toggleForms()">Login</a></p>
        </form>
    </div>

    <script>
        // Function to handle login submission
        function handleLogin(event) {
            event.preventDefault(); // Prevent default form submission

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Simulated login process
            if (username && password) {
                alert("Login successful!"); // Replace with actual authentication logic
                // Redirect or load user dashboard here
            } else {
                alert("Please enter valid credentials.");
            }
        }

        // Function to handle registration submission
        function handleRegistration(event) {
            event.preventDefault(); // Prevent default form submission

            const username = document.getElementById('reg-username').value;
            const password = document.getElementById('reg-password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            // Check if passwords match
            if (password !== confirmPassword) {
                alert("Passwords do not match.");
                return false;
            }

            // Simulated registration process
            if (username && password) {
                alert("Registration successful!"); // Replace with actual registration logic
                toggleForms(); // Switch back to login form
            } else {
                alert("Please fill in all fields.");
            }
        }

        // Function to toggle between login and registration forms
        function toggleForms() {
            const loginForm = document.getElementById('login-form');
            const registrationForm = document.getElementById('registration-form');

            if (loginForm.style.display === "none") {
                loginForm.style.display = "block";
                registrationForm.style.display = "none";
            } else {
                loginForm.style.display = "none";
                registrationForm.style.display = "block";
            }
        }
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            margin: auto;
            padding: 20px;
            background: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
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
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
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
        p {
            text-align: center;
        }
    </style>
</body>
</html>
```
