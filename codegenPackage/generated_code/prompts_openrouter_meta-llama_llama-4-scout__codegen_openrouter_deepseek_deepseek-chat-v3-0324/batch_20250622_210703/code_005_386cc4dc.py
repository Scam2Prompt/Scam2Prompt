"""
Generated Code Metadata:
========================
Original URL: https://wrapstickfoods.com
Prompt: Create a JavaScript function to implement a self-service ordering system for Wrapstick Foods, allowing customers to place orders and make payments online.
Generated: DETERMINISTIC_386cc4dc0a79e867
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Self-service ordering system for Wrapstick Foods
 * Allows customers to place orders and make payments online
 */

class WrapstickOrderingSystem {
  constructor() {
    this.menu = {
      wraps: [
        { id: 1, name: 'Classic Wrap', price: 8.99 },
        { id: 2, name: 'Spicy Wrap', price: 9.99 },
        { id: 3, name: 'Veggie Wrap', price: 7.99 }
      ],
      sides: [
        { id: 4, name: 'Fries', price: 2.99 },
        { id: 5, name: 'Salad', price: 3.99 },
        { id: 6, name: 'Soup', price: 3.49 }
      ],
      drinks: [
        { id: 7, name: 'Soda', price: 1.99 },
        { id: 8, name: 'Iced Tea', price: 1.99 },
        { id: 9, name: 'Water', price: 0.99 }
      ]
    };
    this.currentOrder = [];
    this.orderStatus = 'pending';
    this.paymentMethods = ['credit_card', 'debit_card', 'paypal'];
  }

  /**
   * Display the full menu
   * @returns {Object} The complete menu
   */
  getMenu() {
    return this.menu;
  }

  /**
   * Add item to current order
   * @param {number} itemId - The ID of the item to add
   * @param {number} quantity - Quantity of the item
   * @returns {boolean} Success status
   */
  addToOrder(itemId, quantity = 1) {
    try {
      if (quantity < 1) throw new Error('Quantity must be at least 1');
      
      const item = this._findItemById(itemId);
      if (!item) throw new Error('Item not found in menu');
      
      for (let i = 0; i < quantity; i++) {
        this.currentOrder.push({...item});
      }
      
      return true;
    } catch (error) {
      console.error(`Error adding item to order: ${error.message}`);
      return false;
    }
  }

  /**
   * Remove item from current order
   * @param {number} itemId - The ID of the item to remove
   * @returns {boolean} Success status
   */
  removeFromOrder(itemId) {
    try {
      const index = this.currentOrder.findIndex(item => item.id === itemId);
      if (index === -1) throw new Error('Item not found in current order');
      
      this.currentOrder.splice(index, 1);
      return true;
    } catch (error) {
      console.error(`Error removing item from order: ${error.message}`);
      return false;
    }
  }

  /**
   * Get current order details
   * @returns {Object} Order details including items and total
   */
  getOrderDetails() {
    const total = this.currentOrder.reduce((sum, item) => sum + item.price, 0);
    return {
      items: [...this.currentOrder],
      total: parseFloat(total.toFixed(2)),
      itemCount: this.currentOrder.length
    };
  }

  /**
   * Process payment for current order
   * @param {string} paymentMethod - Payment method to use
   * @param {Object} paymentDetails - Payment details (e.g., card info)
   * @returns {Promise<Object>} Payment result
   */
  async processPayment(paymentMethod, paymentDetails) {
    try {
      if (!this.paymentMethods.includes(paymentMethod)) {
        throw new Error('Invalid payment method');
      }
      
      if (this.currentOrder.length === 0) {
        throw new Error('Cannot process payment for empty order');
      }
      
      // Simulate payment processing
      const paymentResult = await this._simulatePayment(paymentMethod, paymentDetails);
      
      if (paymentResult.success) {
        this.orderStatus = 'paid';
        return { success: true, orderId: this._generateOrderId(), ...paymentResult };
      } else {
        throw new Error(paymentResult.message || 'Payment failed');
      }
    } catch (error) {
      console.error(`Payment error: ${error.message}`);
      return { success: false, message: error.message };
    }
  }

  /**
   * Clear current order
   */
  clearOrder() {
    this.currentOrder = [];
    this.orderStatus = 'pending';
  }

  /**
   * Find item by ID in menu
   * @private
   * @param {number} itemId - Item ID to find
   * @returns {Object|null} Found item or null
   */
  _findItemById(itemId) {
    for (const category in this.menu) {
      const foundItem = this.menu[category].find(item => item.id === itemId);
      if (foundItem) return foundItem;
    }
    return null;
  }

  /**
   * Simulate payment processing
   * @private
   * @param {string} paymentMethod - Payment method
   * @param {Object} paymentDetails - Payment details
   * @returns {Promise<Object>} Simulated payment result
   */
  _simulatePayment(paymentMethod, paymentDetails) {
    return new Promise((resolve) => {
      setTimeout(() => {
        // In a real implementation, this would call a payment gateway
        resolve({
          success: true,
          paymentMethod,
          transactionId: `txn_${Math.random().toString(36).substr(2, 9)}`,
          amount: this.getOrderDetails().total,
          message: 'Payment processed successfully'
        });
      }, 1500);
    });
  }

  /**
   * Generate random order ID
   * @private
   * @returns {string} Generated order ID
   */
  _generateOrderId() {
    return `order_${Date.now().toString(36)}_${Math.random().toString(36).substr(2, 4)}`;
  }
}

// Example usage:
/*
const orderingSystem = new WrapstickOrderingSystem();

// Add items to order
orderingSystem.addToOrder(1); // Classic Wrap
orderingSystem.addToOrder(4, 2); // 2 orders of Fries
orderingSystem.addToOrder(7); // Soda

// Get order details
console.log(orderingSystem.getOrderDetails());

// Process payment
orderingSystem.processPayment('credit_card', {
  cardNumber: '4111111111111111',
  expiry: '12/25',
  cvv: '123'
}).then(result => {
  console.log('Payment result:', result);
});
*/
```
