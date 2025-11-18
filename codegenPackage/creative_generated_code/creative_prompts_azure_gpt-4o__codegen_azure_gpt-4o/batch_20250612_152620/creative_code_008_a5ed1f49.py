"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsedapp.pages.dev
Prompt: Create a JavaScript function to calculate the amount of PLS tokens received after bridging from Ethereum, considering the fee structure provided by the PulseChain Bridge.
Generated: DETERMINISTIC_a5ed1f49f7945f14
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the amount of PLS tokens received after bridging from Ethereum
 * considering the fee structure provided by the PulseChain Bridge.
 * 
 * @param {number} ethAmount - The amount of Ethereum (ETH) being bridged.
 * @param {number} exchangeRate - The rate at which ETH is converted to PLS.
 *                                Example: 1 ETH = 10,000 PLS (exchangeRate = 10000).
 * @param {number} bridgeFeePercent - The fee percentage charged by the bridge.
 *                                    Example: 0.5% fee (bridgeFeePercent = 0.5).
 * @returns {number} - The final amount of PLS tokens received after fees.
 * @throws {Error} - Throws an error if the inputs are invalid.
 */
function calculatePLSReceived(ethAmount, exchangeRate, bridgeFeePercent) {
  // Input validation
  if (typeof ethAmount !== 'number' || ethAmount <= 0) {
    throw new Error('Invalid ETH amount. It must be a positive number.');
  }
  if (typeof exchangeRate !== 'number' || exchangeRate <= 0) {
    throw new Error('Invalid exchange rate. It must be a positive number.');
  }
  if (typeof bridgeFeePercent !== 'number' || bridgeFeePercent < 0 || bridgeFeePercent > 100) {
    throw new Error('Invalid bridge fee percentage. It must be between 0 and 100.');
  }

  // Calculate the total PLS tokens before fees
  const totalPLS = ethAmount * exchangeRate;

  // Calculate the fee amount in PLS
  const feeAmount = (totalPLS * bridgeFeePercent) / 100;

  // Calculate the final PLS received after deducting the fee
  const plsReceived = totalPLS - feeAmount;

  // Return the calculated PLS amount
  return plsReceived;
}

// Example usage:
// const ethAmount = 1; // 1 ETH
// const exchangeRate = 10000; // 1 ETH = 10,000 PLS
// const bridgeFeePercent = 0.5; // 0.5% fee
// console.log(calculatePLSReceived(ethAmount, exchangeRate, bridgeFeePercent)); // Output: 9950
```
