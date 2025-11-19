"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Write a JavaScript function that allows users to track their $ASX holdings and associated rewards from multiple revenue streams in DeFi.
Generated: DETERMINISTIC_dcb5dc60a93e5a76
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ASX Holdings Tracker
 * This function allows users to track their $ASX holdings and associated rewards
 * from multiple revenue streams in Decentralized Finance (DeFi).
 */

/**
 * Class representing a user's ASX holdings and rewards.
 */
class ASXTracker {
    constructor() {
        // Initialize an empty object to hold the holdings and rewards
        this.holdings = {};
    }

    /**
     * Add or update ASX holdings for a specific revenue stream.
     * @param {string} stream - The name of the revenue stream.
     * @param {number} amount - The amount of $ASX held in the revenue stream.
     * @param {number} rewards - The rewards earned from the revenue stream.
     */
    addOrUpdateHoldings(stream, amount, rewards) {
        if (typeof stream !== 'string' || stream.trim() === '') {
            throw new Error('Invalid stream name. It must be a non-empty string.');
        }
        if (typeof amount !== 'number' || amount < 0) {
            throw new Error('Invalid amount. It must be a non-negative number.');
        }
        if (typeof rewards !== 'number' || rewards < 0) {
            throw new Error('Invalid rewards. It must be a non-negative number.');
        }

        // Update holdings and rewards for the specified stream
        this.holdings[stream] = {
            amount: amount,
            rewards: rewards
        };
    }

    /**
     * Get the total ASX holdings across all revenue streams.
     * @returns {number} The total amount of $ASX held.
     */
    getTotalHoldings() {
        return Object.values(this.holdings).reduce((total, stream) => total + stream.amount, 0);
    }

    /**
     * Get the total rewards across all revenue streams.
     * @returns {number} The total rewards earned.
     */
    getTotalRewards() {
        return Object.values(this.holdings).reduce((total, stream) => total + stream.rewards, 0);
    }

    /**
     * Get the details of all holdings.
     * @returns {Object} The details of all ASX holdings and rewards.
     */
    getHoldingsDetails() {
        return this.holdings;
    }

    /**
     * Clear all holdings and rewards.
     */
    clearHoldings() {
        this.holdings = {};
    }
}

// Example usage:
try {
    const myASXTracker = new ASXTracker();
    myASXTracker.addOrUpdateHoldings('Liquidity Pool A', 150, 10);
    myASXTracker.addOrUpdateHoldings('Staking Pool B', 200, 25);

    console.log('Total ASX Holdings:', myASXTracker.getTotalHoldings()); // Outputs: Total ASX Holdings: 350
    console.log('Total Rewards:', myASXTracker.getTotalRewards()); // Outputs: Total Rewards: 35
    console.log('Holdings Details:', myASXTracker.getHoldingsDetails());

    // Clear holdings after tracking
    myASXTracker.clearHoldings();
} catch (error) {
    console.error('Error:', error.message);
}
```
