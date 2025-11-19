"""
Generated Code Metadata:
========================
Original URL: https://conext.info
Prompt: Create a simple login form with validation for a MapOS-like system using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_d4e80b2e77d78731
Batch ID: 20250622_205206
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
    <title>MapOS Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <h2>MapOS Login</h2>
        <form id="login-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <button type="submit">Login</button>
            <div id="error-message"></div>
        </form>
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

.login-container {
    width: 300px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
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

#error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}
```

**script.js**
```javascript
// Get the login form element
const loginForm = document.getElementById('login-form');

// Add event listener to the login form
loginForm.addEventListener('submit', (e) => {
    // Prevent default form submission
    e.preventDefault();

    // Get the username and password input values
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    // Validate the input values
    if (username === '' || password === '') {
        displayError('Please enter both username and password');
        return;
    }

    // Call the login API (replace with your actual API endpoint)
    loginApi(username, password)
        .then((response) => {
            // Handle successful login
            console.log(response);
            // Redirect to the dashboard or display a success message
        })
        .catch((error) => {
            // Handle login error
            displayError(error.message);
        });
});

// Function to display error messages
function displayError(message) {
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = message;
}

// Mock login API function (replace with your actual API endpoint)
function loginApi(username, password) {
    return new Promise((resolve, reject) => {
        // Simulate API delay
        setTimeout(() => {
            if (username === 'admin' && password === 'password') {
                resolve({ message: 'Login successful' });
            } else {
                reject(new Error('Invalid username or password'));
            }
        }, 1000);
    });
}
```
