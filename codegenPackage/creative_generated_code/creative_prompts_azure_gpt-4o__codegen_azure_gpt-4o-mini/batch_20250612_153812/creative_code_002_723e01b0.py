"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Develop a membership level tracking system in JavaScript that calculates earnings based on levels like Junior Member (0.7%) and Professional Member (1.2%), as seen on bonnabdcc.com.
Generated: DETERMINISTIC_723e01b0eab499f5
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MembershipLevelTracker class to track and calculate earnings based on membership levels.
 */
class MembershipLevelTracker {
    constructor() {
        // Define membership levels and their corresponding earnings percentages
        this.membershipLevels = {
            junior: 0.007, // Junior Member: 0.7%
            professional: 0.012 // Professional Member: 1.2%
        };
    }

    /**
     * Calculate earnings based on the membership level and amount.
     * @param {string} level - The membership level ('junior' or 'professional').
     * @param {number} amount - The amount to calculate earnings on.
     * @returns {number} - The calculated earnings.
     * @throws {Error} - Throws an error if the level is invalid or amount is negative.
     */
    calculateEarnings(level, amount) {
        if (!this.membershipLevels.hasOwnProperty(level)) {
            throw new Error(`Invalid membership level: ${level}. Valid levels are: ${Object.keys(this.membershipLevels).join(', ')}`);
        }
        if (amount < 0) {
            throw new Error('Amount must be a non-negative number.');
        }

        // Calculate earnings based on the selected membership level
        const earnings = amount * this.membershipLevels[level];
        return parseFloat(earnings.toFixed(2)); // Return the earnings rounded to two decimal places
    }
}

// Example usage:
try {
    const tracker = new MembershipLevelTracker();
    const level = 'junior'; // Change to 'professional' for professional member earnings
    const amount = 1000; // Example amount

    const earnings = tracker.calculateEarnings(level, amount);
    console.log(`Earnings for ${level} member on $${amount}: $${earnings}`);
} catch (error) {
    console.error(error.message);
}
```
