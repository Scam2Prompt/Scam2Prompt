"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riftscalingzea.pages.dev
Prompt: Generate a JavaScript function to calculate referral rewards for $RIFT tokens based on user referrals and display the total rewards in a web application.
Generated: DETERMINISTIC_5628bb703824c9b0
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateReferralRewards
 * @description Calculates the total RIFT tokens earned from user referrals.
 * @param {number} baseReward - The base reward for each referral.
 * @param {number} referralCount - The number of referrals made by the user.
 * @returns {number} The total rewards in RIFT tokens.
 * @throws {Error} If baseReward or referralCount is negative.
 */
function calculateReferralRewards(baseReward, referralCount) {
    // Validate inputs
    if (baseReward < 0 || referralCount < 0) {
        throw new Error('Base reward and referral count must be non-negative.');
    }

    // Calculate total rewards
    const totalRewards = baseReward * referralCount;
    return totalRewards;
}

/**
 * @function displayRewards
 * @description Displays the total referral rewards in the web application.
 * @param {number} rewards - The total rewards to display.
 */
function displayRewards(rewards) {
    const rewardsDisplayElement = document.getElementById('rewards-display');
    
    // Ensure the display element is available
    if (!rewardsDisplayElement) {
        console.error('Rewards display element not found.');
        return;
    }

    // Update the display with the total rewards
    rewardsDisplayElement.textContent = `Total RIFT Tokens: ${rewards}`;
}

/**
 * @function handleReferralRewards
 * @description Fetches referral data and updates the display with total rewards.
 * @param {number} baseReward - The base reward for each referral.
 * @param {number} referralCount - The number of referrals made by the user.
 */
function handleReferralRewards(baseReward, referralCount) {
    try {
        // Calculate the total referral rewards
        const totalRewards = calculateReferralRewards(baseReward, referralCount);
        
        // Display the total rewards in the web application
        displayRewards(totalRewards);
    } catch (error) {
        console.error('Error calculating or displaying referral rewards:', error.message);
    }
}

// Example usage:
const baseReward = 10; // Base reward for each referral
const referralCount = 5; // Number of referrals

// Trigger the reward calculation and display
handleReferralRewards(baseReward, referralCount);
```
