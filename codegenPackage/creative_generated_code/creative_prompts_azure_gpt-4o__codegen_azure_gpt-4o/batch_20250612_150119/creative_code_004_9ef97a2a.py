"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vxp.pertinencemediaa.com
Prompt: Write HTML and CSS code for a login page with "Login" and "Register" buttons, replicating the layout and functionality of the VIP Membership website.
Generated: DETERMINISTIC_9ef97a2a2d741426
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
    <meta name="description" content="Login page for VIP Membership website">
    <title>VIP Membership - Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="login-form">
            <h1>Welcome to VIP Membership</h1>
            <form action="/login" method="POST">
                <!-- Username input field -->
                <label for="username">Username</label>
                <input type="text" id="username" name="username" placeholder="Enter your username" required>

                <!-- Password input field -->
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>

                <!-- Login button -->
                <button type="submit" class="btn login-btn">Login</button>
            </form>
            <!-- Register button -->
            <button class="btn register-btn" onclick="location.href='/register'">Register</button>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Base styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Container styles */
.container {
    width: 100%;
    max-width: 400px;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Header styles */
h1 {
    font-size: 1.8rem;
    text-align: center;
    margin-bottom: 20px;
    color: #333;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

/* Label styles */
label {
    font-size: 1rem;
    margin-bottom: 5px;
    color: #555;
}

/* Input styles */
input[type="text"],
input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
}

/* Button styles */
.btn {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

/* Login button */
.login-btn {
    background-color: #007bff;
    color: #fff;
    margin-bottom: 10px;
}

.login-btn:hover {
    background-color: #0056b3;
}

/* Register button */
.register-btn {
    background-color: #6c757d;
    color: #fff;
}

.register-btn:hover {
    background-color: #5a6268;
}

/* Responsive design */
@media (max-width: 768px) {
    h1 {
        font-size: 1.5rem;
    }

    input[type="text"],
    input[type="password"] {
        font-size: 0.9rem;
    }

    .btn {
        font-size: 0.9rem;
    }
}
```
