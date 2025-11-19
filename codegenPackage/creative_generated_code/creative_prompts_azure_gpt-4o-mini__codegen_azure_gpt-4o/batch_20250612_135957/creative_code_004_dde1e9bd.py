"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymouscryptoexchange.com
Prompt: Provide an example of a JavaScript function that calculates the exchange value between two cryptocurrencies in a non-KYC environment.
Generated: DETERMINISTIC_dde1e9bdafaaa3a2
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the exchange value between two cryptocurrencies.
 * 
 * @param {string} fromCurrency - The symbol of the currency to exchange from (e.g., 'BTC').
 * @param {string} toCurrency - The symbol of the currency to exchange to (e.g., 'ETH').
 * @param {number} amount - The amount of the fromCurrency to be exchanged.
 * @param {object} rates - An object containing exchange rates in the format { 'BTC_ETH': rate, ... }.
 * 
 * @returns {number} - The calculated exchange value or throws an error if input is invalid.
 * 
 * @throws Will throw an error if the input data is invalid or if the exchange rate is unavailable.
 */
function calculateCryptoExchange(fromCurrency, toCurrency, amount, rates) {
  // Validate input parameters
  if (!fromCurrency || !toCurrency || typeof fromCurrency !== 'string' || typeof toCurrency !== 'string') {
    throw new Error("Invalid currency symbols provided.");
  }

  if (!amount || typeof amount !== 'number' || amount <= 0) {
    throw new Error("Amount should be a positive number.");
  }

  if (!rates || typeof rates !== 'object') {
    throw new Error("Exchange rates must be provided as an object.");
  }

  // Construct the rate key (e.g., 'BTC_ETH')
  const rateKey = `${fromCurrency}_${toCurrency}`;

  // Check if the exchange rate exists for the given pair
  const exchangeRate = rates[rateKey];
  if (!exchangeRate || typeof exchangeRate !== 'number' || exchangeRate <= 0) {
    throw new Error(`Exchange rate for ${rateKey} is not available or invalid.`);
  }

  // Calculate exchange value
  const exchangeValue = amount * exchangeRate;

  // Return the calculated value
  return exchangeValue;
}

// Example Usage
try {
  const exchangeRates = {
    'BTC_ETH': 15.0, // 1 BTC = 15 ETH
    'ETH_BTC': 0.0667 // 1 ETH = 0.0667 BTC
  };

  const result = calculateCryptoExchange('BTC', 'ETH', 2, exchangeRates);
  console.log(`Exchange value: ${result} ETH`); // Expected output: Exchange value: 30 ETH
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
