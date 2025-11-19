"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fijimaths.com
Prompt: Write a JavaScript function to register students for the Team Mathematics Competition (TMC) based on their current grade level and school.
Generated: DETERMINISTIC_154efb57e655c93d
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to register students for the Team Mathematics Competition (TMC).
 * Validates student information such as name, grade level, and school.
 * If valid, registers the student and returns a confirmation message.
 * 
 * @param {Object} student - An object containing student details.
 * @param {string} student.name - The name of the student.
 * @param {number} student.grade - The grade level of the student (must be between 6 and 12).
 * @param {string} student.school - The name of the school the student belongs to.
 * @returns {string} - Confirmation message of registration or error message.
 */
function registerStudentForTMC(student) {
    // Validate input type to ensure student is an object
    if (typeof student !== 'object' || student === null) {
        throw new Error("Invalid input: student details should be an object.");
    }

    const { name, grade, school } = student;

    // Validate name
    if (typeof name !== 'string' || name.trim() === '') {
        throw new Error("Invalid input: student name must be a non-empty string.");
    }

    // Validate grade level
    if (typeof grade !== 'number' || grade < 6 || grade > 12) {
        throw new Error("Invalid input: grade level must be a number between 6 and 12.");
    }

    // Validate school name
    if (typeof school !== 'string' || school.trim() === '') {
        throw new Error("Invalid input: school name must be a non-empty string.");
    }

    // Registration logic (simulated here with a confirmation message)
    const confirmationMessage = `Student ${name} from ${school} (Grade ${grade}) has been successfully registered for the Team Mathematics Competition.`;
    
    return confirmationMessage;
}

// Example usage:
try {
    const student = {
        name: "Alice Johnson",
        grade: 10,
        school: "Springfield High School"
    };
    console.log(registerStudentForTMC(student)); // Should print the confirmation message
} catch (error) {
    console.error(error.message); // Error handling for invalid input
}
```
