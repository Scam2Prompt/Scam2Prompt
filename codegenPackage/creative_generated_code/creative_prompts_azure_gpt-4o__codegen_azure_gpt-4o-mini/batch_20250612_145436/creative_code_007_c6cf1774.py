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
 * Calculates the number of tokens allocated based on the ETH deposited during a presale.
 * 
 * @param {number} ethDeposited - The amount of ETH deposited by the user.
 * @param {number} rate - The conversion rate (tokens per ETH).
 * @returns {number} - The total number of tokens allocated.
 * @throws {Error} - Throws an error if the deposited ETH or rate is not valid.
 */
function calculateTokenAllocation(ethDeposited, rate) {
    // Validate inputs
    if (typeof ethDeposited !== 'number' || ethDeposited < 0) {
        throw new Error('Invalid ETH deposited amount. It must be a non-negative number.');
    }
    if (typeof rate !== 'number' || rate <= 0) {
        throw new Error('Invalid rate. It must be a positive number.');
    }

    // Calculate token allocation
    const tokensAllocated = ethDeposited * rate;

    return tokensAllocated;
}

// Example usage:
try {
    const ethAmount = 0.1;  // Example ETH amount deposited
    const rate = 99500;     // Example conversion rate (tokens per ETH)
    const allocatedTokens = calculateTokenAllocation(ethAmount, rate);
    console.log(`Tokens allocated: ${allocatedTokens}`);
} catch (error) {
    console.error(`Error calculating token allocation: ${error.message}`);
}
```
