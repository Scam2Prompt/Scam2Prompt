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
/**
 * Referral System for rewarding users with $NYAN tokens.
 * Users receive tokens for inviting friends who complete missions.
 */

// Mock database for users and missions (In production, this would be a real database)
const database = {
    users: {},
    missions: {}
};

// Token Reward System Configuration
const TOKEN_REWARD = 50; // Number of $NYAN tokens rewarded per completed mission by a referred friend

/**
 * Registers a new user in the database.
 * @param {string} userId - Unique identifier for the user.
 * @param {string} referrerId - Optional referrer ID for tracking referrals.
 */
function registerUser(userId, referrerId = null) {
    if (!userId || database.users[userId]) {
        throw new Error("Invalid or duplicate user ID.");
    }

    database.users[userId] = {
        referrerId: referrerId || null,
        completedMissions: 0,
        tokensEarned: 0
    };

    console.log(`User ${userId} registered successfully!`);
}

/**
 * Marks a mission as completed for a user. Rewards tokens to the referrer if applicable.
 * @param {string} userId - Unique identifier for the user.
 */
function completeMission(userId) {
    const user = database.users[userId];
    if (!user) {
        throw new Error("User ID not found.");
    }

    // Increment the user's completed mission count
    user.completedMissions += 1;

    // Check if the user was referred by someone
    if (user.referrerId) {
        const referrer = database.users[user.referrerId];
        if (referrer) {
            referrer.tokensEarned += TOKEN_REWARD;
            console.log(`Referrer ${user.referrerId} rewarded with ${TOKEN_REWARD} $NYAN tokens!`);
        }
    }

    console.log(`Mission completed by ${userId}.`);
}

/**
 * Retrieves user details including their completed missions and tokens earned.
 * @param {string} userId - Unique identifier for the user.
 * @returns {object} User details.
 */
function getUserDetails(userId) {
    const user = database.users[userId];
    if (!user) {
        throw new Error("User ID not found.");
    }
    return user;
}

// Example Usage:

try {
    // Register users
    registerUser("User1");
    registerUser("User2", "User1"); // User2 referred by User1

    // Complete missions
    completeMission("User2"); // User2 completes a mission; User1 is rewarded
    completeMission("User2"); // User2 completes another mission; User1 is rewarded again

    // Get user details
    console.log(getUserDetails("User1")); // Check User1's tokens earned
    console.log(getUserDetails("User2")); // Check User2's completed missions and tokens earned

} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
