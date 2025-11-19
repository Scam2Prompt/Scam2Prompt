"""
Generated Code Metadata:
========================
Original URL: https://gudrus.com
Prompt: Write a code snippet in JavaScript to implement a pricing lock-in system for subscription plans, similar to what is described for DeepMarket's Basic and Premium plans.
Generated: DETERMINISTIC_6953a8658e88288c
Batch ID: 20250622_212625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * PricingLockInSystem - Implements a subscription pricing lock-in mechanism
 * to maintain original pricing for existing customers when prices change.
 */
class PricingLockInSystem {
  /**
   * @constructor
   * @param {Object} plans - Initial subscription plans with pricing
   */
  constructor(plans) {
    this.plans = plans;
    this.subscriptions = new Map(); // Stores user subscriptions
  }

  /**
   * Subscribe a user to a plan with lock-in pricing
   * @param {string} userId - Unique user identifier
   * @param {string} planId - Plan identifier (e.g., 'basic', 'premium')
   * @param {Date} startDate - Subscription start date
   * @returns {Object} Subscription details
   * @throws {Error} If plan doesn't exist
   */
  subscribe(userId, planId, startDate = new Date()) {
    if (!this.plans[planId]) {
      throw new Error(`Plan ${planId} does not exist`);
    }

    const subscription = {
      planId,
      originalPrice: this.plans[planId].price,
      startDate,
      isActive: true
    };

    this.subscriptions.set(userId, subscription);
    return subscription;
  }

  /**
   * Update pricing for plans (does not affect existing subscriptions)
   * @param {Object} newPricing - New pricing structure {planId: newPrice}
   */
  updatePricing(newPricing) {
    for (const [planId, price] of Object.entries(newPricing)) {
      if (this.plans[planId]) {
        this.plans[planId].price = price;
      }
    }
  }

  /**
   * Get current price for a user's subscription
   * @param {string} userId - User identifier
   * @returns {number} Current price (locked-in if subscribed before price change)
   * @throws {Error} If user is not subscribed
   */
  getUserPrice(userId) {
    const subscription = this.subscriptions.get(userId);
    if (!subscription) {
      throw new Error(`User ${userId} is not subscribed`);
    }

    return subscription.originalPrice;
  }

  /**
   * Cancel a user's subscription
   * @param {string} userId - User identifier
   */
  cancelSubscription(userId) {
    const subscription = this.subscriptions.get(userId);
    if (subscription) {
      subscription.isActive = false;
    }
  }

  /**
   * Get current plan details (including current price)
   * @param {string} planId - Plan identifier
   * @returns {Object} Plan details
   * @throws {Error} If plan doesn't exist
   */
  getPlanDetails(planId) {
    if (!this.plans[planId]) {
      throw new Error(`Plan ${planId} does not exist`);
    }
    return {...this.plans[planId]};
  }
}

// Example usage:
/*
const plans = {
  basic: { name: 'Basic Plan', price: 9.99, features: ['feature1', 'feature2'] },
  premium: { name: 'Premium Plan', price: 19.99, features: ['feature1', 'feature2', 'feature3'] }
};

const pricingSystem = new PricingLockInSystem(plans);

// User subscribes to basic plan
pricingSystem.subscribe('user1', 'basic');

// Later, prices increase
pricingSystem.updatePricing({ basic: 14.99, premium: 24.99 });

// user1 still pays original price (9.99)
console.log(pricingSystem.getUserPrice('user1')); // 9.99

// New user gets new price
pricingSystem.subscribe('user2', 'basic');
console.log(pricingSystem.getUserPrice('user2')); // 14.99
*/
```
