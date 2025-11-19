"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Write a JavaScript function that calculates the total price of a customer's order from Govind Sweets, incorporating various product options like Dry Fruits and Ghee ki Mithai.
Generated: DETERMINISTIC_89ec394ba0c8b25a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price of a customer's order at Govind Sweets.
 * 
 * @param {Object[]} order - An array of product objects in the order.
 * @param {string} order[].name - The name of the product.
 * @param {number} order[].quantity - The quantity of the product ordered.
 * @param {number} order[].price - The price per unit of the product.
 * @returns {number} - The total price of the order.
 * @throws {Error} - Throws an error if the order is invalid.
 */
function calculateTotalPrice(order) {
    // Validate input
    if (!Array.isArray(order) || order.length === 0) {
        throw new Error("Invalid order: The order must be a non-empty array.");
    }

    let totalPrice = 0;

    // Iterate through each item in the order to calculate the total price
    order.forEach(item => {
        // Validate item properties
        if (typeof item.name !== 'string' || typeof item.quantity !== 'number' || typeof item.price !== 'number') {
            throw new Error("Invalid item in order: Each item must have a name (string), quantity (number), and price (number).");
        }

        // Ensure quantity and price are non-negative
        if (item.quantity < 0 || item.price < 0) {
            throw new Error("Invalid quantity or price: Both must be non-negative.");
        }

        // Calculate total for the item and add to totalPrice
        totalPrice += item.quantity * item.price;
    });

    // Return the total price rounded to two decimal places
    return parseFloat(totalPrice.toFixed(2));
}

// Example usage:
try {
    const order = [
        { name: "Dry Fruits", quantity: 2, price: 300 },
        { name: "Ghee ki Mithai", quantity: 3, price: 150 }
    ];
    const total = calculateTotalPrice(order);
    console.log(`Total Price: ₹${total}`);
} catch (error) {
    console.error(error.message);
}
```
