"""
Generated Code Metadata:
========================
Original URL: https://presale-moonbag.pages.dev
Prompt: Design a simple staking system using JavaScript, where users can stake their $MBAG coins and earn rewards based on the APY.
Generated: DETERMINISTIC_ba09f1649c339652
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// StakingSystem.js

class StakingSystem {
    constructor(apy) {
        // Annual Percentage Yield (APY) for staking rewards
        this.apy = apy; // APY should be a decimal (e.g., 0.05 for 5%)
        this.stakers = new Map(); // Map to hold staker information
    }

    /**
     * Allows a user to stake a certain amount of $MBAG coins.
     * @param {string} userId - The ID of the user staking coins.
     * @param {number} amount - The amount of $MBAG coins to stake.
     * @throws Will throw an error if the amount is less than or equal to zero.
     */
    stake(userId, amount) {
        if (amount <= 0) {
            throw new Error("Stake amount must be greater than zero.");
        }

        const currentStake = this.stakers.get(userId) || { amount: 0, rewards: 0 };
        currentStake.amount += amount;
        this.stakers.set(userId, currentStake);
        console.log(`${userId} has staked ${amount} $MBAG coins.`);
    }

    /**
     * Calculates the rewards for a user based on their staked amount and the APY.
     * @param {string} userId - The ID of the user to calculate rewards for.
     * @returns {number} - The calculated rewards.
     */
    calculateRewards(userId) {
        const staker = this.stakers.get(userId);
        if (!staker) {
            throw new Error("User has no staked amount.");
        }

        // Calculate rewards based on the APY
        const rewards = (staker.amount * this.apy);
        return rewards;
    }

    /**
     * Allows a user to withdraw their staked amount and rewards.
     * @param {string} userId - The ID of the user withdrawing their stake.
     * @throws Will throw an error if the user has no staked amount.
     * @returns {object} - An object containing the withdrawn amount and rewards.
     */
    withdraw(userId) {
        const staker = this.stakers.get(userId);
        if (!staker) {
            throw new Error("User has no staked amount to withdraw.");
        }

        const totalWithdrawn = staker.amount + staker.rewards;
        this.stakers.delete(userId); // Remove the user from the stakers map
        console.log(`${userId} has withdrawn ${totalWithdrawn} $MBAG coins.`);
        return {
            amount: staker.amount,
            rewards: staker.rewards,
        };
    }

    /**
     * Updates the rewards for all stakers based on the APY.
     */
    updateRewards() {
        this.stakers.forEach((staker, userId) => {
            const rewards = this.calculateRewards(userId);
            staker.rewards += rewards; // Accumulate rewards
        });
        console.log("Rewards updated for all stakers.");
    }
}

// Example usage
try {
    const stakingSystem = new StakingSystem(0.05); // 5% APY
    stakingSystem.stake("user1", 100); // User stakes 100 $MBAG
    stakingSystem.updateRewards(); // Update rewards
    const rewards = stakingSystem.calculateRewards("user1"); // Calculate rewards for user1
    console.log(`User1's rewards: ${rewards}`);
    const withdrawn = stakingSystem.withdraw("user1"); // Withdraw stake and rewards
    console.log(`Withdrawn: ${withdrawn.amount} $MBAG and ${withdrawn.rewards} rewards.`);
} catch (error) {
    console.error(error.message);
}
```
