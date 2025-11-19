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
 * Represents a subscription plan with pricing details.
 */
class SubscriptionPlan {
  /**
   * @param {string} name - The name of the plan (e.g., Basic, Premium).
   * @param {number} price - The monthly price of the plan.
   * @param {number} lockedInPrice - The locked-in price for the plan, if any.
   */
  constructor(name, price, lockedInPrice = null) {
    this.name = name;
    this.price = price;
    this.lockedInPrice = lockedInPrice;
  }

  /**
   * Locks in the current price for the plan.
   * @returns {SubscriptionPlan} The updated plan with the locked-in price.
   */
  lockInPrice() {
    this.lockedInPrice = this.price;
    return this;
  }

  /**
   * Updates the price of the plan while keeping the locked-in price.
   * @param {number} newPrice - The new monthly price of the plan.
   * @returns {SubscriptionPlan} The updated plan.
   */
  updatePrice(newPrice) {
    this.price = newPrice;
    return this;
  }

  /**
   * Gets the current price to be charged, considering the locked-in price.
   * @returns {number} The current price to be charged.
   */
  getCurrentPrice() {
    return this.lockedInPrice !== null ? this.lockedInPrice : this.price;
  }
}

/**
 * Manages subscription plans and their pricing.
 */
class PricingLockInSystem {
  /**
   * @param {Object} plans - An object containing subscription plans.
   */
  constructor(plans = {}) {
    this.plans = plans;
  }

  /**
   * Adds a new subscription plan to the system.
   * @param {SubscriptionPlan} plan - The plan to add.
   * @returns {PricingLockInSystem} The updated system.
   */
  addPlan(plan) {
    if (!(plan instanceof SubscriptionPlan)) {
      throw new Error('Invalid plan provided');
    }
    this.plans[plan.name] = plan;
    return this;
  }

  /**
   * Locks in the price for a specific plan.
   * @param {string} planName - The name of the plan to lock in.
   * @returns {PricingLockInSystem} The updated system.
   */
  lockInPrice(planName) {
    if (!this.plans[planName]) {
      throw new Error(`Plan '${planName}' not found`);
    }
    this.plans[planName].lockInPrice();
    return this;
  }

  /**
   * Updates the price of a specific plan.
   * @param {string} planName - The name of the plan to update.
   * @param {number} newPrice - The new price for the plan.
   * @returns {PricingLockInSystem} The updated system.
   */
  updatePlanPrice(planName, newPrice) {
    if (!this.plans[planName]) {
      throw new Error(`Plan '${planName}' not found`);
    }
    this.plans[planName].updatePrice(newPrice);
    return this;
  }

  /**
   * Gets the current price for a specific plan, considering the locked-in price.
   * @param {string} planName - The name of the plan.
   * @returns {number} The current price for the plan.
   */
  getCurrentPrice(planName) {
    if (!this.plans[planName]) {
      throw new Error(`Plan '${planName}' not found`);
    }
    return this.plans[planName].getCurrentPrice();
  }
}

// Example usage
function main() {
  try {
    const system = new PricingLockInSystem();

    const basicPlan = new SubscriptionPlan('Basic', 9.99);
    const premiumPlan = new SubscriptionPlan('Premium', 19.99);

    system.addPlan(basicPlan).addPlan(premiumPlan);

    console.log(`Basic plan initial price: $${basicPlan.getCurrentPrice()}`);
    console.log(`Premium plan initial price: $${premiumPlan.getCurrentPrice()}`);

    system.lockInPrice('Basic');
    basicPlan.updatePrice(12.99); // This won't affect the locked-in price

    console.log(`Basic plan price after lock-in and update: $${system.getCurrentPrice('Basic')}`);
    console.log(`Premium plan price after basic plan operations: $${system.getCurrentPrice('Premium')}`);

    system.updatePlanPrice('Premium', 24.99);

    console.log(`Premium plan price after update: $${system.getCurrentPrice('Premium')}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
