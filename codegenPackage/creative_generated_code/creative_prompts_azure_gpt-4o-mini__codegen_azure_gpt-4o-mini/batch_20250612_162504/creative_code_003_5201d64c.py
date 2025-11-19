"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stoneheads-staking.vercel.app
Prompt: What are the best practices for developing a staking application using JavaScript, as seen in Stone Heads?
Generated: DETERMINISTIC_5201d64cd889f3b1
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Staking Application using JavaScript
 * This application allows users to stake tokens, check staking status, and withdraw tokens.
 */

class StakingApp {
    constructor() {
        this.stakedAmount = 0;
        this.stakers = new Map(); // Store stakers and their staked amounts
    }

    /**
     * Stakes a specified amount of tokens for the user.
     * @param {string} userId - The ID of the user wishing to stake.
     * @param {number} amount - The amount of tokens to stake.
     * @throws Will throw an error if the amount is less than or equal to zero.
     */
    stakeTokens(userId, amount) {
        if (amount <= 0) {
            throw new Error("Amount to stake must be greater than zero.");
        }

        if (!this.stakers.has(userId)) {
            this.stakers.set(userId, 0);
        }

        this.stakers.set(userId, this.stakers.get(userId) + amount);
        this.stakedAmount += amount;

        console.log(`${userId} successfully staked ${amount} tokens.`);
    }

    /**
     * Checks the staking balance of a user.
     * @param {string} userId - The ID of the user.
     * @returns {number} - The amount of tokens staked by the user.
     */
    checkStakingStatus(userId) {
        return this.stakers.get(userId) || 0;
    }

    /**
     * Withdraws a specified amount of tokens for the user.
     * @param {string} userId - The ID of the user wishing to withdraw.
     * @param {number} amount - The amount of tokens to withdraw.
     * @throws Will throw an error if the withdrawal amount is invalid or exceeds staked amount.
     */
    withdrawTokens(userId, amount) {
        const stakedAmount = this.checkStakingStatus(userId);

        if (amount <= 0) {
            throw new Error("Amount to withdraw must be greater than zero.");
        }

        if (amount > stakedAmount) {
            throw new Error("Withdrawal amount exceeds staked amount.");
        }

        this.stakers.set(userId, stakedAmount - amount);
        this.stakedAmount -= amount;

        console.log(`${userId} successfully withdrew ${amount} tokens.`);
    }

    /**
     * Gets the total staked amount across all users.
     * @returns {number} - The total staked amount.
     */
    getTotalStakedAmount() {
        return this.stakedAmount;
    }
}

// Example usage:
try {
    const stakingApp = new StakingApp();

    stakingApp.stakeTokens("user1", 100);
    stakingApp.stakeTokens("user2", 200);
    console.log(`User1 Staked Amount: ${stakingApp.checkStakingStatus("user1")}`);
    console.log(`Total Staked Amount: ${stakingApp.getTotalStakedAmount()}`);

    stakingApp.withdrawTokens("user1", 50);
    console.log(`User1 Staked Amount after withdrawal: ${stakingApp.checkStakingStatus("user1")}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
