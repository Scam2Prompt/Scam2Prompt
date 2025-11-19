"""
Generated Code Metadata:
========================
Original URL: https://blur-nft-marketplace.org
Prompt: Generate a JavaScript function to calculate the discount percentage for a product on sale, similar to the "-90%" discount shown for a product priced at Rp.10.000 to Rp.100.000.
Generated: DETERMINISTIC_aaf2b991dfcdf800
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the discount percentage based on original and sale prices.
 * 
 * @param {number} originalPrice - The original price of the product.
 * @param {number} salePrice - The discounted price of the product.
 * @returns {number} The discount percentage rounded to the nearest integer.
 * @throws {Error} If prices are invalid (non-positive numbers or sale price > original price).
 */
function calculateDiscountPercentage(originalPrice, salePrice) {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || typeof salePrice !== 'number' || 
        originalPrice <= 0 || salePrice <= 0) {
        throw new Error('Prices must be positive numbers');
    }
    
    if (salePrice > originalPrice) {
        throw new Error('Sale price cannot be greater than original price');
    }

    // Calculate discount percentage and round to nearest integer
    const discount = ((originalPrice - salePrice) / originalPrice) * 100;
    return Math.round(discount);
}

// Example usage:
// try {
//     const discount = calculateDiscountPercentage(100000, 10000);
//     console.log(`Discount: ${discount}%`); // Output: Discount: 90%
// } catch (error) {
//     console.error(error.message);
// }
```
