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
 * Function to check eligibility for the 1.45x APR multiplier for matured positions
 * in Bedrock's staking system.
 *
 * @param {Object} position - The staking position object.
 * @param {number} position.amount - The amount staked in the position.
 * @param {Date} position.maturityDate - The date when the position matures.
 * @param {number} position.minimumAmount - The minimum amount required for eligibility.
 * @returns {boolean} - Returns true if eligible for the multiplier, otherwise false.
 * @throws {Error} - Throws an error if the position object is invalid.
 */
function isEligibleForMultiplier(position) {
    // Validate input
    if (!position || typeof position !== 'object') {
        throw new Error('Invalid position object provided.');
    }
  
    const { amount, maturityDate, minimumAmount } = position;

    // Check for required properties
    if (typeof amount !== 'number' || typeof minimumAmount !== 'number' || !(maturityDate instanceof Date)) {
        throw new Error('Position must contain valid amount, maturityDate, and minimumAmount.');
    }

    // Check if the position has matured
    const currentDate = new Date();
    const hasMatured = maturityDate <= currentDate;

    // Check if the amount staked meets the minimum required for eligibility
    const meetsMinimumAmount = amount >= minimumAmount;

    // Determine eligibility
    const isEligible = hasMatured && meetsMinimumAmount;

    return isEligible;
}

// Example usage
try {
    const stakingPosition = {
        amount: 1000,
        maturityDate: new Date('2023-10-01'),
        minimumAmount: 500,
    };
    
    const eligible = isEligibleForMultiplier(stakingPosition);
    console.log(`Is eligible for multiplier: ${eligible}`);
} catch (error) {
    console.error(`Error checking eligibility: ${error.message}`);
}
```
