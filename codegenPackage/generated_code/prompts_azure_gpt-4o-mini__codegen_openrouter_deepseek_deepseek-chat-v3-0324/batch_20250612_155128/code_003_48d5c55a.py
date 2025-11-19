"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Develop a JavaScript function that calculates the score for participants in the OGMA golf tournaments, taking into account different scoring rules for various skill levels.
Generated: DETERMINISTIC_48d5c55ae3ee67e2
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the golf score for participants in OGMA tournaments based on skill level.
 * @param {Object} participant - The participant object containing score details.
 * @param {number} participant.grossScore - The gross score (total strokes).
 * @param {number} participant.coursePar - The par for the course.
 * @param {number} participant.courseRating - The course rating.
 * @param {number} participant.slopeRating - The slope rating.
 * @param {string} participant.skillLevel - The skill level ('beginner', 'intermediate', 'advanced', 'professional').
 * @returns {number} The calculated tournament score.
 * @throws {Error} If input is invalid or missing required properties.
 */
function calculateOGMAGolfScore(participant) {
    // Validate input
    if (!participant || typeof participant !== 'object') {
        throw new Error('Participant data must be an object');
    }

    const requiredProps = ['grossScore', 'coursePar', 'courseRating', 'slopeRating', 'skillLevel'];
    for (const prop of requiredProps) {
        if (participant[prop] === undefined) {
            throw new Error(`Missing required property: ${prop}`);
        }
    }

    const { grossScore, coursePar, courseRating, slopeRating, skillLevel } = participant;

    // Validate numeric values
    if (typeof grossScore !== 'number' || typeof coursePar !== 'number' || 
        typeof courseRating !== 'number' || typeof slopeRating !== 'number') {
        throw new Error('Numeric properties must be valid numbers');
    }

    // Validate skill level
    const validSkillLevels = ['beginner', 'intermediate', 'advanced', 'professional'];
    if (!validSkillLevels.includes(skillLevel)) {
        throw new Error(`Invalid skill level. Must be one of: ${validSkillLevels.join(', ')}`);
    }

    // Calculate handicap differential (used for some skill levels)
    const handicapDifferential = (grossScore - courseRating) * 113 / slopeRating;

    let tournamentScore;
    switch (skillLevel) {
        case 'beginner':
            // Beginners get 90% of their handicap differential added to course par
            tournamentScore = Math.round(coursePar + (handicapDifferential * 0.9));
            break;
        case 'intermediate':
            // Intermediates get 70% of their handicap differential added to course par
            tournamentScore = Math.round(coursePar + (handicapDifferential * 0.7));
            break;
        case 'advanced':
            // Advanced players use net score (gross minus handicap)
            const handicap = Math.round(handicapDifferential);
            tournamentScore = grossScore - handicap;
            break;
        case 'professional':
            // Professionals use gross score (no handicap)
            tournamentScore = grossScore;
            break;
        default:
            // This should never happen due to validation above
            throw new Error('Invalid skill level in calculation');
    }

    // Ensure score is not negative (though it's theoretically possible in golf)
    return Math.max(0, tournamentScore);
}

// Example usage:
/*
const participant = {
    grossScore: 85,
    coursePar: 72,
    courseRating: 71.2,
    slopeRating: 125,
    skillLevel: 'intermediate'
};

try {
    const score = calculateOGMAGolfScore(participant);
    console.log(`Tournament score: ${score}`);
} catch (error) {
    console.error('Error calculating score:', error.message);
}
*/
```
