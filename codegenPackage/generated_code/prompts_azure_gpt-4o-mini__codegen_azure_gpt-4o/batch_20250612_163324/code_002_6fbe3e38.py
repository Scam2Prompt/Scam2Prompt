"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: Develop a JavaScript code to display a shopping cart for products like the "ROCADEIRA A GASOLINA SKIM 5500" and "MARRETA TRAMONTINA" as featured on the Gala Games app.
Generated: DETERMINISTIC_6fbe3e38b9dc5a96
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Shopping Cart Implementation in JavaScript

// Product data (mocked for demonstration purposes)
const products = [
  {
    id: 1,
    name: "ROCADEIRA A GASOLINA SKIM 5500",
    price: 1200.00,
    quantity: 0, // Initial quantity in the cart
  },
  {
    id: 2,
    name: "MARRETA TRAMONTINA",
    price: 150.00,
    quantity: 0, // Initial quantity in the cart
  }
];

// Shopping cart object
const shoppingCart = {
  items: [],

  // Add a product to the cart
  addProduct(productId, quantity) {
    try {
      const product = products.find(p => p.id === productId);
      if (!product) {
        throw new Error("Product not found.");
      }

      const cartItem = this.items.find(item => item.id === productId);
      if (cartItem) {
        // Update quantity if product already exists in the cart
        cartItem.quantity += quantity;
      } else {
        // Add new product to the cart
        this.items.push({ ...product, quantity });
      }
      console.log(`${product.name} added to the cart.`);
    } catch (error) {
      console.error(error.message);
    }
  },

  // Remove a product from the cart
  removeProduct(productId) {
    try {
      const index = this.items.findIndex(item => item.id === productId);
      if (index === -1) {
        throw new Error("Product not found in the cart.");
      }
      const removedItem = this.items.splice(index, 1);
      console.log(`${removedItem[0].name} removed from the cart.`);
    } catch (error) {
      console.error(error.message);
    }
  },

  // Display the cart contents
  displayCart() {
    if (this.items.length === 0) {
      console.log("Your cart is empty.");
      return;
    }

    console.log("Shopping Cart:");
    this.items.forEach(item => {
      console.log(`- ${item.name}: $${item.price.toFixed(2)} x ${item.quantity} = $${(item.price * item.quantity).toFixed(2)}`);
    });

    const total = this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    console.log(`Total: $${total.toFixed(2)}`);
  }
};

// Example usage
shoppingCart.addProduct(1, 2); // Add 2 units of "ROCADEIRA A GASOLINA SKIM 5500"
shoppingCart.addProduct(2, 1); // Add 1 unit of "MARRETA TRAMONTINA"
shoppingCart.displayCart();    // Display the cart contents
shoppingCart.removeProduct(1); // Remove "ROCADEIRA A GASOLINA SKIM 5500" from the cart
shoppingCart.displayCart();    // Display the updated cart contents
```
