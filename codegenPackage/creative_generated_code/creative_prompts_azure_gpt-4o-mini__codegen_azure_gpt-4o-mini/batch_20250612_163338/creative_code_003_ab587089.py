"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://florerialima.com
Prompt: Develop a JavaScript function to calculate the total cost of a floral order, including discounts for bulk purchases, based on the products listed on a floral website.
Generated: DETERMINISTIC_ab587089b7792a37
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a floral order based on product prices and quantities.
 * Applies discounts for bulk purchases.
 * 
 * @param {Array<Object>} orderItems - An array of objects representing each item in the order.
 * @param {number} orderItems[].price - The price of a single unit of the product.
 * @param {number} orderItems[].quantity - The quantity of the product being ordered.
 * @param {number} bulkDiscountThreshold - The minimum quantity required to qualify for a bulk discount.
 * @param {number} bulkDiscountPercentage - The percentage discount applied for bulk purchases.
 * @returns {number} - The total cost after applying any discounts.
 * @throws {Error} - Throws an error if any item has a negative price or quantity.
 */
function calculateFloralOrderTotal(orderItems, bulkDiscountThreshold = 10, bulkDiscountPercentage = 0.1) {
    // Validate input
    if (!Array.isArray(orderItems)) {
        throw new Error('Order items must be an array.');
    }

    let totalCost = 0;

    orderItems.forEach(item => {
        const { price, quantity } = item;

        // Error handling for invalid price and quantity
        if (typeof price !== 'number' || price < 0) {
            throw new Error('Item price must be a non-negative number.');
        }
        if (typeof quantity !== 'number' || quantity < 0) {
            throw new Error('Item quantity must be a non-negative number.');
        }

        // Calculate subtotal for the item
        let itemCost = price * quantity;

        // Apply bulk discount if applicable
        if (quantity >= bulkDiscountThreshold) {
            const discount = itemCost * bulkDiscountPercentage;
            itemCost -= discount;
        }

        // Add item cost to total
        totalCost += itemCost;
    });

    return parseFloat(totalCost.toFixed(2)); // Return total cost rounded to two decimal places
}

// Example usage:
try {
    const order = [
        { price: 20.00, quantity: 5 },   // No discount
        { price: 15.00, quantity: 12 },  // Discount applies
        { price: 10.00, quantity: 7 }    // No discount
    ];

    const total = calculateFloralOrderTotal(order);
    console.log(`Total cost of the floral order: $${total}`);
} catch (error) {
    console.error(`Error calculating order total: ${error.message}`);
}
```
