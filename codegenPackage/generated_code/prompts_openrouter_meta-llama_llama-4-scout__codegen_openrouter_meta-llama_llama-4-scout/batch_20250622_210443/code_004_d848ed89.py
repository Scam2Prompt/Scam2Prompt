"""
Generated Code Metadata:
========================
Original URL: https://ututu.pages.dev
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display a token presale interface, including a buy button and rate information, inspired by the $SHROOM presale page.
Generated: DETERMINISTIC_d848ed890b3a65cb
Batch ID: 20250622_210443
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
    <title>Token Presale</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Token Presale</h1>
        <div class="rate-info">
            <p>1 ETH = 1000 SHROOM</p>
            <p>Presale Rate: $0.10 per SHROOM</p>
        </div>
        <div class="buy-section">
            <input id="amount" type="number" placeholder="Enter amount (ETH)">
            <button id="buy-button">Buy SHROOM</button>
            <p id="error-message"></p>
            <p id="success-message"></p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.rate-info {
    margin-bottom: 20px;
}

.buy-section {
    margin-top: 20px;
}

#amount {
    width: 100%;
    height: 40px;
    margin-bottom: 10px;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
}

#buy-button {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#buy-button:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
}

#success-message {
    color: green;
}
```

**script.js**
```javascript
// Get elements
const buyButton = document.getElementById('buy-button');
const amountInput = document.getElementById('amount');
const errorMessage = document.getElementById('error-message');
const successMessage = document.getElementById('success-message');

// Set rate information
const rate = 1000; // 1 ETH = 1000 SHROOM
const presaleRate = 0.10; // $0.10 per SHROOM

// Add event listener to buy button
buyButton.addEventListener('click', async () => {
    try {
        // Get amount from input
        const amount = parseFloat(amountInput.value);

        // Validate input
        if (isNaN(amount) || amount <= 0) {
            throw new Error('Invalid amount');
        }

        // Calculate SHROOM amount
        const shroomAmount = amount * rate;

        // Simulate buy logic (replace with actual implementation)
        // For demonstration purposes, assume a successful transaction
        // In a real-world scenario, integrate with a blockchain or payment gateway
        console.log(`Buying ${shroomAmount} SHROOM for ${amount} ETH`);

        // Display success message
        successMessage.textContent = `Successfully bought ${shroomAmount} SHROOM`;
        errorMessage.textContent = '';
    } catch (error) {
        // Display error message
        errorMessage.textContent = error.message;
        successMessage.textContent = '';
    }
});
```
