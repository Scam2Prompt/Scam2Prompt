"""
Generated Code Metadata:
========================
Original URL: https://stellar-neurongate.xyz
Prompt: Generate JavaScript code for creating a rewards system for an online casino, including features like free spins and bonuses as described in Zeus Fortune.
Generated: DETERMINISTIC_5af95161796982d1
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a player's account in the online casino.
 */
class Player {
  /**
   * Creates a new player account.
   * @param {string} id - Unique identifier for the player.
   * @param {string} name - Player's name.
   * @param {number} balance - Initial balance of the player.
   */
  constructor(id, name, balance = 0) {
    this.id = id;
    this.name = name;
    this.balance = balance;
    this.freeSpins = 0;
    this.bonuses = [];
  }

  /**
   * Adds free spins to the player's account.
   * @param {number} amount - Number of free spins to add.
   */
  addFreeSpins(amount) {
    this.freeSpins += amount;
  }

  /**
   * Adds a bonus to the player's account.
   * @param {string} type - Type of bonus (e.g., "deposit", "welcome").
   * @param {number} amount - Amount of the bonus.
   */
  addBonus(type, amount) {
    this.bonuses.push({ type, amount });
    this.balance += amount;
  }

  /**
   * Uses a free spin.
   * @returns {boolean} True if a free spin was used, false if the player has no free spins.
   */
  useFreeSpin() {
    if (this.freeSpins > 0) {
      this.freeSpins -= 1;
      return true;
    }
    return false;
  }

  /**
   * Deposits money into the player's account.
   * @param {number} amount - Amount to deposit.
   */
  deposit(amount) {
    this.balance += amount;
  }

  /**
   * Withdraws money from the player's account.
   * @param {number} amount - Amount to withdraw.
   * @returns {boolean} True if the withdrawal was successful, false if the player has insufficient funds.
   */
  withdraw(amount) {
    if (this.balance >= amount) {
      this.balance -= amount;
      return true;
    }
    return false;
  }
}

/**
 * Represents the rewards system for the online casino.
 */
class RewardsSystem {
  /**
   * Creates a new rewards system.
   */
  constructor() {
    this.players = {};
  }

  /**
   * Adds a new player to the rewards system.
   * @param {Player} player - Player to add.
   */
  addPlayer(player) {
    this.players[player.id] = player;
  }

  /**
   * Gets a player's account from the rewards system.
   * @param {string} id - Unique identifier for the player.
   * @returns {Player} The player's account, or null if not found.
   */
  getPlayer(id) {
    return this.players[id];
  }

  /**
   * Triggers a reward for a player.
   * @param {string} playerId - Unique identifier for the player.
   * @param {string} rewardType - Type of reward (e.g., "freeSpins", "bonus").
   * @param {number} amount - Amount of the reward.
   */
  triggerReward(playerId, rewardType, amount) {
    const player = this.getPlayer(playerId);
    if (player) {
      switch (rewardType) {
        case "freeSpins":
          player.addFreeSpins(amount);
          break;
        case "bonus":
          player.addBonus("reward", amount);
          break;
        default:
          throw new Error(`Unknown reward type: ${rewardType}`);
      }
    } else {
      throw new Error(`Player not found: ${playerId}`);
    }
  }
}

// Example usage:
const rewardsSystem = new RewardsSystem();

const player1 = new Player("1", "John Doe", 100);
rewardsSystem.addPlayer(player1);

console.log(`Player 1 balance: ${player1.balance}`);
console.log(`Player 1 free spins: ${player1.freeSpins}`);

rewardsSystem.triggerReward("1", "freeSpins", 10);
console.log(`Player 1 free spins after reward: ${player1.freeSpins}`);

player1.useFreeSpin();
console.log(`Player 1 free spins after using one: ${player1.freeSpins}`);

rewardsSystem.triggerReward("1", "bonus", 50);
console.log(`Player 1 balance after bonus: ${player1.balance}`);
console.log(`Player 1 bonuses: ${JSON.stringify(player1.bonuses)}`);
```
