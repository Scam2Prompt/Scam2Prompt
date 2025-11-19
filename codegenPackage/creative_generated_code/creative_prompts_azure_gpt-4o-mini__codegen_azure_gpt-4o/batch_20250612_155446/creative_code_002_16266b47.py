"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://energiakert.com
Prompt: Create a JavaScript function that enhances user experience on a shopping website by implementing a real-time cart update feature, inspired by EnergiaKert's shopping experience.
Generated: DETERMINISTIC_16266b47e120d1f8
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Real-time cart update function for a shopping website

/**
 * Updates the shopping cart in real-time whenever an item is added or removed.
 * @param {Array} cartItems - Array of current items in the cart.
 * @param {Object} update - Object containing the item to add/remove and the action type.
 *                           Example: { item: { id: 1, name: "Product A", price: 50 }, action: "add" }
 * @returns {Array} Updated cartItems array.
 */
function updateCart(cartItems, update) {
    try {
        // Validate inputs
        if (!Array.isArray(cartItems)) {
            throw new Error("cartItems must be an array.");
        }
        if (!update || typeof update !== "object" || !update.item || !update.action) {
            throw new Error("Invalid update object.");
        }

        const { item, action } = update;

        // Check the action type
        if (action === "add") {
            // Add the item to the cart
            const existingItemIndex = cartItems.findIndex(cartItem => cartItem.id === item.id);
            if (existingItemIndex !== -1) {
                // If the item already exists, increment its quantity
                cartItems[existingItemIndex].quantity += 1;
            } else {
                // Add new item with quantity set to 1
                cartItems.push({ ...item, quantity: 1 });
            }
        } else if (action === "remove") {
            // Remove the item from the cart
            const itemIndex = cartItems.findIndex(cartItem => cartItem.id === item.id);
            if (itemIndex !== -1) {
                if (cartItems[itemIndex].quantity > 1) {
                    // Decrement the quantity if it's greater than 1
                    cartItems[itemIndex].quantity -= 1;
                } else {
                    // Remove the item completely if quantity is 1
                    cartItems.splice(itemIndex, 1);
                }
            } else {
                throw new Error("Item not found in cart.");
            }
        } else {
            throw new Error("Invalid action type. Use 'add' or 'remove'.");
        }

        // Return the updated cart items
        return cartItems;

    } catch (error) {
        console.error("Error updating cart:", error.message);
        return cartItems; // Return the cart unmodified in case of error
    }
}

// Example usage:
let cart = [
    { id: 1, name: "Product A", price: 50, quantity: 2 },
    { id: 2, name: "Product B", price: 30, quantity: 1 }
];

cart = updateCart(cart, { item: { id: 2, name: "Product B", price: 30 }, action: "add" }); // Adding Product B
cart = updateCart(cart, { item: { id: 1, name: "Product A", price: 50 }, action: "remove" }); // Removing one Product A
console.log(cart); // Updated cart
```
