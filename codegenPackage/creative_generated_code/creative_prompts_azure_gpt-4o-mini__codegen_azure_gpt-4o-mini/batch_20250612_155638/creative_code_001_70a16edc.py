"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletguard.pro
Prompt: Write a JavaScript function that calculates potential winnings based on the betting strategies discussed in the "how much to bet poker" section of walletguard.pro.
Generated: DETERMINISTIC_70a16edcea3f3272
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential winnings based on a specified betting strategy.
 * The function supports various betting strategies, including Fixed Bet,
 * Percentage of Bankroll, and Martingale.
 *
 * @param {number} bankroll - The total amount of money available for betting.
 * @param {number} bet - The amount of money to bet based on the selected strategy.
 * @param {string} strategy - The betting strategy to use ("fixed", "percentage", "martingale").
 * @param {number} [winMultiplier=2] - The multiplier for winnings (default is 2 for even bets).
 * @returns {number} - The potential winnings based on the strategy.
 * @throws Will throw an error if the inputs are invalid.
 */
function calculateWinnings(bankroll, bet, strategy, winMultiplier = 2) {
    // Input validation
    if (typeof bankroll !== 'number' || typeof bet !== 'number' || typeof strategy !== 'string') {
        throw new Error('Invalid input types. Bankroll and bet must be numbers, strategy must be a string.');
    }
    if (bankroll <= 0 || bet <= 0) {
        throw new Error('Bankroll and bet must be greater than 0.');
    }
    if (!['fixed', 'percentage', 'martingale'].includes(strategy.toLowerCase())) {
        throw new Error('Invalid betting strategy. Please choose "fixed", "percentage", or "martingale".');
    }

    let potentialWinnings;

    // Calculate potential winnings based on the chosen strategy
    switch (strategy.toLowerCase()) {
        case 'fixed':
            // Fixed bet strategy
            if (bet > bankroll) {
                throw new Error('Bet cannot exceed the bankroll.');
            }
            potentialWinnings = bet * winMultiplier;
            break;

        case 'percentage':
            // Percentage of bankroll strategy
            const percentageBet = (bet / 100) * bankroll;
            if (percentageBet > bankroll) {
                throw new Error('Calculated percentage bet cannot exceed the bankroll.');
            }
            potentialWinnings = percentageBet * winMultiplier;
            break;

        case 'martingale':
            // Martingale betting strategy
            potentialWinnings = bet * winMultiplier; // Potential winnings if the bet wins
            if (bet > bankroll) {
                throw new Error('Bet cannot exceed the bankroll for Martingale strategy.');
            }
            break;

        default:
            throw new Error('Unhandled betting strategy.');
    }

    return potentialWinnings;
}

// Example Usage
try {
    const bankroll = 1000; // Total bankroll
    const bet = 50; // Amount to bet
    const strategy = 'fixed'; // Betting strategy
    const winnings = calculateWinnings(bankroll, bet, strategy);
    console.log(`Potential winnings: $${winnings}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
