"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Create a JavaScript function to calculate the amount of $HEHE tokens received when swapping a specific amount of USDT, referencing the presale details provided on the webpage.
Generated: DETERMINISTIC_52bddc1acb487c2a
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the amount of $HEHE tokens received
 * during a presale swap using a specific amount of USDT.
 * 
 * @param {number} usdtAmount - The amount of USDT to be swapped.
 * @param {number} tokenRate - The rate at which $HEHE tokens are given per USDT.
 * @returns {number} The amount of $HEHE tokens received.
 * @throws {Error} If the input parameters are invalid.
 */
function calculateHEHETokens(usdtAmount, tokenRate) {
  // Input validation
  if (typeof usdtAmount !== 'number' || typeof tokenRate !== 'number') {
    throw new Error("Invalid input: Both 'usdtAmount' and 'tokenRate' must be numbers.");
  }
  if (usdtAmount <= 0) {
    throw new Error("Invalid input: 'usdtAmount' must be greater than zero.");
  }
  if (tokenRate <= 0) {
    throw new Error("Invalid input: 'tokenRate' must be greater than zero.");
  }

  // Perform calculation
  const heheTokens = usdtAmount * tokenRate;

  // Return the result
  return heheTokens;
}

// Example usage:
// Assuming the presale rate is 50 $HEHE tokens per 1 USDT
try {
  const usdtToSwap = 100; // Example: User wants to swap 100 USDT
  const tokenRate = 50;   // Presale rate: 50 $HEHE tokens per 1 USDT

  const receivedTokens = calculateHEHETokens(usdtToSwap, tokenRate);
  console.log(`You will receive ${receivedTokens} $HEHE tokens.`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
