"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teamdga.com
Prompt: Write a JavaScript function that tracks the progress of athletes in a mentorship program, incorporating elements of discipline and character building as emphasized by Team DGA.
Generated: DETERMINISTIC_1d33ec80196c5997
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to track the progress of athletes in a mentorship program.
 * @param {Array<Object>} athletes - Array of athlete objects, each containing name, discipline, and character score.
 * @param {Object} performanceUpdate - Object containing updates to the scores: { name: string, disciplineIncrement: number, characterIncrement: number }.
 * @returns {Array<Object>} Updated list of athlete objects with their scores.
 */
function trackAthleteProgress(athletes, performanceUpdate) {
  // Validate input types
  if (!Array.isArray(athletes) || typeof performanceUpdate !== 'object') {
    throw new TypeError('Invalid input: athletes must be an array and performanceUpdate must be an object.');
  }

  // Validate performanceUpdate properties
  if (
    typeof performanceUpdate.name !== 'string' ||
    typeof performanceUpdate.disciplineIncrement !== 'number' ||
    typeof performanceUpdate.characterIncrement !== 'number'
  ) {
    throw new TypeError('Invalid performanceUpdate object format.');
  }

  // Update athlete scores
  const updatedAthletes = athletes.map((athlete) => {
    if (athlete.name === performanceUpdate.name) {
      return {
        ...athlete,
        discipline: Math.max(0, athlete.discipline + performanceUpdate.disciplineIncrement), // Ensure non-negative discipline score
        character: Math.max(0, athlete.character + performanceUpdate.characterIncrement), // Ensure non-negative character score
      };
    }
    return athlete; // Return unchanged athlete if no match
  });

  return updatedAthletes;
}

// --- Example Usage ---

// List of athletes in the mentorship program
const athletes = [
  { name: "John Doe", discipline: 75, character: 80 },
  { name: "Jane Smith", discipline: 85, character: 90 },
  { name: "Mike Johnson", discipline: 60, character: 70 },
];

// Performance update for an athlete
const performanceUpdate = {
  name: "Jane Smith",
  disciplineIncrement: 5,
  characterIncrement: -10,
};

// Track progress
try {
  const updatedAthletes = trackAthleteProgress(athletes, performanceUpdate);
  console.log("Updated Athlete Progress:", updatedAthletes);
} catch (error) {
  console.error("Error tracking progress:", error.message);
}
```
