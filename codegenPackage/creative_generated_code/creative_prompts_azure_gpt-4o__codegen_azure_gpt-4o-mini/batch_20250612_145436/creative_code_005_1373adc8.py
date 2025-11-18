"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Suggest an open-source library for implementing VAT-inclusive pricing in an e-commerce platform. Provide an example of how to calculate and display VAT-inclusive prices in JavaScript.
Generated: DETERMINISTIC_1373adc8dfb3e635
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// VAT Calculation Module
// This module provides functions to calculate VAT-inclusive pricing

/**
 * Calculates the VAT-inclusive price based on the given price and VAT rate.
 * @param {number} price - The base price before VAT.
 * @param {number} vatRate - The VAT rate as a percentage (e.g., 20 for 20%).
 * @returns {number} The VAT-inclusive price.
 * @throws {Error} Throws an error if the inputs are not valid numbers.
 */
function calculateVatInclusivePrice(price, vatRate) {
    if (typeof price !== 'number' || typeof vatRate !== 'number') {
        throw new Error('Invalid input: price and vatRate must be numbers.');
    }
    if (price < 0 || vatRate < 0) {
        throw new Error('Invalid input: price and vatRate must be non-negative.');
    }

    // Calculate VAT-inclusive price
    const vatAmount = (price * vatRate) / 100;
    const vatInclusivePrice = price + vatAmount;

    return parseFloat(vatInclusivePrice.toFixed(2)); // Return as a fixed decimal
}

/**
 * Displays the VAT-inclusive price in the console.
 * @param {number} price - The base price before VAT.
 * @param {number} vatRate - The VAT rate as a percentage.
 */
function displayVatInclusivePrice(price, vatRate) {
    try {
        const vatInclusivePrice = calculateVatInclusivePrice(price, vatRate);
        console.log(`The VAT-inclusive price for €${price.toFixed(2)} at ${vatRate}% VAT is: €${vatInclusivePrice}`);
    } catch (error) {
        console.error('Error calculating VAT-inclusive price:', error);
    }
}

// Example Usage
const basePrice = 100; // Base price in euros
const vatRate = 20;    // VAT rate in percentage

// Display the VAT-inclusive price
displayVatInclusivePrice(basePrice, vatRate);
```
