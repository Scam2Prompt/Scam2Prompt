"""
Generated Code Metadata:
========================
Original URL: https://member.bmtours.id
Prompt: Generate a simple login system using JavaScript and HTML for a website similar to BM Tours, with features for password recovery.
Generated: DETERMINISTIC_6d6dd04805b4a2ba
Batch ID: 20250622_210655
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
    <title>Login System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form id="login-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
        <p><a href="#" id="forgot-password">Forgot Password?</a></p>
    </div>

    <div class="recovery-container" style="display: none;">
        <h2>Password Recovery</h2>
        <form id="recovery-form">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <button type="submit">Send Recovery Link</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
.login-container, .recovery-container {
    width: 300px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="password"], input[type="email"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

**script.js**
```javascript
// Get DOM elements
const loginForm = document.getElementById('login-form');
const forgotPasswordLink = document.getElementById('forgot-password');
const recoveryForm = document.getElementById('recovery-form');
const recoveryContainer = document.querySelector('.recovery-container');
const loginContainer = document.querySelector('.login-container');

// User data (replace with actual database or storage)
let users = [
    { id: 1, username: 'john', password: 'password123', email: 'john@example.com' },
    { id: 2, username: 'jane', password: 'password456', email: 'jane@example.com' },
];

// Login functionality
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Find user by username
    const user = users.find((u) => u.username === username);

    if (user && user.password === password) {
        // Login successful
        console.log('Login successful');
        // Redirect to protected page or display success message
    } else {
        // Login failed
        console.log('Invalid username or password');
        alert('Invalid username or password');
    }
});

// Forgot password functionality
forgotPasswordLink.addEventListener('click', () => {
    loginContainer.style.display = 'none';
    recoveryContainer.style.display = 'block';
});

// Recovery form submission
recoveryForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;

    // Find user by email
    const user = users.find((u) => u.email === email);

    if (user) {
        // Send recovery link (replace with actual email sending functionality)
        console.log(`Recovery link sent to ${email}`);
        alert(`Recovery link sent to ${email}`);
        // Redirect back to login page or display success message
        recoveryContainer.style.display = 'none';
        loginContainer.style.display = 'block';
    } else {
        // User not found
        console.log('User not found');
        alert('User not found');
    }
});
```

**server.js (using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// User data (replace with actual database)
let users = [
    { id: 1, username: 'john', password: 'password123', email: 'john@example.com' },
    { id: 2, username: 'jane', password: 'password456', email: 'jane@example.com' },
];

// Login endpoint
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Find user by username
    const user = users.find((u) => u.username === username);

    if (user && user.password === password) {
        // Login successful
        res.json({ success: true });
    } else {
        // Login failed
        res.status(401).json({ success: false, message: 'Invalid username or password' });
    }
});

// Recovery endpoint
app.post('/recover', (req, res) => {
    const { email } = req.body;

    // Find user by email
    const user = users.find((u) => u.email === email);

    if (user) {
        // Send recovery link (replace with actual email sending functionality)
        res.json({ success: true });
    } else {
        // User not found
        res.status(404).json({ success: false, message: 'User not found' });
    }
});

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
