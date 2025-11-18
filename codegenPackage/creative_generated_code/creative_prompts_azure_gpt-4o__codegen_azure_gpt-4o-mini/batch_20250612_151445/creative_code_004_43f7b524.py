"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.shibaswaap.us.com
Prompt: Write a function in JavaScript to calculate payout ratios for various betting types, including kèo chấp, kèo tài xỉu, and special bets, as mentioned in 789Club’s sports betting section.
Generated: DETERMINISTIC_43f7b52489bc72f3
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates payout ratios for various betting types.
 * 
 * @param {string} betType - The type of bet (kèo chấp, kèo tài xỉu, special).
 * @param {number} stake - The amount of money wagered.
 * @param {number} odds - The odds associated with the bet.
 * @returns {number} - The potential payout from the bet.
 * @throws {Error} - Throws an error if the bet type is invalid or if stake or odds are negative.
 */
function calculatePayoutRatio(betType, stake, odds) {
    // Validate inputs
    if (stake < 0 || odds < 0) {
        throw new Error('Stake and odds must be non-negative numbers.');
    }

    // Define payout ratios for different bet types
    const payoutRatios = {
        'kèo chấp': 1.9,  // Example payout ratio for kèo chấp
        'kèo tài xỉu': 1.8, // Example payout ratio for kèo tài xỉu
        'special': 2.0     // Example payout ratio for special bets
    };

    // Check if the bet type is valid
    if (!(betType in payoutRatios)) {
        throw new Error(`Invalid bet type: ${betType}. Valid types are: ${Object.keys(payoutRatios).join(', ')}`);
    }

    // Calculate the potential payout
    const payout = stake * odds * payoutRatios[betType];

    return payout;
}

// Example usage:
try {
    const betType = 'kèo tài xỉu';
    const stake = 100; // amount wagered
    const odds = 1.5;  // odds associated with the bet
    const payout = calculatePayoutRatio(betType, stake, odds);
    console.log(`Potential payout for ${betType}: ${payout.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating payout: ${error.message}`);
}
```
