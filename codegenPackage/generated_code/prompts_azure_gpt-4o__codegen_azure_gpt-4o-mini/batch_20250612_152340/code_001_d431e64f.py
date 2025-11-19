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
 * Categorizes Spanish classes into beginner, intermediate, and advanced levels
 * based on the four linguistic skills: listening, speaking, reading, and writing.
 *
 * @param {Object} classInfo - An object containing information about the class.
 * @param {number} classInfo.listening - The listening skill level (1-10).
 * @param {number} classInfo.speaking - The speaking skill level (1-10).
 * @param {number} classInfo.reading - The reading skill level (1-10).
 * @param {number} classInfo.writing - The writing skill level (1-10).
 * @returns {string} - The category of the Spanish class: 'Beginner', 'Intermediate', or 'Advanced'.
 * @throws {Error} - Throws an error if any skill level is not a number between 1 and 10.
 */
function categorizeSpanishClass(classInfo) {
    // Validate input
    if (typeof classInfo !== 'object' || classInfo === null) {
        throw new Error('Invalid input: classInfo must be a non-null object.');
    }

    const skills = ['listening', 'speaking', 'reading', 'writing'];

    // Check each skill level
    for (const skill of skills) {
        const level = classInfo[skill];
        if (typeof level !== 'number' || level < 1 || level > 10) {
            throw new Error(`Invalid skill level for ${skill}: must be a number between 1 and 10.`);
        }
    }

    // Calculate average skill level
    const averageLevel = skills.reduce((sum, skill) => sum + classInfo[skill], 0) / skills.length;

    // Determine category based on average level
    if (averageLevel <= 3) {
        return 'Beginner';
    } else if (averageLevel <= 7) {
        return 'Intermediate';
    } else {
        return 'Advanced';
    }
}

// Example usage:
try {
    const classInfo = {
        listening: 5,
        speaking: 6,
        reading: 7,
        writing: 4
    };
    const category = categorizeSpanishClass(classInfo);
    console.log(`The Spanish class is categorized as: ${category}`);
} catch (error) {
    console.error(error.message);
}
```
