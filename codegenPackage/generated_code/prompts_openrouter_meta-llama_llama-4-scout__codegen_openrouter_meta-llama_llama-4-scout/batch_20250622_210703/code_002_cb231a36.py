"""
Generated Code Metadata:
========================
Original URL: https://farmaciasantiagoapostol.com
Prompt: Generate JavaScript code for a simple user account management system for an online pharmacy, including features for carrito (cart) and finalizar compra (checkout).
Generated: DETERMINISTIC_cb231a3656ca9029
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// UserAccount.js

class UserAccount {
  /**
   * Creates a new UserAccount instance.
   * @param {string} id - Unique identifier for the user.
   * @param {string} name - User's name.
   * @param {string} email - User's email.
   */
  constructor(id, name, email) {
    this.id = id;
    this.name = name;
    this.email = email;
    this.cart = [];
  }

  /**
   * Adds a product to the user's cart.
   * @param {object} product - Product to add to cart.
   * @param {number} quantity - Quantity of product to add.
   */
  addToCart(product, quantity) {
    if (!product || !quantity) {
      throw new Error('Product and quantity are required.');
    }
    const existingProduct = this.cart.find((item) => item.product.id === product.id);
    if (existingProduct) {
      existingProduct.quantity += quantity;
    } else {
      this.cart.push({ product, quantity });
    }
  }

  /**
   * Removes a product from the user's cart.
   * @param {string} productId - ID of product to remove.
   */
  removeFromCart(productId) {
    if (!productId) {
      throw new Error('Product ID is required.');
    }
    this.cart = this.cart.filter((item) => item.product.id !== productId);
  }

  /**
   * Updates the quantity of a product in the user's cart.
   * @param {string} productId - ID of product to update.
   * @param {number} newQuantity - New quantity of product.
   */
  updateCartQuantity(productId, newQuantity) {
    if (!productId || !newQuantity) {
      throw new Error('Product ID and new quantity are required.');
    }
    const existingProduct = this.cart.find((item) => item.product.id === productId);
    if (existingProduct) {
      existingProduct.quantity = newQuantity;
    }
  }

  /**
   * Finalizes the user's purchase (checkout).
   * @returns {object} - Summary of the purchase.
   */
  finalizePurchase() {
    if (this.cart.length === 0) {
      throw new Error('Cart is empty.');
    }
    const purchaseSummary = {
      userId: this.id,
      products: this.cart.map((item) => ({
        product: item.product,
        quantity: item.quantity,
      })),
      totalCost: this.calculateTotalCost(),
    };
    this.cart = []; // Clear cart after purchase
    return purchaseSummary;
  }

  /**
   * Calculates the total cost of products in the cart.
   * @returns {number} - Total cost.
   */
  calculateTotalCost() {
    return this.cart.reduce((total, item) => total + item.product.price * item.quantity, 0);
  }
}

// Product.js

class Product {
  /**
   * Creates a new Product instance.
   * @param {string} id - Unique identifier for the product.
   * @param {string} name - Product name.
   * @param {number} price - Product price.
   */
  constructor(id, name, price) {
    this.id = id;
    this.name = name;
    this.price = price;
  }
}

// Example usage:

// Create some products
const product1 = new Product('1', 'Product A', 19.99);
const product2 = new Product('2', 'Product B', 9.99);

// Create a new user account
const userAccount = new UserAccount('1', 'John Doe', 'john.doe@example.com');

// Add products to cart
userAccount.addToCart(product1, 2);
userAccount.addToCart(product2, 1);

// Update quantity of a product in cart
userAccount.updateCartQuantity(product1.id, 3);

// Finalize purchase
try {
  const purchaseSummary = userAccount.finalizePurchase();
  console.log('Purchase Summary:');
  console.log(purchaseSummary);
} catch (error) {
  console.error('Error:', error.message);
}
```
