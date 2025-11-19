"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Create a function in JavaScript that checks the eligibility for the 1.45x APR multiplier for matured positions in Bedrock's staking system.
Generated: DETERMINISTIC_ec0c37cf5e9a42ef
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check eligibility for the 1.45x APR multiplier in Bedrock's staking system.
 * 
 * @param {Object} position - The staking position object containing relevant details.
 * @param {number} position.stakedAmount - The amount staked in the position (in tokens).
 * @param {Date} position.startDate - The date when the position was started (ISO date format).
 * @param {Date} position.maturityDate - The date when the position matures (ISO date format).
 * @param {boolean} position.isWithdrawn - Indicates if the position has been withdrawn prematurely.
 * 
 * @returns {boolean} - Returns true if the position is eligible for the 1.45x APR multiplier, false otherwise.
 */
function isEligibleForAPRMultiplier(position) {
    try {
        // Validate input: Ensure position object and required properties exist
        if (!position || typeof position !== 'object') {
            throw new Error('Invalid position object.');
        }
        const { stakedAmount, startDate, maturityDate, isWithdrawn } = position;

        if (
            typeof stakedAmount !== 'number' ||
            !(startDate instanceof Date) ||
            !(maturityDate instanceof Date) ||
            typeof isWithdrawn !== 'boolean'
        ) {
            throw new Error('Invalid properties in position object.');
        }

        // Check if the staked amount meets the minimum requirement (example: 100 tokens)
        const MINIMUM_STAKE_AMOUNT = 100;
        if (stakedAmount < MINIMUM_STAKE_AMOUNT) {
            return false;
        }

        // Check if the position has reached maturity
        const currentDate = new Date();
        if (currentDate < maturityDate) {
            return false;
        }

        // Check if the position was withdrawn prematurely
        if (isWithdrawn) {
            return false;
        }

        // If all conditions are met, the position is eligible
        return true;

    } catch (error) {
        // Log error for debugging purposes
        console.error('Error checking eligibility:', error.message);
        return false; // Default to not eligible in case of error
    }
}

// Example Usage:
// const stakingPosition = {
//     stakedAmount: 150,
//     startDate: new Date('2023-01-01'),
//     maturityDate: new Date('2023-10-01'),
//     isWithdrawn: false
// };
// console.log(isEligibleForAPRMultiplier(stakingPosition)); // Output: true or false
```
