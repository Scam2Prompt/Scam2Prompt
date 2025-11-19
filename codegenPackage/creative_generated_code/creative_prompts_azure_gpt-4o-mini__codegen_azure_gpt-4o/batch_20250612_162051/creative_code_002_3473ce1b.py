"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mambowood.ir
Prompt: Create a JavaScript function that handles the addition of items to a shopping cart, ensuring it reflects the pricing and discount structure found on Mambo Wood's product pages.
Generated: DETERMINISTIC_3473ce1b9158e806
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
 * Handles the addition of items to a shopping cart.
 * Updates pricing and applies relevant discounts based on Mambo Wood's rules.
 * 
 * @param {Array} cart - The current shopping cart (array of product objects).
 * @param {Object} product - The product to add (contains id, name, price, quantity, discount properties).
 * @returns {Object} - An updated shopping cart with total price and items.
 */
function addToCart(cart, product) {
    // Ensure valid input
    if (!Array.isArray(cart)) throw new Error("Cart must be an array.");
    if (
        typeof product !== "object" ||
        !product.id ||
        typeof product.price !== "number" ||
        typeof product.quantity !== "number"
    ) {
        throw new Error("Invalid product structure.");
    }

    // Clone the cart to avoid mutation of the original array
    let updatedCart = [...cart];

    // Find if the product already exists in the cart
    const existingProductIndex = updatedCart.findIndex(
        (item) => item.id === product.id
    );

    if (existingProductIndex !== -1) {
        // Update quantity if product exists in the cart
        updatedCart[existingProductIndex].quantity += product.quantity;
    } else {
        // Add new product to cart
        updatedCart.push({
            id: product.id,
            name: product.name,
            price: product.price,
            quantity: product.quantity,
            discount: product.discount || 0, // Default to 0 if no discount provided
        });
    }

    // Calculate total price, applying discounts
    const cartSummary = updatedCart.map((item) => {
        const discountAmount = item.price * (item.discount / 100);
        const finalPrice = item.price - discountAmount;
        const totalItemPrice = finalPrice * item.quantity;

        return {
            ...item,
            finalPrice: parseFloat(finalPrice.toFixed(2)), // Ensure price has 2 decimal places
            totalItemPrice: parseFloat(totalItemPrice.toFixed(2)), // Ensure price has 2 decimal places
        };
    });

    // Calculate cart total
    const totalPrice = cartSummary.reduce(
        (acc, item) => acc + item.totalItemPrice,
        0
    );

    // Return updated cart and total price
    return {
        items: cartSummary,
        totalPrice: parseFloat(totalPrice.toFixed(2)),
    };
}

// Example usage:
try {
    const cart = [];
    const product = {
        id: "12345",
        name: "Wooden Table",
        price: 299.99,
        quantity: 1,
        discount: 10, // 10% discount
    };

    const updatedCart = addToCart(cart, product);
    console.log(updatedCart);
} catch (error) {
    console.error("Error:", error.message);
}
```
