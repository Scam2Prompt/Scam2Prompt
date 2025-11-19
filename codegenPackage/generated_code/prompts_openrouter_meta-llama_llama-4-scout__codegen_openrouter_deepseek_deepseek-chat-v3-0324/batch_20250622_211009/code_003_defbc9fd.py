"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Design a token utility system using JavaScript that allows holders to access exclusive content, participate in contests, and exchange tokens for real-world prizes, as described in METAL's token utility.
Generated: DETERMINISTIC_defbc9fd53e8e779
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * METAL Token Utility System
 * 
 * This system manages token-based access to exclusive content, contests, and prize exchanges.
 * It includes functionality for checking balances, redeeming tokens, and managing access rights.
 */

const METALTokenUtility = (function() {
    // Token configuration
    const config = {
        tokenName: 'METAL',
        tokenSymbol: 'MTL',
        decimals: 18,
        contentAccessPrice: 100, // Tokens required for content access
        contestEntryPrice: 500,  // Tokens required for contest entry
        prizeExchangeRates: {
            'T-Shirt': 1000,
            'ConcertTicket': 5000,
            'VIPExperience': 10000
        }
    };

    // User data storage
    let users = {};

    /**
     * Initialize a new user with default balance
     * @param {string} userId - Unique user identifier
     * @param {number} initialBalance - Initial token balance (in wei)
     */
    function initializeUser(userId, initialBalance = 0) {
        if (!userId) throw new Error('User ID is required');
        if (users[userId]) throw new Error('User already exists');

        users[userId] = {
            balance: initialBalance,
            accessRights: {
                exclusiveContent: false,
                activeContests: []
            },
            prizeHistory: []
        };

        return users[userId];
    }

    /**
     * Get user balance
     * @param {string} userId - Unique user identifier
     * @returns {number} User's token balance
     */
    function getBalance(userId) {
        if (!users[userId]) throw new Error('User not found');
        return users[userId].balance;
    }

    /**
     * Add tokens to user's balance
     * @param {string} userId - Unique user identifier
     * @param {number} amount - Amount of tokens to add
     */
    function addTokens(userId, amount) {
        if (!users[userId]) throw new Error('User not found');
        if (amount <= 0) throw new Error('Amount must be positive');

        users[userId].balance += amount;
        return users[userId].balance;
    }

    /**
     * Purchase exclusive content access
     * @param {string} userId - Unique user identifier
     * @returns {boolean} True if purchase was successful
     */
    function purchaseContentAccess(userId) {
        if (!users[userId]) throw new Error('User not found');
        if (users[userId].accessRights.exclusiveContent) {
            throw new Error('User already has content access');
        }
        if (users[userId].balance < config.contentAccessPrice) {
            throw new Error('Insufficient token balance');
        }

        users[userId].balance -= config.contentAccessPrice;
        users[userId].accessRights.exclusiveContent = true;
        return true;
    }

    /**
     * Enter a contest
     * @param {string} userId - Unique user identifier
     * @param {string} contestId - Unique contest identifier
     * @returns {boolean} True if entry was successful
     */
    function enterContest(userId, contestId) {
        if (!users[userId]) throw new Error('User not found');
        if (users[userId].accessRights.activeContests.includes(contestId)) {
            throw new Error('User already entered this contest');
        }
        if (users[userId].balance < config.contestEntryPrice) {
            throw new Error('Insufficient token balance');
        }

        users[userId].balance -= config.contestEntryPrice;
        users[userId].accessRights.activeContests.push(contestId);
        return true;
    }

    /**
     * Exchange tokens for a prize
     * @param {string} userId - Unique user identifier
     * @param {string} prizeName - Name of the prize to redeem
     * @returns {object} Prize redemption confirmation
     */
    function redeemPrize(userId, prizeName) {
        if (!users[userId]) throw new Error('User not found');
        if (!config.prizeExchangeRates[prizeName]) {
            throw new Error('Invalid prize selection');
        }
        if (users[userId].balance < config.prizeExchangeRates[prizeName]) {
            throw new Error('Insufficient token balance');
        }

        const prizeCost = config.prizeExchangeRates[prizeName];
        users[userId].balance -= prizeCost;

        const redemption = {
            prize: prizeName,
            cost: prizeCost,
            date: new Date().toISOString(),
            status: 'pending'
        };

        users[userId].prizeHistory.push(redemption);
        return redemption;
    }

    /**
     * Check if user has content access
     * @param {string} userId - Unique user identifier
     * @returns {boolean} True if user has access
     */
    function hasContentAccess(userId) {
        if (!users[userId]) throw new Error('User not found');
        return users[userId].accessRights.exclusiveContent;
    }

    /**
     * Get user's contest entries
     * @param {string} userId - Unique user identifier
     * @returns {array} List of contest IDs
     */
    function getContestEntries(userId) {
        if (!users[userId]) throw new Error('User not found');
        return users[userId].accessRights.activeContests;
    }

    /**
     * Get user's prize redemption history
     * @param {string} userId - Unique user identifier
     * @returns {array} List of prize redemptions
     */
    function getPrizeHistory(userId) {
        if (!users[userId]) throw new Error('User not found');
        return users[userId].prizeHistory;
    }

    // Public API
    return {
        initializeUser,
        getBalance,
        addTokens,
        purchaseContentAccess,
        enterContest,
        redeemPrize,
        hasContentAccess,
        getContestEntries,
        getPrizeHistory,
        config
    };
})();

// Example usage:
try {
    // Initialize system and user
    METALTokenUtility.initializeUser('user123', 1000);
    
    // Add more tokens
    METALTokenUtility.addTokens('user123', 500);
    
    // Purchase content access
    METALTokenUtility.purchaseContentAccess('user123');
    
    // Enter a contest
    METALTokenUtility.enterContest('user123', 'summer2023');
    
    // Redeem a prize
    METALTokenUtility.redeemPrize('user123', 'T-Shirt');
    
    // Check access rights
    console.log('Has content access:', METALTokenUtility.hasContentAccess('user123'));
    console.log('Current balance:', METALTokenUtility.getBalance('user123'));
} catch (error) {
    console.error('Error:', error.message);
}
```
