"""
Generated Code Metadata:
========================
Original URL: https://webmail.consesys.io
Prompt: Create a simple HTML form to handle webmail login with email address and password fields, using cPanel's webmail interface as a reference.
Generated: DETERMINISTIC_b41051c8bfe8b1b8
Batch ID: 20250622_205154
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
    <title>Webmail Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 1.5rem;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
        }
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 0.75rem;
            background-color: #0078d7;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #005fa3;
        }
        .error-message {
            color: #d32f2f;
            margin-top: 0.5rem;
            font-size: 0.875rem;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Webmail Login</h1>
        <form id="loginForm" action="/webmail/login" method="POST">
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required placeholder="yourname@example.com">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="••••••••">
            </div>
            <div id="errorMessage" class="error-message"></div>
            <button type="submit">Login</button>
        </form>
    </div>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Clear previous error messages
            document.getElementById('errorMessage').textContent = '';
            
            // Get form values
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;
            
            // Simple validation
            if (!email || !password) {
                document.getElementById('errorMessage').textContent = 'Please fill in all fields';
                return;
            }
            
            // Email format validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                document.getElementById('errorMessage').textContent = 'Please enter a valid email address';
                return;
            }
            
            // If validation passes, submit the form
            this.submit();
        });
    </script>
</body>
</html>
```
