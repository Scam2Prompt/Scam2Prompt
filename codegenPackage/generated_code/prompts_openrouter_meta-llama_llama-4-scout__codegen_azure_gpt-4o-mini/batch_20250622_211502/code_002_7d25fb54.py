"""
Generated Code Metadata:
========================
Original URL: https://1xfa.club
Prompt: Generate a simple sports betting odds calculator using JavaScript, inspired by BaxBet's sports betting section.
Generated: DETERMINISTIC_7d25fb543317b814
Batch ID: 20250622_211502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sports Betting Odds Calculator
 * This program calculates potential winnings based on the odds and the stake amount.
 * It supports both fractional and decimal odds formats.
 */

/**
 * Function to calculate potential winnings
 * @param {number} stake - The amount of money being wagered.
 * @param {number} odds - The odds of the bet, can be in decimal or fractional format.
 * @returns {number} - The potential winnings.
 * @throws {Error} - Throws an error if the stake or odds are invalid.
 */
function calculateWinnings(stake, odds) {
    // Validate stake
    if (typeof stake !== 'number' || stake <= 0) {
        throw new Error('Invalid stake amount. It must be a positive number.');
    }

    // Validate odds
    if (typeof odds !== 'number' || odds <= 0) {
        throw new Error('Invalid odds. It must be a positive number.');
    }

    // Calculate potential winnings
    const potentialWinnings = stake * odds;
    return potentialWinnings;
}

/**
 * Function to display the results
 * @param {number} stake - The amount of money being wagered.
 * @param {number} odds - The odds of the bet.
 */
function displayResults(stake, odds) {
    try {
        const winnings = calculateWinnings(stake, odds);
        console.log(`Stake: $${stake.toFixed(2)}`);
        console.log(`Odds: ${odds}`);
        console.log(`Potential Winnings: $${winnings.toFixed(2)}`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// Example usage
const stakeAmount = 100; // Example stake amount
const oddsValue = 2.5;   // Example odds in decimal format

displayResults(stakeAmount, oddsValue);
```
