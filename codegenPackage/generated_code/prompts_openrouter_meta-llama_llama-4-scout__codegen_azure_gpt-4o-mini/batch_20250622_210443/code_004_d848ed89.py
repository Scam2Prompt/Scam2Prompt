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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$SHROOM Token Presale</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>$SHROOM Token Presale</h1>
            <p>Join the presale and be part of the $SHROOM community!</p>
        </header>
        <main>
            <section class="rate-info">
                <h2>Current Rate</h2>
                <p id="rate">1 ETH = 1000 $SHROOM</p>
            </section>
            <section class="buy-section">
                <h2>Buy $SHROOM Tokens</h2>
                <label for="ethAmount">Amount in ETH:</label>
                <input type="number" id="ethAmount" placeholder="Enter ETH amount" min="0" step="0.01">
                <button id="buyButton">Buy Now</button>
                <p id="message" class="message"></p>
            </section>
        </main>
        <footer>
            <p>&copy; 2023 $SHROOM. All rights reserved.</p>
        </footer>
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

/* Body styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Container styles */
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Header styles */
header {
    text-align: center;
    margin-bottom: 20px;
}

/* Rate info styles */
.rate-info {
    margin-bottom: 20px;
}

/* Buy section styles */
.buy-section {
    margin-bottom: 20px;
}

/* Button styles */
button {
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

/* Message styles */
.message {
    margin-top: 10px;
    font-weight: bold;
}
```

```javascript
// script.js

// Function to handle the buy button click event
document.getElementById('buyButton').addEventListener('click', function() {
    // Get the amount of ETH from the input field
    const ethAmount = parseFloat(document.getElementById('ethAmount').value);
    const messageElement = document.getElementById('message');

    // Validate the input
    if (isNaN(ethAmount) || ethAmount <= 0) {
        messageElement.textContent = 'Please enter a valid amount of ETH.';
        messageElement.style.color = 'red';
        return;
    }

    // Calculate the number of $SHROOM tokens to buy
    const rate = 1000; // 1 ETH = 1000 $SHROOM
    const tokensToBuy = ethAmount * rate;

    // Simulate a purchase process (this would be replaced with actual transaction logic)
    try {
        // Here you would typically call a function to handle the transaction
        // For demonstration, we will just show a success message
        messageElement.textContent = `You have successfully purchased ${tokensToBuy} $SHROOM tokens!`;
        messageElement.style.color = 'green';
    } catch (error) {
        // Handle any errors that may occur during the purchase process
        messageElement.textContent = 'An error occurred while processing your purchase. Please try again.';
        messageElement.style.color = 'red';
        console.error('Purchase error:', error);
    }
});
```
