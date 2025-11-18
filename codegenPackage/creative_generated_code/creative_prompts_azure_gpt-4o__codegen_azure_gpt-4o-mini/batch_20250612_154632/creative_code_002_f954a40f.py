"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindexe.fx-inc.us
Prompt: Create a function in JavaScript that simulates the ranking badge system on Coindexe FX, where the rank increases based on total investment amounts.
Generated: DETERMINISTIC_f954a40f3bdccfd9
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the ranking badge system based on total investment amounts.
 * 
 * @param {number} totalInvestment - The total investment amount of the user.
 * @returns {string} - The rank badge corresponding to the total investment.
 * @throws {Error} - Throws an error if totalInvestment is not a number or is negative.
 */
function getRankBadge(totalInvestment) {
    // Validate input: check if totalInvestment is a number and not negative
    if (typeof totalInvestment !== 'number' || totalInvestment < 0) {
        throw new Error('Invalid input: totalInvestment must be a non-negative number.');
    }

    let badge;

    // Determine badge based on investment thresholds
    if (totalInvestment >= 10000) {
        badge = 'Platinum';
    } else if (totalInvestment >= 5000) {
        badge = 'Gold';
    } else if (totalInvestment >= 1000) {
        badge = 'Silver';
    } else if (totalInvestment >= 100) {
        badge = 'Bronze';
    } else {
        badge = 'No Badge';
    }

    return badge;
}

// Example usage (uncomment to test):
// try {
//     console.log(getRankBadge(12000)); // Output: Platinum
//     console.log(getRankBadge(6000));  // Output: Gold
//     console.log(getRankBadge(1500));  // Output: Silver
//     console.log(getRankBadge(200));   // Output: Bronze
//     console.log(getRankBadge(50));    // Output: No Badge
//     console.log(getRankBadge(-100));  // Throws error
// } catch (error) {
//     console.error(error.message);
// }
```
