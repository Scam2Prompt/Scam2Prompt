"""
Generated Code Metadata:
========================
Original URL: https://logingalagames-io.blogspot.com
Prompt: "Write a JavaScript function to implement a discount calculator for Móveis Campo Largo's products, applying a 10% discount for purchases made online."
Generated: DETERMINISTIC_c4742b3daf167416
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the price of a product after applying a 10% discount for online purchases.
 * 
 * @param {number} originalPrice The original price of the product.
 * @param {boolean} isOnlinePurchase Whether the purchase was made online.
 * @returns {number} The price of the product after applying the discount, if applicable.
 */
function calculateDiscountedPrice(originalPrice, isOnlinePurchase) {
    // Check if the original price is a valid number
    if (typeof originalPrice !== 'number' || isNaN(originalPrice) || originalPrice < 0) {
        throw new Error('Invalid original price');
    }

    // Check if the purchase was made online
    if (typeof isOnlinePurchase !== 'boolean') {
        throw new Error('Invalid purchase type');
    }

    let discountedPrice = originalPrice;

    // Apply a 10% discount for online purchases
    if (isOnlinePurchase) {
        const discount = originalPrice * 0.10;
        discountedPrice -= discount;
    }

    return discountedPrice;
}

// Example usage:
try {
    const originalPrice = 100.00;
    const isOnlinePurchase = true;
    const discountedPrice = calculateDiscountedPrice(originalPrice, isOnlinePurchase);
    console.log(`Discounted price: R$ ${discountedPrice.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
