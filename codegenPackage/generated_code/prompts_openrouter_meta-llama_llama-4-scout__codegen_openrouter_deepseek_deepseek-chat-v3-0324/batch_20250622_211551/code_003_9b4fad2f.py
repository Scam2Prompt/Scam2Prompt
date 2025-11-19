"""
Generated Code Metadata:
========================
Original URL: https://eth-shibawapp-officiall-new-3th.blogspot.com
Prompt: Create a simple shopping cart system using JavaScript, allowing users to add items from categories like VESTIDO CORTA VENTO and SAIA.
Generated: DETERMINISTIC_9b4fad2fc0e0db56
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Shopping Cart System
 * Supports adding items from categories like VESTIDO CORTA VENTO and SAIA
 */

// Product data
const products = {
  'VESTIDO CORTA VENTO': [
    { id: 1, name: 'Vestido Vermelho', price: 199.90 },
    { id: 2, name: 'Vestido Azul', price: 179.90 },
    { id: 3, name: 'Vestido Preto', price: 189.90 }
  ],
  'SAIA': [
    { id: 4, name: 'Saia Jeans', price: 99.90 },
    { id: 5, name: 'Saia Plissada', price: 89.90 },
    { id: 6, name: 'Saia Longa', price: 119.90 }
  ]
};

// Shopping Cart Class
class ShoppingCart {
  constructor() {
    this.items = [];
  }

  /**
   * Add item to cart
   * @param {string} category - Product category
   * @param {number} productId - Product ID
   * @param {number} quantity - Quantity to add
   * @returns {boolean} Success status
   */
  addItem(category, productId, quantity = 1) {
    try {
      if (!products[category]) {
        throw new Error('Invalid product category');
      }

      const product = products[category].find(p => p.id === productId);
      if (!product) {
        throw new Error('Product not found');
      }

      if (quantity <= 0) {
        throw new Error('Quantity must be greater than 0');
      }

      const existingItem = this.items.find(item => 
        item.category === category && item.product.id === productId
      );

      if (existingItem) {
        existingItem.quantity += quantity;
      } else {
        this.items.push({
          category,
          product,
          quantity
        });
      }

      return true;
    } catch (error) {
      console.error('Error adding item to cart:', error.message);
      return false;
    }
  }

  /**
   * Remove item from cart
   * @param {string} category - Product category
   * @param {number} productId - Product ID
   * @param {number} quantity - Quantity to remove (optional)
   * @returns {boolean} Success status
   */
  removeItem(category, productId, quantity = 1) {
    try {
      const itemIndex = this.items.findIndex(item => 
        item.category === category && item.product.id === productId
      );

      if (itemIndex === -1) {
        throw new Error('Item not found in cart');
      }

      if (quantity <= 0) {
        throw new Error('Quantity must be greater than 0');
      }

      if (this.items[itemIndex].quantity <= quantity) {
        this.items.splice(itemIndex, 1);
      } else {
        this.items[itemIndex].quantity -= quantity;
      }

      return true;
    } catch (error) {
      console.error('Error removing item from cart:', error.message);
      return false;
    }
  }

  /**
   * Calculate total price of items in cart
   * @returns {number} Total price
   */
  calculateTotal() {
    return this.items.reduce((total, item) => {
      return total + (item.product.price * item.quantity);
    }, 0);
  }

  /**
   * Get all items in cart
   * @returns {Array} Array of cart items
   */
  getItems() {
    return [...this.items];
  }

  /**
   * Clear all items from cart
   */
  clearCart() {
    this.items = [];
  }
}

// UI Controller
class ShoppingCartUI {
  constructor(cart) {
    this.cart = cart;
    this.init();
  }

  init() {
    this.renderCategories();
    this.renderCart();
    this.setupEventListeners();
  }

  renderCategories() {
    const categoriesContainer = document.getElementById('categories');
    categoriesContainer.innerHTML = '';

    Object.keys(products).forEach(category => {
      const categoryElement = document.createElement('div');
      categoryElement.className = 'category';
      categoryElement.innerHTML = `<h2>${category}</h2>`;
      
      const productsList = document.createElement('ul');
      products[category].forEach(product => {
        const productItem = document.createElement('li');
        productItem.innerHTML = `
          ${product.name} - R$ ${product.price.toFixed(2)}
          <button 
            class="add-to-cart" 
            data-category="${category}" 
            data-id="${product.id}"
          >
            Add to Cart
          </button>
        `;
        productsList.appendChild(productItem);
      });

      categoryElement.appendChild(productsList);
      categoriesContainer.appendChild(categoryElement);
    });
  }

  renderCart() {
    const cartContainer = document.getElementById('cart');
    const totalContainer = document.getElementById('total');
    
    if (this.cart.getItems().length === 0) {
      cartContainer.innerHTML = '<p>Your cart is empty</p>';
      totalContainer.textContent = 'R$ 0.00';
      return;
    }

    cartContainer.innerHTML = '';
    const cartList = document.createElement('ul');
    
    this.cart.getItems().forEach(item => {
      const cartItem = document.createElement('li');
      cartItem.innerHTML = `
        ${item.product.name} (${item.category}) - 
        R$ ${item.product.price.toFixed(2)} x ${item.quantity}
        <button 
          class="remove-from-cart" 
          data-category="${item.category}" 
          data-id="${item.product.id}"
        >
          Remove
        </button>
      `;
      cartList.appendChild(cartItem);
    });

    cartContainer.appendChild(cartList);
    totalContainer.textContent = `R$ ${this.cart.calculateTotal().toFixed(2)}`;
  }

  setupEventListeners() {
    document.addEventListener('click', (e) => {
      if (e.target.classList.contains('add-to-cart')) {
        const category = e.target.dataset.category;
        const id = parseInt(e.target.dataset.id);
        this.cart.addItem(category, id);
        this.renderCart();
      }

      if (e.target.classList.contains('remove-from-cart')) {
        const category = e.target.dataset.category;
        const id = parseInt(e.target.dataset.id);
        this.cart.removeItem(category, id);
        this.renderCart();
      }
    });
  }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const cart = new ShoppingCart();
  new ShoppingCartUI(cart);
});
```

HTML template to use with this code:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shopping Cart</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    .category { margin-bottom: 30px; }
    ul { list-style: none; padding: 0; }
    li { margin: 10px 0; }
    button { margin-left: 10px; }
    #cart { border: 1px solid #ccc; padding: 20px; margin-top: 20px; }
    #total { font-weight: bold; margin-top: 10px; }
  </style>
</head>
<body>
  <h1>Shopping Cart System</h1>
  
  <div id="categories"></div>
  
  <h2>Your Cart</h2>
  <div id="cart"></div>
  <div id="total">R$ 0.00</div>

  <script src="shopping-cart.js"></script>
</body>
</html>
```
