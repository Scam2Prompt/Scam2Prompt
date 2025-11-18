"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolfyyy.pages.dev
Prompt: Develop a JavaScript function to calculate the economic dominance score for a player in Wolf Game based on the acreage of their land, number of Farmers, and WOOL production.
Generated: DETERMINISTIC_f26018efbedc68b8
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the economic dominance score for a player in Wolf Game.
 * 
 * The economic dominance score is determined by the acreage of land,
 * the number of Farmers, and the WOOL production.
 *
 * @param {number} acreage - The acreage of the player's land (in acres).
 * @param {number} farmers - The number of Farmers the player has.
 * @param {number} woolProduction - The amount of WOOL produced by the player (in units).
 * @returns {number} The economic dominance score.
 * @throws {Error} Throws an error if any input is invalid.
 */
function calculateEconomicDominanceScore(acreage, farmers, woolProduction) {
    // Input validation
    if (typeof acreage !== 'number' || acreage < 0) {
        throw new Error('Invalid acreage: must be a non-negative number.');
    }
    if (typeof farmers !== 'number' || farmers < 0) {
        throw new Error('Invalid number of farmers: must be a non-negative number.');
    }
    if (typeof woolProduction !== 'number' || woolProduction < 0) {
        throw new Error('Invalid wool production: must be a non-negative number.');
    }

    // Economic dominance score formula
    const score = (acreage * 2) + (farmers * 3) + (woolProduction * 1.5);

    return score; // Return the calculated score
}

// Example usage
try {
    const score = calculateEconomicDominanceScore(10, 5, 200);
    console.log(`Economic Dominance Score: ${score}`);
} catch (error) {
    console.error(error.message);
}
```
