"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-riftswaptokens.pages.dev
Prompt: Write a function in JavaScript to calculate and display referral rewards ($RIFT tokens) dynamically based on user input on the Rift Swap platform.
Generated: DETERMINISTIC_7c22d93e8dbe1082
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
 * Function to calculate referral rewards ($RIFT tokens) dynamically
 * based on user input on the Rift Swap platform.
 *
 * @param {number} tradeAmount - The trade amount (in USD) entered by the user.
 * @param {number} referralRate - The referral rate percentage (e.g., 5 for 5%).
 *
 * @returns {string} - A formatted string displaying the calculated referral rewards.
 */
function calculateReferralRewards(tradeAmount, referralRate) {
    // Input validation
    if (typeof tradeAmount !== 'number' || tradeAmount <= 0) {
        throw new Error('Invalid trade amount. Please provide a positive number.');
    }
    if (typeof referralRate !== 'number' || referralRate <= 0 || referralRate > 100) {
        throw new Error('Invalid referral rate. Please provide a number between 0 and 100.');
    }

    // Calculate referral rewards in $RIFT tokens
    const rewards = (tradeAmount * referralRate) / 100;

    // Format rewards to two decimal places
    const formattedRewards = rewards.toFixed(2);

    return `$RIFT Tokens Earned: ${formattedRewards}`;
}

// Example usage wrapped in try-catch for error handling
try {
    // Dynamic user input (for demonstration purposes)
    const tradeAmount = 1000; // e.g., trade amount in USD
    const referralRate = 5;   // e.g., referral rate in percentage

    const result = calculateReferralRewards(tradeAmount, referralRate);
    console.log(result); // Output referral rewards
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
