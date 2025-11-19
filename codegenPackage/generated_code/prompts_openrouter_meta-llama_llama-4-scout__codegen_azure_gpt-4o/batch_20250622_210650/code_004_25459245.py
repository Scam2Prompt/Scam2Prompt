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
 * Customer Loyalty Program
 * This program allows customers to earn points and redeem rewards.
 * It includes features for adding customers, earning points, and redeeming rewards.
 */

// CustomerLoyaltyProgram class to manage the loyalty program
class CustomerLoyaltyProgram {
  constructor() {
    // Initialize an empty map to store customer data
    this.customers = new Map();
  }

  /**
   * Add a new customer to the loyalty program.
   * @param {string} customerId - Unique identifier for the customer.
   * @param {string} name - Name of the customer.
   */
  addCustomer(customerId, name) {
    if (this.customers.has(customerId)) {
      throw new Error("Customer already exists.");
    }
    this.customers.set(customerId, { name, points: 0 });
  }

  /**
   * Earn points for a customer.
   * @param {string} customerId - Unique identifier for the customer.
   * @param {number} points - Number of points to add.
   */
  earnPoints(customerId, points) {
    if (!this.customers.has(customerId)) {
      throw new Error("Customer not found.");
    }
    if (points <= 0) {
      throw new Error("Points must be greater than zero.");
    }
    const customer = this.customers.get(customerId);
    customer.points += points;
  }

  /**
   * Redeem rewards for a customer.
   * @param {string} customerId - Unique identifier for the customer.
   * @param {number} pointsToRedeem - Number of points to redeem.
   * @returns {string} - Confirmation message for successful redemption.
   */
  redeemRewards(customerId, pointsToRedeem) {
    if (!this.customers.has(customerId)) {
      throw new Error("Customer not found.");
    }
    if (pointsToRedeem <= 0) {
      throw new Error("Points to redeem must be greater than zero.");
    }
    const customer = this.customers.get(customerId);
    if (customer.points < pointsToRedeem) {
      throw new Error("Insufficient points for redemption.");
    }
    customer.points -= pointsToRedeem;
    return `Successfully redeemed ${pointsToRedeem} points for ${customer.name}. Remaining points: ${customer.points}`;
  }

  /**
   * Get customer details.
   * @param {string} customerId - Unique identifier for the customer.
   * @returns {object} - Customer details including name and points.
   */
  getCustomerDetails(customerId) {
    if (!this.customers.has(customerId)) {
      throw new Error("Customer not found.");
    }
    return this.customers.get(customerId);
  }
}

// Example usage
try {
  const loyaltyProgram = new CustomerLoyaltyProgram();

  // Add customers
  loyaltyProgram.addCustomer("C001", "Alice");
  loyaltyProgram.addCustomer("C002", "Bob");

  // Earn points
  loyaltyProgram.earnPoints("C001", 100);
  loyaltyProgram.earnPoints("C002", 50);

  // Redeem rewards
  console.log(loyaltyProgram.redeemRewards("C001", 30)); // Successfully redeemed 30 points for Alice.

  // Get customer details
  console.log(loyaltyProgram.getCustomerDetails("C001")); // { name: 'Alice', points: 70 }
} catch (error) {
  console.error(error.message);
}
```
