"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Generate code in JavaScript to calculate the price match guarantee for hiring armourer services, including a 10% discount if a cheaper quote is provided, as described on the Powered Production Film Services website.
Generated: DETERMINISTIC_bfb6a8ebcdaf427b
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the final price for hiring armourer services
 * based on a quote provided and the price match guarantee policy.
 * 
 * @param {number} originalPrice - The original price for the armourer services.
 * @param {number} competitorQuote - The competitor's quote for comparison.
 * @returns {number} - The final price after applying the price match guarantee and discount if applicable.
 * @throws {Error} - Throws an error if the input values are not valid numbers.
 */
function calculatePriceMatchGuarantee(originalPrice, competitorQuote) {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || typeof competitorQuote !== 'number') {
        throw new Error('Both originalPrice and competitorQuote must be valid numbers.');
    }
    
    if (originalPrice < 0 || competitorQuote < 0) {
        throw new Error('Prices cannot be negative.');
    }

    // Check if the competitor's quote is lower than the original price
    if (competitorQuote < originalPrice) {
        // Calculate the discounted price (10% off the original price)
        const discount = originalPrice * 0.10;
        const finalPrice = originalPrice - discount;
        return parseFloat(finalPrice.toFixed(2)); // Return the final price rounded to two decimal places
    }

    // If no discount applies, return the original price
    return parseFloat(originalPrice.toFixed(2)); // Return the original price rounded to two decimal places
}

// Example usage
try {
    const originalPrice = 500; // Original price for the service
    const competitorQuote = 450; // Competitor's quote

    const finalPrice = calculatePriceMatchGuarantee(originalPrice, competitorQuote);
    console.log(`The final price for the armourer services is: $${finalPrice}`);
} catch (error) {
    console.error(`Error calculating price: ${error.message}`);
}
```
