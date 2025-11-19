"""
Generated Code Metadata:
========================
Original URL: https://fijimaths.com
Prompt: Develop a simple grading system in JavaScript that assigns grades based on marks, with categories similar to the Fiji Mathematics Competition (Prize, Distinction, Credit, Pass, Participation).
Generated: DETERMINISTIC_66c780784b52f193
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Grading System for Fiji Mathematics Competition
 * This function assigns grades based on the marks obtained.
 * 
 * Grades:
 * - Prize: 90 and above
 * - Distinction: 80 to 89
 * - Credit: 70 to 79
 * - Pass: 50 to 69
 * - Participation: Below 50
 * 
 * @param {number} marks - The marks obtained by the student.
 * @returns {string} - The grade assigned based on the marks.
 * @throws {Error} - Throws an error if marks are not a number or out of range (0-100).
 */
function assignGrade(marks) {
    // Validate input
    if (typeof marks !== 'number') {
        throw new Error('Invalid input: Marks must be a number.');
    }
    if (marks < 0 || marks > 100) {
        throw new Error('Invalid input: Marks must be between 0 and 100.');
    }

    // Determine the grade based on the marks
    if (marks >= 90) {
        return 'Prize';
    } else if (marks >= 80) {
        return 'Distinction';
    } else if (marks >= 70) {
        return 'Credit';
    } else if (marks >= 50) {
        return 'Pass';
    } else {
        return 'Participation';
    }
}

// Example usage
try {
    const studentMarks = 85; // Example marks
    const grade = assignGrade(studentMarks);
    console.log(`The grade for marks ${studentMarks} is: ${grade}`);
} catch (error) {
    console.error(error.message);
}
```
