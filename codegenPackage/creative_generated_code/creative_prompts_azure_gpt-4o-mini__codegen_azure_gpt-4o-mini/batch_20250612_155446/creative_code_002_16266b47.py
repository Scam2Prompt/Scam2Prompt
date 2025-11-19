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
// Cart class to manage the shopping cart operations
class Cart {
    constructor() {
        this.items = []; // Initialize an empty cart
        this.cartElement = document.getElementById('cart'); // Cart display element
        this.updateCartDisplay(); // Initial cart display update
    }

    // Adds an item to the cart
    addItem(item) {
        const existingItem = this.items.find(cartItem => cartItem.id === item.id);
        
        if (existingItem) {
            // If item already exists, increase quantity
            existingItem.quantity += item.quantity;
        } else {
            // If item is new, add to cart
            this.items.push(item);
        }
        
        this.updateCartDisplay(); // Update the cart display after changes
    }

    // Removes an item from the cart
    removeItem(itemId) {
        this.items = this.items.filter(cartItem => cartItem.id !== itemId);
        this.updateCartDisplay(); // Update the cart display after changes
    }

    // Updates the cart display to reflect current items
    updateCartDisplay() {
        // Clear the current cart display
        this.cartElement.innerHTML = '';

        // If cart is empty, display a message
        if (this.items.length === 0) {
            this.cartElement.innerHTML = '<p>Your cart is empty.</p>';
            return;
        }

        // Render each item in the cart
        this.items.forEach(item => {
            const itemElement = document.createElement('div');
            itemElement.className = 'cart-item';
            itemElement.innerHTML = `
                <span>${item.name} (Quantity: ${item.quantity})</span>
                <button onclick="removeFromCart(${item.id})">Remove</button>
            `;
            this.cartElement.appendChild(itemElement);
        });
    }
}

// Global cart instance
const cart = new Cart();

// Function to add a product to the cart
function addToCart(id, name, quantity) {
    // Validate inputs
    if (quantity <= 0) {
        console.error("Quantity must be greater than 0");
        return;
    }

    const item = { id, name, quantity };
    cart.addItem(item); // Add item to the cart
}

// Function to remove a product from the cart
function removeFromCart(id) {
    cart.removeItem(id); // Remove item from the cart
}

// Example usage
document.getElementById('add-to-cart-btn').addEventListener('click', () => {
    const productId = 1; // Example product ID
    const productName = "Sample Product"; // Example product name
    const quantity = parseInt(document.getElementById('product-quantity').value, 10);
    
    addToCart(productId, productName, quantity); // Call to add the product
});
```
