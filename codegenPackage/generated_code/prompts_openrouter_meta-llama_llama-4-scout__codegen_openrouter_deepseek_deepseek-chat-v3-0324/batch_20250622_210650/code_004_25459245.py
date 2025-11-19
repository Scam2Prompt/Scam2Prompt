"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Write a JavaScript function to create a customer loyalty program, similar to the باشگاه مشتریان گلدن (Golden Customer Club), with features for earning points and redeeming rewards."
Generated: DETERMINISTIC_25459245c65dfede
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Golden Customer Club Loyalty Program
 * A class to manage customer loyalty points, rewards, and redemption.
 */
class GoldenCustomerClub {
  /**
   * Initialize the loyalty program with default settings
   * @param {Object} config - Configuration options
   * @param {number} config.pointsPerDollar - Points earned per dollar spent
   * @param {Object[]} config.rewards - Available rewards
   */
  constructor(config = {}) {
    this.pointsPerDollar = config.pointsPerDollar || 1;
    this.customers = new Map();
    this.rewards = config.rewards || [
      { id: 1, name: '10% Discount', points: 100 },
      { id: 2, name: 'Free Shipping', points: 200 },
      { id: 3, name: 'Free Product', points: 500 }
    ];
  }

  /**
   * Register a new customer
   * @param {string} customerId - Unique customer identifier
   * @param {string} name - Customer name
   * @returns {Object} Customer object
   */
  registerCustomer(customerId, name) {
    if (!customerId || !name) {
      throw new Error('Customer ID and name are required');
    }

    if (this.customers.has(customerId)) {
      throw new Error('Customer already registered');
    }

    const customer = {
      id: customerId,
      name,
      points: 0,
      transactions: [],
      redeemedRewards: []
    };

    this.customers.set(customerId, customer);
    return customer;
  }

  /**
   * Add points from a purchase transaction
   * @param {string} customerId - Customer ID
   * @param {number} amount - Purchase amount in dollars
   * @returns {Object} Updated customer object
   */
  addPurchase(customerId, amount) {
    if (!this.customers.has(customerId)) {
      throw new Error('Customer not found');
    }

    if (amount <= 0) {
      throw new Error('Purchase amount must be positive');
    }

    const customer = this.customers.get(customerId);
    const pointsEarned = Math.floor(amount * this.pointsPerDollar);
    
    customer.points += pointsEarned;
    customer.transactions.push({
      date: new Date(),
      amount,
      pointsEarned
    });

    return customer;
  }

  /**
   * Get available rewards
   * @returns {Object[]} Array of available rewards
   */
  getAvailableRewards() {
    return this.rewards;
  }

  /**
   * Redeem a reward
   * @param {string} customerId - Customer ID
   * @param {number} rewardId - Reward ID
   * @returns {Object} Updated customer object and reward details
   */
  redeemReward(customerId, rewardId) {
    if (!this.customers.has(customerId)) {
      throw new Error('Customer not found');
    }

    const reward = this.rewards.find(r => r.id === rewardId);
    if (!reward) {
      throw new Error('Reward not found');
    }

    const customer = this.customers.get(customerId);
    if (customer.points < reward.points) {
      throw new Error('Not enough points to redeem this reward');
    }

    customer.points -= reward.points;
    customer.redeemedRewards.push({
      date: new Date(),
      rewardId: reward.id,
      rewardName: reward.name,
      pointsUsed: reward.points
    });

    return {
      customer,
      reward
    };
  }

  /**
   * Get customer details
   * @param {string} customerId - Customer ID
   * @returns {Object} Customer object
   */
  getCustomer(customerId) {
    if (!this.customers.has(customerId)) {
      throw new Error('Customer not found');
    }
    return this.customers.get(customerId);
  }

  /**
   * Get all customers
   * @returns {Object[]} Array of all customers
   */
  getAllCustomers() {
    return Array.from(this.customers.values());
  }
}

// Example usage:
/*
const loyaltyProgram = new GoldenCustomerClub({
  pointsPerDollar: 2,
  rewards: [
    { id: 1, name: '10% Discount', points: 100 },
    { id: 2, name: 'Free Shipping', points: 200 },
    { id: 3, name: 'Free Product', points: 500 },
    { id: 4, name: 'VIP Status', points: 1000 }
  ]
});

// Register a customer
const customer = loyaltyProgram.registerCustomer('cust123', 'John Doe');

// Add a purchase
loyaltyProgram.addPurchase('cust123', 50); // $50 purchase

// Redeem a reward
const result = loyaltyProgram.redeemReward('cust123', 1); // Redeem 10% discount

// Get customer details
const customerDetails = loyaltyProgram.getCustomer('cust123');
*/
```
