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
 * 
 * This program simulates a customer loyalty program with features for earning points and redeeming rewards.
 */

// Define a class for the customer loyalty program
class LoyaltyProgram {
  /**
   * Constructor to initialize the loyalty program
   */
  constructor() {
    // Initialize an empty object to store customer data
    this.customers = {};
    // Initialize an empty object to store rewards data
    this.rewards = {};
  }

  /**
   * Add a new customer to the loyalty program
   * @param {string} customerId - Unique ID of the customer
   * @param {string} name - Name of the customer
   */
  addCustomer(customerId, name) {
    if (!this.customers[customerId]) {
      this.customers[customerId] = {
        name,
        points: 0,
      };
    } else {
      throw new Error(`Customer with ID ${customerId} already exists`);
    }
  }

  /**
   * Remove a customer from the loyalty program
   * @param {string} customerId - Unique ID of the customer
   */
  removeCustomer(customerId) {
    if (this.customers[customerId]) {
      delete this.customers[customerId];
    } else {
      throw new Error(`Customer with ID ${customerId} does not exist`);
    }
  }

  /**
   * Add a new reward to the loyalty program
   * @param {string} rewardId - Unique ID of the reward
   * @param {string} description - Description of the reward
   * @param {number} pointsRequired - Points required to redeem the reward
   */
  addReward(rewardId, description, pointsRequired) {
    if (!this.rewards[rewardId]) {
      this.rewards[rewardId] = {
        description,
        pointsRequired,
      };
    } else {
      throw new Error(`Reward with ID ${rewardId} already exists`);
    }
  }

  /**
   * Remove a reward from the loyalty program
   * @param {string} rewardId - Unique ID of the reward
   */
  removeReward(rewardId) {
    if (this.rewards[rewardId]) {
      delete this.rewards[rewardId];
    } else {
      throw new Error(`Reward with ID ${rewardId} does not exist`);
    }
  }

  /**
   * Earn points for a customer
   * @param {string} customerId - Unique ID of the customer
   * @param {number} points - Points to earn
   */
  earnPoints(customerId, points) {
    if (this.customers[customerId]) {
      this.customers[customerId].points += points;
    } else {
      throw new Error(`Customer with ID ${customerId} does not exist`);
    }
  }

  /**
   * Redeem a reward for a customer
   * @param {string} customerId - Unique ID of the customer
   * @param {string} rewardId - Unique ID of the reward
   */
  redeemReward(customerId, rewardId) {
    if (this.customers[customerId] && this.rewards[rewardId]) {
      const customerPoints = this.customers[customerId].points;
      const pointsRequired = this.rewards[rewardId].pointsRequired;
      if (customerPoints >= pointsRequired) {
        this.customers[customerId].points -= pointsRequired;
        return `Reward ${rewardId} redeemed successfully`;
      } else {
        throw new Error(`Insufficient points to redeem reward ${rewardId}`);
      }
    } else {
      throw new Error(`Customer or reward does not exist`);
    }
  }

  /**
   * Get customer data
   * @param {string} customerId - Unique ID of the customer
   * @returns {object} Customer data
   */
  getCustomerData(customerId) {
    if (this.customers[customerId]) {
      return this.customers[customerId];
    } else {
      throw new Error(`Customer with ID ${customerId} does not exist`);
    }
  }

  /**
   * Get reward data
   * @param {string} rewardId - Unique ID of the reward
   * @returns {object} Reward data
   */
  getRewardData(rewardId) {
    if (this.rewards[rewardId]) {
      return this.rewards[rewardId];
    } else {
      throw new Error(`Reward with ID ${rewardId} does not exist`);
    }
  }
}

// Example usage
function main() {
  const loyaltyProgram = new LoyaltyProgram();

  // Add customers
  loyaltyProgram.addCustomer('CUST1', 'John Doe');
  loyaltyProgram.addCustomer('CUST2', 'Jane Doe');

  // Add rewards
  loyaltyProgram.addReward('REWARD1', 'Discount on next purchase', 100);
  loyaltyProgram.addReward('REWARD2', 'Free gift', 500);

  // Earn points
  loyaltyProgram.earnPoints('CUST1', 150);
  loyaltyProgram.earnPoints('CUST2', 300);

  // Redeem rewards
  console.log(loyaltyProgram.redeemReward('CUST1', 'REWARD1')); // Reward REWARD1 redeemed successfully
  try {
    console.log(loyaltyProgram.redeemReward('CUST2', 'REWARD2')); // Insufficient points to redeem reward REWARD2
  } catch (error) {
    console.error(error.message);
  }

  // Get customer data
  console.log(loyaltyProgram.getCustomerData('CUST1')); // { name: 'John Doe', points: 50 }

  // Get reward data
  console.log(loyaltyProgram.getRewardData('REWARD1')); // { description: 'Discount on next purchase', pointsRequired: 100 }
}

main();
```
