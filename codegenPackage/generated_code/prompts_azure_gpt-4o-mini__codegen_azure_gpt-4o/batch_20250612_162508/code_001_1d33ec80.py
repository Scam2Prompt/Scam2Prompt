"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Write a JavaScript function that tracks the progress of athletes in a mentorship program, incorporating elements of discipline and character building as emphasized by Team DGA.
Generated: DETERMINISTIC_1d33ec80196c5997
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to track the progress of athletes in a mentorship program.
 * The program emphasizes discipline and character building as core values.
 * 
 * @param {Array} athletes - Array of athlete objects. Each object should have:
 *                           - name: String (Athlete's name)
 *                           - disciplineScore: Number (Score for discipline, 0-100)
 *                           - characterScore: Number (Score for character building, 0-100)
 *                           - progress: Number (Overall progress percentage, 0-100)
 * @param {Object} updates - Object containing updates for athletes. Example:
 *                           {
 *                             "John Doe": { disciplineScore: 10, characterScore: 5 },
 *                             "Jane Smith": { disciplineScore: 15, characterScore: 10 }
 *                           }
 * @returns {Array} Updated array of athlete objects with recalculated progress.
 */
function trackAthleteProgress(athletes, updates) {
  // Validate input
  if (!Array.isArray(athletes)) {
    throw new Error("Invalid input: athletes must be an array.");
  }
  if (typeof updates !== "object" || updates === null) {
    throw new Error("Invalid input: updates must be an object.");
  }

  // Helper function to calculate progress based on discipline and character scores
  const calculateProgress = (disciplineScore, characterScore) => {
    // Weight discipline and character equally (50% each)
    return Math.min(100, Math.round((disciplineScore * 0.5) + (characterScore * 0.5)));
  };

  // Iterate through athletes and apply updates
  return athletes.map((athlete) => {
    const { name, disciplineScore, characterScore, progress } = athlete;

    // Ensure athlete object has required properties
    if (
      typeof name !== "string" ||
      typeof disciplineScore !== "number" ||
      typeof characterScore !== "number" ||
      typeof progress !== "number"
    ) {
      throw new Error(`Invalid athlete object: ${JSON.stringify(athlete)}`);
    }

    // Check if updates exist for the current athlete
    const update = updates[name];
    if (update) {
      // Apply updates to discipline and character scores
      const updatedDisciplineScore = Math.min(100, disciplineScore + (update.disciplineScore || 0));
      const updatedCharacterScore = Math.min(100, characterScore + (update.characterScore || 0));

      // Recalculate progress
      const updatedProgress = calculateProgress(updatedDisciplineScore, updatedCharacterScore);

      // Return updated athlete object
      return {
        ...athlete,
        disciplineScore: updatedDisciplineScore,
        characterScore: updatedCharacterScore,
        progress: updatedProgress,
      };
    }

    // If no updates, return athlete object as is
    return athlete;
  });
}

// Example usage:
const athletes = [
  { name: "John Doe", disciplineScore: 80, characterScore: 70, progress: 75 },
  { name: "Jane Smith", disciplineScore: 60, characterScore: 65, progress: 62.5 },
];

const updates = {
  "John Doe": { disciplineScore: 10, characterScore: 5 },
  "Jane Smith": { disciplineScore: 15, characterScore: 10 },
};

try {
  const updatedAthletes = trackAthleteProgress(athletes, updates);
  console.log(updatedAthletes);
} catch (error) {
  console.error("Error:", error.message);
}
```
