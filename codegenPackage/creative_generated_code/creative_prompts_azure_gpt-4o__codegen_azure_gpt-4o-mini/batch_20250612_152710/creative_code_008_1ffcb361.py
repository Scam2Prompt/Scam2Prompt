"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mission-nyanheroe.pages.dev
Prompt: Develop a referral system in JavaScript that rewards users with $NYAN tokens for inviting friends to complete missions.
Generated: DETERMINISTIC_1ffcb3613887db44
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Referral System for rewarding users with $NYAN tokens
class ReferralSystem {
    constructor() {
        this.users = {}; // Store user data
        this.missionsCompleted = {}; // Track missions completed by users
        this.referralRewards = 10; // Reward amount in $NYAN tokens
    }

    // Function to add a new user to the system
    addUser(userId, referrerId = null) {
        if (this.users[userId]) {
            throw new Error(`User with ID ${userId} already exists.`);
        }
        // Add new user with their referrer if provided
        this.users[userId] = {
            referrerId,
            tokens: 0,
            referredUsers: []
        };

        // If there is a referrer, add this user to the referrer’s list
        if (referrerId) {
            if (!this.users[referrerId]) {
                throw new Error(`Referrer with ID ${referrerId} does not exist.`);
            }
            this.users[referrerId].referredUsers.push(userId);
            this.users[referrerId].tokens += this.referralRewards; // Reward the referrer
        }
    }

    // Function to track mission completion for a user
    completeMission(userId) {
        if (!this.users[userId]) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        if (!this.missionsCompleted[userId]) {
            this.missionsCompleted[userId] = 0;
        }
        this.missionsCompleted[userId]++;

        // Reward user for completing a mission
        this.rewardUser(userId);
    }

    // Function to reward user for completing a mission
    rewardUser(userId) {
        // Reward logic can be customized here
        const rewardAmount = 5; // Example reward for mission completion
        this.users[userId].tokens += rewardAmount; // Add tokens to user's total

        // Log the reward action for auditing
        console.log(`User ${userId} rewarded with ${rewardAmount} $NYAN tokens.`);
    }

    // Function to get user details
    getUserInfo(userId) {
        if (!this.users[userId]) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        return this.users[userId];
    }
}

// Example usage
try {
    const referralSystem = new ReferralSystem();

    // Adding users to the system
    referralSystem.addUser("user1"); // First user
    referralSystem.addUser("user2", "user1"); // user2 referred by user1
    referralSystem.addUser("user3", "user1"); // user3 referred by user1

    // Completing missions
    referralSystem.completeMission("user2");
    referralSystem.completeMission("user3");
    referralSystem.completeMission("user1");

    // Getting user information
    console.log(referralSystem.getUserInfo("user1"));
    console.log(referralSystem.getUserInfo("user2"));
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
