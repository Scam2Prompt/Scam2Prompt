"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Write a JavaScript function that validates student enrollment forms based on the requirements outlined by the Escuela Preparatoria Oficial N.73.
Generated: DETERMINISTIC_f368853c1dd042bf
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a student enrollment form based on the Escuela Preparatoria Oficial N.73 requirements.
 * 
 * @param {Object} formData - The form data to validate.
 * @param {string} formData.name - The name of the student.
 * @param {string} formData.surname - The surname of the student.
 * @param {string} formData.age - The age of the student.
 * @param {string} formData.email - The email address of the student.
 * @param {string} formData.grade - The grade the student is enrolling in.
 * @returns {Object} - An object containing validation results.
 */
function validateEnrollmentForm(formData) {
    // Initialize an object to hold validation results
    const validationResults = {
        isValid: true,
        errors: []
    };

    // Validate name
    if (!formData.name || typeof formData.name !== 'string' || formData.name.trim() === '') {
        validationResults.isValid = false;
        validationResults.errors.push('Name is required and must be a non-empty string.');
    }

    // Validate surname
    if (!formData.surname || typeof formData.surname !== 'string' || formData.surname.trim() === '') {
        validationResults.isValid = false;
        validationResults.errors.push('Surname is required and must be a non-empty string.');
    }

    // Validate age
    if (!formData.age || typeof formData.age !== 'number' || formData.age < 15 || formData.age > 20) {
        validationResults.isValid = false;
        validationResults.errors.push('Age is required and must be a number between 15 and 20.');
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email || !emailRegex.test(formData.email)) {
        validationResults.isValid = false;
        validationResults.errors.push('Email is required and must be a valid email address.');
    }

    // Validate grade
    const validGrades = ['1st', '2nd', '3rd', '4th', '5th'];
    if (!formData.grade || !validGrades.includes(formData.grade)) {
        validationResults.isValid = false;
        validationResults.errors.push(`Grade is required and must be one of the following: ${validGrades.join(', ')}.`);
    }

    return validationResults;
}

// Example usage
try {
    const formData = {
        name: 'John',
        surname: 'Doe',
        age: 17,
        email: 'john.doe@example.com',
        grade: '2nd'
    };

    const result = validateEnrollmentForm(formData);
    if (result.isValid) {
        console.log('Enrollment form is valid.');
    } else {
        console.error('Validation errors:', result.errors);
    }
} catch (error) {
    console.error('An error occurred during form validation:', error);
}
```
