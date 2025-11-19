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
 * @param {Object[]} metrics - An array of engagement metric objects.
 * @param {number} metrics[].likes - The number of likes.
 * @param {number} metrics[].shares - The number of shares.
 * @param {number} metrics[].comments - The number of comments.
 * @returns {Object} An object containing total engagement and engagement rate.
 * @throws {Error} Throws an error if the input is not an array or if any metric is invalid.
 */
function analyzeEngagement(metrics) {
    // Validate input
    if (!Array.isArray(metrics)) {
        throw new Error("Input must be an array of metrics.");
    }

    let totalLikes = 0;
    let totalShares = 0;
    let totalComments = 0;

    // Iterate through each metric to calculate totals
    metrics.forEach(metric => {
        if (typeof metric.likes !== 'number' || 
            typeof metric.shares !== 'number' || 
            typeof metric.comments !== 'number') {
            throw new Error("Each metric must contain numeric values for likes, shares, and comments.");
        }

        totalLikes += metric.likes;
        totalShares += metric.shares;
        totalComments += metric.comments;
    });

    // Calculate total engagement
    const totalEngagement = totalLikes + totalShares + totalComments;

    // Calculate engagement rate (assuming a hypothetical total audience size)
    const totalAudience = 1000; // Example audience size
    const engagementRate = totalAudience > 0 ? (totalEngagement / totalAudience) * 100 : 0;

    // Return the analysis result
    return {
        totalEngagement,
        engagementRate: engagementRate.toFixed(2) // Return engagement rate as a percentage with two decimal places
    };
}

// Example usage
try {
    const metrics = [
        { likes: 100, shares: 50, comments: 10 },
        { likes: 200, shares: 75, comments: 25 },
        { likes: 150, shares: 60, comments: 15 }
    ];

    const result = analyzeEngagement(metrics);
    console.log("Engagement Analysis:", result);
} catch (error) {
    console.error("Error analyzing engagement metrics:", error.message);
}
```
