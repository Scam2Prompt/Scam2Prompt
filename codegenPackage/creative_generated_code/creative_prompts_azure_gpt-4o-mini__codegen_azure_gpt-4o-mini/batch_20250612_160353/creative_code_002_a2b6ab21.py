"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-rayduim.github.io
Prompt: Generate a JavaScript function that calculates impermanent loss for a liquidity provider on Raydium, considering different price scenarios.
Generated: DETERMINISTIC_a2b6ab213104537d
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates impermanent loss for a liquidity provider on Raydium.
 * 
 * @param {number} initialPrice - The initial price of the asset pair.
 * @param {number} finalPrice - The final price of the asset pair after price changes.
 * @param {number} liquidityAmount - The total amount of liquidity provided by the user.
 * @returns {number} - The impermanent loss as a percentage.
 * @throws {Error} - Throws an error if inputs are not valid numbers or less than or equal to zero.
 */
function calculateImpermanentLoss(initialPrice, finalPrice, liquidityAmount) {
    // Validate inputs
    if (typeof initialPrice !== 'number' || typeof finalPrice !== 'number' || typeof liquidityAmount !== 'number') {
        throw new Error('All inputs must be numbers.');
    }
    if (initialPrice <= 0 || finalPrice <= 0 || liquidityAmount <= 0) {
        throw new Error('Initial price, final price, and liquidity amount must be greater than zero.');
    }

    // Calculate the amount of tokens if held separately
    const tokenAAmount = liquidityAmount / 2; // Assume equal distribution for simplicity
    const tokenBAmount = liquidityAmount / 2;

    // Calculate the value if held separately
    const initialValue = (tokenAAmount * initialPrice) + (tokenBAmount * initialPrice);
    const finalValue = (tokenAAmount * finalPrice) + (tokenBAmount * finalPrice);
    
    // Calculate the value in the liquidity pool
    const poolValue = liquidityAmount * Math.sqrt(finalPrice / initialPrice);

    // Calculate impermanent loss
    const impermanentLoss = ((initialValue - poolValue) / initialValue) * 100;

    return impermanentLoss;
}

// Example usage (uncomment to run):
// try {
//     const il = calculateImpermanentLoss(100, 150, 1000);
//     console.log(`Impermanent Loss: ${il.toFixed(2)}%`);
// } catch (error) {
//     console.error(error.message);
// }
```
