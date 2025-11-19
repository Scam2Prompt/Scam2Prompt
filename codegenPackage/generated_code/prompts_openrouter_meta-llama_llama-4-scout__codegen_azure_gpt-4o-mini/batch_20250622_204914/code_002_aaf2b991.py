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
 * Calculates the discount percentage for a product on sale.
 *
 * @param {number} originalPrice - The original price of the product.
 * @param {number} salePrice - The sale price of the product.
 * @returns {string} The discount percentage formatted as a string with a '%' sign.
 * @throws {Error} Throws an error if the original price is less than or equal to zero,
 *                 or if the sale price is greater than or equal to the original price.
 */
function calculateDiscountPercentage(originalPrice, salePrice) {
    // Validate input parameters
    if (originalPrice <= 0) {
        throw new Error("Original price must be greater than zero.");
    }
    if (salePrice >= originalPrice) {
        throw new Error("Sale price must be less than the original price.");
    }

    // Calculate the discount amount
    const discountAmount = originalPrice - salePrice;

    // Calculate the discount percentage
    const discountPercentage = (discountAmount / originalPrice) * 100;

    // Return the discount percentage formatted as a string
    return `-${discountPercentage.toFixed(0)}%`;
}

// Example usage:
try {
    const originalPrice = 100000; // Original price in Rp
    const salePrice = 10000;      // Sale price in Rp
    const discount = calculateDiscountPercentage(originalPrice, salePrice);
    console.log(discount); // Output: -90%
} catch (error) {
    console.error(error.message);
}
```
