"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degenroyale.com
Prompt: Write JavaScript code to implement free spins and deposit matching bonuses for an online casino game, inspired by Royal Reels Casino promotions.
Generated: DETERMINISTIC_140672cef4ab6d19
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Online Casino Bonus System
 * This script implements free spins and deposit matching bonuses for an online casino game.
 * Inspired by Royal Reels Casino promotions.
 */

// Constants for bonus configurations
const FREE_SPINS_BONUS = 20; // Number of free spins
const DEPOSIT_MATCH_PERCENTAGE = 100; // Deposit match percentage (e.g., 100% means 1:1 match)
const MAX_DEPOSIT_MATCH = 500; // Maximum deposit match cap in dollars

// User object to simulate player account data
const user = {
  id: 1,
  balance: 100, // Initial balance in dollars
  freeSpins: 0 // Initial free spins
};

/**
 * Grant free spins to a user.
 * @param {Object} user - The user object.
 * @param {number} spins - The number of free spins to grant.
 */
function grantFreeSpins(user, spins) {
  if (spins <= 0) {
    console.error("Invalid number of spins provided.");
    return;
  }

  user.freeSpins += spins;
  console.log(`Granted ${spins} free spins to user ID ${user.id}.`);
  console.log(`User now has ${user.freeSpins} free spins.`);
}

/**
 * Grant deposit matching bonus to a user.
 * @param {Object} user - The user object.
 * @param {number} depositAmount - The deposit amount in dollars.
 */
function grantDepositMatch(user, depositAmount) {
  if (depositAmount <= 0) {
    console.error("Deposit amount must be greater than zero.");
    return;
  }

  // Calculate the matching bonus
  let bonus = (depositAmount * DEPOSIT_MATCH_PERCENTAGE) / 100;

  // Cap the bonus if it exceeds the maximum allowed
  if (bonus > MAX_DEPOSIT_MATCH) {
    bonus = MAX_DEPOSIT_MATCH;
  }

  // Update user balance with the matching bonus
  user.balance += bonus;

  console.log(`User ID ${user.id} deposited $${depositAmount}.`);
  console.log(`A bonus of $${bonus} has been granted.`);
  console.log(`User's new balance is $${user.balance}.`);
}

/**
 * Main function to simulate the promotion.
 */
function main() {
  try {
    console.log("Starting casino promotion...");

    // Simulate granting free spins
    grantFreeSpins(user, FREE_SPINS_BONUS);

    // Simulate a deposit and grant deposit matching bonus
    const depositAmount = 200; // Example deposit amount
    grantDepositMatch(user, depositAmount);

    console.log("Promotion has concluded successfully.");
  } catch (error) {
    console.error("An error occurred during the promotion:", error.message);
  }
}

// Run the main function
main();
```
