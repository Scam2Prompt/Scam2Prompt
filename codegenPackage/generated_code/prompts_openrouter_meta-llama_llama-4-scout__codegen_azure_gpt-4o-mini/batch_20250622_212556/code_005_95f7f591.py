"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: "Create a JavaScript function to implement a simple discount calculator for products like the 3D Energy Globe, considering different discount rates."
Generated: DETERMINISTIC_95f7f5916292b969
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the final price of a product after applying a discount.
 * 
 * @param {number} originalPrice - The original price of the product.
 * @param {number} discountRate - The discount rate as a percentage (0-100).
 * @returns {number} - The final price after discount.
 * @throws {Error} - Throws an error if the original price or discount rate is invalid.
 */
function calculateDiscount(originalPrice, discountRate) {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || originalPrice < 0) {
        throw new Error('Invalid original price. It must be a non-negative number.');
    }
    if (typeof discountRate !== 'number' || discountRate < 0 || discountRate > 100) {
        throw new Error('Invalid discount rate. It must be a number between 0 and 100.');
    }

    // Calculate the discount amount
    const discountAmount = (originalPrice * discountRate) / 100;

    // Calculate the final price after discount
    const finalPrice = originalPrice - discountAmount;

    return finalPrice;
}

// Example usage
try {
    const productName = "3D Energy Globe";
    const originalPrice = 49.99; // Original price in dollars
    const discountRate = 20; // Discount rate in percentage

    const finalPrice = calculateDiscount(originalPrice, discountRate);
    console.log(`The final price of the ${productName} after a ${discountRate}% discount is $${finalPrice.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
