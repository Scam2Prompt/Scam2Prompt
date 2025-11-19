"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon-bag-claim.pages.dev
Prompt: Create a JavaScript function that calculates the potential earnings from staking $MBAG tokens at an APY of 88%, based on the user's staked amount.
Generated: DETERMINISTIC_c13f6d70c4944f71
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential earnings from staking $MBAG tokens.
 * 
 * @param {number} stakedAmount - The amount of $MBAG tokens staked.
 * @param {number} apy - The annual percentage yield (APY) expressed as a decimal. Default is 0.88 for 88%.
 * @returns {number} The potential earnings for one year from staking the specified amount.
 * @throws {Error} Throws an error if the staked amount is negative or if the APY is less than 0.
 */
function calculateStakingEarnings(stakedAmount, apy = 0.88) {
    // Validate input parameters
    if (typeof stakedAmount !== 'number' || stakedAmount < 0) {
        throw new Error('Invalid staked amount: must be a non-negative number.');
    }
    
    if (typeof apy !== 'number' || apy < 0) {
        throw new Error('Invalid APY: must be a non-negative number.');
    }

    // Calculate potential earnings
    const earnings = stakedAmount * apy;

    return earnings;
}

// Example usage
try {
    const stakedAmount = 1000; // Example staked amount in $MBAG tokens
    const potentialEarnings = calculateStakingEarnings(stakedAmount);
    console.log(`Potential earnings from staking $${stakedAmount} $MBAG tokens at 88% APY: $${potentialEarnings.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
