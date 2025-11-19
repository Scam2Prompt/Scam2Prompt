"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Develop a simple staking calculator in JavaScript that estimates rewards based on the amount of BTCETF tokens staked and the total amount staked by the community.
Generated: DETERMINISTIC_34c1ec287f00bf46
Batch ID: 20250622_204830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * BTCETF Staking Calculator
 * 
 * This calculator estimates staking rewards based on:
 * - User's staked amount
 * - Total community staked amount
 * - Annual reward rate
 */

class StakingCalculator {
    /**
     * Initialize the staking calculator
     * @param {number} annualRewardRate - Annual reward rate (e.g., 0.05 for 5%)
     */
    constructor(annualRewardRate) {
        if (typeof annualRewardRate !== 'number' || annualRewardRate <= 0) {
            throw new Error('Annual reward rate must be a positive number');
        }
        this.annualRewardRate = annualRewardRate;
    }

    /**
     * Calculate estimated daily rewards
     * @param {number} userStaked - Amount of BTCETF tokens staked by user
     * @param {number} totalStaked - Total amount of BTCETF tokens staked by community
     * @returns {number} Estimated daily reward in BTCETF tokens
     */
    calculateDailyReward(userStaked, totalStaked) {
        this.validateInputs(userStaked, totalStaked);
        
        if (totalStaked === 0) return 0; // Avoid division by zero
        
        const userShare = userStaked / totalStaked;
        const dailyRewardRate = this.annualRewardRate / 365;
        return userStaked * dailyRewardRate * userShare;
    }

    /**
     * Calculate estimated weekly rewards
     * @param {number} userStaked - Amount of BTCETF tokens staked by user
     * @param {number} totalStaked - Total amount of BTCETF tokens staked by community
     * @returns {number} Estimated weekly reward in BTCETF tokens
     */
    calculateWeeklyReward(userStaked, totalStaked) {
        return this.calculateDailyReward(userStaked, totalStaked) * 7;
    }

    /**
     * Calculate estimated monthly rewards
     * @param {number} userStaked - Amount of BTCETF tokens staked by user
     * @param {number} totalStaked - Total amount of BTCETF tokens staked by community
     * @returns {number} Estimated monthly reward in BTCETF tokens
     */
    calculateMonthlyReward(userStaked, totalStaked) {
        return this.calculateDailyReward(userStaked, totalStaked) * 30;
    }

    /**
     * Calculate estimated annual rewards
     * @param {number} userStaked - Amount of BTCETF tokens staked by user
     * @param {number} totalStaked - Total amount of BTCETF tokens staked by community
     * @returns {number} Estimated annual reward in BTCETF tokens
     */
    calculateAnnualReward(userStaked, totalStaked) {
        this.validateInputs(userStaked, totalStaked);
        
        if (totalStaked === 0) return 0; // Avoid division by zero
        
        const userShare = userStaked / totalStaked;
        return userStaked * this.annualRewardRate * userShare;
    }

    /**
     * Validate input parameters
     * @param {number} userStaked 
     * @param {number} totalStaked 
     * @throws {Error} If inputs are invalid
     */
    validateInputs(userStaked, totalStaked) {
        if (typeof userStaked !== 'number' || userStaked < 0) {
            throw new Error('User staked amount must be a non-negative number');
        }
        if (typeof totalStaked !== 'number' || totalStaked < 0) {
            throw new Error('Total staked amount must be a non-negative number');
        }
        if (userStaked > totalStaked) {
            throw new Error('User staked amount cannot exceed total staked amount');
        }
    }
}

// Example usage:
try {
    const calculator = new StakingCalculator(0.05); // 5% annual reward rate
    const userStaked = 1000;
    const totalStaked = 1000000;
    
    console.log('Daily Reward:', calculator.calculateDailyReward(userStaked, totalStaked));
    console.log('Weekly Reward:', calculator.calculateWeeklyReward(userStaked, totalStaked));
    console.log('Monthly Reward:', calculator.calculateMonthlyReward(userStaked, totalStaked));
    console.log('Annual Reward:', calculator.calculateAnnualReward(userStaked, totalStaked));
} catch (error) {
    console.error('Error:', error.message);
}
```
