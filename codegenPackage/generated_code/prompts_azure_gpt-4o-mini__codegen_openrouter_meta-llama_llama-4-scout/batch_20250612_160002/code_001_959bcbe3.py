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
 * Analyzes social media engagement metrics.
 * 
 * @param {Object} metrics - Social media engagement metrics.
 * @param {number} metrics.followers - Total number of followers.
 * @param {number} metrics.reach - Total number of people reached.
 * @param {number} metrics.engagements - Total number of engagements (likes, comments, shares).
 * @param {number} metrics.clicks - Total number of clicks.
 * 
 * @returns {Object} Analysis of social media engagement metrics.
 */
function analyzeSocialMediaEngagement(metrics) {
    try {
        // Check if metrics object is provided
        if (!metrics) {
            throw new Error('Metrics object is required');
        }

        // Check if all required metrics are provided
        const requiredMetrics = ['followers', 'reach', 'engagements', 'clicks'];
        if (!requiredMetrics.every(metric => metric in metrics)) {
            throw new Error('All metrics (followers, reach, engagements, clicks) are required');
        }

        // Calculate engagement rate
        const engagementRate = metrics.engagements / metrics.reach * 100;

        // Calculate click-through rate (CTR)
        const ctr = metrics.clicks / metrics.reach * 100;

        // Calculate engagement per follower
        const engagementPerFollower = metrics.engagements / metrics.followers;

        // Create analysis object
        const analysis = {
            engagementRate: engagementRate.toFixed(2),
            ctr: ctr.toFixed(2),
            engagementPerFollower: engagementPerFollower.toFixed(2),
            metrics,
        };

        return analysis;
    } catch (error) {
        // Log and rethrow error
        console.error('Error analyzing social media engagement metrics:', error.message);
        throw error;
    }
}

// Example usage:
const metrics = {
    followers: 1000,
    reach: 5000,
    engagements: 200,
    clicks: 50,
};

const analysis = analyzeSocialMediaEngagement(metrics);
console.log('Social Media Engagement Analysis:');
console.log(`Engagement Rate: ${analysis.engagementRate}%`);
console.log(`CTR: ${analysis.ctr}%`);
console.log(`Engagement per Follower: ${analysis.engagementPerFollower}`);
```
