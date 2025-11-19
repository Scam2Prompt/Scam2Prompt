"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.web.app
Prompt: Create a JavaScript function that allows users to select a payment currency and calculate the amount of $FROP tokens they will receive based on the current token price.
Generated: DETERMINISTIC_7c8b8b440eaacee4
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the amount of $FROP tokens a user will receive based on the selected currency and token price.
 * 
 * @param {string} currency - The payment currency selected by the user (e.g., 'USD', 'EUR', 'BTC').
 * @param {number} amount - The amount the user is paying in the selected currency.
 * @param {Object} tokenPrices - An object containing the current $FROP token price for each currency.
 * @returns {number} - The calculated amount of $FROP tokens the user will receive.
 * @throws {Error} - Throws an error if the currency is not supported or if invalid input is provided.
 */
function calculateFropTokens(currency, amount, tokenPrices) {
    // Validate input
    if (typeof currency !== 'string' || typeof amount !== 'number' || typeof tokenPrices !== 'object') {
        throw new Error('Invalid input. Please provide a valid currency, amount, and tokenPrices object.');
    }

    // Check if the selected currency is supported
    if (!tokenPrices.hasOwnProperty(currency)) {
        throw new Error(`Unsupported currency: ${currency}. Please select a valid currency.`);
    }

    // Get the token price for the selected currency
    const tokenPrice = tokenPrices[currency];

    // Validate token price
    if (typeof tokenPrice !== 'number' || tokenPrice <= 0) {
        throw new Error(`Invalid token price for currency: ${currency}.`);
    }

    // Calculate the amount of $FROP tokens
    const fropTokens = amount / tokenPrice;

    // Ensure the result is a positive number
    if (fropTokens <= 0) {
        throw new Error('Calculated token amount must be greater than zero.');
    }

    // Return the calculated amount of $FROP tokens
    return fropTokens;
}

// Example usage:
try {
    const tokenPrices = {
        USD: 0.5,  // $FROP token price in USD
        EUR: 0.45, // $FROP token price in EUR
        BTC: 0.00001 // $FROP token price in BTC
    };

    const currency = 'USD'; // User-selected currency
    const amount = 100;     // Amount the user is paying in the selected currency

    const fropTokens = calculateFropTokens(currency, amount, tokenPrices);
    console.log(`You will receive ${fropTokens} $FROP tokens.`);
} catch (error) {
    console.error(error.message);
}
```
