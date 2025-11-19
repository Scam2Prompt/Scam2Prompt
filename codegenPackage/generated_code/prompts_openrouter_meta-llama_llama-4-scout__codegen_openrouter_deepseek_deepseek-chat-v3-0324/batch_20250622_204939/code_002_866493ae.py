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
 * Validates the price and discount information for the Plafon Chess 4xe27 Biv Newline 171bt product.
 * @param {number} originalPrice - The original price of the product (must be positive)
 * @param {number} discountPercentage - The discount percentage (must be between 0 and 100)
 * @param {number} discountedPrice - The claimed discounted price
 * @returns {Object} An object containing validation results and messages
 */
function validateProductPricing(originalPrice, discountPercentage, discountedPrice) {
    // Validate input types and ranges
    if (typeof originalPrice !== 'number' || typeof discountPercentage !== 'number' || typeof discountedPrice !== 'number') {
        return {
            isValid: false,
            message: 'All parameters must be numbers'
        };
    }

    if (originalPrice <= 0) {
        return {
            isValid: false,
            message: 'Original price must be greater than 0'
        };
    }

    if (discountPercentage < 0 || discountPercentage > 100) {
        return {
            isValid: false,
            message: 'Discount percentage must be between 0 and 100'
        };
    }

    if (discountedPrice <= 0) {
        return {
            isValid: false,
            message: 'Discounted price must be greater than 0'
        };
    }

    // Calculate expected discounted price
    const expectedDiscountedPrice = originalPrice * (1 - discountPercentage / 100);
    const roundedExpectedPrice = Math.round(expectedDiscountedPrice * 100) / 100; // Round to 2 decimal places

    // Compare with provided discounted price (allow small rounding differences)
    const priceDifference = Math.abs(roundedExpectedPrice - discountedPrice);
    const isPriceValid = priceDifference < 0.01; // Allow 1 cent difference due to rounding

    if (!isPriceValid) {
        return {
            isValid: false,
            message: `Discount calculation mismatch. Expected: $${roundedExpectedPrice.toFixed(2)}, Actual: $${discountedPrice.toFixed(2)}`
        };
    }

    return {
        isValid: true,
        message: 'Price and discount information is valid',
        originalPrice: originalPrice,
        discountPercentage: discountPercentage,
        expectedDiscountedPrice: roundedExpectedPrice,
        providedDiscountedPrice: discountedPrice
    };
}

// Example usage:
// const validation = validateProductPricing(100, 20, 80);
// console.log(validation);
```
