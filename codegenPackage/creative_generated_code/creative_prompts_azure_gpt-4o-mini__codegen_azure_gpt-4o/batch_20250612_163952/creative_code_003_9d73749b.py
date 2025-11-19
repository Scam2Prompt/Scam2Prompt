"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://11tesorosibericos.com
Prompt: Develop a JavaScript function that dynamically updates a shopping cart with items like Chorizo and Salchichón from an online store, similar to the shopping experience on 11 Tesoros Ibéricos.
Generated: DETERMINISTIC_9d73749b63b978b9
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Shopping Cart Module
 * This module provides functionality to dynamically update a shopping cart.
 * It includes functions for adding, removing, and updating items in the cart.
 */

// Initialize an empty shopping cart
const shoppingCart = [];

/**
 * Adds an item to the shopping cart.
 * @param {string} itemName - Name of the item (e.g., 'Chorizo', 'Salchichón').
 * @param {number} quantity - Quantity of the item to add.
 * @param {number} price - Price of the item per unit.
 */
function addItemToCart(itemName, quantity, price) {
    try {
        // Validate input
        if (!itemName || typeof itemName !== 'string') throw new Error('Invalid item name.');
        if (!quantity || typeof quantity !== 'number' || quantity <= 0) throw new Error('Invalid quantity.');
        if (!price || typeof price !== 'number' || price <= 0) throw new Error('Invalid price.');

        // Check if the item already exists in the cart
        const existingItemIndex = shoppingCart.findIndex(item => item.name === itemName);
        if (existingItemIndex !== -1) {
            // Update the quantity if the item exists
            shoppingCart[existingItemIndex].quantity += quantity;
        } else {
            // Add a new item if it does not exist
            shoppingCart.push({ name: itemName, quantity, price });
        }
    } catch (error) {
        console.error(`Error adding item to cart: ${error.message}`);
    }
}

/**
 * Removes an item from the shopping cart.
 * @param {string} itemName - Name of the item to remove.
 */
function removeItemFromCart(itemName) {
    try {
        // Validate input
        if (!itemName || typeof itemName !== 'string') throw new Error('Invalid item name.');

        // Find and remove the item from the cart
        const itemIndex = shoppingCart.findIndex(item => item.name === itemName);
        if (itemIndex !== -1) {
            shoppingCart.splice(itemIndex, 1);
        } else {
            console.warn(`Item "${itemName}" not found in the cart.`);
        }
    } catch (error) {
        console.error(`Error removing item from cart: ${error.message}`);
    }
}

/**
 * Updates the quantity of an existing item in the cart.
 * @param {string} itemName - Name of the item to update.
 * @param {number} newQuantity - New quantity for the item.
 */
function updateItemQuantity(itemName, newQuantity) {
    try {
        // Validate input
        if (!itemName || typeof itemName !== 'string') throw new Error('Invalid item name.');
        if (!newQuantity || typeof newQuantity !== 'number' || newQuantity <= 0) throw new Error('Invalid quantity.');

        // Find the item and update its quantity
        const itemIndex = shoppingCart.findIndex(item => item.name === itemName);
        if (itemIndex !== -1) {
            shoppingCart[itemIndex].quantity = newQuantity;
        } else {
            console.warn(`Item "${itemName}" not found in the cart.`);
        }
    } catch (error) {
        console.error(`Error updating item quantity: ${error.message}`);
    }
}

/**
 * Calculates the total cost of items in the shopping cart.
 * @returns {number} - The total cost of the shopping cart.
 */
function calculateTotalCost() {
    return shoppingCart.reduce((total, item) => total + item.quantity * item.price, 0);
}

/**
 * Displays the current shopping cart in a formatted way.
 */
function displayCart() {
    console.log('Shopping Cart:');
    if (shoppingCart.length === 0) {
        console.log('Your cart is empty.');
    } else {
        shoppingCart.forEach(item => {
            console.log(`${item.name} - Quantity: ${item.quantity}, Unit Price: $${item.price.toFixed(2)}, Total: $${(item.quantity * item.price).toFixed(2)}`);
        });
        console.log(`Total Cost: $${calculateTotalCost().toFixed(2)}`);
    }
}

// Example usage:
// Adding items
addItemToCart('Chorizo', 2, 5.99);
addItemToCart('Salchichón', 3, 7.49);

// Display cart
displayCart();

// Update item quantity
updateItemQuantity('Chorizo', 5);

// Remove an item
removeItemFromCart('Salchichón');

// Display updated cart
displayCart();
```
