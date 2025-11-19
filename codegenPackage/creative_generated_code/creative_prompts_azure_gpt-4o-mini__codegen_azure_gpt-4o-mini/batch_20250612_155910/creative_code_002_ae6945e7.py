"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Create a JavaScript function that calculates the tokenomics for a cryptocurrency with a 0% tax rate, similar to the Crypto Burger model.
Generated: DETERMINISTIC_ae6945e71314f056
Batch ID: 20250612_155910
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This function calculates the tokenomics for a cryptocurrency model
 * with a 0% tax rate, similar to the Crypto Burger model.
 * 
 * @param {number} initialSupply - The initial total supply of the cryptocurrency.
 * @param {number} circulatingSupply - The amount of tokens currently in circulation.
 * @param {number} tokenPrice - The current price of the token in the market.
 * @returns {Object} - An object containing tokenomics details.
 * @throws {Error} - Throws an error if the inputs are invalid.
 */
function calculateTokenomics(initialSupply, circulatingSupply, tokenPrice) {
    // Validate inputs
    if (typeof initialSupply !== 'number' || initialSupply <= 0) {
        throw new Error('Invalid initial supply: must be a positive number.');
    }
    if (typeof circulatingSupply !== 'number' || circulatingSupply < 0) {
        throw new Error('Invalid circulating supply: must be a non-negative number.');
    }
    if (typeof tokenPrice !== 'number' || tokenPrice <= 0) {
        throw new Error('Invalid token price: must be a positive number.');
    }

    // Calculate market capitalization
    const marketCap = circulatingSupply * tokenPrice;

    // Calculate total supply ratio
    const totalSupplyRatio = circulatingSupply / initialSupply;

    // Prepare tokenomics data
    const tokenomics = {
        initialSupply: initialSupply,
        circulatingSupply: circulatingSupply,
        tokenPrice: tokenPrice,
        marketCap: marketCap,
        totalSupplyRatio: totalSupplyRatio,
        taxRate: 0 // 0% tax rate
    };

    return tokenomics;
}

// Example usage (uncomment to test)
// try {
//     const tokenomics = calculateTokenomics(1000000, 500000, 2.5);
//     console.log(tokenomics);
// } catch (error) {
//     console.error(error.message);
// }
```
