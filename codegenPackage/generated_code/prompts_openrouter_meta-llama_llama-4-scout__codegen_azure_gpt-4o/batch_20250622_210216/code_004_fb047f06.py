"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-en.web.app
Prompt: Create a simple calculator in JavaScript to estimate the potential value of DOGE20 tokens after a price increase, given the current presale price and the amount of tokens purchased.
Generated: DETERMINISTIC_fb047f06d25806ca
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator to Estimate Potential Value of DOGE20 Tokens
 * 
 * This script calculates the potential value of DOGE20 tokens after a price increase,
 * given the current presale price and the amount of tokens purchased.
 * 
 * Usage:
 * Call the `calculatePotentialValue` function with the following parameters:
 * - presalePrice: Current price of one DOGE20 token during presale (in USD).
 * - priceIncrease: Expected price increase percentage (e.g., 50 for 50% increase).
 * - tokensPurchased: Number of DOGE20 tokens purchased.
 * 
 * Example:
 * const result = calculatePotentialValue(0.01, 50, 1000);
 * console.log(result); // Outputs the potential value in USD.
 */

// Function to calculate the potential value of DOGE20 tokens
function calculatePotentialValue(presalePrice, priceIncrease, tokensPurchased) {
    try {
        // Input validation
        if (typeof presalePrice !== 'number' || presalePrice <= 0) {
            throw new Error("Invalid presale price. It must be a positive number.");
        }
        if (typeof priceIncrease !== 'number' || priceIncrease < 0) {
            throw new Error("Invalid price increase percentage. It must be a non-negative number.");
        }
        if (typeof tokensPurchased !== 'number' || tokensPurchased <= 0) {
            throw new Error("Invalid number of tokens purchased. It must be a positive number.");
        }

        // Calculate the new price after the increase
        const newPrice = presalePrice * (1 + priceIncrease / 100);

        // Calculate the potential value of the tokens
        const potentialValue = newPrice * tokensPurchased;

        // Return the result
        return potentialValue.toFixed(2); // Return value rounded to 2 decimal places
    } catch (error) {
        // Handle errors gracefully
        console.error("Error calculating potential value:", error.message);
        return null; // Return null in case of an error
    }
}

// Example usage
const presalePrice = 0.01; // Current presale price in USD
const priceIncrease = 50; // Expected price increase percentage
const tokensPurchased = 1000; // Number of tokens purchased

const potentialValue = calculatePotentialValue(presalePrice, priceIncrease, tokensPurchased);
if (potentialValue !== null) {
    console.log(`The potential value of your DOGE20 tokens is $${potentialValue} USD.`);
} else {
    console.log("Failed to calculate the potential value due to an error.");
}
```
