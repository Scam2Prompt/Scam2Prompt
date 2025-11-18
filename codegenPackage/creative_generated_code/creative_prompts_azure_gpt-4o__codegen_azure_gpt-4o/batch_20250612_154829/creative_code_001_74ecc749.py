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
 * Calculates the bonus percentage and dynamically adjusts the token price based on the presale stage.
 * 
 * @param {number} basePrice - The base price of the token.
 * @param {string} stage - The current stage of the presale (e.g., "early", "middle", "late").
 * @returns {number} - The adjusted token price with the bonus applied.
 * @throws {Error} - Throws an error if the stage is invalid or basePrice is not a positive number.
 */
function calculateTokenPrice(basePrice, stage) {
    // Validate input parameters
    if (typeof basePrice !== 'number' || basePrice <= 0) {
        throw new Error("Invalid base price. It must be a positive number.");
    }
    if (typeof stage !== 'string' || !['early', 'middle', 'late'].includes(stage.toLowerCase())) {
        throw new Error("Invalid presale stage. Must be one of: 'early', 'middle', 'late'.");
    }

    // Define bonus percentages for each stage
    const bonusPercentage = {
        early: 15,   // 15% bonus for the early stage
        middle: 10,  // 10% bonus for the middle stage
        late: 5      // 5% bonus for the late stage
    };

    // Convert the stage to lowercase to handle case-insensitive input
    const stageKey = stage.toLowerCase();

    // Calculate the bonus multiplier
    const bonusMultiplier = 1 + bonusPercentage[stageKey] / 100;

    // Calculate the adjusted token price
    const adjustedPrice = basePrice * bonusMultiplier;

    return adjustedPrice;
}

// Example usage:
try {
    const basePrice = 100; // Example base price
    const stage = "early"; // Example presale stage
    const adjustedPrice = calculateTokenPrice(basePrice, stage);
    console.log(`Adjusted Token Price (Stage: ${stage}): $${adjustedPrice}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
