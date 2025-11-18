"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://joincommonwealth-auth.web.app
Prompt: Write a function in JavaScript to claim, stake, and unstake tokens in a cryptocurrency portfolio, inspired by the staking functionality described on the Common Wealth site.
Generated: DETERMINISTIC_fe6109da034479cd
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cryptocurrency Portfolio Manager
 * Functions to claim rewards, stake tokens, and unstake tokens in a portfolio.
 * 
 * Assumes the existence of a `portfolio` object that tracks user balances and staking information.
 * 
 * @author Your Name
 * @version 1.0
 */

// Portfolio structure example (would typically come from a database or external API)
// const portfolio = {
//   tokens: {
//     "TOKEN_A": {
//       balance: 100,
//       stakedBalance: 50,
//       rewardRate: 0.01, // Rewards per token per second
//       lastClaimed: Date.now()
//     }
//   }
// };

/**
 * Claims staking rewards for a given token in the portfolio.
 * Updates the last claimed timestamp and increases the user's balance.
 * 
 * @param {object} portfolio - The user's portfolio object.
 * @param {string} token - The token symbol (e.g., "TOKEN_A").
 * @returns {string} - Success message or error message.
 */
function claimRewards(portfolio, token) {
    try {
        // Validate input
        if (!portfolio.tokens[token]) {
            throw new Error(`Token ${token} not found in portfolio.`);
        }

        const tokenData = portfolio.tokens[token];
        const currentTime = Date.now();
        const timeElapsed = (currentTime - tokenData.lastClaimed) / 1000; // Time in seconds
        const rewards = tokenData.stakedBalance * tokenData.rewardRate * timeElapsed;

        // Update portfolio
        tokenData.balance += rewards;
        tokenData.lastClaimed = currentTime;

        return `Successfully claimed ${rewards.toFixed(2)} ${token} rewards.`;
    } catch (error) {
        return `Error claiming rewards: ${error.message}`;
    }
}

/**
 * Stakes a specified amount of a token.
 * Moves the amount from the balance to the staked balance.
 * 
 * @param {object} portfolio - The user's portfolio object.
 * @param {string} token - The token symbol (e.g., "TOKEN_A").
 * @param {number} amount - The amount to stake.
 * @returns {string} - Success message or error message.
 */
function stakeTokens(portfolio, token, amount) {
    try {
        // Validate input
        if (!portfolio.tokens[token]) {
            throw new Error(`Token ${token} not found in portfolio.`);
        }
        if (amount <= 0) {
            throw new Error(`Stake amount must be greater than zero.`);
        }
        const tokenData = portfolio.tokens[token];
        if (tokenData.balance < amount) {
            throw new Error(`Insufficient balance to stake ${amount} ${token}.`);
        }

        // Update portfolio
        tokenData.balance -= amount;
        tokenData.stakedBalance += amount;

        return `Successfully staked ${amount} ${token}.`;
    } catch (error) {
        return `Error staking tokens: ${error.message}`;
    }
}

/**
 * Unstakes a specified amount of a token.
 * Moves the amount from the staked balance to the user's balance.
 * 
 * @param {object} portfolio - The user's portfolio object.
 * @param {string} token - The token symbol (e.g., "TOKEN_A").
 * @param {number} amount - The amount to unstake.
 * @returns {string} - Success message or error message.
 */
function unstakeTokens(portfolio, token, amount) {
    try {
        // Validate input
        if (!portfolio.tokens[token]) {
            throw new Error(`Token ${token} not found in portfolio.`);
        }
        if (amount <= 0) {
            throw new Error(`Unstake amount must be greater than zero.`);
        }
        const tokenData = portfolio.tokens[token];
        if (tokenData.stakedBalance < amount) {
            throw new Error(`Insufficient staked balance to unstake ${amount} ${token}.`);
        }

        // Update portfolio
        tokenData.stakedBalance -= amount;
        tokenData.balance += amount;

        return `Successfully unstaked ${amount} ${token}.`;
    } catch (error) {
        return `Error unstaking tokens: ${error.message}`;
    }
}

// Example usage (replace with actual portfolio data):
// const portfolio = {
//   tokens: {
//     "TOKEN_A": {
//       balance: 100,
//       stakedBalance: 50,
//       rewardRate: 0.01,
//       lastClaimed: Date.now()
//     }
//   }
// };

// console.log(claimRewards(portfolio, "TOKEN_A"));
// console.log(stakeTokens(portfolio, "TOKEN_A", 20));
// console.log(unstakeTokens(portfolio, "TOKEN_A", 10));
```
