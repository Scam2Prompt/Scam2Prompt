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
// game-rewards-system.js

/**
 * Represents a user's account in the game rewards system.
 */
class UserAccount {
  /**
   * Creates a new user account.
   * @param {string} id - Unique identifier for the user.
   * @param {string} name - Name of the user.
   */
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.points = 0;
    this.inventory = {};
  }

  /**
   * Adds points to the user's account.
   * @param {number} amount - Points to add.
   */
  addPoints(amount) {
    if (amount <= 0) {
      throw new Error('Invalid points amount');
    }
    this.points += amount;
  }

  /**
   * Removes points from the user's account.
   * @param {number} amount - Points to remove.
   * @throws {Error} If the user does not have enough points.
   */
  removePoints(amount) {
    if (amount <= 0) {
      throw new Error('Invalid points amount');
    }
    if (this.points < amount) {
      throw new Error('Insufficient points');
    }
    this.points -= amount;
  }

  /**
   * Adds an item to the user's inventory.
   * @param {string} itemId - Unique identifier for the item.
   * @param {number} quantity - Quantity of the item.
   */
  addItemToInventory(itemId, quantity) {
    if (quantity <= 0) {
      throw new Error('Invalid quantity');
    }
    if (this.inventory[itemId]) {
      this.inventory[itemId] += quantity;
    } else {
      this.inventory[itemId] = quantity;
    }
  }

  /**
   * Removes an item from the user's inventory.
   * @param {string} itemId - Unique identifier for the item.
   * @param {number} quantity - Quantity of the item.
   * @throws {Error} If the user does not have enough of the item.
   */
  removeItemFromInventory(itemId, quantity) {
    if (quantity <= 0) {
      throw new Error('Invalid quantity');
    }
    if (!this.inventory[itemId]) {
      throw new Error('Item not found in inventory');
    }
    if (this.inventory[itemId] < quantity) {
      throw new Error('Insufficient quantity');
    }
    this.inventory[itemId] -= quantity;
    if (this.inventory[itemId] === 0) {
      delete this.inventory[itemId];
    }
  }
}

/**
 * Represents an item in the game.
 */
class Item {
  /**
   * Creates a new item.
   * @param {string} id - Unique identifier for the item.
   * @param {string} name - Name of the item.
   * @param {number} pointsCost - Points required to redeem the item.
   */
  constructor(id, name, pointsCost) {
    this.id = id;
    this.name = name;
    this.pointsCost = pointsCost;
  }
}

/**
 * Manages the game rewards system.
 */
class RewardsSystem {
  /**
   * Creates a new rewards system.
   */
  constructor() {
    this.users = {};
    this.items = {};
  }

  /**
   * Creates a new user account.
   * @param {string} id - Unique identifier for the user.
   * @param {string} name - Name of the user.
   */
  createUserAccount(id, name) {
    this.users[id] = new UserAccount(id, name);
  }

  /**
   * Adds points to a user's account.
   * @param {string} userId - Unique identifier for the user.
   * @param {number} amount - Points to add.
   * @throws {Error} If the user does not exist.
   */
  addPointsToUser(userId, amount) {
    if (!this.users[userId]) {
      throw new Error('User not found');
    }
    this.users[userId].addPoints(amount);
  }

  /**
   * Removes points from a user's account.
   * @param {string} userId - Unique identifier for the user.
   * @param {number} amount - Points to remove.
   * @throws {Error} If the user does not exist.
   */
  removePointsFromUser(userId, amount) {
    if (!this.users[userId]) {
      throw new Error('User not found');
    }
    this.users[userId].removePoints(amount);
  }

  /**
   * Creates a new item.
   * @param {string} id - Unique identifier for the item.
   * @param {string} name - Name of the item.
   * @param {number} pointsCost - Points required to redeem the item.
   */
  createItem(id, name, pointsCost) {
    this.items[id] = new Item(id, name, pointsCost);
  }

  /**
   * Redeems an item for a user.
   * @param {string} userId - Unique identifier for the user.
   * @param {string} itemId - Unique identifier for the item.
   * @throws {Error} If the user or item does not exist.
   */
  redeemItem(userId, itemId) {
    if (!this.users[userId]) {
      throw new Error('User not found');
    }
    if (!this.items[itemId]) {
      throw new Error('Item not found');
    }
    const user = this.users[userId];
    const item = this.items[itemId];
    if (user.points < item.pointsCost) {
      throw new Error('Insufficient points');
    }
    user.removePoints(item.pointsCost);
    user.addItemToInventory(itemId, 1);
  }

  /**
   * Gets a user's account information.
   * @param {string} userId - Unique identifier for the user.
   * @returns {Object} User account information.
   * @throws {Error} If the user does not exist.
   */
  getUserAccount(userId) {
    if (!this.users[userId]) {
      throw new Error('User not found');
    }
    return {
      id: this.users[userId].id,
      name: this.users[userId].name,
      points: this.users[userId].points,
      inventory: this.users[userId].inventory,
    };
  }
}

// Example usage:
const rewardsSystem = new RewardsSystem();

rewardsSystem.createUserAccount('user1', 'John Doe');
rewardsSystem.addPointsToUser('user1', 1000);

rewardsSystem.createItem('item1', 'Sword', 500);
rewardsSystem.redeemItem('user1', 'item1');

console.log(rewardsSystem.getUserAccount('user1'));
```
