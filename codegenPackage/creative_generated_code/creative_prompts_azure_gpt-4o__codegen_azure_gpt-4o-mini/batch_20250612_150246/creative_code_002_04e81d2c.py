"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elixinvestmentltd.info
Prompt: Develop a referral commission calculator in JavaScript for RystonFX Trading's 3-level affiliate program, incorporating the 4%, 0.5%, and 0.5% commission rates.
Generated: DETERMINISTIC_04e81d2cc437c78a
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Referral Commission Calculator for RystonFX Trading
 * This program calculates the commission commissions based on a 3-level affiliate program:
 * - Level 1: 4%
 * - Level 2: 0.5%
 * - Level 3: 0.5%
 * 
 * Author: Your Name
 * Date: 2023-10-01
 */

/**
 * Calculates the commission for a given amount and level.
 * @param {number} amount - The total amount for which the commission is to be calculated.
 * @param {number} level - The level of the affiliate (1, 2, or 3).
 * @returns {number} - The calculated commission.
 * @throws {Error} - Throws an error if the level is not valid.
 */
function calculateCommission(amount, level) {
    // Validate input
    if (typeof amount !== 'number' || amount < 0) {
        throw new Error('Amount must be a non-negative number.');
    }
    if (![1, 2, 3].includes(level)) {
        throw new Error('Level must be 1, 2, or 3.');
    }

    // Define commission rates
    const commissionRates = {
        1: 0.04, // 4%
        2: 0.005, // 0.5%
        3: 0.005  // 0.5%
    };

    // Calculate commission
    const commission = amount * commissionRates[level];
    return parseFloat(commission.toFixed(2)); // Return value rounded to 2 decimal places
}

/**
 * Main function to demonstrate the commission calculations.
 */
function main() {
    // Example amounts and levels to calculate commissions
    const transactions = [
        { amount: 1000, level: 1 },
        { amount: 2000, level: 2 },
        { amount: 1500, level: 3 }
    ];

    // Calculate and display commissions
    transactions.forEach(transaction => {
        try {
            const commission = calculateCommission(transaction.amount, transaction.level);
            console.log(`Commission for amount $${transaction.amount} at level ${transaction.level}: $${commission}`);
        } catch (error) {
            console.error(`Error calculating commission for amount $${transaction.amount} at level ${transaction.level}: ${error.message}`);
        }
    });
}

// Run the main function
main();
```
