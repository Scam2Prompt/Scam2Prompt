"""
Generated Code Metadata:
========================
Original URL: https://asd-col.pages.dev
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display a token presale interface, including a "BUY" button and ETH deposit options.
Generated: DETERMINISTIC_916ec6c93f8fdf6a
Batch ID: 20250622_210803
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
    <title>Token Presale Interface</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Token Presale</h1>
        <p>Purchase your tokens in the presale!</p>
        
        <label for="ethAmount">Enter ETH Amount:</label>
        <input type="number" id="ethAmount" placeholder="0.0" min="0" step="0.01" required>
        
        <button id="buyButton">BUY</button>
        
        <div id="message" class="message"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

input {
    margin: 10px 0;
    padding: 10px;
    width: 80%;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 20px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.message {
    margin-top: 20px;
    font-size: 1.2em;
}
```

```javascript
// script.js

// Function to handle the buy button click event
document.getElementById('buyButton').addEventListener('click', function() {
    // Get the ETH amount from the input field
    const ethAmount = parseFloat(document.getElementById('ethAmount').value);
    
    // Validate the ETH amount
    if (isNaN(ethAmount) || ethAmount <= 0) {
        displayMessage('Please enter a valid ETH amount.', 'error');
        return;
    }

    // Simulate a purchase process (replace with actual purchase logic)
    try {
        // Placeholder for actual purchase logic
        // e.g., call to a smart contract function to buy tokens
        console.log(`Purchasing tokens with ${ethAmount} ETH...`);
        
        // Display success message
        displayMessage(`Successfully purchased tokens with ${ethAmount} ETH!`, 'success');
    } catch (error) {
        // Handle any errors that occur during the purchase process
        console.error('Error during purchase:', error);
        displayMessage('An error occurred during the purchase. Please try again.', 'error');
    }
});

// Function to display messages to the user
function displayMessage(message, type) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
    messageDiv.className = type === 'error' ? 'message error' : 'message success';
}
```
