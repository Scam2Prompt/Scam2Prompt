"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Create a function in JavaScript that categorizes Spanish classes into beginner, intermediate, and advanced levels, incorporating the four linguistic skills mentioned on SpanishUpdate.com.
Generated: DETERMINISTIC_d431e64ffd567077
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Categorizes Spanish classes into beginner, intermediate, and advanced levels
 * based on linguistic skills (reading, writing, speaking, listening).
 *
 * @param {Object} classInfo - Information about the Spanish class.
 * @param {number} classInfo.reading - Reading skill level (1 to 10).
 * @param {number} classInfo.writing - Writing skill level (1 to 10).
 * @param {number} classInfo.speaking - Speaking skill level (1 to 10).
 * @param {number} classInfo.listening - Listening skill level (1 to 10).
 * @returns {string} - The level of the class ('Beginner', 'Intermediate', 'Advanced').
 * @throws {Error} - Throws an error if input data is invalid.
 */
function categorizeSpanishClass(classInfo) {
  // Validate input
  if (
    !classInfo ||
    typeof classInfo.reading !== 'number' ||
    typeof classInfo.writing !== 'number' ||
    typeof classInfo.speaking !== 'number' ||
    typeof classInfo.listening !== 'number'
  ) {
    throw new Error('Invalid input: classInfo must contain numerical values for reading, writing, speaking, and listening.');
  }

  // Ensure skill levels are within the range of 1 to 10
  const skills = [classInfo.reading, classInfo.writing, classInfo.speaking, classInfo.listening];
  if (!skills.every(skill => skill >= 1 && skill <= 10)) {
    throw new Error('Invalid input: skill levels must be between 1 and 10.');
  }

  // Calculate the average skill level
  const averageSkillLevel = skills.reduce((sum, skill) => sum + skill, 0) / skills.length;

  // Determine class level based on average skill level
  if (averageSkillLevel <= 4) {
    return 'Beginner';
  } else if (averageSkillLevel <= 7) {
    return 'Intermediate';
  } else {
    return 'Advanced';
  }
}

// Example usage
try {
  const classLevel = categorizeSpanishClass({
    reading: 6,
    writing: 7,
    speaking: 8,
    listening: 7
  });
  console.log(`Class Level: ${classLevel}`); // Output: Class Level: Intermediate
} catch (error) {
  console.error(error.message);
}
```
