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
 * PricingLockIn class to manage subscription plans with pricing lock-in feature.
 */
class PricingLockIn {
    constructor() {
        // Initialize subscription plans with their respective prices
        this.plans = {
            basic: { price: 10, locked: false },
            premium: { price: 20, locked: false }
        };
        this.currentPlan = null;
    }

    /**
     * Subscribe to a plan and lock in the price if not already locked.
     * @param {string} planName - The name of the plan to subscribe to (basic or premium).
     * @throws Will throw an error if the plan is invalid or already locked.
     */
    subscribe(planName) {
        if (!this.plans[planName]) {
            throw new Error(`Invalid plan: ${planName}. Available plans are: ${Object.keys(this.plans).join(', ')}`);
        }

        const plan = this.plans[planName];

        if (plan.locked) {
            throw new Error(`Cannot subscribe to ${planName} plan. The price is already locked.`);
        }

        this.currentPlan = planName;
        plan.locked = true; // Lock the price for the current plan
        console.log(`Subscribed to ${planName} plan at $${plan.price}/month.`);
    }

    /**
     * Get the current subscription plan details.
     * @returns {Object|null} - The current plan details or null if no plan is subscribed.
     */
    getCurrentPlan() {
        if (!this.currentPlan) {
            return null;
        }
        return {
            plan: this.currentPlan,
            price: this.plans[this.currentPlan].price,
            locked: this.plans[this.currentPlan].locked
        };
    }

    /**
     * Cancel the current subscription plan.
     * @throws Will throw an error if no plan is currently subscribed.
     */
    cancelSubscription() {
        if (!this.currentPlan) {
            throw new Error('No active subscription to cancel.');
        }

        const plan = this.plans[this.currentPlan];
        plan.locked = false; // Unlock the price for the current plan
        console.log(`Cancelled subscription to ${this.currentPlan} plan.`);
        this.currentPlan = null; // Reset current plan
    }
}

// Example usage:
try {
    const pricingLockIn = new PricingLockIn();
    pricingLockIn.subscribe('basic'); // Subscribe to basic plan
    console.log(pricingLockIn.getCurrentPlan()); // Get current plan details
    pricingLockIn.cancelSubscription(); // Cancel subscription
} catch (error) {
    console.error(error.message); // Handle errors gracefully
}
```
