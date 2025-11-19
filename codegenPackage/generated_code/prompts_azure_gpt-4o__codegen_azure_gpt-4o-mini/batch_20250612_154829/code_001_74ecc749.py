"""
Generated Code Metadata:
========================
Original URL: https://nextsophon.io
Prompt: Create a function in JavaScript to calculate the bonus percentage (e.g., 15%) for a token presale based on the current stage and display the adjusted token price dynamically.
Generated: DETERMINISTIC_74ecc749e30a13d0
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the bonus percentage based on the current presale stage.
 * @param {string} stage - The current stage of the presale (e.g., 'early', 'mid', 'late').
 * @returns {number} - The bonus percentage as a decimal (e.g., 0.15 for 15%).
 * @throws {Error} - Throws an error if the stage is invalid.
 */
function getBonusPercentage(stage) {
    const bonusStages = {
        'early': 0.15, // 15% bonus for early stage
        'mid': 0.10,   // 10% bonus for mid stage
        'late': 0.05    // 5% bonus for late stage
    };

    if (bonusStages.hasOwnProperty(stage)) {
        return bonusStages[stage];
    } else {
        throw new Error('Invalid presale stage. Valid stages are: early, mid, late.');
    }
}

/**
 * Calculates the adjusted token price based on the base price and current presale stage.
 * @param {number} basePrice - The base price of the token.
 * @param {string} stage - The current stage of the presale.
 * @returns {number} - The adjusted token price after applying the bonus.
 * @throws {Error} - Throws an error if the base price is negative or if the stage is invalid.
 */
function calculateAdjustedTokenPrice(basePrice, stage) {
    if (basePrice < 0) {
        throw new Error('Base price cannot be negative.');
    }

    const bonusPercentage = getBonusPercentage(stage);
    const adjustedPrice = basePrice * (1 + bonusPercentage);
    return adjustedPrice;
}

/**
 * Updates the displayed token price dynamically based on the current presale stage.
 * @param {number} basePrice - The base price of the token.
 * @param {string} stage - The current stage of the presale.
 */
function updateTokenPriceDisplay(basePrice, stage) {
    try {
        const adjustedPrice = calculateAdjustedTokenPrice(basePrice, stage);
        document.getElementById('tokenPriceDisplay').innerText = `Adjusted Token Price: $${adjustedPrice.toFixed(2)}`;
    } catch (error) {
        console.error(error.message);
        document.getElementById('tokenPriceDisplay').innerText = 'Error calculating token price.';
    }
}

// Example usage:
// Assuming there is an HTML element with id 'tokenPriceDisplay'
// updateTokenPriceDisplay(1.00, 'early'); // Adjusts the price for early stage
```
