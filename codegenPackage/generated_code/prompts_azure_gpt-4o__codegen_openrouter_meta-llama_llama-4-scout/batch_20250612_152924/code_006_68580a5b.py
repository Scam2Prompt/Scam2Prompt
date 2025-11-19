"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Create a simulation in JavaScript that mimics real-time meme market trading, allowing users to buy, sell, and trade meme assets based on the features of the Meme Moguls game.
Generated: DETERMINISTIC_68580a5b1f227fbb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// MemeMarket.js

class MemeAsset {
  /**
   * Represents a meme asset in the market.
   * @param {string} name - The name of the meme asset.
   * @param {number} price - The initial price of the meme asset.
   * @param {number} supply - The total supply of the meme asset.
   */
  constructor(name, price, supply) {
    this.name = name;
    this.price = price;
    this.supply = supply;
  }
}

class UserWallet {
  /**
   * Represents a user's wallet in the meme market.
   */
  constructor() {
    this.balance = 1000; // Initial balance
    this.assets = {}; // Map of meme assets to their quantities
  }

  /**
   * Deposits funds into the user's wallet.
   * @param {number} amount - The amount to deposit.
   */
  deposit(amount) {
    this.balance += amount;
  }

  /**
   * Withdraws funds from the user's wallet.
   * @param {number} amount - The amount to withdraw.
   * @throws {Error} If the withdrawal amount exceeds the balance.
   */
  withdraw(amount) {
    if (amount > this.balance) {
      throw new Error("Insufficient balance");
    }
    this.balance -= amount;
  }

  /**
   * Buys a meme asset.
   * @param {MemeAsset} asset - The meme asset to buy.
   * @param {number} quantity - The quantity to buy.
   * @throws {Error} If the user has insufficient balance.
   */
  buyAsset(asset, quantity) {
    const totalCost = asset.price * quantity;
    if (totalCost > this.balance) {
      throw new Error("Insufficient balance");
    }
    this.balance -= totalCost;
    if (this.assets[asset.name]) {
      this.assets[asset.name] += quantity;
    } else {
      this.assets[asset.name] = quantity;
    }
    asset.supply -= quantity;
  }

  /**
   * Sells a meme asset.
   * @param {MemeAsset} asset - The meme asset to sell.
   * @param {number} quantity - The quantity to sell.
   * @throws {Error} If the user has insufficient quantity.
   */
  sellAsset(asset, quantity) {
    if (!this.assets[asset.name] || this.assets[asset.name] < quantity) {
      throw new Error("Insufficient quantity");
    }
    this.assets[asset.name] -= quantity;
    asset.supply += quantity;
    this.balance += asset.price * quantity;
  }
}

class MemeMarket {
  /**
   * Represents the meme market simulator.
   */
  constructor() {
    this.assets = []; // List of meme assets
    this.users = {}; // Map of user IDs to their wallets
  }

  /**
   * Adds a meme asset to the market.
   * @param {MemeAsset} asset - The meme asset to add.
   */
  addAsset(asset) {
    this.assets.push(asset);
  }

  /**
   * Creates a new user in the market.
   * @param {string} userId - The ID of the user.
   */
  createUser(userId) {
    this.users[userId] = new UserWallet();
  }

  /**
   * Gets a user's wallet.
   * @param {string} userId - The ID of the user.
   * @returns {UserWallet} The user's wallet.
   */
  getUserWallet(userId) {
    return this.users[userId];
  }

  /**
   * Lists all meme assets in the market.
   * @returns {MemeAsset[]} The list of meme assets.
   */
  listAssets() {
    return this.assets;
  }
}

// Example usage:
const market = new MemeMarket();

// Create meme assets
const asset1 = new MemeAsset("Doge", 10, 1000);
const asset2 = new MemeAsset("Shiba", 5, 500);

// Add meme assets to the market
market.addAsset(asset1);
market.addAsset(asset2);

// Create users
market.createUser("user1");
market.createUser("user2");

// Get user wallets
const user1Wallet = market.getUserWallet("user1");
const user2Wallet = market.getUserWallet("user2");

// Deposit funds
user1Wallet.deposit(10000);
user2Wallet.deposit(5000);

// Buy and sell assets
try {
  user1Wallet.buyAsset(asset1, 10);
  user2Wallet.buyAsset(asset2, 20);
  user1Wallet.sellAsset(asset1, 5);
  user2Wallet.sellAsset(asset2, 10);
} catch (error) {
  console.error(error.message);
}

// List assets
console.log("Meme Assets:");
market.listAssets().forEach((asset) => {
  console.log(`${asset.name}: $${asset.price} (${asset.supply} in supply)`);
});

// Display user balances and assets
console.log("\nUser Balances and Assets:");
Object.keys(market.users).forEach((userId) => {
  const wallet = market.getUserWallet(userId);
  console.log(`User ${userId}: $${wallet.balance} balance`);
  console.log(`Assets: ${JSON.stringify(wallet.assets)}`);
});
```
