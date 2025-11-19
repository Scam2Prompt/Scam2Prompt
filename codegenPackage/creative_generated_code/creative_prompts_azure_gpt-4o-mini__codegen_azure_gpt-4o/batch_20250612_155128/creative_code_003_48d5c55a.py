"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ogma.ca
Prompt: Develop a JavaScript function that calculates the score for participants in the OGMA golf tournaments, taking into account different scoring rules for various skill levels.
Generated: DETERMINISTIC_48d5c55ae3ee67e2
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the score for participants in the OGMA golf tournament.
 * 
 * Scoring rules:
 * - Beginner: Par + Handicap
 * - Intermediate: Par + Handicap - 2
 * - Advanced: Par adjusted directly based on strokes
 * 
 * @param {number} par - The course's par score.
 * @param {number} strokes - The number of strokes taken by the participant.
 * @param {string} skillLevel - The skill level of the participant ("Beginner", "Intermediate", "Advanced").
 * @param {number} handicap - The participant's handicap score (only relevant for Beginner and Intermediate levels).
 * @returns {number} Final score of the participant.
 * @throws {Error} If invalid inputs are provided.
 */
function calculateGolfScore(par, strokes, skillLevel, handicap = 0) {
    // Validate input types
    if (typeof par !== 'number' || typeof strokes !== 'number' || typeof handicap !== 'number') {
        throw new Error('Invalid input: par, strokes, and handicap must be numbers.');
    }

    if (typeof skillLevel !== 'string') {
        throw new Error('Invalid input: skillLevel must be a string.');
    }
    
    // Validate skill level
    const validSkillLevels = ['Beginner', 'Intermediate', 'Advanced'];
    if (!validSkillLevels.includes(skillLevel)) {
        throw new Error(`Invalid skillLevel: must be one of ${validSkillLevels.join(', ')}`);
    }

    // Calculate score based on skill level
    let score;
    switch (skillLevel) {
        case 'Beginner':
            // Beginner scoring: Par + Handicap
            score = par + handicap;
            break;
        case 'Intermediate':
            // Intermediate scoring: Par + Handicap - 2
            score = par + handicap - 2;
            break;
        case 'Advanced':
            // Advanced scoring: Par adjusted directly by strokes
            score = strokes - par;
            break;
        default:
            // This should never be reached due to the earlier validation
            throw new Error('Unexpected error: Invalid skill level.');
    }

    return score;
}

// Example usage:
try {
    const par = 72;
    const strokes = 75;
    const skillLevel = 'Intermediate';
    const handicap = 10;

    const finalScore = calculateGolfScore(par, strokes, skillLevel, handicap);
    console.log(`The participant's final score is: ${finalScore}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
