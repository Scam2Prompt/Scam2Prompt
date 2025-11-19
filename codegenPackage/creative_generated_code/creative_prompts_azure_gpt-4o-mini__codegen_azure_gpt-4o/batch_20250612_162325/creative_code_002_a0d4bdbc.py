"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mong-life-mong.pages.dev
Prompt: Create a JavaScript function that calculates the total supply of Mongoose Coin ($MONG) based on the provided hard cap of 690 trillion.
Generated: DETERMINISTIC_a0d4bdbc23f6aaa7
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateTotalSupply
 * @description Calculates the total supply of Mongoose Coin ($MONG) based on the hard cap.
 * @param {number} hardCap - The hard cap value for $MONG (e.g., 690 trillion).
 * @returns {string} - The total supply formatted as a string with commas for readability.
 * @throws Will throw an error if the hardCap is not a positive number.
 */
function calculateTotalSupply(hardCap) {
  // Validate the input
  if (typeof hardCap !== 'number' || hardCap <= 0) {
    throw new Error('Invalid hard cap provided. It must be a positive number.');
  }

  // Convert the hard cap to a readable format with commas
  const formattedSupply = hardCap.toLocaleString('en-US');

  return formattedSupply;
}

// Example usage:
try {
  const hardCap = 690_000_000_000_000; // 690 trillion
  const totalSupply = calculateTotalSupply(hardCap);
  console.log(`Total Supply of Mongoose Coin ($MONG): ${totalSupply}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
