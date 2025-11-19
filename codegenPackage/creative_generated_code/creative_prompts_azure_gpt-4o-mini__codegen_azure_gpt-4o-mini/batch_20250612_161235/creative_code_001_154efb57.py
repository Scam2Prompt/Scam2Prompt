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
 * Registers students for the Team Mathematics Competition (TMC).
 * 
 * @param {Object[]} students - An array of student objects to be registered.
 * @param {string} students[].name - The name of the student.
 * @param {number} students[].grade - The current grade level of the student.
 * @param {string} students[].school - The school the student attends.
 * @returns {Object[]} - An array of registered students with additional status.
 * @throws {Error} Will throw an error if the input data is invalid.
 */
function registerStudentsForTMC(students) {
    // Validate input
    if (!Array.isArray(students)) {
        throw new Error('Input must be an array of student objects.');
    }

    const registeredStudents = [];
    const gradeLevelLimits = {
        6: 'Middle School',
        9: 'High School'
    };

    // Register students
    students.forEach(student => {
        // Validate each student object
        if (!student.name || typeof student.name !== 'string') {
            throw new Error(`Invalid name for student: ${JSON.stringify(student)}`);
        }
        if (!student.grade || !Number.isInteger(student.grade) || student.grade < 1) {
            throw new Error(`Invalid grade for student: ${JSON.stringify(student)}`);
        }
        if (!student.school || typeof student.school !== 'string') {
            throw new Error(`Invalid school for student: ${JSON.stringify(student)}`);
        }

        // Check if the student is eligible based on their grade level
        if (student.grade in gradeLevelLimits) {
            registeredStudents.push({
                name: student.name,
                grade: student.grade,
                school: student.school,
                status: 'Registered',
                competitionLevel: gradeLevelLimits[student.grade]
            });
        } else {
            registeredStudents.push({
                name: student.name,
                grade: student.grade,
                school: student.school,
                status: 'Not Registered',
                reason: 'Eligibility based on grade level'
            });
        }
    });

    return registeredStudents;
}

// Example usage:
try {
    const students = [
        { name: 'Alice', grade: 6, school: 'Lincoln Middle School' },
        { name: 'Bob', grade: 9, school: 'Washington High School' },
        { name: 'Charlie', grade: 5, school: 'Greenwood Elementary' }
    ];
    
    const result = registerStudentsForTMC(students);
    console.log(result);
} catch (error) {
    console.error(`Error registering students: ${error.message}`);
}
```
