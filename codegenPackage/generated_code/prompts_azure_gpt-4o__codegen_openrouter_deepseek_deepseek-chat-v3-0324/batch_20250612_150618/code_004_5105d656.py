"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Write JavaScript code to enable a shopping cart feature for an e-commerce site like "Mass Compras," including functionality for adding items like "Cámara de Seguridad WiFi Inteligente" and calculating the total price.
Generated: DETERMINISTIC_5105d65695099471
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Shopping Cart Module for Mass Compras E-commerce Site
 * Handles adding items, removing items, updating quantities, and calculating totals.
 */

class ShoppingCart {
  constructor() {
    this.items = [];
    this.loadCart();
  }

  /**
   * Load cart from localStorage if available
   */
  loadCart() {
    const savedCart = localStorage.getItem('massComprasCart');
    if (savedCart) {
      this.items = JSON.parse(savedCart);
    }
  }

  /**
   * Save cart to localStorage
   */
  saveCart() {
    localStorage.setItem('massComprasCart', JSON.stringify(this.items));
  }

  /**
   * Add item to cart or update quantity if already exists
   * @param {Object} item - The item to add
   * @param {string} item.id - Product ID
   * @param {string} item.name - Product name
   * @param {number} item.price - Product price
   * @param {number} [quantity=1] - Quantity to add
   */
  addItem(item, quantity = 1) {
    if (!item || !item.id || !item.name || item.price === undefined) {
      throw new Error('Invalid item format');
    }

    const existingItem = this.items.find(i => i.id === item.id);
    
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.items.push({
        id: item.id,
        name: item.name,
        price: item.price,
        quantity: quantity
      });
    }

    this.saveCart();
    this.updateCartUI();
  }

  /**
   * Remove item from cart
   * @param {string} itemId - ID of item to remove
   */
  removeItem(itemId) {
    this.items = this.items.filter(item => item.id !== itemId);
    this.saveCart();
    this.updateCartUI();
  }

  /**
   * Update item quantity in cart
   * @param {string} itemId - ID of item to update
   * @param {number} newQuantity - New quantity
   */
  updateQuantity(itemId, newQuantity) {
    if (newQuantity <= 0) {
      this.removeItem(itemId);
      return;
    }

    const item = this.items.find(i => i.id === itemId);
    if (item) {
      item.quantity = newQuantity;
      this.saveCart();
      this.updateCartUI();
    }
  }

  /**
   * Calculate total price of all items in cart
   * @returns {number} Total price
   */
  calculateTotal() {
    return this.items.reduce((total, item) => {
      return total + (item.price * item.quantity);
    }, 0);
  }

  /**
   * Get count of all items in cart
   * @returns {number} Total item count
   */
  getItemCount() {
    return this.items.reduce((count, item) => {
      return count + item.quantity;
    }, 0);
  }

  /**
   * Clear all items from cart
   */
  clearCart() {
    this.items = [];
    this.saveCart();
    this.updateCartUI();
  }

  /**
   * Update the cart UI (to be implemented based on site structure)
   */
  updateCartUI() {
    // This would be implemented based on your specific HTML structure
    // For example:
    const cartCountElement = document.getElementById('cart-count');
    const cartTotalElement = document.getElementById('cart-total');
    
    if (cartCountElement) {
      cartCountElement.textContent = this.getItemCount();
    }
    
    if (cartTotalElement) {
      cartTotalElement.textContent = `$${this.calculateTotal().toFixed(2)}`;
    }
  }
}

// Example usage:
const cart = new ShoppingCart();

// Example product data
const securityCamera = {
  id: 'prod001',
  name: 'Cámara de Seguridad WiFi Inteligente',
  price: 199.99
};

// Add event listeners for product buttons
document.addEventListener('DOMContentLoaded', () => {
  // Example: Add to cart button for security camera
  const addToCartBtn = document.getElementById('add-to-cart-btn');
  if (addToCartBtn) {
    addToCartBtn.addEventListener('click', () => {
      cart.addItem(securityCamera);
      alert('Producto añadido al carrito');
    });
  }

  // Initialize cart UI
  cart.updateCartUI();
});

// For more complete implementation, you would also need:
// - Cart page with list of items, quantities, and remove buttons
// - Checkout functionality
// - More product data and buttons
```
