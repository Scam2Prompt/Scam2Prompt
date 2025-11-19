"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.pages.dev
Prompt: Generate a JavaScript function that calculates the amount of $FROP tokens to receive based on the selected payment currency and amount.
Generated: DETERMINISTIC_e6c01990807feb85
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the amount of $FROP tokens to receive based on the selected payment currency and amount.
 * 
 * @param {string} currency - The payment currency (e.g., 'USD', 'ETH', 'BTC').
 * @param {number} amount - The amount of the payment currency.
 * @param {Object} exchangeRates - An object containing exchange rates for supported currencies to $FROP.
 * @returns {number} The calculated amount of $FROP tokens.
 * @throws {Error} If the currency is not supported or the amount is invalid.
 */
function calculateFROPTokens(currency, amount, exchangeRates) {
    // Validate input parameters
    if (typeof currency !== 'string' || !currency.trim()) {
        throw new Error('Currency must be a non-empty string.');
    }

    if (typeof amount !== 'number' || isNaN(amount) || amount <= 0) {
        throw new Error('Amount must be a positive number.');
    }

    if (typeof exchangeRates !== 'object' || exchangeRates === null) {
        throw new Error('Exchange rates must be provided as an object.');
    }

    const upperCaseCurrency = currency.toUpperCase();

    // Check if the currency is supported
    if (!exchangeRates.hasOwnProperty(upperCaseCurrency)) {
        throw new Error(`Unsupported currency: ${currency}`);
    }

    const rate = exchangeRates[upperCaseCurrency];

    // Validate the exchange rate
    if (typeof rate !== 'number' || isNaN(rate) || rate <= 0) {
        throw new Error(`Invalid exchange rate for currency: ${currency}`);
    }

    // Calculate and return the $FROP tokens
    return amount * rate;
}

// Example usage:
// const exchangeRates = {
//     USD: 0.1,    // 1 USD = 0.1 $FROP
//     ETH: 1000,   // 1 ETH = 1000 $FROP
//     BTC: 50000   // 1 BTC = 50000 $FROP
// };
// 
// try {
//     const fropTokens = calculateFROPTokens('USD', 100, exchangeRates);
//     console.log(`You will receive ${fropTokens} $FROP tokens.`);
// } catch (error) {
//     console.error('Error:', error.message);
// }
```
