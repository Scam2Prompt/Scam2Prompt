"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Generate code in JavaScript to calculate the price match guarantee for hiring armourer services, including a 10% discount if a cheaper quote is provided, as described on the Powered Production Film Services website.
Generated: DETERMINISTIC_bfb6a8ebcdaf427b
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the final price for hiring armourer services based on a price match guarantee.
 * If a cheaper quote is provided, a 10% discount is applied to the original price.
 *
 * @param {number} originalPrice - The original price for the armourer services.
 * @param {number} competitorQuote - The competitor's quote for the same services.
 * @returns {number} - The final price after applying the price match guarantee and discount if applicable.
 * @throws {Error} - Throws an error if the input values are not valid numbers or if they are negative.
 */
function calculatePriceMatchGuarantee(originalPrice, competitorQuote) {
    // Validate input
    if (typeof originalPrice !== 'number' || typeof competitorQuote !== 'number') {
        throw new Error('Both originalPrice and competitorQuote must be numbers.');
    }
    if (originalPrice < 0 || competitorQuote < 0) {
        throw new Error('Prices must be non-negative.');
    }

    // Check if the competitor's quote is cheaper
    if (competitorQuote < originalPrice) {
        // Apply a 10% discount on the original price
        const discount = originalPrice * 0.10;
        const finalPrice = originalPrice - discount;
        return parseFloat(finalPrice.toFixed(2)); // Return the final price rounded to 2 decimal places
    }

    // If the competitor's quote is not cheaper, return the original price
    return parseFloat(originalPrice.toFixed(2)); // Return the original price rounded to 2 decimal places
}

// Example usage
try {
    const originalPrice = 1000; // Original price for the services
    const competitorQuote = 900; // Competitor's quote
    const finalPrice = calculatePriceMatchGuarantee(originalPrice, competitorQuote);
    console.log(`The final price for the armourer services is: $${finalPrice}`);
} catch (error) {
    console.error(`Error calculating price: ${error.message}`);
}
```
