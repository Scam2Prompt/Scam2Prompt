"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eff-omega.vercel.app
Prompt: Create HTML and CSS code for a form with fields for full name, surname, account number, and a dropdown menu for selecting a bank. Include a "Proceed" button styled to indicate a loading state when clicked.
Generated: DETERMINISTIC_5e59ca370cbb4eec
Batch ID: 20250612_150618
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
    <title>Bank Account Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="form-container">
        <form id="account-form" onsubmit="return handleSubmit(event)">
            <h2>Bank Account Information</h2>
            <label for="full-name">Full Name:</label>
            <input type="text" id="full-name" name="full-name" required>

            <label for="surname">Surname:</label>
            <input type="text" id="surname" name="surname" required>

            <label for="account-number">Account Number:</label>
            <input type="text" id="account-number" name="account-number" required pattern="\d{10}" title="10 digit account number">

            <label for="bank">Select Bank:</label>
            <select id="bank" name="bank" required>
                <option value="" disabled selected>Select your bank</option>
                <option value="bank1">Bank 1</option>
                <option value="bank2">Bank 2</option>
                <option value="bank3">Bank 3</option>
            </select>

            <button type="submit" id="proceed-button">Proceed</button>
            <div id="loading" class="loading" style="display: none;">Loading...</div>
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
    margin: 0;
    padding: 20px;
}

.form-container {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    margin: auto;
}

h2 {
    text-align: center;
}

label {
    margin-top: 10px;
    display: block;
}

input[type="text"], select {
    width: 100%;
    padding: 8px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 4px;
    background-color: #28a745;
    color: white;
    cursor: pointer;
    font-size: 16px;
}

button:disabled {
    background-color: #ccc;
}

.loading {
    margin-top: 10px;
    color: #007bff;
    text-align: center;
}
```

```javascript
// script.js

/**
 * Handles the form submission and simulates a loading state
 * @param {Event} event - The form submission event
 * @returns {boolean} - Returns false to prevent default form submission
 */
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    const proceedButton = document.getElementById('proceed-button');
    const loadingIndicator = document.getElementById('loading');

    // Disable the button to prevent multiple submissions
    proceedButton.disabled = true;
    loadingIndicator.style.display = 'block'; // Show loading state

    // Simulate form processing
    setTimeout(() => {
        // Here you would typically handle form submission (e.g., send data to server)
        console.log('Form submitted successfully');
        
        // Reset form and UI state
        proceedButton.disabled = false;
        loadingIndicator.style.display = 'none';
        document.getElementById('account-form').reset();
    }, 2000); // Simulate an API call with a delay of 2 seconds

    return false; // Prevent the default form submission behavior
}
```
