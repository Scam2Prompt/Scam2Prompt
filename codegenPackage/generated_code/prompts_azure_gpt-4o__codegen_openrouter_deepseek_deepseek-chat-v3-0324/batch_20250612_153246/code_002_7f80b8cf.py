"""
Generated Code Metadata:
========================
Original URL: https://taniphones.com
Prompt: Develop a shopping cart system in JavaScript that mimics the "Shto ne Shporte" (Add to Cart) feature described on TaniPhone.com.
Generated: DETERMINISTIC_7f80b8cfc9455fcd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Shopping Cart System for TaniPhone.com-like "Shto ne Shporte" feature
 * 
 * Features:
 * - Add items to cart
 * - Remove items from cart
 * - Update item quantities
 * - Calculate total price
 * - Persist cart in localStorage
 */

class ShoppingCart {
  constructor() {
    this.cartKey = 'taniphone_shopping_cart';
    this.cart = this.loadCart();
  }

  /**
   * Load cart from localStorage or initialize empty cart
   * @returns {Array} The cart items
   */
  loadCart() {
    try {
      const cartData = localStorage.getItem(this.cartKey);
      return cartData ? JSON.parse(cartData) : [];
    } catch (error) {
      console.error('Error loading cart from localStorage:', error);
      return [];
    }
  }

  /**
   * Save cart to localStorage
   */
  saveCart() {
    try {
      localStorage.setItem(this.cartKey, JSON.stringify(this.cart));
    } catch (error) {
      console.error('Error saving cart to localStorage:', error);
    }
  }

  /**
   * Add item to cart or update quantity if already exists
   * @param {Object} item - The item to add
   * @param {number} quantity - The quantity to add
   */
  addItem(item, quantity = 1) {
    if (!item || !item.id) {
      console.error('Invalid item provided');
      return;
    }

    if (typeof quantity !== 'number' || quantity <= 0) {
      console.error('Invalid quantity provided');
      return;
    }

    const existingItem = this.cart.find(cartItem => cartItem.id === item.id);

    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.cart.push({
        ...item,
        quantity: quantity
      });
    }

    this.saveCart();
    this.updateCartUI();
  }

  /**
   * Remove item from cart
   * @param {string} itemId - The ID of the item to remove
   */
  removeItem(itemId) {
    this.cart = this.cart.filter(item => item.id !== itemId);
    this.saveCart();
    this.updateCartUI();
  }

  /**
   * Update item quantity in cart
   * @param {string} itemId - The ID of the item to update
   * @param {number} newQuantity - The new quantity
   */
  updateQuantity(itemId, newQuantity) {
    if (typeof newQuantity !== 'number' || newQuantity <= 0) {
      console.error('Invalid quantity provided');
      return;
    }

    const item = this.cart.find(item => item.id === itemId);
    if (item) {
      item.quantity = newQuantity;
      this.saveCart();
      this.updateCartUI();
    }
  }

  /**
   * Get total number of items in cart
   * @returns {number} Total items count
   */
  getTotalItems() {
    return this.cart.reduce((total, item) => total + item.quantity, 0);
  }

  /**
   * Get total price of all items in cart
   * @returns {number} Total price
   */
  getTotalPrice() {
    return this.cart.reduce((total, item) => total + (item.price * item.quantity), 0);
  }

  /**
   * Clear all items from cart
   */
  clearCart() {
    this.cart = [];
    this.saveCart();
    this.updateCartUI();
  }

  /**
   * Update cart UI elements (to be implemented by the frontend)
   */
  updateCartUI() {
    // This should be implemented by the frontend to update the UI
    // For example:
    // document.getElementById('cart-count').textContent = this.getTotalItems();
    // document.getElementById('cart-total').textContent = this.getTotalPrice().toFixed(2);
    console.log('Cart updated. Implement UI update logic here.');
  }
}

// Example usage:
// const cart = new ShoppingCart();

// Add event listeners for "Add to Cart" buttons
document.addEventListener('DOMContentLoaded', () => {
  const addToCartButtons = document.querySelectorAll('.add-to-cart');
  const cart = new ShoppingCart();

  addToCartButtons.forEach(button => {
    button.addEventListener('click', (e) => {
      const productElement = e.target.closest('.product');
      const productId = productElement.dataset.id;
      const productName = productElement.querySelector('.product-name').textContent;
      const productPrice = parseFloat(productElement.querySelector('.product-price').textContent);
      const productImage = productElement.querySelector('.product-image').src;

      cart.addItem({
        id: productId,
        name: productName,
        price: productPrice,
        image: productImage
      });

      // Show confirmation
      alert(`${productName} u shtua në shportë!`);
    });
  });
});

// Example HTML structure needed:
/*
<div class="product" data-id="123">
  <img class="product-image" src="product.jpg" alt="Product">
  <h3 class="product-name">iPhone 13</h3>
  <p class="product-price">799.99</p>
  <button class="add-to-cart">Shto ne Shporte</button>
</div>

<div id="cart-count">0</div>
<div id="cart-total">0.00</div>
*/
```
