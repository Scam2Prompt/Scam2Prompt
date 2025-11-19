"""
Generated Code Metadata:
========================
Original URL: https://www.bsc-scan.net
Prompt: Create a function in JavaScript that calculates affiliate earnings based on the three-level affiliate program percentages (5%, 2%, 0.5%) described on the BSC Scan website.
Generated: DETERMINISTIC_e5e4b7113148680c
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates affiliate earnings based on a three-level affiliate program.
 * @param {number} amount - The total transaction amount.
 * @param {Object} [options] - Optional configuration.
 * @param {number} [options.level1Percent=5] - Percentage for level 1 (direct referral).
 * @param {number} [options.level2Percent=2] - Percentage for level 2 (indirect referral).
 * @param {number} [options.level3Percent=0.5] - Percentage for level 3 (second indirect referral).
 * @returns {Object} An object containing earnings for each level and the total.
 * @throws {Error} If the input amount is invalid.
 */
function calculateAffiliateEarnings(amount, options = {}) {
    // Validate input
    if (typeof amount !== 'number' || isNaN(amount) || amount <= 0) {
        throw new Error('Invalid amount: must be a positive number');
    }

    // Set default percentages if not provided
    const {
        level1Percent = 5,
        level2Percent = 2,
        level3Percent = 0.5
    } = options;

    // Validate percentages
    const validatePercentage = (percent, level) => {
        if (typeof percent !== 'number' || isNaN(percent) || percent < 0) {
            throw new Error(`Invalid percentage for level ${level}: must be a non-negative number`);
        }
    };
    validatePercentage(level1Percent, 1);
    validatePercentage(level2Percent, 2);
    validatePercentage(level3Percent, 3);

    // Calculate earnings for each level
    const level1Earnings = (amount * level1Percent) / 100;
    const level2Earnings = (amount * level2Percent) / 100;
    const level3Earnings = (amount * level3Percent) / 100;

    // Calculate total earnings
    const totalEarnings = level1Earnings + level2Earnings + level3Earnings;

    return {
        level1: parseFloat(level1Earnings.toFixed(2)),
        level2: parseFloat(level2Earnings.toFixed(2)),
        level3: parseFloat(level3Earnings.toFixed(2)),
        total: parseFloat(totalEarnings.toFixed(2))
    };
}
```
