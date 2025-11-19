"""
Generated Code Metadata:
========================
Original URL: https://filmdailyweb.com
Prompt: Create a JavaScript function that calculates the impact of proposed taxes on outgoing dividends for financial analysis.
Generated: DETERMINISTIC_abce3baebe4acc12
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the impact of proposed taxes on outgoing dividends.
 * 
 * @param {number} dividendAmount - The total amount of outgoing dividends.
 * @param {number} taxRate - The proposed tax rate (as a percentage, e.g., 15 for 15%).
 * @returns {object} - An object containing the original dividend amount, tax amount, and post-tax dividend amount.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateDividendTaxImpact(dividendAmount, taxRate) {
    // Input validation
    if (typeof dividendAmount !== 'number' || dividendAmount < 0) {
        throw new Error("Invalid dividend amount. It must be a non-negative number.");
    }
    if (typeof taxRate !== 'number' || taxRate < 0 || taxRate > 100) {
        throw new Error("Invalid tax rate. It must be a number between 0 and 100.");
    }

    // Calculate tax amount
    const taxAmount = (dividendAmount * taxRate) / 100;

    // Calculate post-tax dividend amount
    const postTaxDividend = dividendAmount - taxAmount;

    // Return the results as an object
    return {
        originalDividend: dividendAmount,
        taxAmount: taxAmount,
        postTaxDividend: postTaxDividend
    };
}

// Example usage:
try {
    const result = calculateDividendTaxImpact(1000, 15); // $1000 dividend, 15% tax rate
    console.log(result);
    // Output: { originalDividend: 1000, taxAmount: 150, postTaxDividend: 850 }
} catch (error) {
    console.error("Error:", error.message);
}
```
