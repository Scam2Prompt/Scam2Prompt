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
 * Function to calculate the discount percentage for a product on sale.
 * 
 * @param {number} originalPrice - The original price of the product.
 * @param {number} salePrice - The sale price of the product.
 * @returns {string} - The discount percentage as a string (e.g., "-90%").
 * @throws {Error} - Throws an error if inputs are invalid or if originalPrice is less than or equal to salePrice.
 */
function calculateDiscountPercentage(originalPrice, salePrice) {
    // Validate input types
    if (typeof originalPrice !== 'number' || typeof salePrice !== 'number') {
        throw new Error("Both originalPrice and salePrice must be numbers.");
    }

    // Validate input values
    if (originalPrice <= 0 || salePrice < 0) {
        throw new Error("Prices must be positive numbers. originalPrice must be greater than 0.");
    }

    if (salePrice >= originalPrice) {
        throw new Error("Sale price must be less than the original price to calculate a discount.");
    }

    // Calculate the discount percentage
    const discountPercentage = ((originalPrice - salePrice) / originalPrice) * 100;

    // Return the formatted discount percentage
    return `-${discountPercentage.toFixed(0)}%`;
}

// Example usage:
try {
    const originalPrice = 100000; // Rp.100.000
    const salePrice = 10000;     // Rp.10.000
    console.log(calculateDiscountPercentage(originalPrice, salePrice)); // Output: "-90%"
} catch (error) {
    console.error(error.message);
}
```
