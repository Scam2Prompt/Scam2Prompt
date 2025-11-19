"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://filmdailyweb.com
Prompt: Create a JavaScript function that calculates the impact of proposed taxes on outgoing dividends for financial analysis.
Generated: DETERMINISTIC_abce3baebe4acc12
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the impact of proposed taxes on outgoing dividends.
 * 
 * @param {number} dividendAmount - The total amount of dividends being distributed.
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.2 for 20%).
 * @returns {object} - An object containing the net dividend and the tax amount.
 * @throws {Error} - Throws an error if the dividendAmount or taxRate is invalid.
 */
function calculateTaxImpactOnDividends(dividendAmount, taxRate) {
    // Validate input parameters
    if (typeof dividendAmount !== 'number' || dividendAmount < 0) {
        throw new Error('Invalid dividend amount. It must be a non-negative number.');
    }
    if (typeof taxRate !== 'number' || taxRate < 0 || taxRate > 1) {
        throw new Error('Invalid tax rate. It must be a number between 0 and 1.');
    }

    // Calculate the tax amount
    const taxAmount = dividendAmount * taxRate;

    // Calculate the net dividend after tax
    const netDividend = dividendAmount - taxAmount;

    // Return results as an object
    return {
        netDividend: parseFloat(netDividend.toFixed(2)), // Rounded to 2 decimal places
        taxAmount: parseFloat(taxAmount.toFixed(2)) // Rounded to 2 decimal places
    };
}

// Example usage
try {
    const result = calculateTaxImpactOnDividends(1000, 0.25);
    console.log(`Net Dividend: $${result.netDividend}, Tax Amount: $${result.taxAmount}`);
} catch (error) {
    console.error(error.message);
}
```
