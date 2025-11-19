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
/**
 * War Chest Staking Platform Simulator
 * 
 * Simulates staking in two pools with different return rates and locked schedules.
 */

class StakingPool {
    /**
     * @param {string} name - Name of the staking pool
     * @param {number} annualReturnRate - Annual return rate (e.g., 0.1 for 10%)
     * @param {number} lockDurationDays - Duration tokens are locked (in days)
     */
    constructor(name, annualReturnRate, lockDurationDays) {
        this.name = name;
        this.annualReturnRate = annualReturnRate;
        this.lockDurationDays = lockDurationDays;
    }

    /**
     * Calculate rewards for a given stake amount and duration
     * @param {number} amount - Amount of tokens staked
     * @param {number} durationDays - Duration of stake in days
     * @returns {number} Calculated rewards
     */
    calculateRewards(amount, durationDays) {
        if (amount <= 0) throw new Error("Stake amount must be positive");
        if (durationDays <= 0) throw new Error("Duration must be positive");
        
        const dailyRate = this.annualReturnRate / 365;
        return amount * dailyRate * durationDays;
    }
}

class StakingPlatform {
    constructor() {
        this.pools = [
            new StakingPool("Standard Pool", 0.1, 30),  // 10% APR, 30-day lock
            new StakingPool("Premium Pool", 0.2, 90)    // 20% APR, 90-day lock
        ];
        this.stakes = [];
    }

    /**
     * Stake tokens in a pool
     * @param {number} poolIndex - Index of the pool to stake in
     * @param {number} amount - Amount of tokens to stake
     * @param {string} userAddress - User's wallet address
     * @returns {object} Stake details
     */
    stake(poolIndex, amount, userAddress) {
        if (poolIndex < 0 || poolIndex >= this.pools.length) {
            throw new Error("Invalid pool index");
        }
        if (amount <= 0) {
            throw new Error("Stake amount must be positive");
        }
        if (!userAddress || typeof userAddress !== 'string') {
            throw new Error("Invalid user address");
        }

        const pool = this.pools[poolIndex];
        const stake = {
            pool: pool.name,
            amount,
            userAddress,
            startDate: new Date(),
            unlockDate: new Date(Date.now() + pool.lockDurationDays * 24 * 60 * 60 * 1000),
            claimed: false
        };

        this.stakes.push(stake);
        return stake;
    }

    /**
     * Claim rewards for a stake
     * @param {number} stakeIndex - Index of the stake to claim
     * @returns {object} Claim details
     */
    claim(stakeIndex) {
        if (stakeIndex < 0 || stakeIndex >= this.stakes.length) {
            throw new Error("Invalid stake index");
        }

        const stake = this.stakes[stakeIndex];
        if (stake.claimed) {
            throw new Error("Rewards already claimed");
        }

        const currentDate = new Date();
        if (currentDate < stake.unlockDate) {
            throw new Error("Tokens are still locked");
        }

        const pool = this.pools.find(p => p.name === stake.pool);
        if (!pool) {
            throw new Error("Pool not found");
        }

        const durationDays = (currentDate - stake.startDate) / (1000 * 60 * 60 * 24);
        const rewards = pool.calculateRewards(stake.amount, durationDays);

        stake.claimed = true;
        stake.claimedDate = currentDate;
        stake.rewards = rewards;

        return {
            amount: stake.amount,
            rewards,
            total: stake.amount + rewards
        };
    }

    /**
     * Get all stakes for a user
     * @param {string} userAddress - User's wallet address
     * @returns {array} Array of user's stakes
     */
    getUserStakes(userAddress) {
        if (!userAddress || typeof userAddress !== 'string') {
            throw new Error("Invalid user address");
        }
        return this.stakes.filter(stake => stake.userAddress === userAddress);
    }

    /**
     * Get all available pools
     * @returns {array} Array of staking pools
     */
    getPools() {
        return this.pools.map(pool => ({
            name: pool.name,
            annualReturnRate: pool.annualReturnRate,
            lockDurationDays: pool.lockDurationDays
        }));
    }
}

// Example usage:
/*
const platform = new StakingPlatform();

// Display available pools
console.log("Available pools:", platform.getPools());

// Stake tokens
const stake1 = platform.stake(0, 1000, "0xUser1");
console.log("Staked in Standard Pool:", stake1);

const stake2 = platform.stake(1, 2000, "0xUser1");
console.log("Staked in Premium Pool:", stake2);

// Try to claim (will fail if tokens are still locked)
try {
    const claimResult = platform.claim(0);
    console.log("Claim result:", claimResult);
} catch (error) {
    console.error("Claim error:", error.message);
}

// Get user stakes
console.log("User stakes:", platform.getUserStakes("0xUser1"));
*/
```
