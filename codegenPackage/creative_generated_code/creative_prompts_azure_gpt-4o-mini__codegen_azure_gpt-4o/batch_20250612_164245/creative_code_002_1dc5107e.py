"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tronofficial.com
Prompt: Create a JavaScript function that calculates potential winnings from online bets, incorporating the betting examples mentioned on tronofficial.com.
Generated: DETERMINISTIC_1dc5107e7d31fb86
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates potential winnings from online bets based on odds and stake.
 * 
 * @param {number} stake - The amount of money being bet (in currency units).
 * @param {number} odds - The odds for the bet in decimal format (e.g., 1.5, 2.0).
 * @returns {number} - The potential winnings (including stake).
 * @throws {Error} - If input values are invalid (negative numbers or zero).
 */
function calculatePotentialWinnings(stake, odds) {
    // Input validation
    if (typeof stake !== 'number' || typeof odds !== 'number') {
        throw new Error("Invalid input: Stake and odds must be numbers.");
    }
    if (stake <= 0 || odds <= 0) {
        throw new Error("Invalid input: Stake and odds must be greater than zero.");
    }

    // Calculate winnings
    const winnings = stake * odds;

    // Return calculated winnings
    return winnings;
}

// Usage Example:
// const stake = 100; // Amount of money being bet
// const odds = 2.5;  // Decimal odds (e.g., 2.5 means you win 2.5x your stake)
// console.log(`Potential Winnings: ${calculatePotentialWinnings(stake, odds)}`);
// Output: Potential Winnings: 250
```
