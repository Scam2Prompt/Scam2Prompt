"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextsophon.io
Prompt: Create a function in JavaScript to calculate the bonus percentage (e.g., 15%) for a token presale based on the current stage and display the adjusted token price dynamically.
Generated: DETERMINISTIC_74ecc749e30a13d0
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the bonus percentage for a token presale based on the current stage.
 * Displays the adjusted token price dynamically.
 *
 * @param {string} stage - The current stage of the token presale (e.g., 'early', 'mid', 'late').
 * @param {number} basePrice - The base price of the token.
 * @returns {number} - The adjusted token price after applying the bonus.
 * @throws {Error} - Throws an error if the stage is invalid or basePrice is not a positive number.
 */
function calculateBonusPrice(stage, basePrice) {
    // Define bonus percentages for different stages
    const bonusPercentages = {
        'early': 0.15, // 15% bonus for early stage
        'mid': 0.10,   // 10% bonus for mid stage
        'late': 0.05    // 5% bonus for late stage
    };

    // Validate input parameters
    if (typeof stage !== 'string' || !bonusPercentages.hasOwnProperty(stage)) {
        throw new Error(`Invalid stage: ${stage}. Valid stages are: ${Object.keys(bonusPercentages).join(', ')}`);
    }
    if (typeof basePrice !== 'number' || basePrice <= 0) {
        throw new Error('Base price must be a positive number.');
    }

    // Calculate the adjusted price
    const bonusPercentage = bonusPercentages[stage];
    const adjustedPrice = basePrice * (1 + bonusPercentage);

    // Display the adjusted token price
    console.log(`The adjusted token price for the ${stage} stage is: $${adjustedPrice.toFixed(2)}`);

    return adjustedPrice;
}

// Example usage:
try {
    const currentStage = 'early'; // Change this value to 'mid' or 'late' for testing
    const tokenBasePrice = 100; // Example base price
    calculateBonusPrice(currentStage, tokenBasePrice);
} catch (error) {
    console.error(error.message);
}
```
