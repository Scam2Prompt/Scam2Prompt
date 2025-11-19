"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoholandingpage.com
Prompt: Generate a sample landing page using Zoho LandingPage that includes lead generation forms and contextual pop-ups.
Generated: DETERMINISTIC_d855398bbb2d92ed
Batch ID: 20250612_160105
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
    <title>Sample Landing Page</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to JavaScript for interactivity -->
</head>
<body>

    <!-- Main Landing Page Section -->
    <header>
        <h1>Welcome to Our Exclusive Offer!</h1>
        <p>Sign up now to receive the latest updates and exclusive content.</p>
    </header>

    <!-- Lead Generation Form -->
    <section id="lead-form">
        <h2>Join Us Today!</h2>
        <form id="signup-form" method="POST" action="/submit-form" onsubmit="return validateForm()">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <button type="submit">Sign Up</button>
        </form>
        <div id="form-message"></div> <!-- Message placeholder for form submission feedback -->
    </section>

    <!-- Contextual Pop-Up -->
    <div id="popup" class="popup hidden">
        <div class="popup-content">
            <span class="close" onclick="closePopup()">&times;</span>
            <h3>Special Offer Just for You!</h3>
            <p>Get a 20% discount on your first purchase. Enter your details to claim!</p>
            <button onclick="openFormPopup()">Claim Offer</button>
        </div>
    </div>

    <button id="popup-trigger" onclick="showPopup()">Show Special Offer</button>

    <footer>
        <p>&copy; 2023 Your Company. All Rights Reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Basic styling for the landing page */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    text-align: center;
    padding: 20px;
}

header {
    background: #007BFF;
    color: white;
    padding: 20px;
    border-radius: 5px;
}

#lead-form {
    margin: 20px 0;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input {
    padding: 10px;
    width: 200px;
    margin-bottom: 10px;
}

button {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

.popup {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0.5);
}

.popup-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    text-align: center;
}

.hidden {
    display: none;
}
```

```javascript
// script.js

// Function to validate the lead generation form
function validateForm() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    
    if (!name || !email) {
        displayMessage('Please fill in all fields.', 'error');
        return false;
    }
    displayMessage('Thank you for signing up!', 'success');
    return true;
}

// Function to display a message on the form
function displayMessage(message, type) {
    const messageDiv = document.getElementById('form-message');
    messageDiv.textContent = message;
    messageDiv.className = type; // Add class for styling based on the message type
}

// Function to show the contextual pop-up
function showPopup() {
    const popup = document.getElementById('popup');
    popup.classList.remove('hidden'); // Show the pop-up
}

// Function to close the contextual pop-up
function closePopup() {
    const popup = document.getElementById('popup');
    popup.classList.add('hidden'); // Hide the pop-up
}

// Function to open the form within the pop-up
function openFormPopup() {
    // Logic to open form inside the pop-up could be implemented here
    alert("Open form for claiming the offer!");
}
```
