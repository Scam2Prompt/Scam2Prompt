"""
Generated Code Metadata:
========================
Original URL: https://webmail.consesys.io
Prompt: Write a script to log users out of a webmail system and display a confirmation message, similar to the logout functionality described on https://webmail.consesys.io.
Generated: DETERMINISTIC_e7c0ac282d05897f
Batch ID: 20250612_150329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// logout.js

// Function to log the user out of the webmail system
async function logoutUser() {
    try {
        // Send a request to the server to log out the user
        const response = await fetch('/api/logout', {
            method: 'POST',
            credentials: 'include', // Include cookies for session management
        });

        // Check if the response is successful
        if (!response.ok) {
            throw new Error('Logout failed. Please try again.');
        }

        // Parse the response to JSON
        const data = await response.json();

        // Display a confirmation message to the user
        displayConfirmationMessage(data.message);
        
        // Optionally, redirect the user to the login page after logout
        setTimeout(() => {
            window.location.href = '/login';
        }, 2000); // Redirect after 2 seconds

    } catch (error) {
        // Handle any errors that occurred during the logout process
        console.error('Error during logout:', error);
        displayErrorMessage(error.message);
    }
}

// Function to display a confirmation message
function displayConfirmationMessage(message) {
    const confirmationDiv = document.createElement('div');
    confirmationDiv.className = 'confirmation-message';
    confirmationDiv.innerText = message;
    document.body.appendChild(confirmationDiv);

    // Style the confirmation message
    confirmationDiv.style.position = 'fixed';
    confirmationDiv.style.top = '20px';
    confirmationDiv.style.right = '20px';
    confirmationDiv.style.backgroundColor = '#4CAF50';
    confirmationDiv.style.color = 'white';
    confirmationDiv.style.padding = '10px';
    confirmationDiv.style.borderRadius = '5px';
}

// Function to display an error message
function displayErrorMessage(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.innerText = message;
    document.body.appendChild(errorDiv);

    // Style the error message
    errorDiv.style.position = 'fixed';
    errorDiv.style.top = '20px';
    errorDiv.style.right = '20px';
    errorDiv.style.backgroundColor = '#f44336';
    errorDiv.style.color = 'white';
    errorDiv.style.padding = '10px';
    errorDiv.style.borderRadius = '5px';
}

// Event listener for the logout button
document.getElementById('logoutButton').addEventListener('click', logoutUser);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webmail Logout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <button id="logoutButton">Logout</button>
    <script src="logout.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for confirmation and error messages */
.confirmation-message, .error-message {
    transition: opacity 0.5s ease;
    opacity: 1;
}

.confirmation-message {
    opacity: 1;
}

.error-message {
    opacity: 1;
}
```
