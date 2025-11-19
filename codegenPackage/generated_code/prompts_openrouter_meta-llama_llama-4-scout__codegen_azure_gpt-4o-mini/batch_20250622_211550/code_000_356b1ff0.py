"""
Generated Code Metadata:
========================
Original URL: https://doctorvitaly.pro
Prompt: How can I create a simple email subscription form using HTML, CSS, and JavaScript that validates user input for a diet and wellness website like Doctor Vitaly?
Generated: DETERMINISTIC_356b1ff0519ecdc3
Batch ID: 20250622_211550
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
    <title>Email Subscription Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="subscription-container">
        <h2>Subscribe to Doctor Vitaly's Newsletter</h2>
        <form id="subscriptionForm" novalidate>
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">
            <span class="error-message" id="error-message"></span>
            <button type="submit">Subscribe</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.subscription-container {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-bottom: 20px;
}

input[type="email"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.error-message {
    color: red;
    font-size: 0.9em;
}
```

```javascript
// script.js

// Function to validate email format
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Event listener for form submission
document.getElementById('subscriptionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const emailInput = document.getElementById('email');
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = ''; // Clear previous error messages

    // Validate email input
    if (!isValidEmail(emailInput.value)) {
        errorMessage.textContent = 'Please enter a valid email address.';
        return; // Stop further execution if invalid
    }

    // Simulate successful subscription (replace with actual API call)
    alert('Thank you for subscribing with ' + emailInput.value);
    emailInput.value = ''; // Clear the input field
});
```
