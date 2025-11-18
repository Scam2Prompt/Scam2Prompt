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
    <title>Login Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <div class="container">
        <h1>Welcome to VIP Membership</h1>
        <form id="loginForm" action="/login" method="POST">
            <div class="input-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="btn">Login</button>
        </form>
        <p>Don't have an account? <a href="/register" class="link">Register here</a></p>
        <a href="/register" class="btn register-btn">Register</a>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset default margins and paddings */
body, h1, p {
    margin: 0;
    padding: 0;
}

/* Style for the container */
.container {
    max-width: 400px; /* Set max width for the container */
    margin: 100px auto; /* Center the container vertically and horizontally */
    padding: 20px; /* Add padding inside the container */
    border: 1px solid #ccc; /* Add border */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    text-align: center; /* Center text */
}

/* Style for input groups */
.input-group {
    margin-bottom: 15px; /* Space between input groups */
}

/* Style for labels */
label {
    display: block; /* Block display for labels */
    margin-bottom: 5px; /* Space between label and input */
}

/* Style for input fields */
input[type="text"],
input[type="password"] {
    width: 100%; /* Full width inputs */
    padding: 10px; /* Padding inside inputs */
    border: 1px solid #ccc; /* Input border */
    border-radius: 4px; /* Rounded corners on inputs */
}

/* Base style for buttons */
.btn {
    background-color: #007BFF; /* Button color */
    color: white; /* Button text color */
    padding: 10px 15px; /* Button padding */
    border: none; /* No border */
    border-radius: 4px; /* Rounded corners */
    cursor: pointer; /* Pointer on hover */
    text-decoration: none; /* Remove underline from links */
}

/* Change button color on hover */
.btn:hover {
    background-color: #0056b3; /* Darken button on hover */
}

/* Style for the register button */
.register-btn {
    background-color: #28A745; /* Different color for register button */
}

.register-btn:hover {
    background-color: #218838; /* Darken on hover */
}

/* Style for links */
.link {
    color: #007BFF; /* Link color */
    text-decoration: none; /* Remove underline */
}

.link:hover {
    text-decoration: underline; /* Underline on hover */
}
```
