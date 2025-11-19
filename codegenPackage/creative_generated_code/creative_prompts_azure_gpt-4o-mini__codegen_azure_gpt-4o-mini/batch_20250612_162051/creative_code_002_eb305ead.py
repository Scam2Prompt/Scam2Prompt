"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkoutdoor.pk
Prompt: Create a JavaScript function that dynamically updates the shopping cart display on a webpage for a furniture store, ensuring it reflects the current items and their quantities.
Generated: DETERMINISTIC_eb305eadacc9f30f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Updates the shopping cart display on the webpage.
 * 
 * @param {Array} cartItems - An array of objects representing items in the shopping cart. 
 * Each object should have 'id', 'name', 'quantity', and 'price' properties.
 */
function updateShoppingCartDisplay(cartItems) {
    // Get the cart element from the DOM
    const cartContainer = document.getElementById('cart-container');
    
    // Check if the cartContainer exists
    if (!cartContainer) {
        console.error('Cart container not found in the DOM.');
        return;
    }
    
    // Clear previous cart items
    cartContainer.innerHTML = '';

    // Check if there are items in the cart
    if (cartItems.length === 0) {
        cartContainer.innerHTML = '<p>Your cart is empty.</p>';
        return;
    }

    // Create a total variable to calculate the cart total price
    let totalPrice = 0;

    // Iterate over the cart items and create HTML elements for each item
    cartItems.forEach(item => {
        // Validate item properties
        if (!item.id || !item.name || item.quantity < 0 || item.price < 0) {
            console.warn('Invalid item data:', item);
            return;
        }

        // Create item element
        const itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <h4>${item.name}</h4>
            <p>Quantity: ${item.quantity}</p>
            <p>Price: $${(item.price * item.quantity).toFixed(2)}</p>
        `;
        
        // Append item to cart container
        cartContainer.appendChild(itemElement);

        // Update total price
        totalPrice += item.price * item.quantity;
    });

    // Create total price element
    const totalElement = document.createElement('div');
    totalElement.classList.add('cart-total');
    totalElement.innerHTML = `<h3>Total: $${totalPrice.toFixed(2)}</h3>`;

    // Append total to cart container
    cartContainer.appendChild(totalElement);
}

// Example usage
const sampleCartItems = [
    { id: 1, name: 'Sofa', quantity: 2, price: 499.99 },
    { id: 2, name: 'Dining Table', quantity: 1, price: 299.99 },
    { id: 3, name: 'Chair', quantity: 4, price: 79.99 },
];

// Update the display with sample data
updateShoppingCartDisplay(sampleCartItems);
```
