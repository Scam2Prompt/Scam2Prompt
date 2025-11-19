"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paywithcrypto.pages.dev
Prompt: Write a code snippet to create a manual payment instruction page that includes wallet address and amount fields as seen on Pay With Crypto.
Generated: DETERMINISTIC_4980385393b634aa
Batch ID: 20250612_140007
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
    <title>Manual Payment Instruction</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
    <script src="script.js" defer></script> <!-- Link to your JavaScript file -->
</head>
<body>
    <div class="container">
        <h1>Manual Payment Instruction</h1>
        <form id="payment-form">
            <div class="form-group">
                <label for="wallet-address">Wallet Address:</label>
                <input type="text" id="wallet-address" name="wallet-address" required placeholder="Enter your wallet address">
            </div>
            <div class="form-group">
                <label for="amount">Amount:</label>
                <input type="number" id="amount" name="amount" required placeholder="Enter amount in crypto" min="0" step="any">
            </div>
            <button type="submit">Submit Payment</button>
        </form>
        <div id="message" class="message"></div> <!-- Area to display messages to the user -->
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

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 15px;
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
    font-weight: bold;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve input values
    const walletAddress = document.getElementById('wallet-address').value;
    const amount = parseFloat(document.getElementById('amount').value);
    const messageDiv = document.getElementById('message');

    // Basic validation for wallet address and amount
    if (!walletAddress || !amount || amount <= 0) {
        messageDiv.textContent = "Please provide a valid wallet address and amount.";
        messageDiv.style.color = "red";
        return; // Exit if validation fails
    }

    // Display success message
    messageDiv.textContent = `Payment instruction created: ${amount} to ${walletAddress}`;
    messageDiv.style.color = "green";

    // Additional processing can be done here (e.g. sending data to a server)
    // Example: sendPaymentInstruction(walletAddress, amount);
});

// Placeholder function for future backend integration
// async function sendPaymentInstruction(walletAddress, amount) {
//     try {
//         const response = await fetch('/api/payment', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ walletAddress, amount }),
//         });
//         if (!response.ok) throw new Error('Network response was not ok');
//         const data = await response.json();
//         // Handle success data
//     } catch (error) {
//         console.error('Error in sending payment instruction:', error);
//     }
// }
```
