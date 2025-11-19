"""
Generated Code Metadata:
========================
Original URL: https://cpncg.edu.mx
Prompt: Write a JavaScript function that validates user input for a school registration form, inspired by the Colegio Panamericano's enrollment process.
Generated: DETERMINISTIC_adf65f12f7ac3117
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a school registration form.
 * 
 * @param {Object} formData - The user input data.
 * @param {string} formData.firstName - The student's first name.
 * @param {string} formData.lastName - The student's last name.
 * @param {string} formData.email - The student's email address.
 * @param {string} formData.dateOfBirth - The student's date of birth (YYYY-MM-DD).
 * @param {string} formData.gradeLevel - The student's grade level.
 * @returns {Object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */

function validateRegistrationForm(formData) {
    const errors = [];
    let isValid = true;

    // Check if formData is an object
    if (typeof formData !== 'object' || formData === null) {
        throw new Error('Form data must be an object');
    }

    // First name validation
    if (!formData.firstName || typeof formData.firstName !== 'string' || formData.firstName.trim().length === 0) {
        errors.push('First name is required');
        isValid = false;
    } else if (formData.firstName.trim().length < 2 || formData.firstName.trim().length > 50) {
        errors.push('First name must be between 2 and 50 characters');
        isValid = false;
    }

    // Last name validation
    if (!formData.lastName || typeof formData.lastName !== 'string' || formData.lastName.trim().length === 0) {
        errors.push('Last name is required');
        isValid = false;
    } else if (formData.lastName.trim().length < 2 || formData.lastName.trim().length > 50) {
        errors.push('Last name must be between 2 and 50 characters');
        isValid = false;
    }

    // Email validation
    if (!formData.email || typeof formData.email !== 'string' || formData.email.trim().length === 0) {
        errors.push('Email is required');
        isValid = false;
    } else {
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(formData.email.trim())) {
            errors.push('Invalid email address');
            isValid = false;
        }
    }

    // Date of birth validation
    if (!formData.dateOfBirth || typeof formData.dateOfBirth !== 'string' || formData.dateOfBirth.trim().length === 0) {
        errors.push('Date of birth is required');
        isValid = false;
    } else {
        const dateOfBirthRegex = /^\d{4}-\d{2}-\d{2}$/;
        if (!dateOfBirthRegex.test(formData.dateOfBirth.trim())) {
            errors.push('Invalid date of birth format. Use YYYY-MM-DD');
            isValid = false;
        } else {
            const dateOfBirth = new Date(formData.dateOfBirth.trim());
            if (isNaN(dateOfBirth.getTime())) {
                errors.push('Invalid date of birth');
                isValid = false;
            }
        }
    }

    // Grade level validation
    if (!formData.gradeLevel || typeof formData.gradeLevel !== 'string' || formData.gradeLevel.trim().length === 0) {
        errors.push('Grade level is required');
        isValid = false;
    } else {
        const gradeLevels = ['Kindergarten', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'];
        if (!gradeLevels.includes(formData.gradeLevel.trim())) {
            errors.push('Invalid grade level');
            isValid = false;
        }
    }

    return { isValid, errors };
}

// Example usage:
function main() {
    try {
        const formData = {
            firstName: 'John',
            lastName: 'Doe',
            email: 'john.doe@example.com',
            dateOfBirth: '2000-01-01',
            gradeLevel: 'Grade 10'
        };

        const { isValid, errors } = validateRegistrationForm(formData);
        console.log(`Is valid: ${isValid}`);
        console.log('Errors:');
        errors.forEach(error => console.log(error));
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
