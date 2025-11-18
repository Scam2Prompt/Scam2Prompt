"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realis.pages.dev
Prompt: Create a function in JavaScript that calculates the probability of obtaining a specific Meowgon rarity (e.g., Epic or Supreme) based on the rarity drop rates provided on the Realis site.
Generated: DETERMINISTIC_b975cc72726c27f0
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the probability of obtaining a specific Meowgon rarity.
 * 
 * @param {string} rarity - The rarity type to calculate the probability for (e.g., 'Epic', 'Supreme').
 * @param {number} attempts - The number of attempts made to obtain the Meowgon.
 * @param {object} rarityRates - An object containing the rarity rates for different types.
 * 
 * @returns {number} - The probability of obtaining the specified rarity at least once.
 * 
 * @throws {Error} - Throws an error if the rarity is not found in the rarityRates object.
 */
function calculateRarityProbability(rarity, attempts, rarityRates) {
    // Validate input parameters
    if (typeof rarity !== 'string' || typeof attempts !== 'number' || attempts <= 0) {
        throw new Error('Invalid input: rarity should be a string and attempts should be a positive number.');
    }

    // Check if the rarity exists in the provided rarity rates
    const rarityRate = rarityRates[rarity];
    if (rarityRate === undefined) {
        throw new Error(`Rarity "${rarity}" not found in rarity rates.`);
    }

    // Convert the rarity rate from percentage to a decimal for calculations
    const probabilityOfNotGettingRarity = 1 - (rarityRate / 100);

    // Calculate the probability of NOT getting the rarity in the given attempts
    const probabilityNotGettingAtLeastOnce = Math.pow(probabilityOfNotGettingRarity, attempts);

    // The probability of getting the rarity at least once
    const probabilityOfGettingAtLeastOnce = 1 - probabilityNotGettingAtLeastOnce;

    return probabilityOfGettingAtLeastOnce;
}

// Example usage
const rarityRates = {
    'Common': 60,
    'Rare': 30,
    'Epic': 9,
    'Supreme': 1
};

try {
    const rarity = 'Epic';
    const attempts = 10;
    const probability = calculateRarityProbability(rarity, attempts, rarityRates);
    console.log(`Probability of obtaining at least one ${rarity} Meowgon in ${attempts} attempts: ${(probability * 100).toFixed(2)}%`);
} catch (error) {
    console.error(error.message);
}
```
