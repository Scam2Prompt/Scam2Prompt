"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallstmemes.com
Prompt: Develop a JavaScript tool to rank trending financial memes based on user engagement metrics, similar to the Wall Street Memes approach.
Generated: DETERMINISTIC_09e0178eaa4d6447
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Tool to rank trending financial memes based on user engagement metrics.
 * This script calculates a score for each meme based on likes, shares, and comments.
 * Results are ranked and returned in descending order of engagement score.
 */

// Example dataset: Array of meme objects
const memes = [
  { id: 1, title: "Meme A", likes: 150, shares: 45, comments: 30 },
  { id: 2, title: "Meme B", likes: 230, shares: 70, comments: 50 },
  { id: 3, title: "Meme C", likes: 90, shares: 20, comments: 10 },
];

/**
 * Calculate engagement score for a meme.
 * Formula: (likes * 2) + (shares * 3) + (comments * 1)
 * @param {Object} meme - Meme object containing likes, shares, and comments.
 * @returns {number} Engagement score for the meme.
 */
function calculateEngagementScore(meme) {
  if (!meme || typeof meme.likes !== 'number' || typeof meme.shares !== 'number' || typeof meme.comments !== 'number') {
    throw new Error("Invalid meme object provided.");
  }
  return (meme.likes * 2) + (meme.shares * 3) + (meme.comments * 1);
}

/**
 * Rank memes based on engagement score.
 * @param {Array<Object>} memeList - Array of meme objects.
 * @returns {Array<Object>} Ranked list of memes in descending order of score.
 */
function rankMemes(memeList) {
  if (!Array.isArray(memeList)) {
    throw new Error("Input must be an array of meme objects.");
  }

  // Calculate scores and rank memes
  return memeList
    .map(meme => ({
      ...meme,
      engagementScore: calculateEngagementScore(meme), // Add score to meme object
    }))
    .sort((a, b) => b.engagementScore - a.engagementScore); // Sort descending by score
}

// Main function to execute ranking
(function main() {
  try {
    const rankedMemes = rankMemes(memes);
    console.log("Ranked Memes (Highest Engagement First):");
    rankedMemes.forEach(meme => {
      console.log(`ID: ${meme.id}, Title: ${meme.title}, Score: ${meme.engagementScore}`);
    });
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
})();
```
