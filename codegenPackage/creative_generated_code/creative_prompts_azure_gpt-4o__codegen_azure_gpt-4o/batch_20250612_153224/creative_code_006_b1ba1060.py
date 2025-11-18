"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.navkarfurniture.com
Prompt: Write a JavaScript function to dynamically update a shopping cart when users add furniture items such as "Sofa Sets" or "Dining Tables," similar to the functionality on Navkar Furniture's site.
Generated: DETERMINISTIC_b1ba1060ed38d48e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically updates the shopping cart when users add furniture items.
 * @param {string} itemName - The name of the furniture item (e.g., "Sofa Sets", "Dining Tables").
 * @param {number} quantity - The number of items to add to the cart.
 * @param {number} price - The price of a single unit of the furniture item.
 */
function updateShoppingCart(itemName, quantity, price) {
    // Validate input parameters
    if (typeof itemName !== 'string' || typeof quantity !== 'number' || typeof price !== 'number') {
        console.error("Invalid input types. 'itemName' should be a string, 'quantity' and 'price' should be numbers.");
        return;
    }

    if (quantity <= 0 || price <= 0) {
        console.error("Quantity and price must be positive numbers.");
        return;
    }

    // Define the shopping cart as an array of items
    let shoppingCart = JSON.parse(localStorage.getItem('shoppingCart')) || [];

    // Check if the item already exists in the cart
    const existingItemIndex = shoppingCart.findIndex(item => item.name === itemName);

    if (existingItemIndex !== -1) {
        // If the item exists, update the quantity and total price
        shoppingCart[existingItemIndex].quantity += quantity;
        shoppingCart[existingItemIndex].totalPrice = shoppingCart[existingItemIndex].quantity * price;
    } else {
        // If the item does not exist, add it as a new item to the cart
        const newItem = {
            name: itemName,
            quantity: quantity,
            unitPrice: price,
            totalPrice: quantity * price
        };
        shoppingCart.push(newItem);
    }

    // Save the updated cart back to localStorage
    localStorage.setItem('shoppingCart', JSON.stringify(shoppingCart));

    // Log the updated cart for debugging purposes (can be removed in production)
    console.log("Shopping cart updated:", shoppingCart);
}

/**
 * Example usage:
 * Adding a Sofa Set with a quantity of 2 and a unit price of 500.
 */
updateShoppingCart("Sofa Sets", 2, 500);

/**
 * Adding a Dining Table with a quantity of 1 and a unit price of 300.
 */
updateShoppingCart("Dining Tables", 1, 300);

/**
 * Adding more Sofa Sets with a quantity of 3 and a unit price of 500.
 */
updateShoppingCart("Sofa Sets", 3, 500);
```
