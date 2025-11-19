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
// ShoppingCart class to manage the items in the shopping cart
class ShoppingCart {
    constructor() {
        // Initialize an empty cart
        this.cartItems = [];
    }

    /**
     * Adds an item to the shopping cart.
     * @param {Object} item - The item to add, with properties `name` and `price`.
     * @throws Will throw an error if item is invalid.
     */
    addItem(item) {
        if (!item || !item.name || typeof item.price !== 'number') {
            throw new Error('Invalid item. Item must have a name and a price.');
        }
        this.cartItems.push(item);
        this.updateCartDisplay();
    }

    /**
     * Removes an item from the shopping cart by its name.
     * @param {string} itemName - The name of the item to remove.
     */
    removeItem(itemName) {
        this.cartItems = this.cartItems.filter(item => item.name !== itemName);
        this.updateCartDisplay();
    }

    /**
     * Updates the shopping cart display in the UI.
     */
    updateCartDisplay() {
        const cartContainer = document.getElementById('cart');
        cartContainer.innerHTML = ''; // Clear current display

        // Create and display each item
        this.cartItems.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.innerText = `${item.name}: $${item.price.toFixed(2)}`;
            cartContainer.appendChild(itemElement);
        });

        // Display total price
        const total = this.calculateTotal();
        const totalElement = document.createElement('div');
        totalElement.innerText = `Total: $${total.toFixed(2)}`;
        cartContainer.appendChild(totalElement);
    }

    /**
     * Calculates the total price of the items in the cart.
     * @returns {number} The total price.
     */
    calculateTotal() {
        return this.cartItems.reduce((acc, item) => acc + item.price, 0);
    }
}

// Example usage of the ShoppingCart class
const shoppingCart = new ShoppingCart();

// Function to add items to the cart
function addItemToCart(name, price) {
    try {
        shoppingCart.addItem({ name, price });
    } catch (error) {
        console.error(error.message);
    }
}

// Function to remove items from the cart
function removeItemFromCart(name) {
    shoppingCart.removeItem(name);
}

// Sample items to add to the cart
addItemToCart('Chorizo', 12.50);
addItemToCart('Salchichón', 10.00);

// Example HTML element to display the cart
document.body.innerHTML += '<div id="cart"></div>';
```
