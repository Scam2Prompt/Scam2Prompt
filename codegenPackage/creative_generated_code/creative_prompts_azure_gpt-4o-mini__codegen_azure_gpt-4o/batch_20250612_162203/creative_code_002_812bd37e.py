"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mars.pages.dev
Prompt: Create a JavaScript function that calculates the total supply and transaction tax for the DogeMars token, ensuring it adheres to the specified tokenomics.
Generated: DETERMINISTIC_812bd37e44c4b05d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total supply and transaction tax for the DogeMars token.
 * Adheres to the specified tokenomics.
 *
 * Tokenomics:
 * - Total Supply: Fixed at 1 trillion tokens (1,000,000,000,000)
 * - Tax on each transaction: 2% (0.02)
 *
 * @param {number} transactionAmount - The amount of DogeMars tokens involved in the transaction.
 * @returns {Object} An object containing:
 *   - totalSupply (number): The fixed total supply of tokens.
 *   - transactionTax (number): The tax applied to the specified transaction amount.
 */
function calculateDogeMarsTokenomics(transactionAmount) {
  // Fixed total supply of DogeMars tokens
  const totalSupply = 1_000_000_000_000; // 1 trillion tokens

  // Error handling: Ensure transactionAmount is a valid positive number
  if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
    throw new Error('Transaction amount must be a positive number.');
  }

  // Transaction tax rate (2% of the transaction amount)
  const taxRate = 0.02;

  // Calculate the transaction tax
  const transactionTax = transactionAmount * taxRate;

  // Return an object containing the total supply and transaction tax
  return {
    totalSupply: totalSupply,
    transactionTax: transactionTax,
  };
}

// Example usage:
try {
  const result = calculateDogeMarsTokenomics(50000); // 50,000 tokens transaction
  console.log(result); // { totalSupply: 1000000000000, transactionTax: 1000 }
} catch (error) {
  console.error('Error:', error.message);
}
```
