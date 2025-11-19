"""
Generated Code Metadata:
========================
Original URL: https://www.crediblebd.net
Prompt: Create a front-end form using HTML and JavaScript that allows users to request a quote for LED panel lights from Credible BD, capturing necessary specifications.
Generated: DETERMINISTIC_130f966e9ac11a64
Batch ID: 20250612_161331
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
    <title>LED Panel Lights Quote Request</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript for functionality -->
</head>
<body>
    <div class="container">
        <h1>Request a Quote for LED Panel Lights</h1>
        <form id="quoteForm">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>

            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity" min="1" required>

            <label for="dimensions">Dimensions (in mm):</label>
            <input type="text" id="dimensions" name="dimensions" placeholder="e.g., 600x600" required>

            <label for="colorTemperature">Color Temperature:</label>
            <select id="colorTemperature" name="colorTemperature" required>
                <option value="">Select...</option>
                <option value="3000K">3000K (Warm White)</option>
                <option value="4000K">4000K (Neutral White)</option>
                <option value="6000K">6000K (Cool White)</option>
            </select>

            <label for="additionalNotes">Additional Notes:</label>
            <textarea id="additionalNotes" name="additionalNotes" rows="4"></textarea>

            <button type="submit">Request Quote</button>
        </form>
        <div id="responseMessage" class="hidden"></div> <!-- Message display area -->
    </div>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.hidden {
    display: none;
}

.success {
    color: green;
}

.error {
    color: red;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('quoteForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        quantity: document.getElementById('quantity').value,
        dimensions: document.getElementById('dimensions').value,
        colorTemperature: document.getElementById('colorTemperature').value,
        additionalNotes: document.getElementById('additionalNotes').value
    };

    // Validate email format
    if (!validateEmail(formData.email)) {
        displayMessage('Please enter a valid email address.', 'error');
        return;
    }

    // Simulate sending data to the server
    sendQuoteRequest(formData);
});

// Function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

// Function to simulate sending quote request
function sendQuoteRequest(data) {
    // Simulate a successful response after 1 second
    setTimeout(() => {
        displayMessage('Your quote request has been submitted successfully!', 'success');
        document.getElementById('quoteForm').reset(); // Reset the form
    }, 1000);
}

// Function to display messages to the user
function displayMessage(message, type) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.textContent = message;
    responseMessage.className = type; // Set class for styling
    responseMessage.classList.remove('hidden'); // Show the message
}
```
