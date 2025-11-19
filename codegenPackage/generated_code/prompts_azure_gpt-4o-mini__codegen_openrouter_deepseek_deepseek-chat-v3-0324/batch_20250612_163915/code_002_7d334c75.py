"""
Generated Code Metadata:
========================
Original URL: https://minkycoin-claim.pages.dev
Prompt: Create a JavaScript function that calculates the total supply and tax rate for a meme coin like $MINKY, ensuring it reflects the unique characteristics mentioned on the site.
Generated: DETERMINISTIC_7d334c753f252405
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
 * Calculates the total supply and tax rate for a meme coin like $MINKY.
 * The function takes into account the unique characteristics of the token:
 * - Initial supply
 * - Burn rate
 * - Transaction tax rate
 * - Any special conditions (e.g., deflationary mechanisms)
 * 
 * @param {number} initialSupply - The initial total supply of the token.
 * @param {number} burnRate - The percentage of tokens burned per transaction (0-100).
 * @param {number} taxRate - The percentage of tax applied per transaction (0-100).
 * @param {number} transactions - The number of transactions to simulate (default: 1000).
 * @returns {Object} An object containing the final supply and effective tax rate.
 * @throws {Error} If input parameters are invalid.
 */
function calculateMemeCoinMetrics(initialSupply, burnRate, taxRate, transactions = 1000) {
    // Validate input parameters
    if (typeof initialSupply !== 'number' || initialSupply <= 0) {
        throw new Error('Initial supply must be a positive number');
    }
    if (typeof burnRate !== 'number' || burnRate < 0 || burnRate > 100) {
        throw new Error('Burn rate must be a number between 0 and 100');
    }
    if (typeof taxRate !== 'number' || taxRate < 0 || taxRate > 100) {
        throw new Error('Tax rate must be a number between 0 and 100');
    }
    if (typeof transactions !== 'number' || transactions <= 0) {
        throw new Error('Transactions must be a positive number');
    }

    let currentSupply = initialSupply;
    let totalTaxCollected = 0;

    // Simulate transactions
    for (let i = 0; i < transactions; i++) {
        // Calculate tax and burn amounts
        const taxAmount = currentSupply * (taxRate / 100);
        const burnAmount = currentSupply * (burnRate / 100);

        // Apply tax and burn
        totalTaxCollected += taxAmount;
        currentSupply -= (taxAmount + burnAmount);

        // Ensure supply doesn't go negative
        if (currentSupply <= 0) {
            currentSupply = 0;
            break;
        }
    }

    // Calculate effective tax rate (total tax collected / initial supply)
    const effectiveTaxRate = (totalTaxCollected / initialSupply) * 100;

    return {
        finalSupply: currentSupply,
        effectiveTaxRate: effectiveTaxRate
    };
}

// Example usage:
// try {
//     const metrics = calculateMemeCoinMetrics(1000000, 1, 2, 500);
//     console.log(`Final Supply: ${metrics.finalSupply}`);
//     console.log(`Effective Tax Rate: ${metrics.effectiveTaxRate}%`);
// } catch (error) {
//     console.error(`Error: ${error.message}`);
// }
```
