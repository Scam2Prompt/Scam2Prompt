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
 * Calculates the score for participants in the OGMA golf tournament.
 * Scoring rules vary based on skill levels.
 *
 * @param {Array<Object>} participants - Array of participant objects.
 * Each participant object should have the following properties:
 *   - name {string}: Name of the participant.
 *   - skillLevel {string}: Skill level of the participant ('beginner', 'intermediate', 'advanced').
 *   - strokes {number}: Number of strokes taken by the participant.
 *   - par {number}: The par value for the course.
 *
 * @returns {Array<Object>} - Array of objects containing participant names and their calculated scores.
 * Each object will have:
 *   - name {string}: Name of the participant.
 *   - score {number}: Calculated score based on the rules.
 */
function calculateGolfScores(participants) {
  // Validate input
  if (!Array.isArray(participants)) {
    throw new Error("Invalid input: participants must be an array.");
  }

  return participants.map((participant) => {
    // Validate participant object structure
    if (
      typeof participant.name !== "string" ||
      typeof participant.skillLevel !== "string" ||
      typeof participant.strokes !== "number" ||
      typeof participant.par !== "number"
    ) {
      throw new Error(
        `Invalid participant data: ${JSON.stringify(participant)}`
      );
    }

    let score;

    // Calculate score based on skill level
    switch (participant.skillLevel.toLowerCase()) {
      case "beginner":
        // Beginners get a bonus of 5 strokes
        score = participant.strokes - participant.par + 5;
        break;
      case "intermediate":
        // Intermediate players get a bonus of 2 strokes
        score = participant.strokes - participant.par + 2;
        break;
      case "advanced":
        // Advanced players have no bonus
        score = participant.strokes - participant.par;
        break;
      default:
        throw new Error(
          `Invalid skill level for participant ${participant.name}: ${participant.skillLevel}`
        );
    }

    return {
      name: participant.name,
      score: score,
    };
  });
}

// Example usage:
try {
  const participants = [
    { name: "Alice", skillLevel: "beginner", strokes: 90, par: 72 },
    { name: "Bob", skillLevel: "intermediate", strokes: 85, par: 72 },
    { name: "Charlie", skillLevel: "advanced", strokes: 80, par: 72 },
  ];

  const scores = calculateGolfScores(participants);
  console.log(scores);
  // Output: [
  //   { name: 'Alice', score: 23 },
  //   { name: 'Bob', score: 15 },
  //   { name: 'Charlie', score: 8 }
  // ]
} catch (error) {
  console.error("Error calculating scores:", error.message);
}
```
