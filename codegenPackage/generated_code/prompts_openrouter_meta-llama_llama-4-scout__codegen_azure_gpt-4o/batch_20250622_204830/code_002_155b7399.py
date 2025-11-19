"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.web.app
Prompt: Develop a simple staking platform simulator in JavaScript for the War Chest, considering two pools with different return rates and locked schedules.
Generated: DETERMINISTIC_155b7399a1e9c43f
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Staking Platform Simulator for the War Chest
// This script simulates a staking platform with two pools having different return rates and lock schedules.

// Constants for the staking pools
const POOL_A = {
  name: "Pool A",
  returnRate: 0.05, // 5% return rate
  lockPeriodDays: 30 // Locked for 30 days
};

const POOL_B = {
  name: "Pool B",
  returnRate: 0.10, // 10% return rate
  lockPeriodDays: 90 // Locked for 90 days
};

// User's staking data
const userStakes = [];

/**
 * Stake funds into a pool.
 * @param {string} poolName - The name of the pool (e.g., "Pool A" or "Pool B").
 * @param {number} amount - The amount to stake.
 */
function stakeFunds(poolName, amount) {
  if (amount <= 0) {
    console.error("Stake amount must be greater than zero.");
    return;
  }

  const pool = poolName === POOL_A.name ? POOL_A : poolName === POOL_B.name ? POOL_B : null;

  if (!pool) {
    console.error("Invalid pool name. Please choose 'Pool A' or 'Pool B'.");
    return;
  }

  const stake = {
    poolName: pool.name,
    amount: amount,
    returnRate: pool.returnRate,
    lockPeriodDays: pool.lockPeriodDays,
    startDate: new Date(),
    endDate: new Date(Date.now() + pool.lockPeriodDays * 24 * 60 * 60 * 1000) // Calculate lock end date
  };

  userStakes.push(stake);
  console.log(`Successfully staked ${amount} in ${pool.name}.`);
}

/**
 * Calculate rewards for a specific stake.
 * @param {object} stake - The stake object.
 * @returns {number} - The calculated rewards.
 */
function calculateRewards(stake) {
  const daysStaked = Math.floor((new Date() - stake.startDate) / (1000 * 60 * 60 * 24));
  if (daysStaked < stake.lockPeriodDays) {
    console.warn(`Stake in ${stake.poolName} is still locked. No rewards available.`);
    return 0;
  }

  return stake.amount * stake.returnRate;
}

/**
 * Withdraw funds and rewards from a stake.
 * @param {number} stakeIndex - The index of the stake in the userStakes array.
 */
function withdrawFunds(stakeIndex) {
  if (stakeIndex < 0 || stakeIndex >= userStakes.length) {
    console.error("Invalid stake index.");
    return;
  }

  const stake = userStakes[stakeIndex];
  const rewards = calculateRewards(stake);

  if (rewards === 0) {
    console.warn(`Cannot withdraw from ${stake.poolName} yet. Funds are still locked.`);
    return;
  }

  console.log(`Withdrawing ${stake.amount} + ${rewards} rewards from ${stake.poolName}.`);
  userStakes.splice(stakeIndex, 1); // Remove the stake from the user's stakes
}

/**
 * Display all active stakes.
 */
function displayStakes() {
  if (userStakes.length === 0) {
    console.log("No active stakes.");
    return;
  }

  console.log("Active Stakes:");
  userStakes.forEach((stake, index) => {
    console.log(
      `Stake ${index + 1}: ${stake.poolName}, Amount: ${stake.amount}, Start Date: ${stake.startDate.toDateString()}, End Date: ${stake.endDate.toDateString()}`
    );
  });
}

// Example usage
stakeFunds("Pool A", 1000); // Stake 1000 in Pool A
stakeFunds("Pool B", 500);  // Stake 500 in Pool B
displayStakes();            // Display all active stakes

// Simulate waiting for lock period (for demonstration purposes, adjust dates manually in real scenarios)
// Withdraw funds after lock period
setTimeout(() => {
  withdrawFunds(0); // Attempt to withdraw from the first stake
  displayStakes();  // Display remaining stakes
}, 3000); // Simulate a delay (replace with actual date checks in production)
```
