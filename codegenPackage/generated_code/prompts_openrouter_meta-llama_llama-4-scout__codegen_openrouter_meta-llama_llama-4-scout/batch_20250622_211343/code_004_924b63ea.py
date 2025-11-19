"""
Generated Code Metadata:
========================
Original URL: https://webmail.omninetwork.it
Prompt: Create a simple webmail login form with password input validation using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_924b63ea74834e1d
Batch ID: 20250622_211343
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
    <title>Webmail Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <h2>Webmail Login</h2>
        <form id="login-form">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

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

input[type="email"], input[type="password"] {
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
    // Prevent default form submission behavior
    e.preventDefault();

    // Get the email and password input values
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    // Validate the password
    if (!validatePassword(password)) {
        displayError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.');
        return;
    }

    // If validation passes, submit the form data to the server
    submitFormData(email, password);
});

// Function to validate the password
function validatePassword(password) {
    // Regular expression to check for password requirements
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;
    return passwordRegex.test(password);
}

// Function to display error messages
function displayError(message) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.textContent = message;
}

// Function to submit the form data to the server
function submitFormData(email, password) {
    // Replace with your server-side API endpoint
    const apiEndpoint = '/api/login';

    // Create a JSON payload with the form data
    const payload = JSON.stringify({ email, password });

    // Use the Fetch API to send a POST request to the server
    fetch(apiEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: payload
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            // Login successful, redirect to the dashboard or display a success message
            console.log('Login successful!');
        } else {
            displayError(data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        displayError('An error occurred. Please try again.');
    });
}
```
