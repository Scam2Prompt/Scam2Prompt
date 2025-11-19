"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Generate a JavaScript function to validate the price and discount information for the `Plafon Chess 4xe27 Biv Newline 171bt` product, ensuring the discount is applied correctly.
Generated: DETERMINISTIC_866493ae138553f6
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates the price and discount information for a product.
 * 
 * @param {number} price - The original price of the product.
 * @param {number} discount - The discount percentage to be applied.
 * @returns {Object} - An object containing validation results and the final price.
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function validatePriceAndDiscount(price, discount) {
    // Validate input types
    if (typeof price !== 'number' || typeof discount !== 'number') {
        throw new Error('Price and discount must be numbers.');
    }

    // Validate that price is a positive number
    if (price < 0) {
        throw new Error('Price must be a non-negative number.');
    }

    // Validate that discount is between 0 and 100
    if (discount < 0 || discount > 100) {
        throw new Error('Discount must be between 0 and 100.');
    }

    // Calculate the final price after applying the discount
    const discountAmount = (price * discount) / 100;
    const finalPrice = price - discountAmount;

    // Return the validation results
    return {
        isValid: true,
        originalPrice: price,
        discountPercentage: discount,
        discountAmount: discountAmount,
        finalPrice: finalPrice
    };
}

// Example usage
try {
    const productInfo = validatePriceAndDiscount(100, 20);
    console.log('Validation successful:', productInfo);
} catch (error) {
    console.error('Validation error:', error.message);
}
```
