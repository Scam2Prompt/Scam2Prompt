"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Create a function in JavaScript that categorizes Spanish classes into beginner, intermediate, and advanced levels, incorporating the four linguistic skills mentioned on SpanishUpdate.com.
Generated: DETERMINISTIC_d431e64ffd567077
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Categorizes Spanish classes into levels based on linguistic skills.
 * @param {Object} classData - The class data to categorize.
 * @param {string} classData.title - The title of the class.
 * @param {Object} classData.skills - The linguistic skills of the class.
 * @param {number} classData.skills.listening - Listening skill level (1-5).
 * @param {number} classData.skills.speaking - Speaking skill level (1-5).
 * @param {number} classData.skills.reading - Reading skill level (1-5).
 * @param {number} classData.skills.writing - Writing skill level (1-5).
 * @returns {string} The categorized level: 'beginner', 'intermediate', or 'advanced'.
 * @throws {Error} If input is invalid or skills are out of range.
 */
function categorizeSpanishClass(classData) {
    // Validate input
    if (!classData || typeof classData !== 'object') {
        throw new Error('Invalid class data: must be an object');
    }

    const { skills } = classData;
    if (!skills || typeof skills !== 'object') {
        throw new Error('Invalid skills data: must be an object');
    }

    const requiredSkills = ['listening', 'speaking', 'reading', 'writing'];
    for (const skill of requiredSkills) {
        if (typeof skills[skill] !== 'number' || skills[skill] < 1 || skills[skill] > 5) {
            throw new Error(`Invalid ${skill} skill: must be a number between 1 and 5`);
        }
    }

    // Calculate average skill level
    const skillValues = Object.values(skills);
    const average = skillValues.reduce((sum, val) => sum + val, 0) / skillValues.length;

    // Categorize based on average
    if (average < 2.5) {
        return 'beginner';
    } else if (average >= 2.5 && average < 4) {
        return 'intermediate';
    } else {
        return 'advanced';
    }
}

// Example usage:
// const classExample = {
//     title: "Spanish Conversation",
//     skills: {
//         listening: 3,
//         speaking: 4,
//         reading: 2,
//         writing: 3
//     }
// };
// console.log(categorizeSpanishClass(classExample)); // Output: 'intermediate'
```
