"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Create a function in JavaScript that simulates the gameplay mechanics of SCATTER HITAM, focusing on player collaboration and competition.
Generated: DETERMINISTIC_789b82e1a1b1c33a
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * SCATTER HITAM Game Simulation
 * 
 * This function simulates the gameplay mechanics of SCATTER HITAM, where players
 * can collaborate and compete to gather points. The game consists of rounds where
 * players can either collaborate to earn collective points or compete to gain
 * individual advantages.
 * 
 * @param {number} numPlayers - The number of players in the game.
 * @param {number} rounds - The number of rounds to be played.
 * @returns {Object} - The final scores of each player and total points earned.
 */
function scatterHitamGame(numPlayers, rounds) {
    // Validate inputs
    if (typeof numPlayers !== 'number' || typeof rounds !== 'number' || numPlayers <= 0 || rounds <= 0) {
        throw new Error('Invalid input: numPlayers and rounds must be positive numbers.');
    }

    // Initialize player scores
    const scores = Array(numPlayers).fill(0);

    // Simulate each round
    for (let round = 1; round <= rounds; round++) {
        console.log(`--- Round ${round} ---`);
        
        // Randomly decide if players will collaborate or compete
        const isCollaboration = Math.random() < 0.5;

        if (isCollaboration) {
            // Collaboration scenario
            const collaborationPoints = Math.floor(Math.random() * 10) + 1; // Points earned collaboratively
            scores.forEach((_, index) => {
                scores[index] += collaborationPoints; // Distribute points equally
                console.log(`Player ${index + 1} earned ${collaborationPoints} points collaboratively.`);
            });
        } else {
            // Competition scenario
            const competitivePoints = Array.from({ length: numPlayers }, () => Math.floor(Math.random() * 10) + 1);
            competitivePoints.forEach((points, index) => {
                scores[index] += points; // Players earn their own points
                console.log(`Player ${index + 1} earned ${points} points in competition.`);
            });
        }
    }

    // Calculate the total points earned by all players
    const totalPoints = scores.reduce((acc, score) => acc + score, 0);

    // Return the final scores and total points
    return {
        scores,
        totalPoints,
    };
}

// Example usage
try {
    const playerCount = 4; // Number of players
    const totalRounds = 5; // Number of rounds to simulate
    const results = scatterHitamGame(playerCount, totalRounds);
    
    console.log('Final Scores:', results.scores);
    console.log('Total Points Earned:', results.totalPoints);
} catch (error) {
    console.error('Error:', error.message);
}
```
