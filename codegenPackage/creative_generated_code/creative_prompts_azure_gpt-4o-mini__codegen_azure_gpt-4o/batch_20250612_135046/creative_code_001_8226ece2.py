"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metmask.com
Prompt: Write a JavaScript function that calculates the total price of various fishing tackle items from metmask.com, including elastic feeders and waggler floats.
Generated: DETERMINISTIC_8226ece26b4b231d
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total price of various fishing tackle items.
 * @param {Array} items - Array of objects representing items. Each object should have `name`, `price`, and `quantity` properties.
 * @returns {number} - The total price of all items.
 */
function calculateTotalPrice(items) {
    // Validate input
    if (!Array.isArray(items)) {
        throw new Error("Invalid input: items must be an array.");
    }

    let totalPrice = 0;

    items.forEach((item) => {
        // Validate item structure
        if (!item.name || typeof item.name !== "string") {
            throw new Error("Invalid item: 'name' property must be a string.");
        }
        if (!item.price || typeof item.price !== "number" || item.price < 0) {
            throw new Error("Invalid item: 'price' property must be a positive number.");
        }
        if (!item.quantity || typeof item.quantity !== "number" || item.quantity < 0) {
            throw new Error("Invalid item: 'quantity' property must be a positive number.");
        }

        // Calculate the total price for the current item
        totalPrice += item.price * item.quantity;
    });

    return totalPrice;
}

// Example usage:
try {
    const items = [
        { name: "Elastic Feeder", price: 5.99, quantity: 3 },
        { name: "Waggler Float", price: 2.49, quantity: 5 },
        { name: "Fishing Line", price: 12.99, quantity: 1 },
    ];
    const total = calculateTotalPrice(items);
    console.log(`Total price: $${total.toFixed(2)}`); // Output: Total price: $41.92
} catch (error) {
    console.error(error.message);
}
```
