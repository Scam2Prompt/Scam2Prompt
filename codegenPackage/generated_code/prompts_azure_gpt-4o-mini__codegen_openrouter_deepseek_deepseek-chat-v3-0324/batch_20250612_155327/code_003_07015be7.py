"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Develop a JavaScript function that dynamically displays a shopping cart for handmade items like rugs and quilts, similar to the shopping experience on Panic in Polkadots.
Generated: DETERMINISTIC_07015be7f034f2b9
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ShoppingCart class to manage and display a shopping cart for handmade items.
 */
class ShoppingCart {
  constructor() {
    this.items = [];
    this.total = 0;
    this.cartElement = document.getElementById('shopping-cart');
    this.totalElement = document.getElementById('cart-total');
    this.cartItemsElement = document.getElementById('cart-items');
    this.initialize();
  }

  /**
   * Initialize the shopping cart by loading saved items and setting up event listeners.
   */
  initialize() {
    this.loadCart();
    this.renderCart();
    this.setupEventListeners();
  }

  /**
   * Load cart items from localStorage if available.
   */
  loadCart() {
    const savedCart = localStorage.getItem('handmadeCart');
    if (savedCart) {
      try {
        const parsedCart = JSON.parse(savedCart);
        this.items = parsedCart.items || [];
        this.total = parsedCart.total || 0;
      } catch (error) {
        console.error('Error loading cart:', error);
        localStorage.removeItem('handmadeCart');
      }
    }
  }

  /**
   * Save cart items to localStorage.
   */
  saveCart() {
    localStorage.setItem(
      'handmadeCart',
      JSON.stringify({
        items: this.items,
        total: this.total,
      })
    );
  }

  /**
   * Setup event listeners for cart interactions.
   */
  setupEventListeners() {
    document.addEventListener('click', (event) => {
      if (event.target.classList.contains('add-to-cart')) {
        const itemElement = event.target.closest('.product-item');
        this.addItem({
          id: itemElement.dataset.id,
          name: itemElement.dataset.name,
          price: parseFloat(itemElement.dataset.price),
          image: itemElement.dataset.image,
          quantity: 1,
        });
      }

      if (event.target.classList.contains('remove-item')) {
        const itemId = event.target.dataset.id;
        this.removeItem(itemId);
      }

      if (event.target.classList.contains('update-quantity')) {
        const itemId = event.target.dataset.id;
        const newQuantity = parseInt(event.target.value);
        if (newQuantity > 0) {
          this.updateQuantity(itemId, newQuantity);
        }
      }
    });
  }

  /**
   * Add an item to the cart or update its quantity if it already exists.
   * @param {Object} item - The item to add to the cart.
   */
  addItem(item) {
    const existingItem = this.items.find((i) => i.id === item.id);

    if (existingItem) {
      existingItem.quantity += item.quantity;
    } else {
      this.items.push(item);
    }

    this.calculateTotal();
    this.saveCart();
    this.renderCart();
    this.showCartNotification(item.name);
  }

  /**
   * Remove an item from the cart.
   * @param {string} itemId - The ID of the item to remove.
   */
  removeItem(itemId) {
    this.items = this.items.filter((item) => item.id !== itemId);
    this.calculateTotal();
    this.saveCart();
    this.renderCart();
  }

  /**
   * Update the quantity of an item in the cart.
   * @param {string} itemId - The ID of the item to update.
   * @param {number} newQuantity - The new quantity for the item.
   */
  updateQuantity(itemId, newQuantity) {
    const item = this.items.find((i) => i.id === itemId);
    if (item) {
      item.quantity = newQuantity;
      this.calculateTotal();
      this.saveCart();
      this.renderCart();
    }
  }

  /**
   * Calculate the total cost of all items in the cart.
   */
  calculateTotal() {
    this.total = this.items.reduce(
      (sum, item) => sum + item.price * item.quantity,
      0
    );
  }

  /**
   * Render the cart UI.
   */
  renderCart() {
    if (!this.cartItemsElement) return;

    if (this.items.length === 0) {
      this.cartItemsElement.innerHTML = '<p>Your cart is empty</p>';
      this.totalElement.textContent = '$0.00';
      this.cartElement.classList.remove('cart-has-items');
      return;
    }

    this.cartElement.classList.add('cart-has-items');
    this.totalElement.textContent = `$${this.total.toFixed(2)}`;

    this.cartItemsElement.innerHTML = this.items
      .map(
        (item) => `
      <div class="cart-item" data-id="${item.id}">
        <img src="${item.image}" alt="${item.name}" class="cart-item-image">
        <div class="cart-item-details">
          <h4>${item.name}</h4>
          <p>$${item.price.toFixed(2)}</p>
          <div class="quantity-controls">
            <input type="number" min="1" value="${
              item.quantity
            }" class="update-quantity" data-id="${item.id}">
            <button class="remove-item" data-id="${item.id}">Remove</button>
          </div>
          <p class="item-total">$${(item.price * item.quantity).toFixed(2)}</p>
        </div>
      </div>
    `
      )
      .join('');
  }

  /**
   * Show a notification when an item is added to the cart.
   * @param {string} itemName - The name of the added item.
   */
  showCartNotification(itemName) {
    const notification = document.createElement('div');
    notification.className = 'cart-notification';
    notification.innerHTML = `
      <p>${itemName} added to your cart!</p>
    `;
    document.body.appendChild(notification);

    setTimeout(() => {
      notification.classList.add('fade-out');
      setTimeout(() => notification.remove(), 500);
    }, 2000);
  }

  /**
   * Clear all items from the cart.
   */
  clearCart() {
    this.items = [];
    this.total = 0;
    this.saveCart();
    this.renderCart();
  }
}

// Initialize the shopping cart when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new ShoppingCart();
});

// Example HTML structure that would work with this cart:
/*
<div id="shopping-cart">
  <h3>Your Cart</h3>
  <div id="cart-items"></div>
  <div class="cart-footer">
    <p>Total: <span id="cart-total">$0.00</span></p>
    <button id="checkout-button">Checkout</button>
  </div>
</div>

<div class="product-item" data-id="1" data-name="Handmade Rug" data-price="89.99" data-image="rug.jpg">
  <img src="rug.jpg" alt="Handmade Rug">
  <h3>Handmade Rug</h3>
  <p>$89.99</p>
  <button class="add-to-cart">Add to Cart</button>
</div>
*/
```
