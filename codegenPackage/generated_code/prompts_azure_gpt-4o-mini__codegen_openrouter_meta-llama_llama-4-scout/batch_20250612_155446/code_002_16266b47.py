"""
Generated Code Metadata:
========================
Original URL: https://energiakert.com
Prompt: Create a JavaScript function that enhances user experience on a shopping website by implementing a real-time cart update feature, inspired by EnergiaKert's shopping experience.
Generated: DETERMINISTIC_16266b47e120d1f8
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// cartUpdater.js

/**
 * Updates the shopping cart in real-time.
 * 
 * @param {Object} cartElement - The HTML element representing the cart.
 * @param {Object} cartItemsElement - The HTML element representing the cart items.
 * @param {Object} productListElement - The HTML element representing the product list.
 */
class CartUpdater {
  constructor(cartElement, cartItemsElement, productListElement) {
    this.cartElement = cartElement;
    this.cartItemsElement = cartItemsElement;
    this.productListElement = productListElement;
    this.cart = {};

    // Bind event listeners
    this.productListElement.addEventListener('click', (event) => this.handleProductClick(event));
    this.cartElement.addEventListener('click', (event) => this.handleCartClick(event));
  }

  /**
   * Handles product click event.
   * 
   * @param {Event} event - The click event.
   */
  handleProductClick(event) {
    if (event.target.classList.contains('add-to-cart')) {
      const productId = event.target.dataset.productId;
      this.addProductToCart(productId);
    }
  }

  /**
   * Handles cart click event.
   * 
   * @param {Event} event - The click event.
   */
  handleCartClick(event) {
    if (event.target.classList.contains('remove-from-cart')) {
      const productId = event.target.dataset.productId;
      this.removeProductFromCart(productId);
    }
  }

  /**
   * Adds a product to the cart.
   * 
   * @param {string} productId - The ID of the product to add.
   */
  addProductToCart(productId) {
    try {
      // Get product details from product list
      const product = this.getProductFromList(productId);
      if (!product) {
        throw new Error(`Product with ID ${productId} not found`);
      }

      // Update cart
      if (this.cart[productId]) {
        this.cart[productId].quantity++;
      } else {
        this.cart[productId] = { ...product, quantity: 1 };
      }

      // Update cart display
      this.updateCartDisplay();
    } catch (error) {
      console.error('Error adding product to cart:', error);
    }
  }

  /**
   * Removes a product from the cart.
   * 
   * @param {string} productId - The ID of the product to remove.
   */
  removeProductFromCart(productId) {
    try {
      // Check if product exists in cart
      if (!this.cart[productId]) {
        throw new Error(`Product with ID ${productId} not found in cart`);
      }

      // Update cart
      if (this.cart[productId].quantity > 1) {
        this.cart[productId].quantity--;
      } else {
        delete this.cart[productId];
      }

      // Update cart display
      this.updateCartDisplay();
    } catch (error) {
      console.error('Error removing product from cart:', error);
    }
  }

  /**
   * Gets a product from the product list.
   * 
   * @param {string} productId - The ID of the product to get.
   * @returns {Object|null} The product object or null if not found.
   */
  getProductFromList(productId) {
    const productList = Array.from(this.productListElement.children);
    return productList.find((product) => product.dataset.productId === productId);
  }

  /**
   * Updates the cart display.
   */
  updateCartDisplay() {
    // Clear cart items element
    this.cartItemsElement.innerHTML = '';

    // Calculate total cost
    let totalCost = 0;

    // Iterate over cart items
    Object.values(this.cart).forEach((product) => {
      // Create cart item element
      const cartItemElement = document.createElement('div');
      cartItemElement.innerHTML = `
        <span>${product.name} x ${product.quantity}</span>
        <span>$${product.price * product.quantity}</span>
        <button class="remove-from-cart" data-product-id="${product.id}">Remove</button>
      `;

      // Add cart item element to cart items element
      this.cartItemsElement.appendChild(cartItemElement);

      // Update total cost
      totalCost += product.price * product.quantity;
    });

    // Update cart element
    this.cartElement.innerHTML = `
      <span>Cart (${Object.keys(this.cart).length} items)</span>
      <span>Total: $${totalCost}</span>
    `;
  }
}

// Example usage:
const cartElement = document.getElementById('cart');
const cartItemsElement = document.getElementById('cart-items');
const productListElement = document.getElementById('product-list');

const cartUpdater = new CartUpdater(cartElement, cartItemsElement, productListElement);
```
