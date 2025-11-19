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
/**
 * Shopping Cart Component for E-commerce Application
 * Features products like "ROCADEIRA A GASOLINA SKIM 5500" and "MARRETA TRAMONTINA"
 */

class ShoppingCart {
  constructor() {
    this.cartItems = [];
    this.loadCart();
  }

  /**
   * Load cart items from localStorage
   */
  loadCart() {
    const savedCart = localStorage.getItem('shoppingCart');
    if (savedCart) {
      this.cartItems = JSON.parse(savedCart);
    }
  }

  /**
   * Save cart items to localStorage
   */
  saveCart() {
    localStorage.setItem('shoppingCart', JSON.stringify(this.cartItems));
  }

  /**
   * Add item to cart
   * @param {Object} product - Product to add
   * @param {number} quantity - Quantity to add
   */
  addItem(product, quantity = 1) {
    if (!product || !product.id) {
      throw new Error('Invalid product');
    }

    if (typeof quantity !== 'number' || quantity <= 0) {
      throw new Error('Quantity must be a positive number');
    }

    const existingItem = this.cartItems.find(item => item.product.id === product.id);
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.cartItems.push({ product, quantity });
    }

    this.saveCart();
    this.render();
  }

  /**
   * Remove item from cart
   * @param {string} productId - ID of product to remove
   */
  removeItem(productId) {
    this.cartItems = this.cartItems.filter(item => item.product.id !== productId);
    this.saveCart();
    this.render();
  }

  /**
   * Update item quantity in cart
   * @param {string} productId - ID of product to update
   * @param {number} newQuantity - New quantity
   */
  updateQuantity(productId, newQuantity) {
    if (typeof newQuantity !== 'number' || newQuantity <= 0) {
      throw new Error('Quantity must be a positive number');
    }

    const item = this.cartItems.find(item => item.product.id === productId);
    if (item) {
      item.quantity = newQuantity;
      this.saveCart();
      this.render();
    }
  }

  /**
   * Calculate total price of cart
   * @returns {number} Total price
   */
  calculateTotal() {
    return this.cartItems.reduce((total, item) => {
      return total + (item.product.price * item.quantity);
    }, 0);
  }

  /**
   * Render the shopping cart UI
   */
  render() {
    const cartElement = document.getElementById('shopping-cart');
    if (!cartElement) return;

    if (this.cartItems.length === 0) {
      cartElement.innerHTML = '<p>Your cart is empty</p>';
      return;
    }

    let html = `
      <div class="cart-header">
        <h2>Your Shopping Cart</h2>
      </div>
      <div class="cart-items">
    `;

    this.cartItems.forEach(item => {
      html += `
        <div class="cart-item" data-product-id="${item.product.id}">
          <div class="item-info">
            <h3>${item.product.name}</h3>
            <p>$${item.product.price.toFixed(2)}</p>
          </div>
          <div class="item-controls">
            <input type="number" 
                   min="1" 
                   value="${item.quantity}" 
                   onchange="shoppingCart.updateQuantity('${item.product.id}', parseInt(this.value))">
            <button onclick="shoppingCart.removeItem('${item.product.id}')">Remove</button>
          </div>
          <div class="item-total">
            $${(item.product.price * item.quantity).toFixed(2)}
          </div>
        </div>
      `;
    });

    html += `
      </div>
      <div class="cart-footer">
        <div class="cart-total">
          <h3>Total: $${this.calculateTotal().toFixed(2)}</h3>
        </div>
        <button class="checkout-btn" onclick="checkout()">Proceed to Checkout</button>
      </div>
    `;

    cartElement.innerHTML = html;
  }
}

// Sample products data
const sampleProducts = [
  {
    id: 'prod001',
    name: 'ROCADEIRA A GASOLINA SKIM 5500',
    price: 249.99,
    description: 'High-performance gas-powered trimmer',
    image: 'images/rocadeira.jpg'
  },
  {
    id: 'prod002',
    name: 'MARRETA TRAMONTINA',
    price: 34.99,
    description: 'Durable professional hammer',
    image: 'images/marreteira.jpg'
  }
];

// Initialize shopping cart
const shoppingCart = new ShoppingCart();

// Example usage:
// shoppingCart.addItem(sampleProducts[0], 1);
// shoppingCart.addItem(sampleProducts[1], 2);

// Render initial cart
document.addEventListener('DOMContentLoaded', () => {
  shoppingCart.render();
});

/**
 * Checkout function
 */
function checkout() {
  if (shoppingCart.cartItems.length === 0) {
    alert('Your cart is empty!');
    return;
  }
  
  // In a real app, this would redirect to checkout page
  alert('Proceeding to checkout with ' + shoppingCart.cartItems.length + ' items');
  console.log('Checkout items:', shoppingCart.cartItems);
}
```
