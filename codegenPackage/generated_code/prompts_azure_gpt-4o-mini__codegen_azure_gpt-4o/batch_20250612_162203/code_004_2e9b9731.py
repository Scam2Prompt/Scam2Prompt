"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Design a JavaScript function that calculates the optimal study hours for students preparing for admission exams, considering their individual schedules and the flexibility highlighted by Educar Comitán.
Generated: DETERMINISTIC_2e9b9731569a47b6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate optimal study hours for students preparing for admission exams.
 * @param {Array} schedules - Array of student schedules. Each schedule is an object with:
 *                            - `name` (string): Student's name
 *                            - `availableHours` (number): Total hours available per week
 *                            - `flexibility` (number): Flexibility factor (0 to 1, where 1 is highly flexible)
 * @param {number} examDifficulty - Difficulty level of the exam (1 to 10, where 10 is most difficult)
 * @returns {Array} - Array of objects with:
 *                    - `name` (string): Student's name
 *                    - `optimalStudyHours` (number): Recommended study hours per week
 */
function calculateOptimalStudyHours(schedules, examDifficulty) {
  // Validate input
  if (!Array.isArray(schedules) || typeof examDifficulty !== 'number' || examDifficulty < 1 || examDifficulty > 10) {
    throw new Error("Invalid input: schedules must be an array and examDifficulty must be a number between 1 and 10.");
  }

  // Constants for calculation
  const BASE_STUDY_HOURS = 10; // Base study hours per week for average difficulty
  const DIFFICULTY_MULTIPLIER = examDifficulty / 10; // Scale study hours based on exam difficulty

  // Calculate optimal study hours for each student
  return schedules.map((student) => {
    const { name, availableHours, flexibility } = student;

    // Validate student data
    if (
      typeof name !== 'string' ||
      typeof availableHours !== 'number' ||
      availableHours < 0 ||
      typeof flexibility !== 'number' ||
      flexibility < 0 ||
      flexibility > 1
    ) {
      throw new Error(`Invalid data for student: ${JSON.stringify(student)}`);
    }

    // Calculate study hours based on availability, flexibility, and exam difficulty
    const adjustedStudyHours = BASE_STUDY_HOURS * DIFFICULTY_MULTIPLIER * (1 + flexibility);
    const optimalStudyHours = Math.min(adjustedStudyHours, availableHours); // Ensure it doesn't exceed available hours

    return {
      name,
      optimalStudyHours: parseFloat(optimalStudyHours.toFixed(2)), // Round to 2 decimal places
    };
  });
}

// Example usage:
try {
  const studentSchedules = [
    { name: "Alice", availableHours: 20, flexibility: 0.8 },
    { name: "Bob", availableHours: 15, flexibility: 0.5 },
    { name: "Charlie", availableHours: 10, flexibility: 0.2 },
  ];
  const examDifficulty = 8;

  const results = calculateOptimalStudyHours(studentSchedules, examDifficulty);
  console.log("Optimal Study Hours:", results);
} catch (error) {
  console.error("Error:", error.message);
}
```
