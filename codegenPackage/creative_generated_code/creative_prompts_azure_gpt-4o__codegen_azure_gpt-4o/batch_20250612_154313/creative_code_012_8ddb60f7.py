"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Create a JavaScript function to calculate payouts for WW88's "Kèo phạt góc" (corner betting) based on the site's guidelines.
Generated: DETERMINISTIC_8ddb60f7b2e26e55
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate payouts for WW88's "Kèo phạt góc" (corner betting).
 * 
 * @param {number} stake - The amount of money bet by the user.
 * @param {number} odds - The betting odds provided by WW88.
 * @param {boolean} isWin - Whether the user won the bet (true if won, false otherwise).
 * 
 * @returns {number} - The payout amount. Returns 0 if the user lost the bet.
 * 
 * @throws {Error} - Throws an error if inputs are invalid (e.g., negative stake or odds).
 */
function calculateCornerBetPayout(stake, odds, isWin) {
    // Input validation
    if (typeof stake !== 'number' || stake <= 0) {
        throw new Error("Invalid stake: Stake must be a positive number.");
    }
    if (typeof odds !== 'number' || odds <= 0) {
        throw new Error("Invalid odds: Odds must be a positive number.");
    }
    if (typeof isWin !== 'boolean') {
        throw new Error("Invalid isWin: Must be a boolean value.");
    }

    // If the user lost the bet, payout is 0
    if (!isWin) {
        return 0;
    }

    // Calculate payout for a winning bet
    const payout = stake * odds;

    // Ensure payout is rounded to two decimal places for precision
    return parseFloat(payout.toFixed(2));
}

// Example usage:
try {
    const stake = 100; // Amount bet by the user
    const odds = 1.85; // Example odds from WW88
    const isWin = true; // Example outcome: user won the bet

    const payout = calculateCornerBetPayout(stake, odds, isWin);
    console.log(`Payout Amount: $${payout}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
