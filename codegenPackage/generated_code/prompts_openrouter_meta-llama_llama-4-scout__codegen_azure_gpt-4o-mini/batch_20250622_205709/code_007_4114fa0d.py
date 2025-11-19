"""
Generated Code Metadata:
========================
Original URL: https://freshnglow.in
Prompt: Write a JavaScript code snippet to implement a discount calculator for Fresh N Glow's e-commerce platform, applying discounts based on product categories, customer loyalty programs, and order totals.
Generated: DETERMINISTIC_4114fa0dc48d6c81
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Discount Calculator for Fresh N Glow's E-commerce Platform
 * This module calculates discounts based on product categories,
 * customer loyalty programs, and order totals.
 */

/**
 * Enum for product categories
 * @enum {number}
 */
const ProductCategory = {
    BEAUTY: 0.1, // 10% discount
    SKINCARE: 0.15, // 15% discount
    HAIRCARE: 0.2, // 20% discount
    OTHER: 0 // No discount
};

/**
 * Enum for customer loyalty levels
 * @enum {number}
 */
const LoyaltyLevel = {
    NONE: 0,
    SILVER: 0.05, // 5% discount
    GOLD: 0.1, // 10% discount
    PLATINUM: 0.15 // 15% discount
};

/**
 * Calculates the total discount based on product category, loyalty level, and order total.
 * @param {number} orderTotal - The total amount of the order before discounts.
 * @param {string} category - The category of the product.
 * @param {string} loyaltyLevel - The loyalty level of the customer.
 * @returns {number} - The total discount amount.
 * @throws {Error} - Throws an error if the category or loyalty level is invalid.
 */
function calculateDiscount(orderTotal, category, loyaltyLevel) {
    // Validate inputs
    if (typeof orderTotal !== 'number' || orderTotal < 0) {
        throw new Error('Invalid order total. It must be a non-negative number.');
    }

    if (!Object.keys(ProductCategory).includes(category)) {
        throw new Error('Invalid product category.');
    }

    if (!Object.keys(LoyaltyLevel).includes(loyaltyLevel)) {
        throw new Error('Invalid loyalty level.');
    }

    // Calculate category discount
    const categoryDiscount = ProductCategory[category] || 0;
    // Calculate loyalty discount
    const loyaltyDiscount = LoyaltyLevel[loyaltyLevel] || 0;

    // Calculate total discount
    const totalDiscount = orderTotal * (categoryDiscount + loyaltyDiscount);
    
    // Ensure total discount does not exceed order total
    return Math.min(totalDiscount, orderTotal);
}

// Example usage
try {
    const orderTotal = 100; // Example order total
    const category = 'SKINCARE'; // Example product category
    const loyaltyLevel = 'GOLD'; // Example customer loyalty level

    const discount = calculateDiscount(orderTotal, category, loyaltyLevel);
    console.log(`Total discount applied: $${discount.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating discount: ${error.message}`);
}
```
