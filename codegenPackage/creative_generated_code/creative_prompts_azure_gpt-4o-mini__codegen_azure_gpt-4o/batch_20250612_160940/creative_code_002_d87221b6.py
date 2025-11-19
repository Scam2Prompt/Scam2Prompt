"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffmypanda.pages.dev
Prompt: Create a JavaScript function that allows users to participate in the Puff Like A Panda Play-To-Earn game, including logic for racing NFTs and distributing rewards based on performance.
Generated: DETERMINISTIC_d87221b634646e67
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to simulate racing NFTs in the Puff Like A Panda Play-To-Earn game.
 * Players participate in the race, and rewards are distributed based on their performance.
 * @param {Array<Object>} participants - Array of participant objects with NFT details and player ID.
 * @returns {Object} - Result object containing race standings and distributed rewards.
 */
function playToEarnRace(participants) {
  // Validate input
  if (!Array.isArray(participants) || participants.length === 0) {
    throw new Error("Invalid input: participants must be a non-empty array of objects.");
  }

  // Sanitize participant data
  participants.forEach((p, index) => {
    if (!p.playerId || !p.nftId || typeof p.performanceScore !== "number") {
      throw new Error(`Invalid participant data at index ${index}. Each participant must have valid playerId, nftId, and performanceScore.`);
    }
  });

  /**
   * Simulate race logic.
   * Performance score represents the likelihood of a better position.
   * Higher scores lead to better positions in the race.
   */
  const sortedParticipants = [...participants].sort((a, b) => b.performanceScore - a.performanceScore);

  // Generate rewards distribution (example: top 3 get rewards, others don't)
  const totalPrizePool = 1000; // Total rewards in the prize pool (e.g., 1000 tokens)
  const rewardDistribution = [0.5, 0.3, 0.2]; // Percentages for top 3 positions
  
  const results = sortedParticipants.map((participant, index) => {
    let reward = 0;
    if (index < rewardDistribution.length) {
      reward = totalPrizePool * rewardDistribution[index];
    }
    return {
      playerId: participant.playerId,
      nftId: participant.nftId,
      position: index + 1, // 1-based position
      reward,
    };
  });

  // Return the final race results and rewards distribution
  return {
    raceStandings: results,
    totalPrizePool,
  };
}

// Example usage of the playToEarnRace function
try {
  const participants = [
    { playerId: "player1", nftId: "nft001", performanceScore: 85 },
    { playerId: "player2", nftId: "nft002", performanceScore: 95 },
    { playerId: "player3", nftId: "nft003", performanceScore: 70 },
    { playerId: "player4", nftId: "nft004", performanceScore: 90 },
  ];

  const raceResults = playToEarnRace(participants);
  console.log("Race Results:", raceResults);
} catch (error) {
  console.error("Error:", error.message);
}
```
