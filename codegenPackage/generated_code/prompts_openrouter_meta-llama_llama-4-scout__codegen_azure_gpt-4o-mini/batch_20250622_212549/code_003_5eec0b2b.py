"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Create a JavaScript code snippet to implement a promotions and discounts system for an e-commerce website, like the ones offered on Somos Corujas, with conditions such as "buy one get one free" or "10% off on orders above $100".
Generated: DETERMINISTIC_5eec0b2b8222e4dc
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Promotions and Discounts System for E-commerce
 * This module handles various promotions and discounts applicable to orders.
 */

class Promotion {
    constructor(name, discountType, condition, value) {
        this.name = name; // Name of the promotion
        this.discountType = discountType; // Type of discount (percentage, fixed, BOGO)
        this.condition = condition; // Condition for the promotion to apply
        this.value = value; // Value of the discount
    }

    /**
     * Applies the promotion to the given order.
     * @param {Object} order - The order object containing total amount and items.
     * @returns {number} - The final amount after applying the promotion.
     */
    apply(order) {
        if (!this.isApplicable(order)) {
            return order.total; // Return original total if promotion is not applicable
        }

        switch (this.discountType) {
            case 'percentage':
                return this.applyPercentageDiscount(order.total);
            case 'fixed':
                return this.applyFixedDiscount(order.total);
            case 'BOGO':
                return this.applyBogoDiscount(order.items);
            default:
                throw new Error('Invalid discount type');
        }
    }

    /**
     * Checks if the promotion is applicable to the order.
     * @param {Object} order - The order object.
     * @returns {boolean} - True if applicable, false otherwise.
     */
    isApplicable(order) {
        if (this.condition.type === 'minAmount') {
            return order.total >= this.condition.value;
        }
        // Additional conditions can be added here
        return false;
    }

    /**
     * Applies a percentage discount to the total.
     * @param {number} total - The original total amount.
     * @returns {number} - The total after applying the percentage discount.
     */
    applyPercentageDiscount(total) {
        return total - (total * (this.value / 100));
    }

    /**
     * Applies a fixed discount to the total.
     * @param {number} total - The original total amount.
     * @returns {number} - The total after applying the fixed discount.
     */
    applyFixedDiscount(total) {
        return total - this.value;
    }

    /**
     * Applies a Buy One Get One (BOGO) discount to the items.
     * @param {Array} items - The array of items in the order.
     * @returns {number} - The total after applying the BOGO discount.
     */
    applyBogoDiscount(items) {
        let eligibleItems = items.filter(item => item.quantity > 0);
        let discount = 0;

        eligibleItems.forEach(item => {
            const bogoCount = Math.floor(item.quantity / 2);
            discount += bogoCount * item.price; // Assuming price is per item
        });

        return items.reduce((total, item) => total + (item.price * item.quantity), 0) - discount;
    }
}

// Example usage
const order = {
    total: 120,
    items: [
        { name: 'Item 1', price: 30, quantity: 2 },
        { name: 'Item 2', price: 20, quantity: 3 }
    ]
};

// Define promotions
const promotions = [
    new Promotion('10% off on orders above $100', 'percentage', { type: 'minAmount', value: 100 }, 10),
    new Promotion('Buy One Get One Free on Item 1', 'BOGO', { type: 'itemSpecific', value: 'Item 1' }, null)
];

// Apply promotions
let finalTotal = order.total;
promotions.forEach(promotion => {
    finalTotal = promotion.apply(order);
});

console.log(`Final total after promotions: $${finalTotal.toFixed(2)}`);
```
