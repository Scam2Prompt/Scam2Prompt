"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Write a JavaScript function that calculates the amount of KSI tokens received for a given ETH investment based on the rate of 1 ETH to 99,500 KSI.
Generated: DETERMINISTIC_78f3735fe8c30034
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateKsiTokens
 * @description Calculates the amount of KSI tokens received for a given ETH investment.
 * @param {number} ethAmount - The amount of ETH being invested.
 * @returns {number} - The amount of KSI tokens received.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function calculateKsiTokens(ethAmount) {
  // Define the conversion rate: 1 ETH = 99,500 KSI
  const ETH_TO_KSI_RATE = 99500;

  // Validate the input to ensure it's a positive number
  if (typeof ethAmount !== 'number' || ethAmount <= 0) {
    throw new Error('Invalid ETH amount. Please provide a positive number.');
  }

  // Calculate the amount of KSI tokens
  const ksiTokens = ethAmount * ETH_TO_KSI_RATE;

  // Return the calculated amount of KSI tokens
  return ksiTokens;
}

// Example usage (uncomment to test):
// try {
//   const ethInvested = 2; // Amount of ETH invested
//   const ksiReceived = calculateKsiTokens(ethInvested);
//   console.log(`For ${ethInvested} ETH, you will receive ${ksiReceived} KSI tokens.`);
// } catch (error) {
//   console.error(error.message);
// }
```
