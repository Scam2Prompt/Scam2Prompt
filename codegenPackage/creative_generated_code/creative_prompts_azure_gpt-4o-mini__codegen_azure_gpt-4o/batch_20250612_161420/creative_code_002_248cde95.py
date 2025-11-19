"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vlaunch-dapp.web.app
Prompt: Generate a JavaScript function that calculates the VPAD rewards based on different lockup durations mentioned on the VLaunch website.
Generated: DETERMINISTIC_248cde95290986f3
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate VPAD rewards based on lockup duration.
 * 
 * Lockup durations and their multipliers (example values):
 * - 1 month: 1x multiplier
 * - 3 months: 1.5x multiplier
 * - 6 months: 2x multiplier
 * - 12 months: 3x multiplier
 * 
 * @param {number} stakedAmount - The amount of VPAD staked.
 * @param {number} lockupDuration - The lockup duration in months.
 * @returns {number} - The calculated rewards based on lockup duration.
 * @throws {Error} - If inputs are invalid.
 */
function calculateVPADRewards(stakedAmount, lockupDuration) {
  // Validate inputs
  if (typeof stakedAmount !== 'number' || stakedAmount <= 0) {
    throw new Error('Invalid staked amount. It must be a positive number.');
  }

  if (typeof lockupDuration !== 'number' || lockupDuration <= 0) {
    throw new Error('Invalid lockup duration. It must be a positive number.');
  }

  // Define lockup duration multipliers
  const multipliers = {
    1: 1,   // 1 month lockup => 1x multiplier
    3: 1.5, // 3 months lockup => 1.5x multiplier
    6: 2,   // 6 months lockup => 2x multiplier
    12: 3   // 12 months lockup => 3x multiplier
  };

  // Get the multiplier for the specified lockup duration
  const multiplier = multipliers[lockupDuration];

  // If the lockup duration is not supported, throw an error
  if (!multiplier) {
    throw new Error('Unsupported lockup duration. Valid durations are: 1, 3, 6, 12 months.');
  }

  // Calculate the rewards
  const rewards = stakedAmount * multiplier;

  return rewards;
}

// Example usage:
try {
  const stakedAmount = 1000; // Example: 1000 VPAD staked
  const lockupDuration = 6;  // Example: Lockup duration of 6 months

  const rewards = calculateVPADRewards(stakedAmount, lockupDuration);
  console.log(`Calculated VPAD Rewards: ${rewards}`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
