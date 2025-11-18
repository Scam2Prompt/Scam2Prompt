"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balloon-gomble-io.pages.dev
Prompt: Write JavaScript code for a game where balloons are lifted by heating them, and players collect "Mystery Marbles" as rewards.
Generated: DETERMINISTIC_d85c30401230f6b1
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Balloon Heating and Mystery Marble Game
// Author: [Your Name]
// Version: 1.0.0
// Description: A simple game where players heat balloons to make them rise and collect Mystery Marbles as rewards.

// Constants and configurations
const BALLOON_HEAT_INCREMENT = 10; // Heat increment per interaction
const MAX_BALLOON_HEAT = 100; // Maximum heat level for balloons to rise
const MYSTERY_MARBLE_COLLECT_THRESHOLD = 2; // Number of balloons required to collect a marble

// Game Variables
let balloonHeatLevels = {}; // Tracks heat level of each balloon
let playerScore = 0; // Tracks player's score
let collectedMarbles = 0; // Tracks number of Mystery Marbles collected

// Function to heat a balloon
function heatBalloon(balloonId) {
    // Initialize heat level if balloonId is new
    if (!balloonHeatLevels[balloonId]) {
        balloonHeatLevels[balloonId] = 0;
    }

    // Increase heat level
    balloonHeatLevels[balloonId] += BALLOON_HEAT_INCREMENT;

    // Check if balloon rises
    if (balloonHeatLevels[balloonId] >= MAX_BALLOON_HEAT) {
        console.log(`Balloon ${balloonId} has risen!`);
        playerScore++;
        balloonHeatLevels[balloonId] = 0; // Reset heat level for the balloon

        // Check if player earned a Mystery Marble
        if (playerScore % MYSTERY_MARBLE_COLLECT_THRESHOLD === 0) {
            collectedMarbles++;
            console.log('You have collected a Mystery Marble!');
        }
    } else {
        console.log(`Balloon ${balloonId} heat level: ${balloonHeatLevels[balloonId]}`);
    }
}

// Function to display player stats
function displayStats() {
    console.log('Player Stats:');
    console.log(`Score: ${playerScore}`);
    console.log(`Mystery Marbles Collected: ${collectedMarbles}`);
}

// Error handling for invalid inputs
function validateInput(balloonId) {
    if (typeof balloonId !== 'string' || balloonId.trim() === '') {
        throw new Error('Invalid balloon ID. Please provide a non-empty string.');
    }
}

// Game loop (example usage)
try {
    heatBalloon('balloon1'); // Heat balloon1
    heatBalloon('balloon2'); // Heat balloon2
    heatBalloon('balloon1'); // Heat balloon1 further
    heatBalloon('balloon1'); // Heat balloon1 to make it rise
    heatBalloon('balloon2'); // Heat balloon2 further
    heatBalloon('balloon2'); // Heat balloon2 further to make it rise

    displayStats(); // Show player stats
} catch (error) {
    console.error(`Error: ${error.message}`);
}

// Export module for testing or extension
module.exports = {
    heatBalloon,
    displayStats,
    BALLOON_HEAT_INCREMENT,
    MAX_BALLOON_HEAT,
    MYSTERY_MARBLE_COLLECT_THRESHOLD,
};
```
