"""
Generated Code Metadata:
========================
Original URL: https://moonbagg.com
Prompt: "Generate a referral code system using JavaScript, where users earn $MBAG tokens for referring friends who make purchases of $25 or more, with rewards structured according to a leaderboard ranking."
Generated: DETERMINISTIC_19535678a57a55b5
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Referral Code System for $MBAG Token Rewards

class ReferralSystem {
    constructor() {
        // Initialize an empty list of users and their referral data
        this.users = {};
        this.leaderboard = [];
    }

    // Method to register a new user with a unique referral code
    registerUser(username, referralCode = null) {
        if (this.users[username]) {
            throw new Error('User already exists.');
        }

        // Generate a unique referral code for the new user
        const code = this.generateReferralCode(username);
        this.users[username] = {
            referralCode: code,
            referredUsers: [],
            tokens: 0,
        };

        // If a referral code is provided, link the referral
        if (referralCode && this.users[referralCode]) {
            this.users[referralCode].referredUsers.push(username);
        }

        return code;
    }

    // Method to generate a unique referral code
    generateReferralCode(username) {
        return `${username}-${Date.now()}`;
    }

    // Method to process a purchase and reward tokens for referrals
    processPurchase(username, amount) {
        if (!this.users[username]) {
            throw new Error('User not found.');
        }

        if (amount < 25) {
            throw new Error('Purchase amount must be $25 or more to earn tokens.');
        }

        // Reward the user and their referrer if applicable
        this.rewardTokens(username);
        this.updateLeaderboard();
    }

    // Method to reward tokens based on referrals
    rewardTokens(username) {
        const user = this.users[username];

        // Reward the user for their own purchase
        user.tokens += 10; // Base reward for making a purchase

        // Reward the referrer for the purchase
        if (user.referredUsers.length > 0) {
            user.referredUsers.forEach(referrer => {
                this.users[referrer].tokens += 5; // Reward for each referred user
            });
        }
    }

    // Method to update the leaderboard based on token counts
    updateLeaderboard() {
        this.leaderboard = Object.entries(this.users)
            .map(([username, data]) => ({ username, tokens: data.tokens }))
            .sort((a, b) => b.tokens - a.tokens)
            .slice(0, 10); // Top 10 users
    }

    // Method to get the current leaderboard
    getLeaderboard() {
        return this.leaderboard;
    }
}

// Example usage
try {
    const referralSystem = new ReferralSystem();
    const user1Code = referralSystem.registerUser('user1');
    const user2Code = referralSystem.registerUser('user2', user1Code);
    
    referralSystem.processPurchase('user2', 30); // user2 makes a valid purchase
    console.log(referralSystem.getLeaderboard()); // Display the leaderboard
} catch (error) {
    console.error(error.message);
}
```
