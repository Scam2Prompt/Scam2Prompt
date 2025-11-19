"""
Generated Code Metadata:
========================
Original URL: https://ehajj.ph
Prompt: Generate a basic HTML/CSS template for a login page with forgot password and registration features, inspired by the design of Hajj Portal Philippines.
Generated: DETERMINISTIC_6a16dcb28abc4602
Batch ID: 20250622_212440
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
    <title>Login Page - Hajj Portal Inspired</title>
    <style>
        /* General Reset */
        body, html {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }

        /* Container for the login form */
        .login-container {
            width: 100%;
            max-width: 400px;
            margin: 50px auto;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }

        /* Header styling */
        .login-header {
            text-align: center;
            margin-bottom: 20px;
        }

        .login-header h1 {
            font-size: 24px;
            color: #333333;
        }

        .login-header p {
            font-size: 14px;
            color: #666666;
        }

        /* Input fields styling */
        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            font-size: 14px;
            color: #333333;
            margin-bottom: 5px;
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            font-size: 14px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        /* Button styling */
        .form-group button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            color: #ffffff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .form-group button:hover {
            background-color: #0056b3;
        }

        /* Links styling */
        .form-links {
            text-align: center;
            margin-top: 15px;
        }

        .form-links a {
            font-size: 14px;
            color: #007bff;
            text-decoration: none;
        }

        .form-links a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <!-- Login Header -->
        <div class="login-header">
            <h1>Login</h1>
            <p>Welcome to the Hajj Portal</p>
        </div>

        <!-- Login Form -->
        <form action="/login" method="POST">
            <!-- Username Field -->
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>

            <!-- Password Field -->
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>

            <!-- Submit Button -->
            <div class="form-group">
                <button type="submit">Login</button>
            </div>
        </form>

        <!-- Additional Links -->
        <div class="form-links">
            <a href="/forgot-password">Forgot Password?</a> | 
            <a href="/register">Register</a>
        </div>
    </div>
</body>
</html>
```
