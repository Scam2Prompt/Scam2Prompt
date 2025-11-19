"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: Create a JavaScript function that calculates potential earnings from participating in CowSwap's Fair Sales.
Generated: DETERMINISTIC_d750b75e124401aa
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates potential earnings from participating in CowSwap's Fair Sales.
 * 
 * @param {number} initialInvestment - The amount of money invested in the Fair Sale.
 * @param {number} salePrice - The expected sale price of the token after the Fair Sale.
 * @param {number} tokenAmount - The amount of tokens received from the Fair Sale.
 * @returns {number} - The potential earnings from the investment.
 * @throws {Error} - Throws an error if any input is invalid (negative or non-numeric).
 */
function calculatePotentialEarnings(initialInvestment, salePrice, tokenAmount) {
    // Validate inputs
    if (typeof initialInvestment !== 'number' || initialInvestment < 0) {
        throw new Error('Invalid initial investment. It must be a non-negative number.');
    }
    if (typeof salePrice !== 'number' || salePrice < 0) {
        throw new Error('Invalid sale price. It must be a non-negative number.');
    }
    if (typeof tokenAmount !== 'number' || tokenAmount < 0) {
        throw new Error('Invalid token amount. It must be a non-negative number.');
    }

    // Calculate potential earnings
    const potentialEarnings = (salePrice * tokenAmount) - initialInvestment;

    // Return potential earnings, ensuring it is not negative
    return Math.max(potentialEarnings, 0);
}

// Example usage
try {
    const initialInvestment = 1000; // Example investment amount
    const salePrice = 10;           // Example expected sale price per token
    const tokenAmount = 150;        // Example number of tokens received

    const earnings = calculatePotentialEarnings(initialInvestment, salePrice, tokenAmount);
    console.log(`Potential Earnings: $${earnings}`);
} catch (error) {
    console.error(`Error calculating potential earnings: ${error.message}`);
}
```
