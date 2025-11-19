"""
Generated Code Metadata:
========================
Original URL: https://eff-omega.vercel.app
Prompt: Create HTML and CSS code for a form with fields for full name, surname, account number, and a dropdown menu for selecting a bank. Include a "Proceed" button styled to indicate a loading state when clicked.
Generated: DETERMINISTIC_5e59ca370cbb4eec
Batch ID: 20250612_150618
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
    <title>Bank Account Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="form-container">
        <h1>Bank Account Information</h1>
        <form id="accountForm">
            <label for="fullName">Full Name:</label>
            <input type="text" id="fullName" name="fullName" required>

            <label for="surname">Surname:</label>
            <input type="text" id="surname" name="surname" required>

            <label for="accountNumber">Account Number:</label>
            <input type="text" id="accountNumber" name="accountNumber" required pattern="\d{10}" title="Please enter a 10-digit account number.">

            <label for="bank">Select Bank:</label>
            <select id="bank" name="bank" required>
                <option value="" disabled selected>Select your bank</option>
                <option value="bank1">Bank 1</option>
                <option value="bank2">Bank 2</option>
                <option value="bank3">Bank 3</option>
            </select>

            <button type="submit" id="proceedButton">Proceed</button>
        </form>
        <div id="loadingMessage" class="hidden">Loading...</div>
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
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    margin: auto;
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select {
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
    font-size: 16px;
}

button.loading {
    background-color: #007bff;
    cursor: not-allowed;
}

.hidden {
    display: none;
}

#loadingMessage {
    text-align: center;
    margin-top: 10px;
    font-weight: bold;
}
```

```javascript
// script.js
document.getElementById('accountForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const proceedButton = document.getElementById('proceedButton');
    const loadingMessage = document.getElementById('loadingMessage');

    // Indicate loading state
    proceedButton.classList.add('loading');
    proceedButton.disabled = true; // Disable the button to prevent multiple submissions
    loadingMessage.classList.remove('hidden');

    // Simulate form submission (replace with actual submission logic)
    setTimeout(() => {
        // Reset loading state
        proceedButton.classList.remove('loading');
        proceedButton.disabled = false;
        loadingMessage.classList.add('hidden');

        // Here you can handle the form data (e.g., send it to a server)
        alert('Form submitted successfully!');
    }, 2000); // Simulate a 2-second loading time
});
```
