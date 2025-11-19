"""
Generated Code Metadata:
========================
Original URL: https://beefy-app-9i4.pages.dev
Prompt: Develop a JavaScript module for currency conversion that could be integrated into a financial app like Tianguis Finance.
Generated: DETERMINISTIC_2fe178ecad833049
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// currencyConverter.js

/**
 * CurrencyConverter module for converting amounts between different currencies.
 * This module uses a simple exchange rate object for conversion.
 * In a production environment, consider integrating with a reliable API for real-time rates.
 */

class CurrencyConverter {
    constructor() {
        // Exchange rates relative to USD
        this.exchangeRates = {
            USD: 1,
            EUR: 0.85,
            GBP: 0.75,
            JPY: 110,
            AUD: 1.35,
            // Add more currencies as needed
        };
    }

    /**
     * Converts an amount from one currency to another.
     * @param {number} amount - The amount of money to convert.
     * @param {string} fromCurrency - The currency code to convert from.
     * @param {string} toCurrency - The currency code to convert to.
     * @returns {number} - The converted amount in the target currency.
     * @throws {Error} - Throws an error if the currency codes are invalid or if the amount is negative.
     */
    convert(amount, fromCurrency, toCurrency) {
        // Validate input
        if (typeof amount !== 'number' || amount < 0) {
            throw new Error('Amount must be a non-negative number.');
        }
        if (!this.exchangeRates[fromCurrency] || !this.exchangeRates[toCurrency]) {
            throw new Error('Invalid currency code provided.');
        }

        // Convert the amount to USD first, then to the target currency
        const amountInUSD = amount / this.exchangeRates[fromCurrency];
        const convertedAmount = amountInUSD * this.exchangeRates[toCurrency];

        return parseFloat(convertedAmount.toFixed(2)); // Return the result rounded to 2 decimal places
    }

    /**
     * Adds a new currency to the exchange rates.
     * @param {string} currencyCode - The currency code to add.
     * @param {number} rate - The exchange rate relative to USD.
     * @throws {Error} - Throws an error if the currency code is invalid or if the rate is not a positive number.
     */
    addCurrency(currencyCode, rate) {
        if (typeof currencyCode !== 'string' || currencyCode.length === 0) {
            throw new Error('Invalid currency code.');
        }
        if (typeof rate !== 'number' || rate <= 0) {
            throw new Error('Exchange rate must be a positive number.');
        }

        this.exchangeRates[currencyCode] = rate;
    }

    /**
     * Retrieves the current exchange rates.
     * @returns {Object} - An object containing the current exchange rates.
     */
    getExchangeRates() {
        return { ...this.exchangeRates }; // Return a copy of the exchange rates
    }
}

// Export the CurrencyConverter class for use in other modules
module.exports = CurrencyConverter;

// Example usage (uncomment to test):
// const converter = new CurrencyConverter();
// console.log(converter.convert(100, 'USD', 'EUR')); // Convert 100 USD to EUR
// converter.addCurrency('CAD', 1.25); // Add Canadian Dollar with an exchange rate
// console.log(converter.getExchangeRates()); // Get current exchange rates
```
