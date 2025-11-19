"""
Generated Code Metadata:
========================
Original URL: https://geamini-looggoiinn.godaddysites.com
Prompt: Generate a basic HTML and CSS code snippet for a login page inspired by the design of Gemini's login page.
Generated: DETERMINISTIC_80f2135ef07351af
Batch ID: 20250622_212609
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
    <title>Login Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <form class="login-form" id="loginForm" action="/login" method="POST">
            <h1>Login</h1>
            <div class="input-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Log In</button>
            <div class="error-message" id="errorMessage"></div>
        </form>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Full height and width for body */
body {
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f5f5f5; /* Light background color */
    font-family: Arial, sans-serif; /* Font style */
}

/* Container for the login form */
.container {
    background-color: #ffffff; /* White background for the form */
    padding: 2rem; /* Padding around the form */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Subtle shadow */
}

/* Styling for the form title */
h1 {
    margin-bottom: 1.5rem; /* Space below the title */
    color: #333; /* Dark text color */
}

/* Input group styling */
.input-group {
    margin-bottom: 1rem; /* Space between input groups */
}

/* Label styling */
label {
    display: block; /* Block display for labels */
    margin-bottom: 0.5rem; /* Space below labels */
    color: #555; /* Medium gray text color */
}

/* Input field styling */
input {
    width: 100%; /* Full width */
    padding: 0.5rem; /* Padding inside input */
    border: 1px solid #ccc; /* Light gray border */
    border-radius: 4px; /* Rounded corners */
}

/* Button styling */
button {
    width: 100%; /* Full width */
    padding: 0.5rem; /* Padding inside button */
    background-color: #007bff; /* Primary button color */
    color: white; /* White text color */
    border: none; /* No border */
    border-radius: 4px; /* Rounded corners */
    cursor: pointer; /* Pointer cursor on hover */
    font-size: 1rem; /* Font size */
}

/* Button hover effect */
button:hover {
    background-color: #0056b3; /* Darker blue on hover */
}

/* Error message styling */
.error-message {
    color: red; /* Red text for error messages */
    margin-top: 1rem; /* Space above error message */
    display: none; /* Hidden by default */
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Basic validation (could be expanded)
    if (username === '' || password === '') {
        showError('Please fill in all fields.');
        return;
    }

    // Simulate a login request (replace with actual API call)
    fakeLogin(username, password)
        .then(response => {
            if (response.success) {
                // Redirect on successful login
                window.location.href = '/dashboard';
            } else {
                showError(response.message);
            }
        })
        .catch(error => {
            showError('An error occurred. Please try again later.');
            console.error('Login error:', error);
        });
});

// Function to simulate a login request
function fakeLogin(username, password) {
    return new Promise((resolve) => {
        setTimeout(() => {
            // Simulate success or failure
            if (username === 'user' && password === 'pass') {
                resolve({ success: true });
            } else {
                resolve({ success: false, message: 'Invalid username or password.' });
            }
        }, 1000);
    });
}

// Function to display error messages
function showError(message) {
    const errorMessageElement = document.getElementById('errorMessage');
    errorMessageElement.textContent = message;
    errorMessageElement.style.display = 'block'; // Show error message
}
```
