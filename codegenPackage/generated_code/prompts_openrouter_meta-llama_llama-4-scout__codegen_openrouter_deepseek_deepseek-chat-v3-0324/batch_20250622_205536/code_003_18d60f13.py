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
    <title>Crypto Exchange</title>
    <style>
        :root {
            --primary-color: #6200ee;
            --secondary-color: #03dac6;
            --background-color: #f5f5f5;
            --card-color: #ffffff;
            --text-color: #333333;
            --error-color: #b00020;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--background-color);
            color: var(--text-color);
            padding: 20px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
        }

        .header h1 {
            color: var(--primary-color);
            margin-bottom: 10px;
        }

        .card {
            background-color: var(--card-color);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 25px;
            margin-bottom: 20px;
        }

        .card-title {
            font-size: 1.2rem;
            margin-bottom: 20px;
            color: var(--primary-color);
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 500;
        }

        select, input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        input:focus, select:focus {
            outline: none;
            border-color: var(--primary-color);
        }

        .rate-toggle {
            display: flex;
            margin-bottom: 20px;
            border-radius: 4px;
            overflow: hidden;
        }

        .rate-toggle button {
            flex: 1;
            padding: 10px;
            border: none;
            background-color: #e0e0e0;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .rate-toggle button.active {
            background-color: var(--primary-color);
            color: white;
        }

        .rate-info {
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 15px;
        }

        .btn {
            width: 100%;
            padding: 12px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .btn:hover {
            background-color: #7c4dff;
        }

        .error {
            color: var(--error-color);
            font-size: 0.9rem;
            margin-top: 5px;
        }

        .swap-icon {
            text-align: center;
            margin: 10px 0;
            cursor: pointer;
        }

        .swap-icon svg {
            width: 24px;
            height: 24px;
            fill: var(--primary-color);
        }

        .rate-display {
            margin-top: 15px;
            padding: 10px;
            background-color: #f0f0f0;
            border-radius: 4px;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Crypto Exchange</h1>
            <p>Fast and secure cryptocurrency exchange</p>
        </div>

        <div class="card">
            <h2 class="card-title">Exchange</h2>
            
            <div class="rate-toggle">
                <button id="float-rate-btn" class="active">Float Rate</button>
                <button id="fixed-rate-btn">Fixed Rate</button>
            </div>

            <p id="rate-info" class="rate-info">
                Float rate: The exchange rate may change before the transaction is completed.
            </p>

            <div class="form-group">
                <label for="from-currency">You send</label>
                <div class="input-group">
                    <input type="number" id="from-amount" placeholder="0.00" min="0" step="0.00000001">
                    <select id="from-currency">
                        <option value="BTC">Bitcoin (BTC)</option>
                        <option value="ETH">Ethereum (ETH)</option>
                        <option value="USDT">Tether (USDT)</option>
                        <option value="XRP">Ripple (XRP)</option>
                    </select>
                </div>
            </div>

            <div class="swap-icon" id="swap-currencies">
                <svg viewBox="0 0 24 24">
                    <path d="M16,17.01V10h-2v7.01h-3L15,21l4-3.99H16z M9,3L5,6.99h3V14h2V6.99h3L9,3z"/>
                </svg>
            </div>

            <div class="form-group">
                <label for="to-currency">You receive</label>
                <div class="input-group">
                    <input type="number" id="to-amount" placeholder="0.00" min="0" step="0.00000001" readonly>
                    <select id="to-currency">
                        <option value="ETH">Ethereum (ETH)</option>
                        <option value="BTC">Bitcoin (BTC)</option>
                        <option value="USDT">Tether (USDT)</option>
                        <option value="XRP">Ripple (XRP)</option>
                    </select>
                </div>
            </div>

            <div id="rate-display" class="rate-display">
                Exchange rate: Loading...
            </div>

            <button id="exchange-btn" class="btn">Exchange</button>
        </div>
    </div>

    <script>
        // Mock exchange rates (in a real app, these would come from an API)
        const exchangeRates = {
            BTC: { ETH: 15.2, USDT: 50000, XRP: 2000000 },
            ETH: { BTC: 0.066, USDT: 3300, XRP: 130000 },
            USDT: { BTC: 0.00002, ETH: 0.0003, XRP: 40 },
            XRP: { BTC: 0.0000005, ETH: 0.0000077, USDT: 0.025 }
        };

        // DOM elements
        const fromAmountInput = document.getElementById('from-amount');
        const toAmountInput = document.getElementById('to-amount');
        const fromCurrencySelect = document.getElementById('from-currency');
        const toCurrencySelect = document.getElementById('to-currency');
        const swapButton = document.getElementById('swap-currencies');
        const floatRateBtn = document.getElementById('float-rate-btn');
        const fixedRateBtn = document.getElementById('fixed-rate-btn');
        const rateInfo = document.getElementById('rate-info');
        const rateDisplay = document.getElementById('rate-display');
        const exchangeBtn = document.getElementById('exchange-btn');

        // Current rate type (float or fixed)
        let rateType = 'float';
        let currentRate = 0;

        // Initialize the app
        document.addEventListener('DOMContentLoaded', () => {
            updateExchangeRate();
        });

        // Event listeners
        fromAmountInput.addEventListener('input', calculateToAmount);
        fromCurrencySelect.addEventListener('change', updateExchangeRate);
        toCurrencySelect.addEventListener('change', updateExchangeRate);
        swapButton.addEventListener('click', swapCurrencies);
        floatRateBtn.addEventListener('click', () => setRateType('float'));
        fixedRateBtn.addEventListener('click', () => setRateType('fixed'));
        exchangeBtn.addEventListener('click', performExchange);

        // Calculate the amount to receive based on the input amount
        function calculateToAmount() {
            const fromAmount = parseFloat(fromAmountInput.value);
            
            if (isNaN(fromAmount) || fromAmount <= 0) {
                toAmountInput.value = '';
                return;
            }

            const fromCurrency = fromCurrencySelect.value;
            const toCurrency = toCurrencySelect.value;

            if (fromCurrency === toCurrency) {
                toAmountInput.value = fromAmountInput.value;
                currentRate = 1;
                updateRateDisplay();
                return;
            }

            const rate = exchangeRates[fromCurrency][toCurrency];
            currentRate = rate;
            const toAmount = from
