"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auction-gomble.pages.dev
Prompt: Develop a function in JavaScript to calculate the leaderboard rankings for the GOMBLE Auction based on bid prices and display the top users as shown on the leaderboard.
Generated: DETERMINISTIC_10ee953c6954e56d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate leaderboard rankings for the GOMBLE Auction
 * based on bid prices and display the top users.
 * 
 * @param {Array<Object>} bids - Array of bid objects with structure:
 *                               { userId: string, bidPrice: number }
 * @param {number} topN - Number of top users to display on the leaderboard.
 * @returns {Array<Object>} - Array of top users sorted by bidPrice in descending order.
 */
function calculateLeaderboard(bids, topN) {
  // Input validation
  if (!Array.isArray(bids)) {
    throw new Error("Invalid input: bids must be an array of objects.");
  }

  if (typeof topN !== "number" || topN < 1) {
    throw new Error("Invalid input: topN must be a positive number.");
  }

  // Validate bid objects
  bids.forEach((bid) => {
    if (
      typeof bid.userId !== "string" ||
      typeof bid.bidPrice !== "number" ||
      bid.bidPrice < 0
    ) {
      throw new Error("Invalid bid object format.");
    }
  });

  // Sort bids by bidPrice in descending order
  const sortedBids = bids.sort((a, b) => b.bidPrice - a.bidPrice);

  // Limit to topN users
  const leaderboard = sortedBids.slice(0, topN);

  // Prepare the leaderboard data
  const formattedLeaderboard = leaderboard.map((entry, index) => ({
    rank: index + 1,
    userId: entry.userId,
    bidPrice: entry.bidPrice,
  }));

  return formattedLeaderboard;
}

// Example usage
try {
  const bids = [
    { userId: "user1", bidPrice: 250 },
    { userId: "user2", bidPrice: 500 },
    { userId: "user3", bidPrice: 300 },
    { userId: "user4", bidPrice: 450 },
  ];
  
  const topN = 3;

  const leaderboard = calculateLeaderboard(bids, topN);
  console.log("Leaderboard:", leaderboard);
} catch (error) {
  console.error("Error:", error.message);
}
```
