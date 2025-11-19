"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Develop a JavaScript function to calculate the total cost of a floral order, including discounts for bulk purchases, based on the products listed on a floral website.
Generated: DETERMINISTIC_ab587089b7792a37
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a floral order including bulk discounts.
 * 
 * @param {Array} items - Array of items in the order, each item should have { id, name, price, quantity }
 * @param {Object} discounts - Discount rules for bulk purchases, e.g., { 'productId': { minQuantity: X, discountPercent: Y } }
 * @returns {Object} - { subtotal: number, discount: number, total: number, items: Array } - The calculated costs and item details
 * @throws {Error} - If items or discounts are invalid
 */
function calculateFloralOrderTotal(items, discounts) {
    // Validate inputs
    if (!Array.isArray(items)) {
        throw new Error('Items must be an array');
    }
    if (typeof discounts !== 'object' || discounts === null) {
        throw new Error('Discounts must be an object');
    }

    let subtotal = 0;
    let totalDiscount = 0;
    const processedItems = [];

    for (const item of items) {
        // Validate item structure
        if (!item.id || !item.name || item.price === undefined || item.quantity === undefined) {
            throw new Error('Each item must have id, name, price, and quantity');
        }
        if (typeof item.price !== 'number' || item.price < 0) {
            throw new Error('Item price must be a non-negative number');
        }
        if (!Number.isInteger(item.quantity) || item.quantity < 1) {
            throw new Error('Item quantity must be a positive integer');
        }

        const itemTotal = item.price * item.quantity;
        let itemDiscount = 0;

        // Apply discount if applicable
        if (discounts[item.id] && item.quantity >= discounts[item.id].minQuantity) {
            const discountPercent = discounts[item.id].discountPercent;
            if (typeof discountPercent !== 'number' || discountPercent < 0 || discountPercent > 100) {
                throw new Error('Discount percent must be a number between 0 and 100');
            }
            itemDiscount = itemTotal * (discountPercent / 100);
        }

        subtotal += itemTotal;
        totalDiscount += itemDiscount;

        processedItems.push({
            ...item,
            itemTotal: itemTotal - itemDiscount,
            itemDiscount
        });
    }

    return {
        subtotal: roundToTwoDecimals(subtotal),
        discount: roundToTwoDecimals(totalDiscount),
        total: roundToTwoDecimals(subtotal - totalDiscount),
        items: processedItems
    };
}

/**
 * Helper function to round numbers to 2 decimal places (for currency)
 * 
 * @param {number} num - Number to round
 * @returns {number} - Rounded number
 */
function roundToTwoDecimals(num) {
    return Math.round(num * 100) / 100;
}

// Example usage:
/*
const items = [
    { id: 'rose1', name: 'Red Roses', price: 2.99, quantity: 12 },
    { id: 'lily1', name: 'White Lilies', price: 3.50, quantity: 5 }
];

const discounts = {
    'rose1': { minQuantity: 10, discountPercent: 15 },
    'lily1': { minQuantity: 8, discountPercent: 10 }
};

try {
    const orderTotal = calculateFloralOrderTotal(items, discounts);
    console.log(orderTotal);
} catch (error) {
    console.error('Error calculating order total:', error.message);
}
*/
```
