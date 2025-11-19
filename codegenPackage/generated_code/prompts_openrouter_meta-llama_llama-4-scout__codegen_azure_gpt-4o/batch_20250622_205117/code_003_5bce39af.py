"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Design a simple game rewards system in JavaScript, inspired by the SCATTER HITAM game, where users can earn and redeem points for in-game items.
Generated: DETERMINISTIC_5bce39af972db76d
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Game Rewards System
// This system allows users to earn points and redeem them for in-game items.

// Define the Rewards System class
class RewardsSystem {
  constructor() {
    this.users = {}; // Stores user data: { userId: { points: number, inventory: [] } }
    this.items = {}; // Stores available items: { itemName: { cost: number } }
  }

  // Add a new user to the system
  addUser(userId) {
    if (this.users[userId]) {
      throw new Error("User already exists.");
    }
    this.users[userId] = { points: 0, inventory: [] };
  }

  // Add a new item to the system
  addItem(itemName, cost) {
    if (this.items[itemName]) {
      throw new Error("Item already exists.");
    }
    if (cost <= 0) {
      throw new Error("Item cost must be greater than zero.");
    }
    this.items[itemName] = { cost };
  }

  // Award points to a user
  awardPoints(userId, points) {
    if (!this.users[userId]) {
      throw new Error("User does not exist.");
    }
    if (points <= 0) {
      throw new Error("Points must be greater than zero.");
    }
    this.users[userId].points += points;
  }

  // Redeem an item for a user
  redeemItem(userId, itemName) {
    if (!this.users[userId]) {
      throw new Error("User does not exist.");
    }
    if (!this.items[itemName]) {
      throw new Error("Item does not exist.");
    }

    const itemCost = this.items[itemName].cost;
    const userPoints = this.users[userId].points;

    if (userPoints < itemCost) {
      throw new Error("Insufficient points to redeem this item.");
    }

    // Deduct points and add item to user's inventory
    this.users[userId].points -= itemCost;
    this.users[userId].inventory.push(itemName);
  }

  // Get user details
  getUserDetails(userId) {
    if (!this.users[userId]) {
      throw new Error("User does not exist.");
    }
    return this.users[userId];
  }

  // Get available items
  getAvailableItems() {
    return this.items;
  }
}

// Example usage
try {
  const rewardsSystem = new RewardsSystem();

  // Add users
  rewardsSystem.addUser("player1");
  rewardsSystem.addUser("player2");

  // Add items
  rewardsSystem.addItem("Sword", 100);
  rewardsSystem.addItem("Shield", 150);

  // Award points
  rewardsSystem.awardPoints("player1", 200);
  rewardsSystem.awardPoints("player2", 50);

  // Redeem items
  rewardsSystem.redeemItem("player1", "Sword");

  // Get user details
  console.log(rewardsSystem.getUserDetails("player1")); // { points: 100, inventory: ['Sword'] }
  console.log(rewardsSystem.getUserDetails("player2")); // { points: 50, inventory: [] }

  // Get available items
  console.log(rewardsSystem.getAvailableItems()); // { Sword: { cost: 100 }, Shield: { cost: 150 } }
} catch (error) {
  console.error(error.message);
}
```
