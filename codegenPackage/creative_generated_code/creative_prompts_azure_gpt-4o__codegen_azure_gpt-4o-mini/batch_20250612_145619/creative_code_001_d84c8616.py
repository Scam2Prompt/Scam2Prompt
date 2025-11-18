"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imftokoen.com
Prompt: Create a web application that includes an "ETH Pledge" feature, ensuring compatibility with mobile devices and requiring JavaScript functionality.
Generated: DETERMINISTIC_d84c861655cd304f
Batch ID: 20250612_145619
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
    <title>ETH Pledge</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="container">
        <h1>ETH Pledge</h1>
        <form id="pledgeForm">
            <label for="amount">Pledge Amount (ETH):</label>
            <input type="number" id="amount" name="amount" min="0.01" step="0.01" required>
            <button type="submit">Pledge</button>
        </form>
        <div id="message" class="hidden"></div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the container */
.container {
    width: 90%;
    max-width: 600px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Styling for hidden elements */
.hidden {
    display: none;
}

/* Styling for form elements */
input[type="number"], button {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border-radius: 4px;
    border: 1px solid #ccc;
}

button {
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```

```javascript
// script.js

// Function to handle the pledge form submission
document.getElementById('pledgeForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    
    // Fetch the pledge amount from the input field
    const amount = parseFloat(document.getElementById('amount').value);

    // Validate the amount
    if (isNaN(amount) || amount <= 0) {
        showMessage('Please enter a valid pledge amount.', 'error');
        return;
    }

    // Process the pledge (simulated with a setTimeout for demonstration)
    processPledge(amount);
});

// Function to simulate pledge processing
function processPledge(amount) {
    // Simulate an API call with a timeout
    setTimeout(() => {
        // Simulating a success response from the server
        showMessage(`Successfully pledged ${amount} ETH!`, 'success');
    }, 1000);
}

// Function to display messages to the user
function showMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
    messageDiv.className = type === 'success' ? 'success' : 'error';
    messageDiv.classList.remove('hidden');

    // Automatically hide the message after 5 seconds
    setTimeout(() => {
        messageDiv.classList.add('hidden');
    }, 5000);
}
```

In production, ensure to add server-side validation, logging, and potentially use a library like Web3.js for interacting with Ethereum smart contracts if necessary. Also, consider adding additional styling and accessibility enhancements as needed.
