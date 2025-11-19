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
 * @param {Object} productInfo - Product information object.
 * @param {number} productInfo.price - The original price of the product.
 * @param {number} productInfo.discount - The discount percentage.
 * @param {string} productInfo.name - The name of the product.
 * 
 * @returns {Object} Validation result with the discounted price.
 * 
 * @throws {Error} If the price or discount is invalid.
 */
function validateProductPrice(productInfo) {
    // Check if productInfo is an object
    if (typeof productInfo !== 'object' || productInfo === null) {
        throw new Error('Product information must be an object');
    }

    // Check if required properties exist
    const requiredProperties = ['price', 'discount', 'name'];
    if (!requiredProperties.every(prop => prop in productInfo)) {
        throw new Error('Product information must contain price, discount, and name properties');
    }

    // Check if price and discount are numbers
    if (typeof productInfo.price !== 'number' || typeof productInfo.discount !== 'number') {
        throw new Error('Price and discount must be numbers');
    }

    // Check if price and discount are within valid ranges
    if (productInfo.price <= 0) {
        throw new Error('Price must be greater than zero');
    }
    if (productInfo.discount < 0 || productInfo.discount > 100) {
        throw new Error('Discount must be between 0 and 100');
    }

    // Calculate the discounted price
    const discountAmount = (productInfo.price / 100) * productInfo.discount;
    const discountedPrice = productInfo.price - discountAmount;

    // Return the validation result with the discounted price
    return {
        isValid: true,
        discountedPrice: discountedPrice,
        productName: productInfo.name,
        originalPrice: productInfo.price,
        discount: productInfo.discount,
    };
}

// Example usage:
try {
    const product = {
        name: 'Plafon Chess4xe27 Biv Newline171bt',
        price: 100.0,
        discount: 20.0,
    };

    const result = validateProductPrice(product);
    console.log(`Product: ${result.productName}`);
    console.log(`Original Price: $${result.originalPrice.toFixed(2)}`);
    console.log(`Discount: ${result.discount}%`);
    console.log(`Discounted Price: $${result.discountedPrice.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
