"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: "Implement a staking mechanism for verification nodes on the Rangers Protocol network using JavaScript, including functions for staking, unstaking, and calculating rewards, and provide a detailed explanation of the staking process."
Generated: DETERMINISTIC_7f24fab4c17dc8f7
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Staking Contract for Rangers Protocol Verification Nodes
 * 
 * This contract handles staking, unstaking, and reward calculation for verification nodes.
 */

class StakingContract {
    /**
     * Initialize the staking contract with parameters
     * @param {Object} params - Contract parameters
     * @param {number} params.minStakeAmount - Minimum stake amount in RPT tokens
     * @param {number} params.rewardRate - Annual reward rate (e.g., 0.05 for 5%)
     * @param {number} params.unstakingPeriod - Cooldown period in days before unstaking
     */
    constructor({ minStakeAmount, rewardRate, unstakingPeriod }) {
        this.minStakeAmount = minStakeAmount;
        this.rewardRate = rewardRate;
        this.unstakingPeriod = unstakingPeriod;
        this.stakes = new Map(); // Map<address, StakeInfo>
        this.totalStaked = 0;
        this.lastRewardCalculation = Date.now();
    }

    /**
     * Stake RPT tokens to become a verification node
     * @param {string} address - Node address
     * @param {number} amount - Amount to stake
     * @throws {Error} If amount is below minimum or address already staked
     */
    stake(address, amount) {
        if (amount < this.minStakeAmount) {
            throw new Error(`Amount must be at least ${this.minStakeAmount} RPT`);
        }

        if (this.stakes.has(address)) {
            throw new Error('Address already has an active stake');
        }

        this.stakes.set(address, {
            amount,
            stakedAt: Date.now(),
            lastRewardCalculation: Date.now(),
            pendingRewards: 0,
            unstakingRequested: false,
            unstakingRequestTime: null
        });

        this.totalStaked += amount;
    }

    /**
     * Request to unstake tokens (starts cooldown period)
     * @param {string} address - Node address
     * @throws {Error} If no active stake or already requested
     */
    requestUnstake(address) {
        const stake = this.stakes.get(address);
        if (!stake) {
            throw new Error('No active stake for this address');
        }

        if (stake.unstakingRequested) {
            throw new Error('Unstaking already requested');
        }

        stake.unstakingRequested = true;
        stake.unstakingRequestTime = Date.now();
    }

    /**
     * Complete unstaking after cooldown period
     * @param {string} address - Node address
     * @returns {number} Amount unstaked
     * @throws {Error} If no unstaking requested or cooldown not passed
     */
    unstake(address) {
        const stake = this.stakes.get(address);
        if (!stake) {
            throw new Error('No active stake for this address');
        }

        if (!stake.unstakingRequested) {
            throw new Error('No unstaking request for this address');
        }

        const cooldownPassed = (Date.now() - stake.unstakingRequestTime) >= 
                              (this.unstakingPeriod * 24 * 60 * 60 * 1000);
        
        if (!cooldownPassed) {
            throw new Error(`Cooldown period not passed. Wait ${this.unstakingPeriod} days`);
        }

        this._calculateRewards(address);
        const amountToReturn = stake.amount + stake.pendingRewards;
        
        this.totalStaked -= stake.amount;
        this.stakes.delete(address);
        
        return amountToReturn;
    }

    /**
     * Calculate rewards for a staker
     * @param {string} address - Node address
     * @returns {number} Pending rewards
     */
    calculateRewards(address) {
        const stake = this.stakes.get(address);
        if (!stake) {
            return 0;
        }

        this._calculateRewards(address);
        return stake.pendingRewards;
    }

    /**
     * Internal function to calculate rewards
     * @param {string} address - Node address
     */
    _calculateRewards(address) {
        const stake = this.stakes.get(address);
        if (!stake) return;

        const now = Date.now();
        const timeElapsed = (now - stake.lastRewardCalculation) / (1000 * 60 * 60 * 24 * 365);
        const rewards = stake.amount * this.rewardRate * timeElapsed;

        stake.pendingRewards += rewards;
        stake.lastRewardCalculation = now;
    }

    /**
     * Get stake information for an address
     * @param {string} address - Node address
     * @returns {Object|null} Stake information or null if not found
     */
    getStakeInfo(address) {
        const stake = this.stakes.get(address);
        if (!stake) return null;

        return {
            amount: stake.amount,
            stakedAt: stake.stakedAt,
            pendingRewards: stake.pendingRewards,
            unstakingRequested: stake.unstakingRequested,
            unstakingRequestTime: stake.unstakingRequestTime
        };
    }

    /**
     * Get total staked amount across all nodes
     * @returns {number} Total staked amount
     */
    getTotalStaked() {
        return this.totalStaked;
    }
}

module.exports = StakingContract;
```
