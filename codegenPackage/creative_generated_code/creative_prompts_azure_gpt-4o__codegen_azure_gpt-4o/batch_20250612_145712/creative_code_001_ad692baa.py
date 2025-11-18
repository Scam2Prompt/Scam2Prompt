"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerinde.com
Prompt: Create a function in JavaScript that multiplies the number of coins earned per click based on user upgrades, as described in the "Verbessern Sie Ihre Klicks" section of the TG WebApp Euro Verdienen webpage.
Generated: DETERMINISTIC_ad692baa29b71f96
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Multiplies the number of coins earned per click based on user upgrades.
 * 
 * This function calculates the total coins earned per click by applying
 * multipliers from the user's upgrades. Each upgrade increases the multiplier,
 * enhancing the coins earned per click.
 * 
 * @param {number} baseCoinsPerClick - The base number of coins earned per click without upgrades.
 * @param {Array<number>} upgradeMultipliers - An array of multipliers (e.g., [1.5, 2, 3]) from user upgrades.
 * @returns {number} - The total number of coins earned per click after applying all upgrades.
 * 
 * Example Usage:
 * const totalCoins = calculateCoinsPerClick(10, [1.5, 2, 3]);
 * console.log(totalCoins); // Output: 90
 */
function calculateCoinsPerClick(baseCoinsPerClick, upgradeMultipliers) {
    try {
        // Input validation
        if (typeof baseCoinsPerClick !== 'number' || baseCoinsPerClick <= 0) {
            throw new Error("baseCoinsPerClick must be a positive number.");
        }

        if (!Array.isArray(upgradeMultipliers)) {
            throw new Error("upgradeMultipliers must be an array of numbers.");
        }

        if (!upgradeMultipliers.every(multiplier => typeof multiplier === 'number' && multiplier > 0)) {
            throw new Error("All elements in upgradeMultipliers must be positive numbers.");
        }

        // Calculate the total multiplier by multiplying all upgrade multipliers
        const totalMultiplier = upgradeMultipliers.reduce((acc, multiplier) => acc * multiplier, 1);

        // Calculate and return the total coins earned per click
        return baseCoinsPerClick * totalMultiplier;

    } catch (error) {
        console.error("Error calculating coins per click:", error.message);
        return 0; // Return 0 in case of an error
    }
}

// Example usage
const baseCoins = 10; // Base coins earned per click
const upgrades = [1.5, 2, 3]; // Multipliers from user upgrades
const totalCoins = calculateCoinsPerClick(baseCoins, upgrades);
console.log("Total Coins Per Click:", totalCoins); // Output: 90
```
