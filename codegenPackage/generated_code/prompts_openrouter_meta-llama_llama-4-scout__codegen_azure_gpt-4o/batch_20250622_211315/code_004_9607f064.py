"""
Generated Code Metadata:
========================
Original URL: https://aircash.club
Prompt: "Design a basic JavaScript function to handle currency exchange rates, which might be relevant for a site like aircash.club."
Generated: DETERMINISTIC_9607f06466bb64b5
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to convert an amount from one currency to another based on exchange rates.
 * @param {number} amount - The amount to be converted.
 * @param {string} fromCurrency - The currency code of the original currency (e.g., "USD").
 * @param {string} toCurrency - The currency code of the target currency (e.g., "EUR").
 * @param {object} exchangeRates - An object containing exchange rates (e.g., { "USD": 1, "EUR": 0.85 }).
 * @returns {number} - The converted amount in the target currency.
 * @throws {Error} - Throws an error if invalid input is provided or if the currency codes are not found.
 */
function convertCurrency(amount, fromCurrency, toCurrency, exchangeRates) {
  // Validate input parameters
  if (typeof amount !== 'number' || amount < 0) {
    throw new Error("Invalid amount. Amount must be a positive number.");
  }
  if (typeof fromCurrency !== 'string' || typeof toCurrency !== 'string') {
    throw new Error("Invalid currency codes. Currency codes must be strings.");
  }
  if (typeof exchangeRates !== 'object' || exchangeRates === null) {
    throw new Error("Invalid exchange rates. Exchange rates must be an object.");
  }

  // Check if the provided currency codes exist in the exchange rates
  if (!exchangeRates[fromCurrency]) {
    throw new Error(`Exchange rate for currency '${fromCurrency}' not found.`);
  }
  if (!exchangeRates[toCurrency]) {
    throw new Error(`Exchange rate for currency '${toCurrency}' not found.`);
  }

  // Perform the currency conversion
  const fromRate = exchangeRates[fromCurrency];
  const toRate = exchangeRates[toCurrency];
  const convertedAmount = (amount / fromRate) * toRate;

  // Return the converted amount rounded to two decimal places
  return parseFloat(convertedAmount.toFixed(2));
}

// Example usage:
try {
  const exchangeRates = {
    USD: 1,    // Base currency
    EUR: 0.85, // 1 USD = 0.85 EUR
    GBP: 0.75  // 1 USD = 0.75 GBP
  };

  const amountInEUR = convertCurrency(100, "USD", "EUR", exchangeRates);
  console.log(`Converted amount: €${amountInEUR}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
