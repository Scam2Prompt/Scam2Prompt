"""
Generated Code Metadata:
========================
Original URL: https://garmin-boutique.com
Prompt: Generate a JavaScript code to implement a discount calculator for Garmin products, similar to the 15% discount code "WEB15" offered on the website.
Generated: DETERMINISTIC_d140833a2badd3ac
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Discount Calculator for Garmin Products
 * This function calculates the final price after applying a discount code.
 * 
 * @param {number} originalPrice - The original price of the Garmin product.
 * @param {string} discountCode - The discount code to apply.
 * @returns {number} - The final price after applying the discount.
 * @throws {Error} - Throws an error if the original price is negative or if the discount code is invalid.
 */
function calculateDiscount(originalPrice, discountCode) {
    // Validate the original price
    if (typeof originalPrice !== 'number' || originalPrice < 0) {
        throw new Error('Invalid original price. It must be a non-negative number.');
    }

    // Define valid discount codes and their corresponding discount percentages
    const discountCodes = {
        'WEB15': 0.15 // 15% discount
    };

    // Check if the provided discount code is valid
    if (!discountCodes.hasOwnProperty(discountCode)) {
        throw new Error('Invalid discount code. Please provide a valid code.');
    }

    // Calculate the discount amount
    const discountPercentage = discountCodes[discountCode];
    const discountAmount = originalPrice * discountPercentage;

    // Calculate the final price after applying the discount
    const finalPrice = originalPrice - discountAmount;

    // Return the final price, rounded to two decimal places
    return parseFloat(finalPrice.toFixed(2));
}

// Example usage
try {
    const originalPrice = 100; // Example original price
    const discountCode = 'WEB15'; // Example discount code
    const finalPrice = calculateDiscount(originalPrice, discountCode);
    console.log(`The final price after applying the discount is: $${finalPrice}`);
} catch (error) {
    console.error(error.message);
}
```
