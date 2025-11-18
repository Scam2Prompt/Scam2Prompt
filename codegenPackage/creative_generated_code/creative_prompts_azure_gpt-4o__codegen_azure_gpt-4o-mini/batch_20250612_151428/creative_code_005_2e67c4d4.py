"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Develop a web form in HTML and JavaScript for scheduling a viewing session of replica weapons, as encouraged by Powered Production Film Services.
Generated: DETERMINISTIC_2e67c4d4fae3dfc6
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Viewing Session Scheduler</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Schedule Your Viewing Session</h1>
    </header>
    <main>
        <form id="viewingSessionForm">
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="date">Preferred Date:</label>
                <input type="date" id="date" name="date" required>
            </div>
            <div class="form-group">
                <label for="time">Preferred Time:</label>
                <input type="time" id="time" name="time" required>
            </div>
            <button type="submit">Schedule Viewing</button>
        </form>
        <div id="confirmationMessage" class="hidden"></div>
    </main>
    <footer>
        <p>&copy; 2023 Powered Production Film Services</p>
    </footer>
</body>
</html>
```

```javascript
// script.js

/**
 * Handles the form submission for scheduling a viewing session.
 * @param {Event} event - The form submission event.
 */
function handleFormSubmission(event) {
    event.preventDefault(); // Prevent the default form submission

    // Retrieve form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Validate form data
    if (!validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Create confirmation message
    const confirmationMessage = `
        Thank you, ${name}! Your viewing session has been scheduled for 
        ${date} at ${time}. We will send a confirmation to ${email}.
    `;
    
    // Display the confirmation message
    const confirmationDiv = document.getElementById('confirmationMessage');
    confirmationDiv.innerText = confirmationMessage;
    confirmationDiv.classList.remove('hidden');
    
    // Reset the form
    document.getElementById('viewingSessionForm').reset();
}

/**
 * Validates the email format using a regular expression.
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if the email is valid, otherwise false.
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Event listener for form submission
document.getElementById('viewingSessionForm').addEventListener('submit', handleFormSubmission);
```

```css
/* styles.css */

/* Basic styling for the form and layout */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f5f5f5;
    color: #333;
}

header, footer {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.hidden {
    display: none;
}
```
