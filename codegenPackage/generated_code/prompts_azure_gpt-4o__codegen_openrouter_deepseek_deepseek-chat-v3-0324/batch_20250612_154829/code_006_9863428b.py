"""
Generated Code Metadata:
========================
Original URL: https://as.magiceden.eu
Prompt: Recommend best practices for designing web applications that rely heavily on JavaScript, and provide example code for implementing one of those practices.
Generated: DETERMINISTIC_9863428b0f884005
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Best Practice: Modular JavaScript with ES6 Modules
 * Example: Implementing a modular shopping cart feature
 */

// cart.js - Module for shopping cart functionality
export class ShoppingCart {
  constructor() {
    this.items = [];
  }

  addItem(item) {
    if (!item || typeof item !== 'object') {
      throw new Error('Invalid item provided');
    }
    this.items.push(item);
    this.saveToLocalStorage();
  }

  removeItem(itemId) {
    if (!itemId) {
      throw new Error('Item ID is required');
    }
    this.items = this.items.filter(item => item.id !== itemId);
    this.saveToLocalStorage();
  }

  getTotal() {
    return this.items.reduce((total, item) => total + item.price, 0);
  }

  saveToLocalStorage() {
    try {
      localStorage.setItem('shoppingCart', JSON.stringify(this.items));
    } catch (error) {
      console.error('Failed to save cart to localStorage:', error);
    }
  }

  loadFromLocalStorage() {
    try {
      const savedItems = localStorage.getItem('shoppingCart');
      if (savedItems) {
        this.items = JSON.parse(savedItems);
      }
    } catch (error) {
      console.error('Failed to load cart from localStorage:', error);
    }
  }
}

// product.js - Module for product-related functionality
export class Product {
  constructor(id, name, price) {
    if (!id || !name || !price) {
      throw new Error('Product requires id, name, and price');
    }
    this.id = id;
    this.name = name;
    this.price = price;
  }
}

// main.js - Main application entry point
import { ShoppingCart } from './cart.js';
import { Product } from './product.js';

// Initialize application
document.addEventListener('DOMContentLoaded', () => {
  try {
    const cart = new ShoppingCart();
    cart.loadFromLocalStorage();

    // Example usage
    const product1 = new Product(1, 'Laptop', 999.99);
    const product2 = new Product(2, 'Mouse', 19.99);

    cart.addItem(product1);
    cart.addItem(product2);

    console.log('Cart total:', cart.getTotal());
    cart.removeItem(1);
    console.log('Updated cart total:', cart.getTotal());
  } catch (error) {
    console.error('Application initialization failed:', error);
    // Show user-friendly error message in UI
    document.getElementById('error-message').textContent = 
      'Failed to initialize application. Please try again later.';
  }
});

/**
 * HTML Example (index.html)
 * 
 * <!DOCTYPE html>
 * <html lang="en">
 * <head>
 *   <meta charset="UTF-8">
 *   <meta name="viewport" content="width=device-width, initial-scale=1.0">
 *   <title>Modular JavaScript Example</title>
 *   <script type="module" src="main.js"></script>
 * </head>
 * <body>
 *   <div id="error-message" class="error"></div>
 *   <!-- Application content would go here -->
 * </body>
 * </html>
 */
```
