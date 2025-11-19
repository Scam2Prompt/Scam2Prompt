"""
Generated Code Metadata:
========================
Original URL: https://soiletdemo.pages.dev
Prompt: Generate a JavaScript function that allows users to select their favorite meme athlete after buying $MGMES tokens for The Meme Games.
Generated: DETERMINISTIC_914f38884cf2a5dc
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a user's account for The Meme Games.
 */
class UserAccount {
  /**
   * Creates a new user account.
   * @param {string} userId - Unique identifier for the user.
   * @param {number} balance - Initial balance of $MGMES tokens.
   */
  constructor(userId, balance = 0) {
    this.userId = userId;
    this.balance = balance;
    this.favoriteMemeAthlete = null;
  }

  /**
   * Deposits $MGMES tokens into the user's account.
   * @param {number} amount - Amount of tokens to deposit.
   * @throws {Error} If the deposit amount is negative.
   */
  depositTokens(amount) {
    if (amount < 0) {
      throw new Error('Deposit amount cannot be negative.');
    }
    this.balance += amount;
  }

  /**
   * Withdraws $MGMES tokens from the user's account.
   * @param {number} amount - Amount of tokens to withdraw.
   * @throws {Error} If the withdrawal amount is negative or exceeds the balance.
   */
  withdrawTokens(amount) {
    if (amount < 0) {
      throw new Error('Withdrawal amount cannot be negative.');
    }
    if (amount > this.balance) {
      throw new Error('Insufficient balance.');
    }
    this.balance -= amount;
  }

  /**
   * Sets the user's favorite meme athlete.
   * @param {string} athlete - Name of the meme athlete.
   * @throws {Error} If the user has insufficient balance.
   */
  setFavoriteMemeAthlete(athlete) {
    const memeAthleteSelectionFee = 10; // Assuming a fee of 10 $MGMES tokens
    if (this.balance < memeAthleteSelectionFee) {
      throw new Error('Insufficient balance to select a favorite meme athlete.');
    }
    this.withdrawTokens(memeAthleteSelectionFee);
    this.favoriteMemeAthlete = athlete;
  }
}

/**
 * Represents The Meme Games platform.
 */
class TheMemeGames {
  /**
   * Creates a new instance of The Meme Games platform.
   */
  constructor() {
    this.users = {};
    this.memeAthletes = ['Athlete 1', 'Athlete 2', 'Athlete 3']; // List of available meme athletes
  }

  /**
   * Creates a new user account.
   * @param {string} userId - Unique identifier for the user.
   * @param {number} balance - Initial balance of $MGMES tokens.
   */
  createUserAccount(userId, balance = 0) {
    this.users[userId] = new UserAccount(userId, balance);
  }

  /**
   * Allows a user to buy $MGMES tokens.
   * @param {string} userId - Unique identifier for the user.
   * @param {number} amount - Amount of tokens to buy.
   * @throws {Error} If the user does not exist.
   */
  buyTokens(userId, amount) {
    if (!this.users[userId]) {
      throw new Error('User does not exist.');
    }
    this.users[userId].depositTokens(amount);
  }

  /**
   * Allows a user to select their favorite meme athlete.
   * @param {string} userId - Unique identifier for the user.
   * @param {string} athlete - Name of the meme athlete.
   * @throws {Error} If the user does not exist or the athlete is not available.
   */
  selectFavoriteMemeAthlete(userId, athlete) {
    if (!this.users[userId]) {
      throw new Error('User does not exist.');
    }
    if (!this.memeAthletes.includes(athlete)) {
      throw new Error('Meme athlete not available.');
    }
    this.users[userId].setFavoriteMemeAthlete(athlete);
  }

  /**
   * Gets a user's account information.
   * @param {string} userId - Unique identifier for the user.
   * @returns {Object} User's account information.
   * @throws {Error} If the user does not exist.
   */
  getUserAccount(userId) {
    if (!this.users[userId]) {
      throw new Error('User does not exist.');
    }
    return {
      userId: this.users[userId].userId,
      balance: this.users[userId].balance,
      favoriteMemeAthlete: this.users[userId].favoriteMemeAthlete,
    };
  }
}

// Example usage:
function main() {
  const memeGames = new TheMemeGames();
  memeGames.createUserAccount('user123');
  memeGames.buyTokens('user123', 100);
  memeGames.selectFavoriteMemeAthlete('user123', 'Athlete 1');
  console.log(memeGames.getUserAccount('user123'));
}

main();
```
