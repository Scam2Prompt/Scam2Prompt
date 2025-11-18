"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbased.beautyjibindia.com
Prompt: Develop a front-end login page using HTML and CSS that replicates the design of "Coin Base Login," including all the mentioned fields and buttons.
Generated: DETERMINISTIC_b4c7cf79a4bdb41c
Batch ID: 20250612_150237
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
    <title>Login - Coin Base</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Log In to Your Account</h1>
        <form id="loginForm" action="/login" method="POST">
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email" />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required placeholder="Enter your password" />
            </div>
            <div class="form-group">
                <button type="submit">Log In</button>
            </div>
            <div class="form-footer">
                <a href="/forgot-password">Forgot password?</a>
                <p>Don't have an account? <a href="/signup">Sign up</a></p>
            </div>
        </form>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset to ensure consistent styling across browsers */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Container for the login form */
.container {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 2rem;
    width: 300px;
}

/* Header styling */
h1 {
    margin-bottom: 1.5rem;
    font-size: 1.5rem;
    color: #333;
}

/* Form group styling */
.form-group {
    margin-bottom: 1.5rem;
}

/* Label styling */
label {
    margin-bottom: 0.5rem;
    display: block;
    font-size: 0.9rem;
    color: #666;
}

/* Input styling */
input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
}

/* Button styling */
button {
    width: 100%;
    padding: 0.75rem;
    border: none;
    border-radius: 4px;
    background-color: #0070f3;
    color: #fff;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s;
}

/* Button hover effect */
button:hover {
    background-color: #005bb5;
}

/* Form footer styling */
.form-footer {
    margin-top: 1rem;
    text-align: center;
}

/* Link styling */
a {
    color: #0070f3;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```
