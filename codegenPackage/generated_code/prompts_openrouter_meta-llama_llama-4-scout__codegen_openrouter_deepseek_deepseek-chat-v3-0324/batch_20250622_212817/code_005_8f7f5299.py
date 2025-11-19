"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Create a code snippet in JavaScript that calculates a user's mindshare and potential rewards on the Loud platform, given their contribution metrics.
Generated: DETERMINISTIC_8f7f5299363e3b89
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates mindshare and potential rewards for a user on the Loud platform.
 * @param {Object} metrics - User contribution metrics
 * @param {number} metrics.contentContributions - Number of content contributions
 * @param {number} metrics.engagementScore - User engagement score (0-100)
 * @param {number} metrics.referrals - Number of successful referrals
 * @param {number} metrics.activeDays - Number of days active in the last 30 days
 * @returns {Object} - Contains calculated mindshare and potential rewards
 * @throws {Error} - If input metrics are invalid
 */
function calculateLoudRewards(metrics) {
    // Validate input metrics
    if (!metrics || typeof metrics !== 'object') {
        throw new Error('Invalid metrics: must be an object');
    }

    const requiredFields = ['contentContributions', 'engagementScore', 'referrals', 'activeDays'];
    for (const field of requiredFields) {
        if (typeof metrics[field] !== 'number' || metrics[field] < 0) {
            throw new Error(`Invalid value for ${field}: must be a non-negative number`);
        }
    }

    if (metrics.engagementScore > 100) {
        throw new Error('Engagement score must be between 0 and 100');
    }

    if (metrics.activeDays > 30) {
        throw new Error('Active days cannot exceed 30');
    }

    // Calculate base mindshare components
    const contentFactor = Math.min(metrics.contentContributions * 0.5, 50);
    const engagementFactor = metrics.engagementScore * 0.3;
    const referralFactor = Math.min(metrics.referrals * 2, 20);
    const activityFactor = (metrics.activeDays / 30) * 10;

    // Calculate total mindshare (capped at 100)
    const mindshare = Math.min(
        contentFactor + engagementFactor + referralFactor + activityFactor,
        100
    );

    // Calculate potential rewards based on mindshare tiers
    let rewards;
    if (mindshare >= 80) {
        rewards = 1000;
    } else if (mindshare >= 60) {
        rewards = 500;
    } else if (mindshare >= 40) {
        rewards = 250;
    } else if (mindshare >= 20) {
        rewards = 100;
    } else {
        rewards = 50;
    }

    // Apply bonus for top contributors
    if (metrics.contentContributions >= 50) {
        rewards *= 1.2; // 20% bonus
    }

    return {
        mindshare: parseFloat(mindshare.toFixed(2)),
        potentialRewards: Math.round(rewards)
    };
}

// Example usage:
// try {
//     const userMetrics = {
//         contentContributions: 45,
//         engagementScore: 85,
//         referrals: 8,
//         activeDays: 25
//     };
//     const result = calculateLoudRewards(userMetrics);
//     console.log(result);
// } catch (error) {
//     console.error('Error calculating rewards:', error.message);
// }
```
