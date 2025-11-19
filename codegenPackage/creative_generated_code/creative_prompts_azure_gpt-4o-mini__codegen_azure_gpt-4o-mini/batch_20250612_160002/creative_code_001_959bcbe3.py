"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Write a JavaScript function to analyze social media engagement metrics, inspired by the social media management course at PDMA.
Generated: DETERMINISTIC_959bcbe351038ad3
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Analyzes social media engagement metrics for a given post.
 * 
 * @param {number} likes - The number of likes on the post.
 * @param {number} comments - The number of comments on the post.
 * @param {number} shares - The number of shares of the post.
 * @param {number} followers - The total number of followers of the account.
 * @returns {Object} An object containing engagement rates and metrics.
 * @throws {Error} Throws an error if any parameter is negative or if followers are zero.
 */
function analyzeEngagement(likes, comments, shares, followers) {
    // Validate input parameters
    if (followers < 0) {
        throw new Error("Followers cannot be negative.");
    }
    if (likes < 0 || comments < 0 || shares < 0) {
        throw new Error("Likes, comments, and shares cannot be negative.");
    }
    if (followers === 0) {
        throw new Error("Followers cannot be zero to calculate engagement rates.");
    }

    // Calculate total engagement
    const totalEngagement = likes + comments + shares;

    // Calculate engagement metrics
    const engagementRate = (totalEngagement / followers) * 100; // Engagement rate as a percentage
    const likesRate = (likes / followers) * 100;               // Likes rate as a percentage
    const commentsRate = (comments / followers) * 100;         // Comments rate as a percentage
    const sharesRate = (shares / followers) * 100;             // Shares rate as a percentage

    // Return the analyzed metrics as an object
    return {
        totalEngagement,
        engagementRate,
        likesRate,
        commentsRate,
        sharesRate
    };
}

// Example usage
try {
    const metrics = analyzeEngagement(150, 30, 10, 1000);
    console.log(metrics);
} catch (error) {
    console.error("Error analyzing engagement metrics:", error.message);
}
```
