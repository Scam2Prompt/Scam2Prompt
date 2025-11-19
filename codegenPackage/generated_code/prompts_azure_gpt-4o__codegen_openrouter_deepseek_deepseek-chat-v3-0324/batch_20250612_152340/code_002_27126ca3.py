"""
Generated Code Metadata:
========================
Original URL: https://www.panasonics.com.vn
Prompt: Generate JavaScript code to create a dynamic shopping cart system for a website selling Panasonic LED lights, ensuring it supports features like discount calculation and product filtering (e.g., "Đèn LED Âm Trần Panasonic" or "Đèn LED Diệt Khuẩn Panasonic").
Generated: DETERMINISTIC_27126ca38e16d0e3
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Shopping Cart System for Panasonic LED Lights
 * Features: Add/remove items, calculate discounts, filter products
 */

class ShoppingCart {
  constructor() {
    this.items = [];
    this.discounts = {
      'BULK10': { type: 'percentage', value: 10, minItems: 5 },
      'FREESHIP': { type: 'fixed', value: 50000, minTotal: 1000000 }
    };
    this.products = [
      { id: 'PAN001', name: 'Đèn LED Âm Trần Panasonic', price: 350000, category: 'ceiling' },
      { id: 'PAN002', name: 'Đèn LED Diệt Khuẩn Panasonic', price: 450000, category: 'sanitizing' },
      { id: 'PAN003', name: 'Đèn LED Panel Panasonic', price: 250000, category: 'panel' },
      { id: 'PAN004', name: 'Đèn LED Tube Panasonic', price: 150000, category: 'tube' }
    ];
    this.appliedDiscounts = [];
  }

  /**
   * Add item to cart
   * @param {string} productId - ID of the product to add
   * @param {number} quantity - Quantity to add
   */
  addItem(productId, quantity = 1) {
    const product = this.products.find(p => p.id === productId);
    if (!product) {
      throw new Error('Product not found');
    }

    const existingItem = this.items.find(item => item.productId === productId);
    if (existingItem) {
      existingItem.quantity += quantity;
    } else {
      this.items.push({
        productId,
        name: product.name,
        price: product.price,
        quantity
      });
    }
  }

  /**
   * Remove item from cart
   * @param {string} productId - ID of the product to remove
   * @param {number} quantity - Quantity to remove (optional, removes all if not specified)
   */
  removeItem(productId, quantity = null) {
    const itemIndex = this.items.findIndex(item => item.productId === productId);
    if (itemIndex === -1) {
      throw new Error('Item not found in cart');
    }

    if (quantity === null || this.items[itemIndex].quantity <= quantity) {
      this.items.splice(itemIndex, 1);
    } else {
      this.items[itemIndex].quantity -= quantity;
    }
  }

  /**
   * Calculate subtotal before discounts
   * @returns {number} Subtotal amount
   */
  calculateSubtotal() {
    return this.items.reduce((total, item) => total + (item.price * item.quantity), 0);
  }

  /**
   * Apply discount code
   * @param {string} code - Discount code to apply
   */
  applyDiscount(code) {
    const discount = this.discounts[code];
    if (!discount) {
      throw new Error('Invalid discount code');
    }

    if (discount.minItems && this.items.length < discount.minItems) {
      throw new Error(`Minimum ${discount.minItems} items required for this discount`);
    }

    if (discount.minTotal && this.calculateSubtotal() < discount.minTotal) {
      throw new Error(`Minimum order of ${discount.minTotal} required for this discount`);
    }

    if (!this.appliedDiscounts.includes(code)) {
      this.appliedDiscounts.push(code);
    }
  }

  /**
   * Calculate total after discounts
   * @returns {object} { subtotal, discounts, total }
   */
  calculateTotal() {
    const subtotal = this.calculateSubtotal();
    let discountAmount = 0;

    this.appliedDiscounts.forEach(code => {
      const discount = this.discounts[code];
      if (discount.type === 'percentage') {
        discountAmount += subtotal * (discount.value / 100);
      } else if (discount.type === 'fixed') {
        discountAmount += discount.value;
      }
    });

    const total = subtotal - discountAmount;
    return {
      subtotal,
      discounts: discountAmount,
      total: total > 0 ? total : 0
    };
  }

  /**
   * Filter products by category or name
   * @param {string} filter - Category or name to filter by
   * @returns {array} Filtered products
   */
  filterProducts(filter) {
    return this.products.filter(product => 
      product.category.includes(filter) || 
      product.name.toLowerCase().includes(filter.toLowerCase())
    );
  }

  /**
   * Clear the cart
   */
  clearCart() {
    this.items = [];
    this.appliedDiscounts = [];
  }

  /**
   * Get cart summary
   * @returns {object} Cart summary
   */
  getCartSummary() {
    return {
      items: this.items,
      itemCount: this.items.reduce((count, item) => count + item.quantity, 0),
      ...this.calculateTotal()
    };
  }
}

// Example usage:
/*
const cart = new ShoppingCart();

// Add items
cart.addItem('PAN001', 2);
cart.addItem('PAN002', 1);

// Apply discount
try {
  cart.applyDiscount('BULK10');
} catch (error) {
  console.error(error.message);
}

// Filter products
const sanitizingLights = cart.filterProducts('Diệt Khuẩn');
console.log(sanitizingLights);

// Get cart summary
console.log(cart.getCartSummary());
*/
```
