"""
Generated Code Metadata:
========================
Original URL: https://minkycoin.pages.dev
Prompt: Create a JavaScript function to display the tokenomics of a meme coin, specifically for a token with a supply of 10,000,000,000 and a 0% tax rate.
Generated: DETERMINISTIC_712ed6fcd8669483
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays the tokenomics information for a meme coin.
 * 
 * @param {string} tokenName - The name of the token.
 * @param {number} totalSupply - The total supply of the token.
 * @param {number} taxRate - The tax rate applied to transactions (in percentage).
 * @returns {string} Formatted tokenomics information.
 * @throws {Error} If invalid parameters are provided.
 */
function displayTokenomics(tokenName, totalSupply, taxRate) {
    // Validate input parameters
    if (typeof tokenName !== 'string' || tokenName.trim() === '') {
        throw new Error('Token name must be a non-empty string.');
    }
    if (typeof totalSupply !== 'number' || totalSupply <= 0) {
        throw new Error('Total supply must be a positive number.');
    }
    if (typeof taxRate !== 'number' || taxRate < 0 || taxRate > 100) {
        throw new Error('Tax rate must be a number between 0 and 100.');
    }

    // Format large numbers with commas
    const formattedSupply = totalSupply.toLocaleString('en-US');

    // Generate tokenomics string
    const tokenomicsInfo = `
        Tokenomics for ${tokenName}:
        - Total Supply: ${formattedSupply} tokens
        - Tax Rate: ${taxRate}%
        - No transaction fees (0% tax)
    `;

    return tokenomicsInfo;
}

// Example usage
try {
    const tokenName = "MemeCoin";
    const totalSupply = 10000000000; // 10,000,000,000
    const taxRate = 0; // 0%

    const tokenomics = displayTokenomics(tokenName, totalSupply, taxRate);
    console.log
