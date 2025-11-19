"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogemarsclaim.pages.dev
Prompt: Develop a JavaScript function that calculates the total supply and transaction tax for DogeMars ($MARS) based on the tokenomics described on the DogeMars webpage.
Generated: DETERMINISTIC_7b51e34f97d99e40
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total supply and transaction tax for DogeMars ($MARS).
 * @param {number} supplyPercentage - Percentage of total supply allocated for calculation (e.g., 100 for full supply).
 * @param {number} transactionAmount - Amount of $MARS tokens being transacted.
 * @returns {Object} - An object containing total supply and transaction tax details.
 */
function calculateDogeMarsMetrics(supplyPercentage, transactionAmount) {
  // Tokenomics constants based on DogeMars webpage
  const FULL_SUPPLY = 1_000_000_000_000; // Total supply: 1 trillion $MARS tokens
  const TAX_RATE = 0.10; // Transaction tax: 10%

  // Input validation
  if (typeof supplyPercentage !== 'number' || supplyPercentage <= 0 || supplyPercentage > 100) {
    throw new Error('Invalid supply percentage. Must be a number between 1 and 100.');
  }
  if (typeof transactionAmount !== 'number' || transactionAmount <= 0) {
    throw new Error('Invalid transaction amount. Must be a positive number.');
  }

  // Calculate the total supply based on the given percentage
  const calculatedSupply = FULL_SUPPLY * (supplyPercentage / 100);

  // Calculate transaction tax
  const transactionTax = transactionAmount * TAX_RATE;

  // Return results
  return {
    totalSupply: calculatedSupply,
    transactionTax: transactionTax,
  };
}

// Example usage:
try {
  const metrics = calculateDogeMarsMetrics(100, 50000);
  console.log('Total Supply:', metrics.totalSupply); // Total supply for 100% allocation
  console.log('Transaction Tax:', metrics.transactionTax); // Tax for 50,000 $MARS tokens
} catch (error) {
  console.error(error.message);
}
```
