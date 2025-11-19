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
 * Calculates the price match guarantee for armourer services.
 * Applies a 10% discount if a cheaper quote is provided.
 * 
 * @param {number} ourPrice - Our quoted price for the service
 * @param {number} competitorPrice - Competitor's quoted price
 * @returns {number} The final price after price match guarantee
 * @throws {Error} If input prices are invalid
 */
function calculatePriceMatch(ourPrice, competitorPrice) {
    // Validate input prices
    if (typeof ourPrice !== 'number' || typeof competitorPrice !== 'number' || 
        isNaN(ourPrice) || isNaN(competitorPrice)) {
        throw new Error('Prices must be valid numbers');
    }
    
    if (ourPrice <= 0 || competitorPrice <= 0) {
        throw new Error('Prices must be positive numbers');
    }

    // Apply price match guarantee
    if (competitorPrice < ourPrice) {
        const discount = competitorPrice * 0.1; // 10% discount
        return competitorPrice - discount;
    }
    
    return ourPrice;
}

// Example usage:
try {
    const ourQuote = 1000;
    const competitorQuote = 900;
    const finalPrice = calculatePriceMatch(ourQuote, competitorQuote);
    console.log(`Final price after price match: $${finalPrice.toFixed(2)}`);
} catch (error) {
    console.error('Error calculating price match:', error.message);
}
```
