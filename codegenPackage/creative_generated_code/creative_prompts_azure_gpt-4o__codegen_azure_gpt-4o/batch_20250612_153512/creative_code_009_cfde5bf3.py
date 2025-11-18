"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfinance.xyz
Prompt: Develop a tool in JavaScript to allow users to deposit and withdraw assets from Symbiotic Finance's yield pools, ensuring the correct calculation of earnings based on APY and deposit duration.
Generated: DETERMINISTIC_cfde5bf3e173f212
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Symbiotic Finance Yield Pool Tool
// This script allows users to deposit and withdraw assets from yield pools,
// calculates earnings based on APY and deposit duration, and ensures proper error handling.

// Mocked data for demonstration purposes.
const yieldPools = {
  pool1: {
    name: "USDT Yield Pool",
    apy: 12, // Annual Percentage Yield in percentage
  },
  pool2: {
    name: "ETH Yield Pool",
    apy: 8, // Annual Percentage Yield in percentage
  },
};

// User accounts and balances
const userAccounts = {};

// Utility function to calculate earnings based on APY and deposit duration.
/**
 * Calculates earnings from a deposit in a yield pool.
 * @param {number} principal - The initial deposited amount.
 * @param {number} apy - Annual Percentage Yield (in percentage).
 * @param {number} days - Duration of deposit in days.
 * @returns {number} The calculated earnings.
 */
function calculateEarnings(principal, apy, days) {
  if (principal <= 0 || apy <= 0 || days <= 0) {
    throw new Error("Invalid input for earnings calculation.");
  }
  const annualEarnings = principal * (apy / 100);
  const dailyEarnings = annualEarnings / 365; // Assuming 365 days in a year
  return dailyEarnings * days;
}

// Deposit function
/**
 * Deposits assets into a yield pool for a user.
 * @param {string} userId - The user ID.
 * @param {string} poolId - The yield pool ID.
 * @param {number} amount - The amount to deposit.
 */
function deposit(userId, poolId, amount) {
  if (!yieldPools[poolId]) {
    throw new Error("Invalid pool ID.");
  }
  if (amount <= 0) {
    throw new Error("Deposit amount must be greater than zero.");
  }

  // Initialize user account if not already present
  if (!userAccounts[userId]) {
    userAccounts[userId] = {};
  }

  // Initialize pool balance for user if not already present
  if (!userAccounts[userId][poolId]) {
    userAccounts[userId][poolId] = { balance: 0, depositDate: null };
  }

  // Update balance and deposit date
  userAccounts[userId][poolId].balance += amount;
  userAccounts[userId][poolId].depositDate = new Date();

  console.log(`Successfully deposited ${amount} assets into ${yieldPools[poolId].name}.`);
}

// Withdraw function
/**
 * Withdraws assets and earnings from a yield pool for a user.
 * @param {string} userId - The user ID.
 * @param {string} poolId - The yield pool ID.
 */
function withdraw(userId, poolId) {
  if (!yieldPools[poolId]) {
    throw new Error("Invalid pool ID.");
  }
  if (!userAccounts[userId] || !userAccounts[userId][poolId]) {
    throw new Error("No deposits found for the user in the specified pool.");
  }

  const userPoolData = userAccounts[userId][poolId];
  const { balance, depositDate } = userPoolData;

  if (balance <= 0) {
    throw new Error("Insufficient balance to withdraw.");
  }

  const depositDuration = Math.floor((new Date() - new Date(depositDate)) / (1000 * 60 * 60 * 24)); // Convert duration to days
  const earnings = calculateEarnings(balance, yieldPools[poolId].apy, depositDuration);

  // Reset user pool data
  userAccounts[userId][poolId] = { balance: 0, depositDate: null };

  console.log(`Successfully withdrew ${balance} assets from ${yieldPools[poolId].name}.`);
  console.log(`Earnings for ${depositDuration} days: ${earnings.toFixed(2)}.`);
}

// Example usage
try {
  deposit("user123", "pool1", 1000); // Deposit assets
  withdraw("user123", "pool1"); // Withdraw assets and earnings
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
