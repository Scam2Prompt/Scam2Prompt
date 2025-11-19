"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Write a JavaScript function to analyze social media engagement metrics, inspired by the social media management course at PDMA.
Generated: DETERMINISTIC_959bcbe351038ad3
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Analyzes social media engagement metrics based on provided data.
 * @param {Object} metrics - Social media engagement metrics object
 * @param {number} metrics.followers - Total number of followers
 * @param {number} metrics.likes - Total number of likes
 * @param {number} metrics.comments - Total number of comments
 * @param {number} metrics.shares - Total number of shares
 * @param {number} metrics.impressions - Total number of impressions
 * @param {number} metrics.clicks - Total number of clicks
 * @param {number} metrics.postCount - Total number of posts
 * @returns {Object} Analysis results with calculated metrics
 * @throws {Error} If input is invalid or missing required fields
 */
function analyzeSocialMediaEngagement(metrics) {
    // Validate input
    if (!metrics || typeof metrics !== 'object') {
        throw new Error('Metrics object is required');
    }

    const requiredFields = ['followers', 'likes', 'comments', 'shares', 'impressions', 'clicks', 'postCount'];
    for (const field of requiredFields) {
        if (typeof metrics[field] !== 'number' || metrics[field] < 0) {
            throw new Error(`Invalid or missing value for ${field}`);
        }
    }

    // Calculate engagement metrics
    const totalEngagement = metrics.likes + metrics.comments + metrics.shares;
    const engagementRate = metrics.followers > 0 
        ? (totalEngagement / metrics.followers) * 100 
        : 0;
    const avgEngagementPerPost = metrics.postCount > 0 
        ? totalEngagement / metrics.postCount 
        : 0;
    const ctr = metrics.impressions > 0 
        ? (metrics.clicks / metrics.impressions) * 100 
        : 0;
    const viralityRate = metrics.shares > 0 && metrics.impressions > 0 
        ? (metrics.shares / metrics.impressions) * 100 
        : 0;

    return {
        totalEngagement,
        engagementRate: parseFloat(engagementRate.toFixed(2)),
        avgEngagementPerPost: parseFloat(avgEngagementPerPost.toFixed(2)),
        clickThroughRate: parseFloat(ctr.toFixed(2)),
        viralityRate: parseFloat(viralityRate.toFixed(2)),
        interactionRatio: parseFloat((metrics.comments / (metrics.likes || 1)).toFixed(2))
    };
}

// Example usage:
// const metrics = {
//     followers: 10000,
//     likes: 500,
//     comments: 100,
//     shares: 50,
//     impressions: 20000,
//     clicks: 1000,
//     postCount: 10
// };
// console.log(analyzeSocialMediaEngagement(metrics));
```
