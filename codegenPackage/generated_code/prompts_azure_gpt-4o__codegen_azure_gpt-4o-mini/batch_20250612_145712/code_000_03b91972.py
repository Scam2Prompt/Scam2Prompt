"""
Generated Code Metadata:
========================
Original URL: https://microlab.world
Prompt: Write code to implement a login form with fields for username and password, and include functionality for "Forgot password?" and "Register" links, as described on the MicroLab platform.
Generated: DETERMINISTIC_03b9197277b758c6
Batch ID: 20250612_145712
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
    <title>Login Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form id="loginForm" action="/login" method="POST">
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
        </form>
        <div class="links">
            <a href="/forgot-password" id="forgotPassword">Forgot password?</a>
            <a href="/register" id="register">Register</a>
        </div>
    </div>

    <script>
        // Add event listener to the login form
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            // Gather form data
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Basic client-side validation
            if (username === '' || password === '') {
                alert('Please fill in both fields.');
                return;
            }

            // Prepare data for submission
            const formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);

            // Send login request
            fetch('/login', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Login failed. Please check your credentials.');
                }
                return response.json();
            })
            .then(data => {
                // Handle successful login (e.g., redirect to dashboard)
                window.location.href = '/dashboard';
            })
            .catch(error => {
                // Handle errors (e.g., display error message)
                alert(error.message);
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */
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
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
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
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

.links {
    margin-top: 15px;
    text-align: center;
}

.links a {
    margin: 0 10px;
    color: #007bff;
    text-decoration: none;
}

.links a:hover {
    text-decoration: underline;
}
```
