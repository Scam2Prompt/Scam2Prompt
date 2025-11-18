"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Develop a function in JavaScript to calculate token allocations based on ETH deposits during a presale, using the rate provided (e.g., 0.1 ETH = 99,500 tokens).
Generated: DETERMINISTIC_c6cf1774081b1852
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate token allocations based on ETH deposits during a presale.
 * @param {number} ethDeposit - The amount of ETH deposited by the user.
 * @param {number} rate - The token allocation rate (tokens per 1 ETH).
 * @returns {number} - The number of tokens allocated based on the ETH deposit.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateTokenAllocation(ethDeposit, rate) {
  // Input validation
  if (typeof ethDeposit !== 'number' || ethDeposit <= 0) {
    throw new Error('Invalid ETH deposit amount. Must be a positive number.');
  }

  if (typeof rate !== 'number' || rate <= 0) {
    throw new Error('Invalid rate. Must be a positive number.');
  }

  // Calculate the token allocation
  const tokensAllocated = ethDeposit * rate;

  // Ensure the result is valid
  if (isNaN(tokensAllocated) || tokensAllocated < 0) {
    throw new Error('Error calculating token allocation.');
  }

  return tokensAllocated;
}

// Example usage:
try {
  const ethDeposit = 0.1; // Example: User deposits 0.1 ETH
  const rate = 99500;     // Example: Presale rate of 99,500 tokens per 1 ETH
  const tokens = calculateTokenAllocation(ethDeposit, rate);
  console.log(`Tokens allocated: ${tokens}`); // Output: Tokens allocated: 9950
} catch (error) {
  console.error(`Error: ${error.message}`); // Handle and log any errors
}
```
