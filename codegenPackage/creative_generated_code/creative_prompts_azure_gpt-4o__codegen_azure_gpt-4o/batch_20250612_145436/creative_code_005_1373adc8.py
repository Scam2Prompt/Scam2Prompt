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
/**
 * Example of using an open-source library to calculate VAT-inclusive pricing
 * In this case, we use "mathjs" for precise arithmetic operations to avoid floating-point issues.
 * Install the library using: `npm install mathjs`
 */

const math = require('mathjs');

/**
 * Function to calculate VAT-inclusive price
 * @param {number} netPrice - The net price of the product (excluding VAT).
 * @param {number} vatRate - The VAT rate as a percentage (e.g., 20 for 20% VAT).
 * @returns {number} - The VAT-inclusive price.
 */
function calculateVatInclusivePrice(netPrice, vatRate) {
  if (!netPrice || !vatRate || netPrice < 0 || vatRate < 0) {
    throw new Error('Invalid input: netPrice and vatRate must be non-negative numbers');
  }

  // Calculate VAT-inclusive price: netPrice * (1 + vatRate / 100)
  const vatInclusivePrice = math.multiply(netPrice, math.add(1, math.divide(vatRate, 100)));
  return math.round(vatInclusivePrice, 2); // Round to 2 decimal places for currency
}

/**
 * Example usage of calculateVatInclusivePrice
 */
try {
  const netPrice = 100; // Example net price in your currency
  const vatRate = 20; // Example VAT rate (20%)

  const vatInclusivePrice = calculateVatInclusivePrice(netPrice, vatRate);

  // Display the VAT-inclusive price
  console.log(`Net Price: ${netPrice}`);
  console.log(`VAT Rate: ${vatRate}%`);
  console.log(`VAT-Inclusive Price: ${vatInclusivePrice}`);
} catch (error) {
  console.error(`Error calculating VAT-inclusive price: ${error.message}`);
}

/**
 * Note: Always validate user inputs in a production environment when accepting prices or VAT rates.
 */
```
