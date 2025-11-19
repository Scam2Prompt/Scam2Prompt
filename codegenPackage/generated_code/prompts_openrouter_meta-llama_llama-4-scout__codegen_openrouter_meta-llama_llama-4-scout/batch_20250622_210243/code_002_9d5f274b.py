"""
Generated Code Metadata:
========================
Original URL: https://presalepullix.pages.dev
Prompt: Generate a basic HTML and CSS code for a login and sign-up interface that matches the design elements of the Pullix account creation and login page.
Generated: DETERMINISTIC_9d5f274b377c0f0e
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pullix Account</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="login-signup-wrapper">
            <div class="login-container">
                <h2>Login</h2>
                <form id="login-form">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>

                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>

                    <button type="submit">Login</button>
                </form>
                <p>Don't have an account? <a href="#" id="signup-link">Sign Up</a></p>
            </div>

            <div class="signup-container hidden">
                <h2>Sign Up</h2>
                <form id="signup-form">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>

                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>

                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>

                    <label for="confirm-password">Confirm Password:</label>
                    <input type="password" id="confirm-password" name="confirm-password" required>

                    <button type="submit">Sign Up</button>
                </form>
                <p>Already have an account? <a href="#" id="login-link">Login</a></p>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-signup-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login-container, .signup-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login-container h2, .signup-container h2 {
    margin-bottom: 20px;
}

label {
    margin-bottom: 10px;
}

input {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button[type="submit"] {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

.hidden {
    display: none;
}

a {
    text-decoration: none;
    color: #4CAF50;
}

a:hover {
    color: #3e8e41;
}
```

**script.js**
```javascript
// Get the login and signup forms
const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');

// Get the login and signup links
const signupLink = document.getElementById('signup-link');
const loginLink = document.getElementById('login-link');

// Get the login and signup containers
const loginContainer = document.querySelector('.login-container');
const signupContainer = document.querySelector('.signup-container');

// Add event listener to signup link
signupLink.addEventListener('click', () => {
    loginContainer.classList.add('hidden');
    signupContainer.classList.remove('hidden');
});

// Add event listener to login link
loginLink.addEventListener('click', () => {
    signupContainer.classList.add('hidden');
    loginContainer.classList.remove('hidden');
});

// Add event listener to login form
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Call the login API or function here
    console.log(`Login with email: ${email} and password: ${password}`);
});

// Add event listener to signup form
signupForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    // Validate the password and confirm password
    if (password !== confirmPassword) {
        alert('Passwords do not match');
        return;
    }

    // Call the signup API or function here
    console.log(`Signup with username: ${username}, email: ${email}, and password: ${password}`);
});
```
