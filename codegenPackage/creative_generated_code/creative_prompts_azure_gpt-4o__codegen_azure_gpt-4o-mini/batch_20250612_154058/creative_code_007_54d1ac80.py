"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonanzavc.com
Prompt: Provide code to calculate cumulative earnings for different membership levels (e.g., Junior Member, Intermediate Member, etc.) using JavaScript, based on the percentages provided on BonanzaVC.
Generated: DETERMINISTIC_54d1ac809f9c340a
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates cumulative earnings for different membership levels.
 * 
 * @param {Object} levels - An object containing membership levels and their respective earnings percentages.
 * @param {number} initialInvestment - The initial amount of money invested.
 * @param {number} months - The number of months to calculate the cumulative earnings for.
 * @returns {Object} - An object containing the cumulative earnings for each membership level.
 * @throws {Error} - Throws an error if input values are invalid.
 */
function calculateCumulativeEarnings(levels, initialInvestment, months) {
    // Validate input parameters
    if (typeof initialInvestment !== 'number' || initialInvestment < 0) {
        throw new Error('Initial investment must be a non-negative number.');
    }
    if (typeof months !== 'number' || months < 0) {
        throw new Error('Months must be a non-negative number.');
    }
    if (typeof levels !== 'object' || levels === null) {
        throw new Error('Levels must be a valid object with membership levels.');
    }

    const cumulativeEarnings = {};

    // Iterate through each membership level
    for (const [level, percentage] of Object.entries(levels)) {
        // Validate the percentage value
        if (typeof percentage !== 'number' || percentage < 0 || percentage > 100) {
            throw new Error(`Percentage for ${level} must be a number between 0 and 100.`);
        }
        
        let totalEarnings = initialInvestment;

        // Calculate cumulative earnings over the specified months
        for (let month = 1; month <= months; month++) {
            totalEarnings += totalEarnings * (percentage / 100);
        }

        // Store the cumulative earnings in the result object
        cumulativeEarnings[level] = totalEarnings.toFixed(2); // Round to 2 decimal places
    }

    return cumulativeEarnings;
}

// Example usage
try {
    const membershipLevels = {
        'Junior Member': 5, // 5% earnings
        'Intermediate Member': 10, // 10% earnings
        'Senior Member': 15 // 15% earnings
    };
    
    const initialInvestment = 1000; // Initial investment amount
    const months = 12; // Calculation for 12 months

    const earnings = calculateCumulativeEarnings(membershipLevels, initialInvestment, months);
    console.log('Cumulative Earnings:', earnings);
} catch (error) {
    console.error('Error calculating cumulative earnings:', error.message);
}
```
