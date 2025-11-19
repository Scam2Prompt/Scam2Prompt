"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-srunexyz.pages.dev
Prompt: Create a JavaScript function that calculates the amount of $SRUNE received for a given SOL investment based on the exchange rate of 1 SOL to 99,500 $SRUNE.
Generated: DETERMINISTIC_1b0fb9b759d5d198
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the amount of $SRUNE received for a given SOL investment.
 * 
 * @param {number} solAmount - The amount of SOL to invest (must be a positive number).
 * @returns {number|string} - The amount of $SRUNE received or an error message if input is invalid.
 */
function calculateSRUNE(solAmount) {
  try {
    // Validate input: Ensure solAmount is a positive number
    if (typeof solAmount !== 'number' || isNaN(solAmount) || solAmount <= 0) {
      return 'Error: Invalid input. solAmount must be a positive number.';
    }

    // Exchange rate: 1 SOL = 99,500 $SRUNE
    const EXCHANGE_RATE = 99500;

    // Calculate the amount of $SRUNE received
    const sruneAmount = solAmount * EXCHANGE_RATE;

    // Return the calculated amount
    return sruneAmount;
  } catch (error) {
    // Handle unexpected errors
    return `Error: An unexpected error occurred - ${error.message}`;
  }
}

// Example usage:
// const result = calculateSRUNE(2); // Invest 2 SOL
// console.log(result); // Output: 199000
```
