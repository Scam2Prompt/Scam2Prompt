"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Construct a simple HTML form that mimics the login interface of the Vertiv GmbH Mitarbeiterangebote site, including fields for email and password.
Generated: DETERMINISTIC_314a996369fcbb23
Batch ID: 20250612_162538
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
    <title>Login - Vertiv GmbH Mitarbeiterangebote</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <style>
        body {
            font-family: Arial, sans-serif; /* Set a default font */
            background-color: #f4f4f4; /* Light gray background */
            color: #333; /* Darker text color */
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh; /* Full viewport height */
            margin: 0; /* Remove default margin */
        }

        .login-container {
            background-color: #fff; /* White background for the form */
            padding: 20px; /* Inner space for the form */
            border-radius: 8px; /* Rounded corners */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
            width: 300px; /* Fixed width for the form */
        }

        input[type="email"], input[type="password"] {
            width: 100%; /* Full width inputs */
            padding: 10px; /* Inner space for inputs */
            margin: 10px 0; /* Space between inputs */
            border: 1px solid #ccc; /* Light border */
            border-radius: 4px; /* Rounded corners for inputs */
        }

        button {
            background-color: #5cb85c; /* Bootstrap success color */
            color: white; /* White text color */
            border: none; /* No border */
            padding: 10px; /* Inner space for button */
            border-radius: 4px; /* Rounded corners for button */
            cursor: pointer; /* Pointer cursor on hover */
            width: 100%; /* Full width button */
        }

        button:hover {
            background-color: #4cae4c; /* Darken button on hover */
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2> <!-- Header for the form -->
        <form id="loginForm" action="/login" method="POST"> <!-- Form action and method -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="you@example.com" /> <!-- Email input -->

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required placeholder="Your password" /> <!-- Password input -->

            <button type="submit">Login</button> <!-- Submit button -->
        </form>
    </div>

    <script>
        // Form submission event handler for additional validation (if needed)
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            // Example: Prevent form submission if email format is invalid
            const emailInput = document.getElementById('email');
            if (!emailInput.validity.valid) {
                event.preventDefault(); // Prevent form submission
                alert('Please enter a valid email address.'); // Alert user
            }
        });
    </script>
</body>
</html>
```
