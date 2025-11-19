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
 * Calculates the price match guarantee for hiring armourer services.
 * 
 * @param {number} ourQuote - The quote provided by Powered Production Film Services.
 * @param {number} competitorQuote - The quote provided by a competitor.
 * @returns {number} The final price after applying the price match guarantee.
 */
function calculatePriceMatchGuarantee(ourQuote, competitorQuote) {
    // Check if inputs are valid numbers
    if (typeof ourQuote !== 'number' || typeof competitorQuote !== 'number') {
        throw new Error('Both ourQuote and competitorQuote must be numbers');
    }

    // Check if quotes are non-negative
    if (ourQuote < 0 || competitorQuote < 0) {
        throw new Error('Both ourQuote and competitorQuote must be non-negative');
    }

    // If competitor's quote is cheaper, apply 10% discount to our quote
    if (competitorQuote < ourQuote) {
        // Calculate the discount amount
        const discountAmount = ourQuote * 0.1;
        // Apply the discount
        const finalPrice = ourQuote - discountAmount;
        return finalPrice;
    } else {
        // If our quote is already the cheapest, return it as is
        return ourQuote;
    }
}

/**
 * Calculates the price match guarantee for hiring armourer services with an additional fee.
 * 
 * @param {number} ourQuote - The quote provided by Powered Production Film Services.
 * @param {number} competitorQuote - The quote provided by a competitor.
 * @param {number} additionalFee - Any additional fees.
 * @returns {number} The final price after applying the price match guarantee.
 */
function calculatePriceMatchGuaranteeWithAdditionalFee(ourQuote, competitorQuote, additionalFee) {
    // Check if inputs are valid numbers
    if (typeof ourQuote !== 'number' || typeof competitorQuote !== 'number' || typeof additionalFee !== 'number') {
        throw new Error('All inputs must be numbers');
    }

    // Check if quotes and additional fee are non-negative
    if (ourQuote < 0 || competitorQuote < 0 || additionalFee < 0) {
        throw new Error('All inputs must be non-negative');
    }

    // Calculate the total our quote with additional fee
    const ourTotalQuote = ourQuote + additionalFee;

    // If competitor's quote is cheaper, apply 10% discount to our total quote
    if (competitorQuote < ourTotalQuote) {
        // Calculate the discount amount
        const discountAmount = ourTotalQuote * 0.1;
        // Apply the discount
        const finalPrice = ourTotalQuote - discountAmount;
        return finalPrice;
    } else {
        // If our quote is already the cheapest, return it as is
        return ourTotalQuote;
    }
}

// Example usage:
try {
    const ourQuote = 1000;
    const competitorQuote = 900;
    const finalPrice = calculatePriceMatchGuarantee(ourQuote, competitorQuote);
    console.log(`The final price is: $${finalPrice.toFixed(2)}`);

    const ourQuoteWithFee = 1000;
    const competitorQuoteWithFee = 900;
    const additionalFeeWithFee = 100;
    const finalPriceWithFee = calculatePriceMatchGuaranteeWithAdditionalFee(ourQuoteWithFee, competitorQuoteWithFee, additionalFeeWithFee);
    console.log(`The final price with additional fee is: $${finalPriceWithFee.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
