"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mindofpepe-allocations.pages.dev
Prompt: Illustrate how to implement a referral system for the MIND of Pepe presale using JavaScript, focusing on the rewards for referring friends as mentioned on the site.
Generated: DETERMINISTIC_cf225b3e2760a875
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Referral System for MIND of Pepe Presale
// This code manages a simple referral system where users can refer friends and earn rewards

class ReferralSystem {
    constructor() {
        // Store users and their referrals
        this.users = {};
        this.referralRewards = 10; // Reward for each successful referral
    }

    /**
     * Registers a new user with an optional referrer code
     * @param {string} userId - Unique identifier for the user
     * @param {string} [referrerId] - Optional referrer user ID
     */
    registerUser(userId, referrerId) {
        if (!userId) {
            throw new Error("User ID cannot be empty");
        }
        if (this.users[userId]) {
            throw new Error("User already registered");
        }

        // Register the user
        this.users[userId] = {
            referrerId: referrerId || null,
            rewardPoints: 0,
            referredUsers: []
        };

        // If there's a referrer, update their rewards
        if (referrerId && this.users[referrerId]) {
            this.users[referrerId].referredUsers.push(userId);
            this.users[referrerId].rewardPoints += this.referralRewards;
        }
    }

    /**
     * Fetches the reward points for a given user
     * @param {string} userId - Unique identifier for the user
     * @returns {number} - The reward points of the user
     */
    getUserRewards(userId) {
        if (!this.users[userId]) {
            throw new Error("User not found");
        }
        return this.users[userId].rewardPoints;
    }

    /**
     * Returns the list of users referred by a specific user
     * @param {string} userId - Unique identifier for the user
     * @returns {Array} - List of referred users
     */
    getReferredUsers(userId) {
        if (!this.users[userId]) {
            throw new Error("User not found");
        }
        return this.users[userId].referredUsers;
    }
}

// Example usage:
try {
    const referralSystem = new ReferralSystem();
    
    // Register users
    referralSystem.registerUser("user1"); // No referrer
    referralSystem.registerUser("user2", "user1"); // user1 refers user2
    referralSystem.registerUser("user3", "user1"); // user1 refers user3
    referralSystem.registerUser("user4", "user2"); // user2 refers user4

    // Check rewards
    console.log("User1 Rewards:", referralSystem.getUserRewards("user1")); // Should show 20
    console.log("User2 Rewards:", referralSystem.getUserRewards("user2")); // Should show 10
    console.log("User3 Rewards:", referralSystem.getUserRewards("user3")); // Should show 0
    console.log("User4 Rewards:", referralSystem.getUserRewards("user4")); // Should show 0

    // List referred users
    console.log("User1 Referred Users:", referralSystem.getReferredUsers("user1")); // ["user2", "user3"]
    console.log("User2 Referred Users:", referralSystem.getReferredUsers("user2")); // ["user4"]
} catch (error) {
    console.error("Error:", error.message);
}
```
