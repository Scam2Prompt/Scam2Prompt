"""
Generated Code Metadata:
========================
Original URL: https://solvexswap.pages.dev
Prompt: Design a simple token swap interface with HTML, CSS, and JavaScript, inspired by the Solvex Swap "Enter amount to swap" feature.
Generated: DETERMINISTIC_fb9b10b687f13829
Batch ID: 20250622_211721
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
    <title>Token Swap Interface</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="swap-container">
        <h2>Token Swap</h2>
        <form id="swap-form">
            <div class="input-group">
                <label for="from-amount">From:</label>
                <input type="number" id="from-amount" step="0.01">
                <select id="from-token">
                    <option value="token1">Token 1</option>
                    <option value="token2">Token 2</option>
                </select>
            </div>
            <div class="input-group">
                <label for="to-amount">To:</label>
                <input type="number" id="to-amount" step="0.01" disabled>
                <select id="to-token">
                    <option value="token2">Token 2</option>
                    <option value="token1">Token 1</option>
                </select>
            </div>
            <button id="swap-button">Swap</button>
        </form>
        <p id="swap-details"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
.swap-container {
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.input-group {
    margin-bottom: 20px;
}

.input-group label {
    display: block;
    margin-bottom: 10px;
}

.input-group input[type="number"] {
    width: 100%;
    height: 40px;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
}

.input-group select {
    width: 100%;
    height: 40px;
    padding: 10px;
    border: 1px solid #ccc;
}

#swap-button {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#swap-button:hover {
    background-color: #3e8e41;
}

#swap-details {
    margin-top: 20px;
    font-size: 14px;
    color: #666;
}
```

**script.js**
```javascript
// Get elements
const fromAmountInput = document.getElementById('from-amount');
const fromTokenSelect = document.getElementById('from-token');
const toAmountInput = document.getElementById('to-amount');
const toTokenSelect = document.getElementById('to-token');
const swapButton = document.getElementById('swap-button');
const swapForm = document.getElementById('swap-form');
const swapDetails = document.getElementById('swap-details');

// Token swap rates (mock data)
const tokenSwapRates = {
    token1: {
        token2: 0.5,
    },
    token2: {
        token1: 1.5,
    },
};

// Function to calculate swap amount
function calculateSwapAmount(fromAmount, fromToken, toToken) {
    if (!fromAmount || !fromToken || !toToken) return '';

    const swapRate = tokenSwapRates[fromToken][toToken];
    if (!swapRate) return '';

    const toAmount = fromAmount * swapRate;
    return toAmount.toFixed(2);
}

// Event listeners
fromAmountInput.addEventListener('input', () => {
    const fromAmount = parseFloat(fromAmountInput.value);
    const fromToken = fromTokenSelect.value;
    const toToken = toTokenSelect.value;

    const toAmount = calculateSwapAmount(fromAmount, fromToken, toToken);
    toAmountInput.value = toAmount || '';
});

fromTokenSelect.addEventListener('change', () => {
    const fromAmount = parseFloat(fromAmountInput.value);
    const fromToken = fromTokenSelect.value;
    const toToken = toTokenSelect.value;

    const toAmount = calculateSwapAmount(fromAmount, fromToken, toToken);
    toAmountInput.value = toAmount || '';
});

toTokenSelect.addEventListener('change', () => {
    const fromAmount = parseFloat(fromAmountInput.value);
    const fromToken = fromTokenSelect.value;
    const toToken = toTokenSelect.value;

    const toAmount = calculateSwapAmount(fromAmount, fromToken, toToken);
    toAmountInput.value = toAmount || '';
});

swapButton.addEventListener('click', (e) => {
    e.preventDefault();

    try {
        const fromAmount = parseFloat(fromAmountInput.value);
        const fromToken = fromTokenSelect.value;
        const toToken = toTokenSelect.value;

        if (!fromAmount || !fromToken || !toToken) {
            throw new Error('Please fill in all fields');
        }

        // Perform swap logic here
        swapDetails.textContent = `Swapping ${fromAmount} ${fromToken} for ${toAmountInput.value} ${toToken}`;
    } catch (error) {
        swapDetails.textContent = error.message;
    }
});
```
