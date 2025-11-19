"""
Generated Code Metadata:
========================
Original URL: https://exodusiiiuatapi.azurewebsites.net
Prompt: Generate HTML code for a basic login page with a username field, password field, and a "Next" button, inspired by the Exodus III login page layout.
Generated: DETERMINISTIC_32e9cc79b8cd3b6a
Batch ID: 20250622_211609
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
    <title>Login Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <style>
        /* Basic styles for the login page */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form id="loginForm" onsubmit="return handleLogin(event)">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Next</button>
        </form>
    </div>

    <script>
        /**
         * Handles the login form submission.
         * @param {Event} event - The form submission event.
         * @returns {boolean} - Returns false to prevent default form submission.
         */
        function handleLogin(event) {
            event.preventDefault(); // Prevent default form submission

            // Retrieve username and password values
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Basic validation (could be expanded)
            if (username === '' || password === '') {
                alert('Please fill in both fields.');
                return false;
            }

            // Simulate a login process (replace with actual authentication logic)
            console.log('Username:', username);
            console.log('Password:', password);
            alert('Login successful!'); // Placeholder for successful login

            // Redirect or perform further actions here
            // window.location.href = 'nextPage.html'; // Example redirect

            return false; // Prevent form submission
        }
    </script>
</body>
</html>
```
