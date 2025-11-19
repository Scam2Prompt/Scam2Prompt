"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: Create a JavaScript function to calculate the total amount raised in USDT for a presale event, referencing the BOI Coin presale model.
Generated: DETERMINISTIC_a5c2a60554fa9ded
Batch ID: 20250612_135202
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total amount raised in USDT for a presale event.
 * 
 * @param {Array<Object>} contributions - An array of contribution objects.
 * @param {string} contributions[].contributor - The address of the contributor.
 * @param {number} contributions[].amount - The amount contributed in USDT.
 * @returns {number} - The total amount raised in USDT.
 * @throws {Error} - Throws error if input is not valid.
 */
function calculateTotalRaised(contributions) {
    // Validate input is an array
    if (!Array.isArray(contributions)) {
        throw new Error('Input must be an array of contributions.');
    }

    let totalRaised = 0;

    // Iterate through contributions and accumulate the total amount
    contributions.forEach(contribution => {
        // Validate each contribution object
        if (typeof contribution !== 'object' || contribution === null) {
            throw new Error('Each contribution must be a valid object.');
        }
        if (typeof contribution.amount !== 'number' || contribution.amount < 0) {
            throw new Error('Contribution amount must be a non-negative number.');
        }

        // Accumulate the total amount
        totalRaised += contribution.amount;
    });

    return totalRaised;
}

// Example usage
try {
    const contributions = [
        { contributor: '0x123...', amount: 100 },
        { contributor: '0x456...', amount: 250 },
        { contributor: '0x789...', amount: 50 }
    ];
    
    const total = calculateTotalRaised(contributions);
    console.log(`Total amount raised in USDT: ${total}`);
} catch (error) {
    console.error(`Error calculating total raised: ${error.message}`);
}
```
