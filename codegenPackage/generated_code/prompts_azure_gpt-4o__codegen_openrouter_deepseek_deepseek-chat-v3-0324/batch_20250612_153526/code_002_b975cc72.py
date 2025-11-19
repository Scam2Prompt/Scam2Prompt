"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Create a function in JavaScript that calculates the probability of obtaining a specific Meowgon rarity (e.g., Epic or Supreme) based on the rarity drop rates provided on the Realis site.
Generated: DETERMINISTIC_b975cc72726c27f0
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the probability of obtaining a specific Meowgon rarity based on given drop rates.
 * 
 * @param {string} targetRarity - The desired rarity (e.g., 'Epic', 'Supreme').
 * @param {Object} dropRates - An object mapping rarities to their drop rates (e.g., { Common: 0.7, Epic: 0.2, Supreme: 0.1 }).
 * @returns {number} The probability of obtaining the target rarity (0 if rarity is not found).
 * @throws {Error} If dropRates is not an object or targetRarity is not a string.
 */
function calculateMeowgonProbability(targetRarity, dropRates) {
    // Validate input types
    if (typeof targetRarity !== 'string') {
        throw new Error('targetRarity must be a string');
    }
    if (typeof dropRates !== 'object' || dropRates === null) {
        throw new Error('dropRates must be an object');
    }

    // Normalize the target rarity to handle case insensitivity
    const normalizedTarget = targetRarity.trim().toLowerCase();
    let probability = 0;

    // Iterate through drop rates to find the target rarity
    for (const [rarity, rate] of Object.entries(dropRates)) {
        if (rarity.toLowerCase() === normalizedTarget) {
            probability = rate;
            break;
        }
    }

    // Ensure probability is a valid number
    if (typeof probability !== 'number' || isNaN(probability)) {
        return 0;
    }

    return probability;
}

// Example usage:
// const dropRates = { Common: 0.7, Epic: 0.2, Supreme: 0.1 };
// const probability = calculateMeowgonProbability('Epic', dropRates);
// console.log(probability); // Output: 0.2
```
