"""
Generated Code Metadata:
========================
Original URL: https://adhive.net
Prompt: Design a simple e-commerce cart system using JavaScript that updates the total price when items like the "Anas Ali Shopify Course Complete" are added or removed.
Generated: DETERMINISTIC_ad5caa186c49a60a
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * E-commerce Cart System
 * 
 * Features:
 * - Add items to cart
 * - Remove items from cart
 * - Update quantity of items
 * - Calculate total price
 * - Persist cart in localStorage
 */

class CartItem {
  /**
   * @param {string} id - Unique identifier for the item
   * @param {string} name - Name of the item
   * @param {number} price - Price of the item
   * @param {number} quantity - Quantity of the item (default: 1)
   */
  constructor(id, name, price, quantity = 1) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.quantity = quantity;
  }

  /**
   * Calculate total price for this item
   * @returns {number} Total price
   */
  getTotalPrice() {
    return this.price * this.quantity;
  }
}

class ShoppingCart {
  constructor() {
    this.items = this.loadCart();
    this.renderCart();
  }

  /**
   * Load cart from localStorage
   * @returns {Array<CartItem>} Array of cart items
   */
  loadCart() {
    try {
      const savedCart = localStorage.getItem('shoppingCart');
      if (savedCart) {
        return JSON.parse(savedCart).map(item => new CartItem(
          item.id,
          item.name,
          item.price,
          item.quantity
        ));
      }
      return [];
    } catch (error) {
      console.error('Error loading cart:', error);
      return [];
    }
  }

  /**
   * Save cart to localStorage
   */
  saveCart() {
    localStorage.setItem('shoppingCart', JSON.stringify(this.items));
  }

  /**
   * Add item to cart or update quantity if already exists
   * @param {string} id - Item ID
   * @param {string} name - Item name
   * @param {number} price - Item price
   * @param {number} quantity - Item quantity (default: 1)
   */
  addItem(id, name, price, quantity = 1) {
    const existingItem = this.items.find(item => item.id === id);
    
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.items.push(new CartItem(id, name, price, quantity));
    }
    
    this.saveCart();
    this.renderCart();
  }

  /**
   * Remove item from cart
   * @param {string} id - Item ID to remove
   */
  removeItem(id) {
    this.items = this.items.filter(item => item.id !== id);
    this.saveCart();
    this.renderCart();
  }

  /**
   * Update item quantity in cart
   * @param {string} id - Item ID
   * @param {number} newQuantity - New quantity
   */
  updateQuantity(id, newQuantity) {
    const item = this.items.find(item => item.id === id);
    if (item) {
      item.quantity = newQuantity;
      this.saveCart();
      this.renderCart();
    }
  }

  /**
   * Calculate total price of all items in cart
   * @returns {number} Total price
   */
  calculateTotal() {
    return this.items.reduce((total, item) => total + item.getTotalPrice(), 0);
  }

  /**
   * Render cart to the DOM
   */
  renderCart() {
    const cartElement = document.getElementById('cart');
    const totalElement = document.getElementById('cart-total');
    
    if (!cartElement || !totalElement) return;

    cartElement.innerHTML = '';
    
    if (this.items.length === 0) {
      cartElement.innerHTML = '<p>Your cart is empty</p>';
      totalElement.textContent = '$0.00';
      return;
    }

    this.items.forEach(item => {
      const itemElement = document.createElement('div');
      itemElement.className = 'cart-item';
      itemElement.innerHTML = `
        <div class="item-info">
          <h4>${item.name}</h4>
          <p>$${item.price.toFixed(2)} x ${item.quantity}</p>
        </div>
        <div class="item-actions">
          <button class="quantity-btn" data-id="${item.id}" data-action="decrease">-</button>
          <button class="quantity-btn" data-id="${item.id}" data-action="increase">+</button>
          <button class="remove-btn" data-id="${item.id}">Remove</button>
        </div>
      `;
      cartElement.appendChild(itemElement);
    });

    totalElement.textContent = `$${this.calculateTotal().toFixed(2)}`;

    // Add event listeners
    document.querySelectorAll('.remove-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        this.removeItem(e.target.dataset.id);
      });
    });

    document.querySelectorAll('.quantity-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.target.dataset.id;
        const action = e.target.dataset.action;
        const item = this.items.find(item => item.id === id);
        
        if (item) {
          if (action === 'increase') {
            this.updateQuantity(id, item.quantity + 1);
          } else if (action === 'decrease' && item.quantity > 1) {
            this.updateQuantity(id, item.quantity - 1);
          }
        }
      });
    });
  }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
  const cart = new ShoppingCart();

  // Example product addition
  document.getElementById('add-course-btn')?.addEventListener('click', () => {
    cart.addItem(
      'course1',
      'Anas Ali Shopify Course Complete',
      99.99
    );
  });
});

// HTML structure needed for this to work:
/*
<div id="cart"></div>
<p>Total: <span id="cart-total">$0.00</span></p>
<button id="add-course-btn">Add Course</button>
*/
```
