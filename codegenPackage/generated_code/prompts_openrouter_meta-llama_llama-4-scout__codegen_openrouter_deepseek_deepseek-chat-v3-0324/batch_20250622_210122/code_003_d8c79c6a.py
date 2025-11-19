"""
Generated Code Metadata:
========================
Original URL: https://shubaswap.com
Prompt: Create a JavaScript function to calculate daily bonuses and cashback rewards for users on a platform like MESIN128.
Generated: DETERMINISTIC_d8c79c6a9098e08e
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates daily bonuses and cashback rewards for users.
 * 
 * @param {Object} user - The user object containing necessary details
 * @param {number} user.dailyStreak - Current daily login streak
 * @param {number} user.totalDeposits - Total deposits made by the user
 * @param {number} user.totalWagered - Total amount wagered by the user
 * @param {boolean} [user.isVIP=false] - Whether the user is a VIP member
 * @param {Object} [config] - Configuration object for bonus calculations
 * @param {number} [config.baseBonus=10] - Base bonus amount
 * @param {number} [config.streakMultiplier=1.5] - Multiplier for daily streak
 * @param {number} [config.vipMultiplier=2] - Multiplier for VIP users
 * @param {number} [config.cashbackRate=0.01] - Cashback percentage (0-1)
 * @returns {Object} An object containing bonus and cashback amounts
 * @throws {Error} If invalid input parameters are provided
 */
function calculateRewards(user, config = {}) {
    // Validate input parameters
    if (!user || typeof user !== 'object') {
        throw new Error('Invalid user object provided');
    }

    const {
        dailyStreak = 0,
        totalDeposits = 0,
        totalWagered = 0,
        isVIP = false
    } = user;

    if (typeof dailyStreak !== 'number' || dailyStreak < 0) {
        throw new Error('Invalid dailyStreak value');
    }
    if (typeof totalDeposits !== 'number' || totalDeposits < 0) {
        throw new Error('Invalid totalDeposits value');
    }
    if (typeof totalWagered !== 'number' || totalWagered < 0) {
        throw new Error('Invalid totalWagered value');
    }

    // Set default config values
    const {
        baseBonus = 10,
        streakMultiplier = 1.5,
        vipMultiplier = 2,
        cashbackRate = 0.01
    } = config;

    // Calculate daily bonus
    let bonus = baseBonus;
    bonus *= Math.min(1 + (dailyStreak * 0.1), streakMultiplier); // Cap at streakMultiplier
    if (isVIP) {
        bonus *= vipMultiplier;
    }

    // Calculate cashback
    const cashback = totalWagered * cashbackRate;

    // Ensure values are numbers and round to 2 decimal places
    const formatValue = (value) => {
        const num = Number(value);
        return isNaN(num) ? 0 : parseFloat(num.toFixed(2));
    };

    return {
        dailyBonus: formatValue(bonus),
        cashback: formatValue(cashback)
    };
}

// Example usage:
// const user = {
//     dailyStreak: 5,
//     totalDeposits: 1000,
//     totalWagered: 5000,
//     isVIP: true
// };
// const rewards = calculateRewards(user);
// console.log(rewards);
```
