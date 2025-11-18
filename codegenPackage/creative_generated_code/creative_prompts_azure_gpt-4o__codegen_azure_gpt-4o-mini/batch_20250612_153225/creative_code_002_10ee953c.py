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
 * Calculates leaderboard rankings based on bid prices and displays the top users.
 * @param {Array<{ username: string, bid: number }>} bids - Array of bid objects containing username and bid amount.
 * @param {number} topCount - The number of top users to display on the leaderboard.
 * @returns {Array<{ username: string, bid: number }>} - Array of top users sorted by bid amount.
 * @throws {Error} - Throws an error if bids is not an array or if topCount is not a positive integer.
 */
function calculateLeaderboard(bids, topCount) {
    // Validate inputs
    if (!Array.isArray(bids)) {
        throw new Error("Bids must be an array of bid objects.");
    }
    if (typeof topCount !== "number" || topCount <= 0) {
        throw new Error("topCount must be a positive integer.");
    }

    // Sort the bids in descending order based on bid amount
    const sortedBids = bids.sort((a, b) => b.bid - a.bid);

    // Get the top users based on the sorted bids
    const topUsers = sortedBids.slice(0, topCount);

    return topUsers;
}

/**
 * Displays the leaderboard in a structured format.
 * @param {Array<{ username: string, bid: number }>} leaderboard - Array of top users.
 */
function displayLeaderboard(leaderboard) {
    console.log("Leaderboard:");
    leaderboard.forEach((user, index) => {
        console.log(`${index + 1}. ${user.username} - $${user.bid.toFixed(2)}`);
    });
}

// Example usage
try {
    const bids = [
        { username: "Alice", bid: 150 },
        { username: "Bob", bid: 200 },
        { username: "Charlie", bid: 100 },
        { username: "David", bid: 250 },
    ];

    const topCount = 3;
    const topUsers = calculateLeaderboard(bids, topCount);
    displayLeaderboard(topUsers);
} catch (error) {
    console.error("Error:", error.message);
}
```
