"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appscottyclaims.pages.dev
Prompt: Create a function in JavaScript that calculates a user's share of the staking pool and their estimated annual returns percentage for Scotty AI token staking.
Generated: DETERMINISTIC_637d7839f940d55a
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the user's share of the staking pool 
 * and their estimated annual returns percentage for Scotty AI token staking.
 * 
 * @param {number} userStake - The amount of tokens the user has staked.
 * @param {number} totalStake - The total amount of tokens in the staking pool.
 * @param {number} annualReward - The total annual rewards distributed for the staking pool.
 * @returns {Object} - An object containing the user's share of the pool and estimated annual return percentage.
 * @throws {Error} - Throws an error if inputs are invalid (negative or zero).
 */
function calculateStakingReturns(userStake, totalStake, annualReward) {
    // Input validation: Check if inputs are valid numbers and greater than zero
    if (typeof userStake !== 'number' || typeof totalStake !== 'number' || typeof annualReward !== 'number') {
        throw new Error('Invalid input type: All inputs must be numbers.');
    }
    if (userStake <= 0 || totalStake <= 0 || annualReward < 0) {
        throw new Error('Invalid input value: Stakes must be greater than zero and rewards cannot be negative.');
    }
    
    // Calculate user's share of the staking pool
    const userShare = userStake / totalStake;

    // Calculate estimated annual returns percentage
    const estimatedAnnualReturns = (annualReward * userShare) / userStake * 100;

    return {
        userShare: userShare,
        estimatedAnnualReturns: estimatedAnnualReturns
    };
}

// Example usage (uncomment to test):
// try {
//     const result = calculateStakingReturns(1000, 10000, 500);
//     console.log(`User's Share: ${result.userShare}, Estimated Annual Returns: ${result.estimatedAnnualReturns}%`);
// } catch (error) {
//     console.error(error.message);
// }
```
