"""
Generated Code Metadata:
========================
Original URL: https://snackpointemmen.nl
Prompt: Develop a JavaScript function that simulates ordering from a snack bar, including options for soft serve ice cream and chicken buckets, as seen at Snackpoint Emmen.
Generated: DETERMINISTIC_b4948039ea92b674
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates ordering from a snack bar.
 * Options include soft serve ice cream and chicken buckets.
 * 
 * @param {string} item - The name of the item to order (e.g., "soft serve", "chicken bucket").
 * @param {number} quantity - The quantity of the item to order.
 * @param {Object} menu - The menu with available items and their prices.
 * @returns {Object} - An object containing the order summary or an error message.
 */
function orderSnackBar(item, quantity, menu) {
    // Validate input parameters
    if (typeof item !== 'string' || item.trim() === '') {
        return { error: "Invalid item name. Please provide a valid string." };
    }
    if (typeof quantity !== 'number' || quantity <= 0 || !Number.isInteger(quantity)) {
        return { error: "Invalid quantity. Please provide a positive integer." };
    }
    if (!menu || typeof menu !== 'object' || !menu[item]) {
        return { error: `Item "${item}" is not available on the menu.` };
    }

    // Calculate total price
    const pricePerItem = menu[item];
    const totalPrice = pricePerItem * quantity;

    // Return order summary
    return {
        success: true,
        message: `You have ordered ${quantity} ${item}(s).`,
        item: item,
        quantity: quantity,
        pricePerItem: pricePerItem.toFixed(2),
        totalPrice: totalPrice.toFixed(2),
    };
}

// Example usage
const snackBarMenu = {
    "soft serve": 2.50, // Price per soft serve ice cream
    "chicken bucket": 8.99, // Price per chicken bucket
    "fries": 3.00, // Additional menu item
    "soda": 1.50 // Additional menu item
};

const order1 = orderSnackBar("soft serve", 3, snackBarMenu);
console.log(order1);

const order2 = orderSnackBar("chicken bucket", 2, snackBarMenu);
console.log(order2);

const order3 = orderSnackBar("pizza", 1, snackBarMenu); // Invalid item
console.log(order3);

const order4 = orderSnackBar("fries", -1, snackBarMenu); // Invalid quantity
console.log(order4);
```
