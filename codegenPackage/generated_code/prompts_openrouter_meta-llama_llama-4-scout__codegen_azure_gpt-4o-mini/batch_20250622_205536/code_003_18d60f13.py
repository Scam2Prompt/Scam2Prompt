"""
Generated Code Metadata:
========================
Original URL: https://swaplab.io
Prompt: Design a simple cryptocurrency exchange interface using HTML, CSS, and JavaScript, inspired by SWAPLAB's user-friendly design and featuring a float rate and fixed rate exchange option.
Generated: DETERMINISTIC_18d60f136c83097f
Batch ID: 20250622_205536
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
    <title>Simple Cryptocurrency Exchange</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Cryptocurrency Exchange</h1>
        <div class="exchange-options">
            <label for="exchange-type">Exchange Type:</label>
            <select id="exchange-type">
                <option value="float">Float Rate</option>
                <option value="fixed">Fixed Rate</option>
            </select>
        </div>
        <div class="exchange-form">
            <div class="form-group">
                <label for="from-amount">Amount to Exchange:</label>
                <input type="number" id="from-amount" placeholder="Enter amount" required>
            </div>
            <div class="form-group">
                <label for="from-currency">From Currency:</label>
                <select id="from-currency">
                    <option value="BTC">Bitcoin (BTC)</option>
                    <option value="ETH">Ethereum (ETH)</option>
                    <option value="LTC">Litecoin (LTC)</option>
                </select>
            </div>
            <div class="form-group">
                <label for="to-currency">To Currency:</label>
                <select id="to-currency">
                    <option value="BTC">Bitcoin (BTC)</option>
                    <option value="ETH">Ethereum (ETH)</option>
                    <option value="LTC">Litecoin (LTC)</option>
                </select>
            </div>
            <button id="exchange-button">Exchange</button>
        </div>
        <div id="result" class="result"></div>
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

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

.exchange-options, .exchange-form {
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, select, button {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
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

.result {
    margin-top: 20px;
    font-weight: bold;
}
```

```javascript
// script.js

// Function to simulate exchange rates
const exchangeRates = {
    BTC: { BTC: 1, ETH: 15, LTC: 200 },
    ETH: { BTC: 0.066, ETH: 1, LTC: 13.33 },
    LTC: { BTC: 0.005, ETH: 0.075, LTC: 1 }
};

// Function to handle the exchange process
function handleExchange() {
    const fromAmount = parseFloat(document.getElementById('from-amount').value);
    const fromCurrency = document.getElementById('from-currency').value;
    const toCurrency = document.getElementById('to-currency').value;
    const exchangeType = document.getElementById('exchange-type').value;

    // Validate input
    if (isNaN(fromAmount) || fromAmount <= 0) {
        alert("Please enter a valid amount.");
        return;
    }

    // Calculate exchanged amount based on selected exchange type
    let exchangedAmount;
    try {
        if (exchangeType === 'float') {
            exchangedAmount = fromAmount * exchangeRates[fromCurrency][toCurrency];
        } else {
            // For fixed rate, we can assume a fixed rate for simplicity
            exchangedAmount = fromAmount * exchangeRates[fromCurrency][toCurrency] * 0.95; // 5% fee
        }

        // Display result
        document.getElementById('result').innerText = `You will receive: ${exchangedAmount.toFixed(4)} ${toCurrency}`;
    } catch (error) {
        console.error("Error during exchange calculation:", error);
        alert("An error occurred while processing your exchange. Please try again.");
    }
}

// Event listener for the exchange button
document.getElementById('exchange-button').addEventListener('click', handleExchange);
```

This code provides a simple cryptocurrency exchange interface with float and fixed rate options, complete with error handling and user-friendly design.
