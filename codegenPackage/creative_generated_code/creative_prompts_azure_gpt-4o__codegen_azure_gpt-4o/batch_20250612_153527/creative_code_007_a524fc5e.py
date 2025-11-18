"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinnice.xyz
Prompt: Write a function in JavaScript to calculate transaction fees for Ethereum-based DeFi operations.
Generated: DETERMINISTIC_a524fc5ee7eeb9ef
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateTransactionFee
 * @description Calculates the transaction fee for Ethereum-based DeFi operations.
 * @param {number} gasLimit - The maximum amount of gas the transaction can use.
 * @param {number} gasPrice - The price of gas in gwei.
 * @returns {number} The calculated transaction fee in Ether.
 * @throws Will throw an error if inputs are invalid.
 */
function calculateTransactionFee(gasLimit, gasPrice) {
  // Input validation
  if (typeof gasLimit !== 'number' || gasLimit <= 0) {
    throw new Error('Invalid gasLimit: Must be a positive number.');
  }
  if (typeof gasPrice !== 'number' || gasPrice <= 0) {
    throw new Error('Invalid gasPrice: Must be a positive number.');
  }

  try {
    // Convert gasPrice from gwei to ether (1 gwei = 10^-9 ether)
    const gasPriceInEther = gasPrice * Math.pow(10, -9);

    // Calculate the transaction fee: gasLimit * gasPrice in ether
    const transactionFee = gasLimit * gasPriceInEther;

    // Ensure the result is a valid number
    if (!isFinite(transactionFee)) {
      throw new Error('Calculation resulted in an invalid transaction fee.');
    }

    return transactionFee;
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error('Error during transaction fee calculation:', error.message);
    throw error;
  }
}

// Example usage
try {
  const gasLimit = 21000; // Typical gas limit for Ethereum transactions
  const gasPrice = 50; // Example gas price in gwei
  const fee = calculateTransactionFee(gasLimit, gasPrice);
  console.log(`Transaction Fee: ${fee} Ether`);
} catch (error) {
  console.error('Failed to calculate transaction fee:', error.message);
}
```
