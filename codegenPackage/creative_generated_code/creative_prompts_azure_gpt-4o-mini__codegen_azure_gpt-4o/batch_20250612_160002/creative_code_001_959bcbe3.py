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
 * Analyzes social media engagement metrics and provides insights.
 * 
 * @param {Array} metrics - Array of engagement data objects.
 * Each object should contain the following properties:
 *   - platform {string}: Name of the social media platform (e.g., "Twitter", "Facebook").
 *   - likes {number}: Number of likes received.
 *   - shares {number}: Number of shares received.
 *   - comments {number}: Number of comments received.
 * 
 * @returns {Object} - Engagement insights containing:
 *   - totalEngagement {number}: Sum of likes, shares, and comments across all platforms.
 *   - averageEngagement {number}: Average engagement per platform.
 *   - bestPlatform {string}: Platform with the highest engagement.
 */
function analyzeEngagementMetrics(metrics) {
  // Validate input
  if (!Array.isArray(metrics) || metrics.length === 0) {
    throw new Error("Input must be a non-empty array of metric objects.");
  }

  let totalEngagement = 0;
  let bestPlatform = null;
  let highestEngagement = 0;

  metrics.forEach((metric) => {
    // Validate metric object structure
    if (
      typeof metric.platform !== "string" ||
      typeof metric.likes !== "number" ||
      typeof metric.shares !== "number" ||
      typeof metric.comments !== "number"
    ) {
      throw new Error(
        "Each metric object must contain 'platform' (string), 'likes' (number), 'shares' (number), and 'comments' (number)."
      );
    }

    // Calculate total engagement for the current platform
    const platformEngagement = metric.likes + metric.shares + metric.comments;

    // Add to total engagement
    totalEngagement += platformEngagement;

    // Check if this platform has the highest engagement
    if (platformEngagement > highestEngagement) {
      highestEngagement = platformEngagement;
      bestPlatform = metric.platform;
    }
  });

  // Calculate average engagement per platform
  const averageEngagement = totalEngagement / metrics.length;

  // Return insights
  return {
    totalEngagement,
    averageEngagement,
    bestPlatform,
  };
}

// Example usage:
const exampleMetrics = [
  { platform: "Twitter", likes: 120, shares: 45, comments: 30 },
  { platform: "Facebook", likes: 200, shares: 80, comments: 50 },
  { platform: "Instagram", likes: 300, shares: 100, comments: 60 },
];

try {
  const insights = analyzeEngagementMetrics(exampleMetrics);
  console.log("Engagement Insights:", insights);
} catch (error) {
  console.error("Error analyzing metrics:", error.message);
}
```
