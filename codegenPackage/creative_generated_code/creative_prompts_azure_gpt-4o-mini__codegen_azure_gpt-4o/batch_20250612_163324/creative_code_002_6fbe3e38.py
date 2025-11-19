"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Develop a JavaScript code to display a shopping cart for products like the "ROCADEIRA A GASOLINA SKIM 5500" and "MARRETA TRAMONTINA" as featured on the Gala Games app.
Generated: DETERMINISTIC_6fbe3e38b9dc5a96
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Shopping Cart Implementation
 * This script displays a shopping cart for products, allowing users to view items,
 * add or remove items, and calculate the total price.
 */

// Product data (mocked for demonstration purposes)
const products = [
  {
    id: 1,
    name: "ROCADEIRA A GASOLINA SKIM 5500",
    price: 499.99,
  },
  {
    id: 2,
    name: "MARRETA TRAMONTINA",
    price: 29.99,
  },
];

// Shopping cart array to store selected items
let shoppingCart = [];

/**
 * Adds a product to the shopping cart.
 * @param {number} productId - The ID of the product to add.
 */
function addToCart(productId) {
  const product = products.find((item) => item.id === productId);
  if (product) {
    shoppingCart.push(product);
    console.log(`${product.name} added to the cart.`);
  } else {
    console.error("Product not found.");
  }
}

/**
 * Removes a product from the shopping cart.
 * @param {number} productId - The ID of the product to remove.
 */
function removeFromCart(productId) {
  const index = shoppingCart.findIndex((item) => item.id === productId);
  if (index > -1) {
    const removedProduct = shoppingCart.splice(index, 1)[0];
    console.log(`${removedProduct.name} removed from the cart.`);
  } else {
    console.error("Product not found in cart.");
  }
}

/**
 * Calculates the total price of items in the shopping cart.
 * @returns {number} - The total price.
 */
function calculateTotal() {
  return shoppingCart.reduce((total, item) => total + item.price, 0).toFixed(2);
}

/**
 * Displays the shopping cart contents in a readable format.
 */
function displayCart() {
  if (shoppingCart.length === 0) {
    console.log("Your shopping cart is empty.");
  } else {
    console.log("Shopping Cart:");
    shoppingCart.forEach((item, index) => {
      console.log(`${index + 1}. ${item.name} - $${item.price.toFixed(2)}`);
    });
    console.log(`Total: $${calculateTotal()}`);
  }
}

// Example usage
addToCart(1); // Add "ROCADEIRA A GASOLINA SKIM 5500" to the cart
addToCart(2); // Add "MARRETA TRAMONTINA" to the cart
displayCart(); // Display the cart contents
removeFromCart(1); // Remove "ROCADEIRA A GASOLINA SKIM 5500" from the cart
displayCart(); // Display the updated cart contents
```
