"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.web.app
Prompt: Create a JavaScript function that allows users to select a payment currency and calculate the amount of $FROP tokens they will receive based on the current token price.
Generated: DETERMINISTIC_7c8b8b440eaacee4
Batch ID: 20250612_163848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the amount of $FROP tokens a user will receive
 * based on the selected payment currency and its amount.
 * 
 * @param {string} currency - The user's selected currency (e.g., 'USD', 'EUR').
 * @param {number} amount - The amount in the selected currency.
 * @returns {number} - The equivalent amount of $FROP tokens.
 * @throws {Error} - Throws an error if the currency is not supported or if the amount is negative.
 */
function calculateFROPTokens(currency, amount) {
    // Define the current price of $FROP token in each supported currency
    const tokenPrices = {
        'USD': 2.5, // Price of 1 $FROP in USD
        'EUR': 2.3, // Price of 1 $FROP in EUR
        'GBP': 2.0  // Price of 1 $FROP in GBP
    };

    // Error handling for unsupported currencies
    if (!(currency in tokenPrices)) {
        throw new Error(`Unsupported currency: ${currency}. Supported currencies are: ${Object.keys(tokenPrices).join(', ')}`);
    }

    // Error handling for negative amount
    if (amount < 0) {
        throw new Error('Amount must be a non-negative number.');
    }

    // Calculate the number of $FROP tokens based on the selected currency and amount
    const fropTokens = amount / tokenPrices[currency];
    
    // Return the calculated amount of $FROP tokens
    return fropTokens;
}

// Example Usage:
try {
    const currency = 'USD';
    const amount = 100; // Amount in the selected currency
    const fropTokens = calculateFROPTokens(currency, amount);
    console.log(`You will receive ${fropTokens.toFixed(2)} $FROP tokens for ${amount} ${currency}.`);
} catch (error) {
    console.error(error.message);
}
```
