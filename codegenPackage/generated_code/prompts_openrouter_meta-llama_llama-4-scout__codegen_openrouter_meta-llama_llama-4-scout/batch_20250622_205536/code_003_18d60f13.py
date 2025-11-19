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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cryptocurrency Exchange Interface</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Cryptocurrency Exchange</h1>
        <div class="exchange-options">
            <button id="float-rate-btn" class="active">Float Rate</button>
            <button id="fixed-rate-btn">Fixed Rate</button>
        </div>
        <div class="exchange-interface">
            <div class="from-section">
                <label for="from-amount">From:</label>
                <input type="number" id="from-amount" placeholder="0.0">
                <select id="from-currency">
                    <option value="BTC">BTC</option>
                    <option value="ETH">ETH</option>
                    <option value="LTC">LTC</option>
                </select>
            </div>
            <div class="to-section">
                <label for="to-amount">To:</label>
                <input type="number" id="to-amount" placeholder="0.0" disabled>
                <select id="to-currency">
                    <option value="BTC">BTC</option>
                    <option value="ETH">ETH</option>
                    <option value="LTC">LTC</option>
                </select>
            </div>
            <button id="swap-btn">Swap</button>
            <p id="exchange-rate"></p>
            <p id="error-message"></p>
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
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.exchange-options {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #4CAF50;
    color: #fff;
    cursor: pointer;
}

button.active {
    background-color: #3e8e41;
}

button:hover {
    background-color: #3e8e41;
}

.exchange-interface {
    display: flex;
    flex-direction: column;
}

.from-section, .to-section {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

label {
    margin-right: 10px;
}

input[type="number"] {
    width: 100px;
    height: 30px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

select {
    width: 100px;
    height: 30px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-left: 10px;
}

#swap-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #4CAF50;
    color: #fff;
    cursor: pointer;
}

#error-message {
    color: red;
}
```

**script.js**
```javascript
// Define exchange rates (sample data)
const exchangeRates = {
    BTC: {
        ETH: 10.5,
        LTC: 50.2
    },
    ETH: {
        BTC: 0.095,
        LTC: 4.8
    },
    LTC: {
        BTC: 0.02,
        ETH: 0.21
    }
};

// Get elements
const floatRateBtn = document.getElementById('float-rate-btn');
const fixedRateBtn = document.getElementById('fixed-rate-btn');
const fromAmountInput = document.getElementById('from-amount');
const fromCurrencySelect = document.getElementById('from-currency');
const toAmountInput = document.getElementById('to-amount');
const toCurrencySelect = document.getElementById('to-currency');
const swapBtn = document.getElementById('swap-btn');
const exchangeRateElement = document.getElementById('exchange-rate');
const errorMessageElement = document.getElementById('error-message');

// Set initial state
let exchangeType = 'float';
let fromCurrency = fromCurrencySelect.value;
let toCurrency = toCurrencySelect.value;

// Add event listeners
floatRateBtn.addEventListener('click', () => {
    exchangeType = 'float';
    floatRateBtn.classList.add('active');
    fixedRateBtn.classList.remove('active');
    updateExchangeRate();
});

fixedRateBtn.addEventListener('click', () => {
    exchangeType = 'fixed';
    fixedRateBtn.classList.add('active');
    floatRateBtn.classList.remove('active');
    updateExchangeRate();
});

fromAmountInput.addEventListener('input', updateExchangeRate);
fromCurrencySelect.addEventListener('change', updateExchangeRate);
toCurrencySelect.addEventListener('change', updateExchangeRate);

swapBtn.addEventListener('click', () => {
    try {
        const fromAmount = parseFloat(fromAmountInput.value);
        if (isNaN(fromAmount) || fromAmount <= 0) {
            throw new Error('Invalid from amount');
        }
        const toAmount = calculateToAmount(fromAmount);
        toAmountInput.value = toAmount.toFixed(2);
    } catch (error) {
        errorMessageElement.textContent = error.message;
    }
});

// Update exchange rate
function updateExchangeRate() {
    fromCurrency = fromCurrencySelect.value;
    toCurrency = toCurrencySelect.value;
    const rate = getExchangeRate(fromCurrency, toCurrency);
    if (rate) {
        exchangeRateElement.textContent = `1 ${fromCurrency} = ${rate} ${toCurrency}`;
        if (exchangeType === 'fixed') {
            toAmountInput.value = (fromAmountInput.value * rate).toFixed(2);
        }
    } else {
        exchangeRateElement.textContent = '';
    }
}

// Get exchange rate
function getExchangeRate(fromCurrency, toCurrency) {
    if (fromCurrency === toCurrency) return 1;
    return exchangeRates[fromCurrency][toCurrency];
}

// Calculate to amount
function calculateToAmount(fromAmount) {
    const rate = getExchangeRate(fromCurrency, toCurrency);
    if (exchangeType === 'float') {
        return fromAmount * rate;
    } else {
        return fromAmount * rate;
    }
}
```
