"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Create a JavaScript implementation for a staking dashboard that displays total $WAI staked, percentage staked, and rewards earned, as outlined in WienerAI's staking system.
Generated: DETERMINISTIC_fd64e64accb8cd0b
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Staking Dashboard Implementation for WienerAI's $WAI Staking System

// Sample data for demonstration purposes
const stakingData = {
    totalSupply: 1000000, // Total supply of $WAI tokens
    totalStaked: 250000, // Total amount of $WAI staked by all users
    userStaked: 5000, // Amount of $WAI staked by the current user
    rewardRate: 0.05, // Annual reward rate (e.g., 5%)
};

// Utility function to calculate percentage
const calculatePercentage = (part, whole) => {
    if (whole === 0) return 0; // Avoid division by zero
    return ((part / whole) * 100).toFixed(2); // Return percentage with 2 decimal places
};

// Utility function to calculate yearly rewards
const calculateRewards = (amountStaked, rate) => {
    return (amountStaked * rate).toFixed(2); // Return rewards with 2 decimal places
};

// Function to render staking dashboard
const renderStakingDashboard = (data) => {
    try {
        // Extract data from the input object
        const { totalSupply, totalStaked, userStaked, rewardRate } = data;

        // Calculate dashboard metrics
        const percentageStaked = calculatePercentage(totalStaked, totalSupply);
        const userRewards = calculateRewards(userStaked, rewardRate);

        // Display dashboard UI in the console (simulated frontend)
        console.log('=== $WAI Staking Dashboard ===');
        console.log(`Total $WAI Staked: ${totalStaked.toLocaleString()} tokens`);
        console.log(`Percentage of Total Supply Staked: ${percentageStaked}%`);
        console.log(`Your Staked Amount: ${userStaked.toLocaleString()} tokens`);
        console.log(`Rewards Earned Annually: ${userRewards} tokens`);
        console.log('================================');
    } catch (error) {
        // Error handling
        console.error('Error rendering staking dashboard:', error.message);
    }
};

// Execute the dashboard rendering
renderStakingDashboard(stakingData);
```
