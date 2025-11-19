"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-ui-v3-inner-bfms69e9g-raydium.vercel.app
Prompt: Generate a function that calculates estimated fees for a swap transaction on Raydium's UI.
Generated: DETERMINISTIC_5d3aeb7a9a71ead5
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate estimated fees for a swap transaction on Raydium's UI.
 * @param {number} inputAmount - The amount of tokens to be swapped.
 * @param {number} swapRate - The rate at which tokens are swapped (e.g., 1 TokenA -> 0.9 TokenB).
 * @param {number} feeRate - The fee rate as a percentage (e.g., 0.3 for 0.3%).
 * @returns {Object} - An object containing the estimated fees and the final amount after fees.
 */
function calculateSwapFees(inputAmount, swapRate, feeRate) {
  // Input validation
  if (typeof inputAmount !== 'number' || inputAmount <= 0) {
    throw new Error("Invalid input amount. Must be a positive number.");
  }
  
  if (typeof swapRate !== 'number' || swapRate <= 0) {
    throw new Error("Invalid swap rate. Must be a positive number.");
  }
  
  if (typeof feeRate !== 'number' || feeRate < 0 || feeRate > 100) {
    throw new Error("Invalid fee rate. Must be a percentage between 0 and 100.");
  }

  // Calculate the gross output amount before fees
  const grossOutputAmount = inputAmount * swapRate;

  // Calculate the fee amount
  const feeAmount = (grossOutputAmount * feeRate) / 100;

  // Calculate the final output amount after deducting fees
  const finalOutputAmount = grossOutputAmount - feeAmount;

  // Return the estimated fees and final output amount
  return {
    estimatedFees: feeAmount,
    finalAmount: finalOutputAmount,
  };
}

// Example usage:
try {
  const inputAmount = 100; // Amount to swap
  const swapRate = 0.9;    // Example swap rate
  const feeRate = 0.3;     // Fee rate in percentage

  const result = calculateSwapFees(inputAmount, swapRate, feeRate);
  console.log("Estimated Fees:", result.estimatedFees);
  console.log("Final Amount:", result.finalAmount);
} catch (error) {
  console.error("Error:", error.message);
}
```
