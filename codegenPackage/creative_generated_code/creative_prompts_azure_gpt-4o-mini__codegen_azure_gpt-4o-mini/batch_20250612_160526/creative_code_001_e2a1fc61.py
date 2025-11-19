"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solitairenetwork.com
Prompt: Write a JavaScript function to implement the scoring system for Mahjong games as described on Solitaire Network, including tile matching logic.
Generated: DETERMINISTIC_e2a1fc61d859f26d
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Mahjong Scoring System
 * This function computes the score based on the tile matching logic for Mahjong.
 * 
 * @param {Array} matchedTiles - Array of matched tile objects with properties: type and value
 * @returns {number} - Total score calculated based on the matched tiles
 * @throws {Error} - Throws an error if the input is invalid
 */

function calculateMahjongScore(matchedTiles) {
    // Validate input
    if (!Array.isArray(matchedTiles)) {
        throw new Error("Input must be an array of matched tiles.");
    }

    // Initialize score
    let totalScore = 0;

    // Scoring rules for different tile types
    const scoringRules = {
        bamboo: 2,
        character: 3,
        dot: 4,
        honor: 5 // Honor tiles have higher score
    };

    // Iterate over matched tiles to calculate score
    matchedTiles.forEach(tile => {
        // Validate tile structure
        if (!tile || typeof tile.type !== 'string' || typeof tile.value !== 'number') {
            throw new Error("Each tile must have a type (string) and value (number).");
        }

        const { type, value } = tile;

        // Check if the tile type has a defined scoring rule
        if (scoringRules[type]) {
            totalScore += scoringRules[type] * value;
        } else {
            throw new Error(`Unknown tile type: ${type}`);
        }
    });

    return totalScore;
}

// Example usage
try {
    const matchedTiles = [
        { type: 'bamboo', value: 2 },
        { type: 'character', value: 3 },
        { type: 'dot', value: 1 },
        { type: 'honor', value: 1 }
    ];
    
    const score = calculateMahjongScore(matchedTiles);
    console.log(`Total Mahjong Score: ${score}`);
} catch (error) {
    console.error(error.message);
}
```
