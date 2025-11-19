"""
Generated Code Metadata:
========================
Original URL: https://abubit.com
Prompt: Write a simple HTML and CSS page that displays a "Launching Soon" message with a subscription sign-up form.
Generated: DETERMINISTIC_821756656ebacd56
Batch ID: 20250622_205537
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
    <title>Launching Soon</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Launching Soon</h1>
        <p>Sign up to be the first to know when we launch!</p>
        <form id="signup-form">
            <input type="email" id="email" placeholder="Your email address" required>
            <button type="submit">Sign Up</button>
            <p id="error-message"></p>
            <p id="success-message"></p>
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
    margin: 0;
    padding: 0;
}

.container {
    max-width: 400px;
    margin: 40px auto;
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
}

#signup-form {
    margin-top: 20px;
}

#email {
    width: 100%;
    height: 40px;
    margin-bottom: 10px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#error-message, #success-message {
    font-size: 14px;
    margin-top: 10px;
}

#error-message {
    color: #f44336;
}

#success-message {
    color: #2ecc71;
}
```

**script.js**
```javascript
// Get the form and message elements
const form = document.getElementById('signup-form');
const errorMessage = document.getElementById('error-message');
const successMessage = document.getElementById('success-message');

// Add event listener to the form
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the email input
    const emailInput = document.getElementById('email');
    const email = emailInput.value.trim();

    // Validate the email
    if (!email || !validateEmail(email)) {
        errorMessage.textContent = 'Invalid email address';
        return;
    }

    // Clear error message
    errorMessage.textContent = '';

    // Submit the email (replace with your actual submission logic)
    submitEmail(email)
        .then(() => {
            successMessage.textContent = 'Thank you for signing up!';
            emailInput.value = '';
        })
        .catch((error) => {
            errorMessage.textContent = 'Error signing up. Please try again.';
            console.error(error);
        });
});

// Validate email function
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

// Submit email function (replace with your actual submission logic)
function submitEmail(email) {
    // Example submission logic (replace with your own)
    return new Promise((resolve, reject) => {
        // Simulate a successful submission
        setTimeout(() => {
            resolve();
        }, 1000);
    });
}
```
