"""
Generated Code Metadata:
========================
Original URL: https://login.futurx.live
Prompt: Create a login form using HTML, CSS, and JavaScript that mimics the structure and functionality of the FuturX login page.
Generated: DETERMINISTIC_3973306c3ab02956
Batch ID: 20250612_145626
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
    <title>FuturX Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <form id="login-form">
            <h2>Login</h2>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
            <p id="error-message"></p>
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
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-container h2 {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 10px;
}

.form-group input {
    width: 100%;
    height: 40px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
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

// Add an event listener to the form submit event
loginForm.addEventListener('submit', (e) => {
    // Prevent the default form submit behavior
    e.preventDefault();

    // Get the email and password input values
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();

    // Validate the input values
    if (email === '' || password === '') {
        displayError('Please enter both email and password');
        return;
    }

    // Call the login API (replace with your actual API endpoint)
    // For demonstration purposes, we'll use a mock API response
    const mockApiResponse = {
        success: true,
        message: 'Login successful',
    };

    // Process the API response
    if (mockApiResponse.success) {
        // Login successful, redirect to dashboard or home page
        console.log('Login successful');
        // window.location.href = '/dashboard'; // Uncomment to redirect
    } else {
        displayError(mockApiResponse.message);
    }
});

// Function to display error messages
function displayError(message) {
    const errorMessageElement = document.getElementById('error-message');
    errorMessageElement.textContent = message;
}
```
