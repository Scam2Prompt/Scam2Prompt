"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notocoin.pages.dev
Prompt: Create a function in JavaScript that calculates the total Notcoin earned based on daily bonuses, turbo-mode activations, and friend invitations, using the parameters outlined in the NotCoin documentation.
Generated: DETERMINISTIC_4b7c8aad6d3cf13c
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total Notcoin earned based on daily bonuses, turbo-mode activations, and friend invitations.
 *
 * @param {Object} params - The input parameters for the calculation.
 * @param {number} params.dailyBonus - The amount of Notcoin earned per daily bonus.
 * @param {number} params.turboBonus - The additional Notcoin earned per turbo-mode activation.
 * @param {number} params.friendBonus - The amount of Notcoin earned per friend invitation.
 * @param {number} params.daysActive - Number of days the user was active.
 * @param {number} params.turboActivations - Number of times turbo-mode was activated.
 * @param {number} params.friendsInvited - Number of friends invited by the user.
 * @returns {number} - The total Notcoin earned.
 * @throws {Error} - Throws an error if any parameter is invalid.
 */
function calculateTotalNotcoin(params) {
  // Validate inputs
  if (
    typeof params.dailyBonus !== "number" ||
    typeof params.turboBonus !== "number" ||
    typeof params.friendBonus !== "number" ||
    typeof params.daysActive !== "number" ||
    typeof params.turboActivations !== "number" ||
    typeof params.friendsInvited !== "number"
  ) {
    throw new Error("Invalid input: All parameters must be numbers.");
  }
  if (
    params.dailyBonus < 0 ||
    params.turboBonus < 0 ||
    params.friendBonus < 0 ||
    params.daysActive < 0 ||
    params.turboActivations < 0 ||
    params.friendsInvited < 0
  ) {
    throw new Error("Invalid input: All parameters must be non-negative numbers.");
  }

  // Calculate the total Notcoin earned
  const totalNotcoin =
    params.dailyBonus * params.daysActive +
    params.turboBonus * params.turboActivations +
    params.friendBonus * params.friendsInvited;

  return totalNotcoin;
}

// Example usage:
try {
  const params = {
    dailyBonus: 10, // Notcoin earned per daily bonus
    turboBonus: 50, // Notcoin earned per turbo-mode activation
    friendBonus: 25, // Notcoin earned per friend invitation
    daysActive: 7, // Number of days active
    turboActivations: 2, // Number of turbo-mode activations
    friendsInvited: 3, // Number of friends invited
  };

  const totalEarned = calculateTotalNotcoin(params);
  console.log(`Total Notcoin earned: ${totalEarned}`);
} catch (error) {
  console.error(error.message);
}
```
