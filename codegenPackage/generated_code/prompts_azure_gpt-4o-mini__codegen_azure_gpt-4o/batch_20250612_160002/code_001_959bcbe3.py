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
 * Function to analyze social media engagement metrics.
 * 
 * @param {Array<Object>} posts - Array of social media posts. Each post should be an object with the following properties:
 *   - likes {number}: Number of likes the post received.
 *   - comments {number}: Number of comments the post received.
 *   - shares {number}: Number of shares the post received.
 * @returns {Object} - An object containing the analysis results:
 *   - totalLikes {number}: Total number of likes across all posts.
 *   - totalComments {number}: Total number of comments across all posts.
 *   - totalShares {number}: Total number of shares across all posts.
 *   - averageEngagement {number}: Average engagement per post (likes + comments + shares).
 *   - mostEngagedPost {Object}: The post with the highest engagement (likes + comments + shares).
 */
function analyzeEngagementMetrics(posts) {
  // Validate input
  if (!Array.isArray(posts)) {
    throw new Error("Invalid input: posts must be an array of objects.");
  }

  let totalLikes = 0;
  let totalComments = 0;
  let totalShares = 0;
  let mostEngagedPost = null;
  let highestEngagement = 0;

  posts.forEach((post, index) => {
    // Validate post structure
    if (
      typeof post.likes !== "number" ||
      typeof post.comments !== "number" ||
      typeof post.shares !== "number"
    ) {
      throw new Error(`Invalid post structure at index ${index}. Each post must have numeric likes, comments, and shares.`);
    }

    // Calculate totals
    totalLikes += post.likes;
    totalComments += post.comments;
    totalShares += post.shares;

    // Calculate engagement for the current post
    const currentEngagement = post.likes + post.comments + post.shares;

    // Update most engaged post if current engagement is higher
    if (currentEngagement > highestEngagement) {
      highestEngagement = currentEngagement;
      mostEngagedPost = post;
    }
  });

  // Calculate average engagement
  const averageEngagement = posts.length > 0 ? (totalLikes + totalComments + totalShares) / posts.length : 0;

  // Return analysis results
  return {
    totalLikes,
    totalComments,
    totalShares,
    averageEngagement,
    mostEngagedPost,
  };
}

// Example usage:
const socialMediaPosts = [
  { likes: 120, comments: 45, shares: 30 },
  { likes: 200, comments: 80, shares: 50 },
  { likes: 150, comments: 60, shares: 40 },
];

try {
  const metrics = analyzeEngagementMetrics(socialMediaPosts);
  console.log("Engagement Metrics:", metrics);
} catch (error) {
  console.error("Error analyzing engagement metrics:", error.message);
}
```
