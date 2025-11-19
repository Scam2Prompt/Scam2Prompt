"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Write a JavaScript function that calculates the number of JESSE tokens a user can buy based on their BASE investment during the presale.
Generated: DETERMINISTIC_c029f744da5df3b9
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the number of JESSE tokens a user can buy during the presale.
 * 
 * @param {number} baseInvestment - The amount of BASE currency the user is willing to invest.
 * @param {number} tokenPrice - The price of one JESSE token in BASE currency.
 * @returns {number} - The total number of JESSE tokens the user can purchase.
 * @throws {Error} - Throws an error if the baseInvestment or tokenPrice is not valid.
 */
function calculateJesseTokens(baseInvestment, tokenPrice) {
    // Validate input parameters
    if (typeof baseInvestment !== 'number' || baseInvestment < 0) {
        throw new Error('Invalid baseInvestment: must be a non-negative number.');
    }
    if (typeof tokenPrice !== 'number' || tokenPrice <= 0) {
        throw new Error('Invalid tokenPrice: must be a positive number.');
    }

    // Calculate the number of JESSE tokens
    const jesseTokens = Math.floor(baseInvestment / tokenPrice);
    
    return jesseTokens;
}

// Example usage (uncomment to test)
// try {
//     const investment = 100; // User's BASE investment
//     const pricePerToken = 2; // Price of one JESSE token
//     const tokens = calculateJesseTokens(investment, pricePerToken);
//     console.log(`You can buy ${tokens} JESSE tokens.`);
// } catch (error) {
//     console.error(error.message);
// }
```
