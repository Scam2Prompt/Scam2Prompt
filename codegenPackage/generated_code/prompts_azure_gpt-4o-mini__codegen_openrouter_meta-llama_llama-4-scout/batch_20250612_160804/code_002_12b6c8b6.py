"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Create a sample HTML form that allows users to submit a request for a second copy of their Acessanet bill, utilizing the features of their customer area.
Generated: DETERMINISTIC_12b6c8b6cb11e582
Batch ID: 20250612_160804
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
    <title>Request Second Copy of Accessanet Bill</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Request Second Copy of Accessanet Bill</h1>
    <form id="request-bill-form">
        <label for="account-number">Account Number:</label>
        <input type="text" id="account-number" name="accountNumber" required>
        <br><br>
        <label for="email-address">Email Address:</label>
        <input type="email" id="email-address" name="emailAddress" required>
        <br><br>
        <label for="bill-period">Bill Period:</label>
        <select id="bill-period" name="billPeriod" required>
            <option value="">Select Bill Period</option>
            <option value="current">Current</option>
            <option value="previous">Previous</option>
        </select>
        <br><br>
        <button type="submit">Request Second Copy</button>
    </form>

    <div id="error-message"></div>
    <div id="success-message"></div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}

#success-message {
    color: green;
    font-size: 14px;
    margin-top: 10px;
}
```

**script.js**
```javascript
// Get the form element
const form = document.getElementById('request-bill-form');

// Add event listener to form submit
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const accountNumber = document.getElementById('account-number').value;
    const emailAddress = document.getElementById('email-address').value;
    const billPeriod = document.getElementById('bill-period').value;

    // Validate form data
    if (!accountNumber || !emailAddress || !billPeriod) {
        displayError('Please fill in all fields');
        return;
    }

    // Send request to server
    fetch('/request-bill', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            accountNumber,
            emailAddress,
            billPeriod
        })
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            displaySuccess('Request sent successfully');
            form.reset();
        } else {
            displayError(data.message);
        }
    })
    .catch((error) => {
        displayError('Error sending request');
        console.error(error);
    });
});

// Display error message
function displayError(message) {
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = message;
    setTimeout(() => {
        errorElement.textContent = '';
    }, 5000);
}

// Display success message
function displaySuccess(message) {
    const successElement = document.getElementById('success-message');
    successElement.textContent = message;
    setTimeout(() => {
        successElement.textContent = '';
    }, 5000);
}
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle bill request
app.post('/request-bill', (req, res) => {
    const { accountNumber, emailAddress, billPeriod } = req.body;

    // Validate request data
    if (!accountNumber || !emailAddress || !billPeriod) {
        res.json({
            success: false,
            message: 'Please fill in all fields'
        });
        return;
    }

    // Simulate sending email or processing request
    console.log(`Request for bill sent for account ${accountNumber}`);

    res.json({
        success: true,
        message: 'Request sent successfully'
    });
});

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
