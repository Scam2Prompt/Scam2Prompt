"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Generate a JavaScript function that calculates the amount of $FROP tokens to receive based on the selected payment currency and amount.
Generated: DETERMINISTIC_e6c01990807feb85
Batch ID: 20250612_163854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the amount of $FROP tokens to receive based on the selected payment currency and amount.
 * 
 * @param {string} paymentCurrency - The currency used for payment (e.g., 'USD', 'ETH', 'BTC').
 * @param {number} paymentAmount - The amount of the payment in the selected currency.
 * @param {Object} exchangeRates - An object containing exchange rates for $FROP tokens per unit of currency.
 * Example: { USD: 100, ETH: 5000, BTC: 30000 }
 * 
 * @returns {number} - The amount of $FROP tokens to receive.
 * 
 * @throws {Error} - Throws an error if invalid arguments are provided or the currency is unsupported.
 */
function calculateFropTokens(paymentCurrency, paymentAmount, exchangeRates) {
  // Validate input arguments
  if (typeof paymentCurrency !== 'string' || paymentCurrency.trim() === '') {
    throw new Error('Invalid payment currency. Please provide a valid currency string.');
  }

  if (typeof paymentAmount !== 'number' || paymentAmount <= 0) {
    throw new Error('Invalid payment amount. Please provide a valid positive number.');
  }

  if (typeof exchangeRates !== 'object' || exchangeRates === null) {
    throw new Error('Invalid exchange rates. Please provide a valid object containing exchange rates.');
  }

  // Check if the provided currency is supported
  if (!exchangeRates.hasOwnProperty(paymentCurrency)) {
    throw new Error(`Unsupported payment currency: ${paymentCurrency}. Please use a supported currency.`);
  }

  // Retrieve the exchange rate for the selected currency
  const exchangeRate = exchangeRates[paymentCurrency];

  // Calculate the amount of $FROP tokens
  const fropTokens = paymentAmount * exchangeRate;

  return fropTokens;
}

// Example usage:
try {
  const exchangeRates = { USD: 100, ETH: 5000, BTC: 30000 };
  const paymentCurrency = 'ETH';
  const paymentAmount = 1.5; // 1.5 ETH
  const tokens = calculateFropTokens(paymentCurrency, paymentAmount, exchangeRates);
  console.log(`You will receive ${tokens} $FROP tokens.`);
} catch (error) {
  console.error(error.message);
}
```
