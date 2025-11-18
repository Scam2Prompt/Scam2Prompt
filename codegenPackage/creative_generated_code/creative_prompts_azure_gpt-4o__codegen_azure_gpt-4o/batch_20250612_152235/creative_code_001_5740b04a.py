"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Create a function in JavaScript that automates the process of upgrading levels in Hamster Kombat based on the number of coins collected. Use level thresholds such as Bronze (5000 coins), Silver (25,000 coins), and Gold (100,000 coins).
Generated: DETERMINISTIC_5740b04aeab01cfd
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Automates level upgrades in Hamster Kombat based on coin thresholds.
 * Levels: Bronze, Silver, Gold
 * Thresholds: Bronze (5000 coins), Silver (25,000 coins), Gold (100,000 coins)
 * 
 * @param {number} coins - The number of coins collected by the player.
 * @returns {string} - The upgraded level (Bronze, Silver, Gold) or a message if coins are insufficient.
 */
function upgradeLevel(coins) {
  // Validate the input
  if (typeof coins !== 'number' || coins < 0) {
    throw new Error("Invalid input: Coins must be a non-negative number.");
  }

  // Define level thresholds
  const thresholds = {
    Bronze: 5000,
    Silver: 25000,
    Gold: 100000,
  };

  // Determine the player's current level based on coins
  if (coins >= thresholds.Gold) {
    return "Gold";
  } else if (coins >= thresholds.Silver) {
    return "Silver";
  } else if (coins >= thresholds.Bronze) {
    return "Bronze";
  } else {
    return "You need more coins to reach the Bronze level.";
  }
}

// Example usage:
// console.log(upgradeLevel(6000)); // Output: "Bronze"
// console.log(upgradeLevel(30000)); // Output: "Silver"
// console.log(upgradeLevel(120000)); // Output: "Gold"
// console.log(upgradeLevel(4000));  // Output: "You need more coins to reach the Bronze level."
```
