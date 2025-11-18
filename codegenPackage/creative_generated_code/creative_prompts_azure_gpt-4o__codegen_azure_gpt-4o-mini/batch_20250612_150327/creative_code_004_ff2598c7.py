"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Create a JavaScript snippet to dynamically update the shopping cart subtotal and free shipping eligibility (e.g., ₹ 3,050.00 threshold) on a WordPress eCommerce site.
Generated: DETERMINISTIC_ff2598c7f9b3e834
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to update the shopping cart subtotal and shipping eligibility
function updateCartSubtotal(cartItems) {
    // Define the free shipping threshold
    const FREE_SHIPPING_THRESHOLD = 3050.00; // in local currency (₹)

    // Calculate subtotal from cart items
    let subtotal = 0;
    try {
        for (const item of cartItems) {
            // Ensure item price and quantity are numbers
            if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
                throw new Error('Item price or quantity is not a valid number');
            }
            subtotal += item.price * item.quantity;
        }
    } catch (error) {
        console.error('Error calculating subtotal:', error);
        return; // Exit if there's an error
    }

    // Update the subtotal display in the DOM
    const subtotalElement = document.getElementById('cart-subtotal');
    if (subtotalElement) {
        subtotalElement.textContent = `Subtotal: ₹ ${subtotal.toFixed(2)}`;
    } else {
        console.warn('Subtotal element not found in the DOM');
    }

    // Check free shipping eligibility
    const shippingMessageElement = document.getElementById('shipping-message');
    if (shippingMessageElement) {
        if (subtotal >= FREE_SHIPPING_THRESHOLD) {
            shippingMessageElement.textContent = 'Congratulations! You are eligible for free shipping.';
        } else {
            const remainingAmount = FREE_SHIPPING_THRESHOLD - subtotal;
            shippingMessageElement.textContent = `Add ₹ ${remainingAmount.toFixed(2)} more for free shipping.`;
        }
    } else {
        console.warn('Shipping message element not found in the DOM');
    }
}

// Example usage: call this function when the cart is updated
// Assuming cartItems is an array of objects with price and quantity properties
const cartItems = [
    { price: 1000, quantity: 2 }, // Example item 1
    { price: 500, quantity: 1 },   // Example item 2
    { price: 2000, quantity: 1 }    // Example item 3
];

// Update cart subtotal and eligibility
updateCartSubtotal(cartItems);
```

Make sure to update the HTML structure to include elements with IDs `cart-subtotal` and `shipping-message` for this code to function correctly.
