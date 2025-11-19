"""
Generated Code Metadata:
========================
Original URL: https://oberbank-ag.myfreesites.net
Prompt: Design a user interface for a prize claim page that includes a button for winners to submit their addresses, inspired by the layout of the Oberbank AG website.
Generated: DETERMINISTIC_b95dec1eae43d5f2
Batch ID: 20250612_163924
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
    <title>Prize Claim Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript for functionality -->
</head>
<body>
    <header>
        <h1>Claim Your Prize</h1>
        <p>Congratulations on winning! Please submit your address to claim your prize.</p>
    </header>
    
    <main>
        <form id="claimForm" onsubmit="return handleSubmit(event)">
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="address">Address:</label>
                <textarea id="address" name="address" required></textarea>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <button type="submit">Submit Address</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- Message display area -->
    </main>

    <footer>
        <p>&copy; 2023 Prize Claim. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
body, h1, p, form {
    margin: 0;
    padding: 0;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background-color: #0072B8; /* Oberbank AG color */
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main content styling */
main {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Form group styling */
.form-group {
    margin-bottom: 15px;
}

/* Button styling */
button {
    background-color: #0072B8; /* Oberbank AG color */
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #005f8a; /* Darker shade for hover effect */
}

/* Response message styling */
.hidden {
    display: none;
}

#responseMessage {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #0072B8;
    border-radius: 5px;
    background-color: #e7f3fe;
    color: #31708f;
}
```

```javascript
// script.js

/**
 * Handles the form submission for the prize claim.
 * @param {Event} event - The form submission event.
 * @returns {boolean} - Returns false to prevent default form submission.
 */
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    const name = document.getElementById('name').value;
    const address = document.getElementById('address').value;
    const email = document.getElementById('email').value;

    // Validate form data (basic validation)
    if (!name || !address || !email) {
        displayMessage('Please fill in all fields.', 'error');
        return false;
    }

    // Simulate an API call to submit the address
    submitAddress({ name, address, email })
        .then(response => {
            displayMessage('Your address has been submitted successfully!', 'success');
        })
        .catch(error => {
            console.error('Error submitting address:', error);
            displayMessage('There was an error submitting your address. Please try again later.', 'error');
        });

    return false; // Prevent default form submission
}

/**
 * Simulates an API call to submit the address.
 * @param {Object} data - The data to submit.
 * @returns {Promise} - A promise that resolves or rejects based on the simulated API response.
 */
function submitAddress(data) {
    return new Promise((resolve, reject) => {
        // Simulate a successful submission after 1 second
        setTimeout(() => {
            // Randomly simulate success or failure
            Math.random() > 0.2 ? resolve() : reject(new Error('Submission failed'));
        }, 1000);
    });
}

/**
 * Displays a message to the user.
 * @param {string} message - The message to display.
 * @param {string} type - The type of message ('success' or 'error').
 */
function displayMessage(message, type) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.textContent = message;
    responseMessage.className = type === 'success' ? '' : 'error';
    responseMessage.classList.remove('hidden');
}
```
