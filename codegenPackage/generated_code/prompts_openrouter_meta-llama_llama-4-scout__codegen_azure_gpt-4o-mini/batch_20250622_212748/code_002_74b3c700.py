"""
Generated Code Metadata:
========================
Original URL: https://trog-three.vercel.app
Prompt: Generate a JavaScript code snippet to implement a referral system for the TROG Hunt campaign, allowing users to invite friends and earn additional rewards.
Generated: DETERMINISTIC_74b3c700083be520
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Referral System for TROG Hunt Campaign

class ReferralSystem {
    constructor() {
        // Store users and their referrals
        this.users = {};
    }

    /**
     * Register a new user in the system.
     * @param {string} userId - Unique identifier for the user.
     */
    registerUser(userId) {
        if (this.users[userId]) {
            throw new Error('User already registered.');
        }
        this.users[userId] = {
            referrals: [],
            rewards: 0
        };
    }

    /**
     * Invite a friend to join the campaign.
     * @param {string} userId - The ID of the user inviting a friend.
     * @param {string} friendId - The ID of the friend being invited.
     */
    inviteFriend(userId, friendId) {
        if (!this.users[userId]) {
            throw new Error('User not registered.');
        }
        if (this.users[friendId]) {
            throw new Error('Friend already registered.');
        }

        // Add friend to user's referrals
        this.users[userId].referrals.push(friendId);
        this.registerUser(friendId); // Register the friend
        this.users[userId].rewards += 10; // Reward the user for inviting
    }

    /**
     * Get the referral details for a user.
     * @param {string} userId - The ID of the user.
     * @returns {Object} - The referral details including referrals and rewards.
     */
    getReferralDetails(userId) {
        if (!this.users[userId]) {
            throw new Error('User not registered.');
        }
        return {
            referrals: this.users[userId].referrals,
            rewards: this.users[userId].rewards
        };
    }
}

// Example usage
try {
    const referralSystem = new ReferralSystem();
    
    // Register users
    referralSystem.registerUser('user1');
    referralSystem.registerUser('user2');

    // User1 invites User2
    referralSystem.inviteFriend('user1', 'user3');

    // Get referral details for User1
    const user1Details = referralSystem.getReferralDetails('user1');
    console.log(user1Details); // { referrals: ['user3'], rewards: 10 }

} catch (error) {
    console.error('Error:', error.message);
}
```
