"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socrates-gm.com
Prompt: Generate code in JavaScript to implement a form for resetting the username and password on the Socrates GM portal, including email validation and security question prompts.
Generated: DETERMINISTIC_ebcd82ed153fc872
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to implement a form for resetting username and password on the Socrates GM portal.

// Function to validate email format using a regular expression
function isValidEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get form values
    const email = document.getElementById('email').value.trim();
    const securityQuestion = document.getElementById('security-question').value.trim();
    const newPassword = document.getElementById('password').value.trim();

    // Validate email
    if (!isValidEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Validate security question
    if (securityQuestion.length === 0) {
        alert('Please answer the security question.');
        return;
    }

    // Validate password
    if (newPassword.length < 8) {
        alert('Password must be at least 8 characters long.');
        return;
    }

    // Create a data object to send to the server
    const data = {
        email: email,
        securityQuestion: securityQuestion,
        newPassword: newPassword
    };

    // Simulated API request to reset the username and password
    fetch('/api/reset-credentials', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to reset credentials. Please try again.');
            }
            return response.json();
        })
        .then(data => {
            // Handle successful response
            alert('Username and password reset successfully! Please check your email for confirmation.');
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
            alert('An error occurred: ' + error.message);
        });
}

// Document ready function to set up event listeners after the DOM has loaded
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('reset-form');
    form.addEventListener('submit', handleFormSubmit);
});
```

```html
<!-- HTML form for resetting username and password -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Credentials - Socrates GM Portal</title>
    <script src="reset-credentials.js" defer></script> <!-- Link to the JavaScript file -->
</head>
<body>
    <h1>Reset Username and Password</h1>
    <form id="reset-form">
        <label for="email">Email:</label>
        <input type="email" id="email" required>
        
        <label for="security-question">Security Question Answer:</label>
        <input type="text" id="security-question" required>
        
        <label for="password">New Password:</label>
        <input type="password" id="password" required>
        
        <button type="submit">Reset Credentials</button>
    </form>
</body>
</html>
```
