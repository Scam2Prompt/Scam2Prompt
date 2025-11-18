"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memegames-web.pages.dev
Prompt: Write a function in JavaScript to calculate the 25% bonus on $MGMES token purchases when a user's selected meme athlete wins an event.
Generated: DETERMINISTIC_5d847be988526a85
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the 25% bonus on $MGMES token purchases.
 * 
 * @param {number} purchaseAmount - The amount of $MGMES tokens purchased.
 * @param {boolean} athleteWon - Indicates if the selected meme athlete won the event.
 * @returns {number} - The total amount of tokens including the bonus if applicable.
 * @throws {Error} - Throws an error if purchaseAmount is negative or not a number.
 */
function calculateBonus(purchaseAmount, athleteWon) {
    // Validate input
    if (typeof purchaseAmount !== 'number' || purchaseAmount < 0) {
        throw new Error('Invalid purchase amount. It must be a non-negative number.');
    }

    // Calculate the bonus only if the athlete has won
    const bonusPercentage = 0.25; // 25% bonus
    let totalTokens = purchaseAmount;

    if (athleteWon) {
        // Calculate bonus and add it to the total tokens
        const bonusAmount = purchaseAmount * bonusPercentage;
        totalTokens += bonusAmount;
    }

    return totalTokens;
}

// Example usage
try {
    const purchaseAmount = 100; // Example purchase amount
    const athleteWon = true; // Example event result
    const total = calculateBonus(purchaseAmount, athleteWon);
    console.log(`Total tokens after bonus: ${total}`);
} catch (error) {
    console.error(`Error calculating bonus: ${error.message}`);
}
```
