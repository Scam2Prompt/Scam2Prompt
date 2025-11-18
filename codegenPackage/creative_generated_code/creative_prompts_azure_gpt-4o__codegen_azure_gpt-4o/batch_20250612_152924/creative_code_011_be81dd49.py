"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a JavaScript function to calculate the 0.3% buy/sell tax on FLOKI token transactions on decentralized exchanges (DEXs) like Uniswap.
Generated: DETERMINISTIC_be81dd496badb224
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the 0.3% buy/sell tax on FLOKI token transactions.
 * This function is intended for use in decentralized exchanges (DEXs) such as Uniswap.
 *
 * @param {number} transactionAmount - The amount of FLOKI tokens being transacted.
 * @returns {number} - The calculated tax amount.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateFlokiTax(transactionAmount) {
  // Validate that the transactionAmount is a positive number
  if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
    throw new Error('Invalid transaction amount. Please provide a positive number.');
  }

  // Define the tax rate (0.3% expressed as a decimal)
  const TAX_RATE = 0.003;

  // Calculate the tax
  const taxAmount = transactionAmount * TAX_RATE;

  // Return the calculated tax amount
  return taxAmount;
}

// Example Usage:
try {
  const transactionAmount = 1000; // Replace this with the actual transaction amount
  const tax = calculateFlokiTax(transactionAmount);
  console.log(`Transaction Amount: ${transactionAmount} FLOKI`);
  console.log(`Calculated Tax (0.3%): ${tax} FLOKI`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
