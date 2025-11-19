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
 * Pricing Lock-In System for Subscription Plans
 * This code implements a pricing lock-in system for Basic and Premium subscription plans.
 * Users are locked into the price they signed up for, even if prices change later.
 */

// Subscription plans with initial prices
const subscriptionPlans = {
  Basic: 10, // Price in USD
  Premium: 20 // Price in USD
};

// Database simulation to store user subscriptions
const userSubscriptions = new Map();

/**
 * Function to sign up a user for a subscription plan
 * @param {string} userId - Unique identifier for the user
 * @param {string} plan - Subscription plan name ('Basic' or 'Premium')
 * @returns {string} - Confirmation message
 */
function signUpUser(userId, plan) {
  if (!subscriptionPlans[plan]) {
    throw new Error(`Invalid subscription plan: ${plan}`);
  }

  if (userSubscriptions.has(userId)) {
    throw new Error(`User ${userId} is already subscribed.`);
  }

  // Lock in the price at the time of signup
  const lockedPrice = subscriptionPlans[plan];
  userSubscriptions.set(userId, { plan, lockedPrice });

  return `User ${userId} successfully subscribed to ${plan} plan at $${lockedPrice}/month.`;
}

/**
 * Function to update subscription plan prices
 * @param {string} plan - Subscription plan name ('Basic' or 'Premium')
 * @param {number} newPrice - New price for the subscription plan
 */
function updatePlanPrice(plan, newPrice) {
  if (!subscriptionPlans[plan]) {
    throw new Error(`Invalid subscription plan: ${plan}`);
  }

  if (newPrice <= 0) {
    throw new Error(`Price must be greater than zero.`);
  }

  subscriptionPlans[plan] = newPrice;
  console.log(`Price for ${plan} plan updated to $${newPrice}/month.`);
}

/**
 * Function to get the subscription details for a user
 * @param {string} userId - Unique identifier for the user
 * @returns {object} - Subscription details (plan and locked price)
 */
function getUserSubscription(userId) {
  if (!userSubscriptions.has(userId)) {
    throw new Error(`User ${userId} is not subscribed.`);
  }

  return userSubscriptions.get(userId);
}

// Example usage
try {
  console.log(signUpUser('user123', 'Basic')); // User subscribes to Basic plan
  console.log(signUpUser('user456', 'Premium')); // User subscribes to Premium plan

  updatePlanPrice('Basic', 12); // Update Basic plan price
  updatePlanPrice('Premium', 25); // Update Premium plan price

  console.log(getUserSubscription('user123')); // Get subscription details for user123
  console.log(getUserSubscription('user456')); // Get subscription details for user456
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
