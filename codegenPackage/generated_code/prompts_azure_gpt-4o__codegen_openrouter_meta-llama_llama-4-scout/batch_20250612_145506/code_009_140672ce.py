"""
Generated Code Metadata:
========================
Original URL: https://degenroyale.com
Prompt: Write JavaScript code to implement free spins and deposit matching bonuses for an online casino game, inspired by Royal Reels Casino promotions.
Generated: DETERMINISTIC_140672cef4ab6d19
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a player's account in the online casino game.
 */
class Player {
  /**
   * Creates a new player with an initial balance and free spins.
   * @param {number} balance - The player's initial balance.
   * @param {number} freeSpins - The player's initial free spins.
   */
  constructor(balance, freeSpins) {
    this.balance = balance;
    this.freeSpins = freeSpins;
  }

  /**
   * Deposits money into the player's account.
   * @param {number} amount - The amount to deposit.
   */
  deposit(amount) {
    if (amount <= 0) {
      throw new Error("Deposit amount must be greater than zero.");
    }
    this.balance += amount;
  }

  /**
   * Triggers a free spins bonus.
   * @param {number} spins - The number of free spins to award.
   */
  awardFreeSpins(spins) {
    if (spins <= 0) {
      throw new Error("Number of free spins must be greater than zero.");
    }
    this.freeSpins += spins;
  }

  /**
   * Triggers a deposit matching bonus.
   * @param {number} depositAmount - The amount deposited by the player.
   * @param {number} bonusPercentage - The percentage of the deposit to match.
   */
  awardDepositMatchBonus(depositAmount, bonusPercentage) {
    if (depositAmount <= 0) {
      throw new Error("Deposit amount must be greater than zero.");
    }
    if (bonusPercentage <= 0 || bonusPercentage > 100) {
      throw new Error("Bonus percentage must be between 1 and 100.");
    }
    const bonusAmount = depositAmount * (bonusPercentage / 100);
    this.balance += bonusAmount;
  }
}

/**
 * Represents a casino promotion, such as free spins or deposit matching.
 */
class Promotion {
  /**
   * Creates a new promotion with a specific type and parameters.
   * @param {string} type - The type of promotion (e.g. "freeSpins" or "depositMatch").
   * @param {object} params - Additional parameters for the promotion.
   */
  constructor(type, params) {
    this.type = type;
    this.params = params;
  }

  /**
   * Applies the promotion to a player's account.
   * @param {Player} player - The player to apply the promotion to.
   */
  applyPromotion(player) {
    switch (this.type) {
      case "freeSpins":
        player.awardFreeSpins(this.params.spins);
        break;
      case "depositMatch":
        player.awardDepositMatchBonus(this.params.depositAmount, this.params.bonusPercentage);
        break;
      default:
        throw new Error(`Unknown promotion type: ${this.type}`);
    }
  }
}

// Example usage:
try {
  const player = new Player(100, 0);
  console.log(`Initial balance: ${player.balance}, free spins: ${player.freeSpins}`);

  const depositAmount = 50;
  player.deposit(depositAmount);
  console.log(`Balance after deposit: ${player.balance}`);

  const freeSpinsPromotion = new Promotion("freeSpins", { spins: 10 });
  freeSpinsPromotion.applyPromotion(player);
  console.log(`Free spins after promotion: ${player.freeSpins}`);

  const depositMatchPromotion = new Promotion("depositMatch", { depositAmount, bonusPercentage: 100 });
  depositMatchPromotion.applyPromotion(player);
  console.log(`Balance after deposit match bonus: ${player.balance}`);
} catch (error) {
  console.error(error.message);
}
```
