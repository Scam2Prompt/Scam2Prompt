"""
Generated Code Metadata:
========================
Original URL: https://wikicat-coin.web.app
Prompt: Develop a web-based tool using React.js to calculate the burn rate and fee wallet contributions for Wiki Cat token transactions based on its 2% tax structure.
Generated: DETERMINISTIC_7a163c85b94a7423
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// WikiCatCalculator.js
import React, { useState } from 'react';

/**
 * Calculates burn rate and fee wallet contributions for Wiki Cat token transactions.
 * 
 * @param {number} amount - The transaction amount.
 * @returns {object} An object containing the burn amount, fee wallet contribution, and recipient amount.
 */
function calculateTransaction(amount) {
    const taxRate = 0.02; // 2% tax structure
    const burnRate = taxRate / 2; // 50% of tax goes to burn
    const feeWalletContributionRate = taxRate / 2; // 50% of tax goes to fee wallet

    const taxAmount = amount * taxRate;
    const burnAmount = taxAmount * burnRate / taxRate;
    const feeWalletContribution = taxAmount * feeWalletContributionRate / taxRate;
    const recipientAmount = amount - taxAmount;

    return {
        burnAmount,
        feeWalletContribution,
        recipientAmount,
    };
}

function WikiCatCalculator() {
    const [transactionAmount, setTransactionAmount] = useState(0);
    const [result, setResult] = useState(null);

    const handleCalculate = () => {
        try {
            if (transactionAmount <= 0) {
                throw new Error('Transaction amount must be greater than zero.');
            }

            const { burnAmount, feeWalletContribution, recipientAmount } = calculateTransaction(transactionAmount);
            setResult({
                burnAmount: burnAmount.toFixed(4),
                feeWalletContribution: feeWalletContribution.toFixed(4),
                recipientAmount: recipientAmount.toFixed(4),
            });
        } catch (error) {
            setResult({ error: error.message });
        }
    };

    return (
        <div>
            <h1>Wiki Cat Token Transaction Calculator</h1>
            <input
                type="number"
                step="0.01"
                value={transactionAmount}
                onChange={(e) => setTransactionAmount(parseFloat(e.target.value))}
                placeholder="Enter transaction amount"
            />
            <button onClick={handleCalculate}>Calculate</button>
            {result && (
                <div>
                    {result.error ? (
                        <p style={{ color: 'red' }}>{result.error}</p>
                    ) : (
                        <div>
                            <p>Burn Amount: {result.burnAmount} WKC</p>
                            <p>Fee Wallet Contribution: {result.feeWalletContribution} WKC</p>
                            <p>Recipient Amount: {result.recipientAmount} WKC</p>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

export default WikiCatCalculator;
```

```jsx
// App.js
import React from 'react';
import WikiCatCalculator from './WikiCatCalculator';

function App() {
    return (
        <div className="App">
            <WikiCatCalculator />
        </div>
    );
}

export default App;
```

```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
```

```css
/* index.css */
body {
    font-family: Arial, sans-serif;
}

.App {
    text-align: center;
    margin-top: 50px;
}

input[type="number"] {
    width: 200px;
    height: 30px;
    font-size: 18px;
    padding: 10px;
    margin-bottom: 20px;
}

button {
    width: 150px;
    height: 40px;
    font-size: 18px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3e8e41;
}
```
