"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc922122.pages.dev
Prompt: Generate a JavaScript function to swap Notcoin vouchers for hTON balance in the Notcoin ecosystem.
Generated: DETERMINISTIC_8748ecffc8db9e3a
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to swap Notcoin vouchers for hTON balance in the Notcoin ecosystem.
 * 
 * @param {number} notcoinAmount - The quantity of Notcoin vouchers to be swapped.
 * @param {number} exchangeRate - The current exchange rate (hTON per Notcoin voucher).
 * @returns {number} - The resulting hTON balance after the swap.
 * @throws {Error} - If invalid input parameters are provided.
 */
function swapNotcoinForHTON(notcoinAmount, exchangeRate) {
  // Input validation
  if (typeof notcoinAmount !== 'number' || notcoinAmount <= 0) {
    throw new Error("Invalid Notcoin amount. Must be a positive number.");
  }
  if (typeof exchangeRate !== 'number' || exchangeRate <= 0) {
    throw new Error("Invalid exchange rate. Must be a positive number.");
  }

  // Calculate hTON balance
  const hTONBalance = notcoinAmount * exchangeRate;

  // Return the resulting hTON balance
  return hTONBalance;
}

// Example Usage:
try {
  const notcoinAmount = 100; // Example: 100 Notcoin vouchers
  const exchangeRate = 0.05; // Example: 0.05 hTON per Notcoin voucher
  const hTONBalance = swapNotcoinForHTON(notcoinAmount, exchangeRate);
  console.log(`You received ${hTONBalance} hTON.`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
