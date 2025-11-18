"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-neurongate.xyz
Prompt: Generate JavaScript code for creating a rewards system for an online casino, including features like free spins and bonuses as described in Zeus Fortune.
Generated: DETERMINISTIC_5af95161796982d1
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// RewardsSystem class manages rewards for users in the online casino
class RewardsSystem {
    constructor() {
        // Initialize rewards database
        this.users = {};
    }

    // Adds a new user to the rewards system
    addUser(userId) {
        if (this.users[userId]) {
            throw new Error(`User with ID ${userId} already exists.`);
        }
        this.users[userId] = {
            freeSpins: 0,
            bonuses: 0,
            totalRewards: 0,
        };
    }

    // Adds free spins to a user's account
    addFreeSpins(userId, spins) {
        this._validateUser(userId);
        if (spins <= 0) {
            throw new Error('Number of spins must be greater than zero.');
        }
        this.users[userId].freeSpins += spins;
        this.users[userId].totalRewards += spins; // Assuming each spin counts as a reward
    }

    // Adds a bonus to a user's account
    addBonus(userId, amount) {
        this._validateUser(userId);
        if (amount <= 0) {
            throw new Error('Bonus amount must be greater than zero.');
        }
        this.users[userId].bonuses += amount;
        this.users[userId].totalRewards += amount; // Assuming bonus adds to total rewards
    }

    // Redeems free spins for a user
    redeemFreeSpins(userId, spins) {
        this._validateUser(userId);
        if (spins <= 0 || spins > this.users[userId].freeSpins) {
            throw new Error('Invalid number of spins to redeem.');
        }
        this.users[userId].freeSpins -= spins;
        console.log(`User ${userId} redeemed ${spins} free spins.`);
    }

    // Redeems bonus for a user
    redeemBonus(userId, amount) {
        this._validateUser(userId);
        if (amount <= 0 || amount > this.users[userId].bonuses) {
            throw new Error('Invalid bonus amount to redeem.');
        }
        this.users[userId].bonuses -= amount;
        console.log(`User ${userId} redeemed a bonus of ${amount}.`);
    }

    // Retrieves the rewards summary for a user
    getRewardsSummary(userId) {
        this._validateUser(userId);
        return {
            freeSpins: this.users[userId].freeSpins,
            bonuses: this.users[userId].bonuses,
            totalRewards: this.users[userId].totalRewards,
        };
    }

    // Private method to validate whether a user exists
    _validateUser(userId) {
        if (!this.users[userId]) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
    }
}

// Example usage
try {
    const rewardsSystem = new RewardsSystem();
    rewardsSystem.addUser('user123');
    rewardsSystem.addFreeSpins('user123', 10);
    rewardsSystem.addBonus('user123', 50);
    rewardsSystem.redeemFreeSpins('user123', 5);
    rewardsSystem.redeemBonus('user123', 20);
    
    console.log(rewardsSystem.getRewardsSummary('user123'));
} catch (error) {
    console.error(error.message);
}
```
