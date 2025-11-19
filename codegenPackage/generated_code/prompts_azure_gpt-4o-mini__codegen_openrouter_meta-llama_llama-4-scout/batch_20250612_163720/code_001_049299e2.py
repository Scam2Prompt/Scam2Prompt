"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Generate a JavaScript function that validates user input for scheduling an endoscopy appointment, ensuring all required fields are filled correctly.
Generated: DETERMINISTIC_049299e2b9d32a7a
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for scheduling an endoscopy appointment.
 * 
 * @param {Object} input - The user input object.
 * @param {string} input.patientName - The patient's name.
 * @param {string} input.patientEmail - The patient's email.
 * @param {string} input.patientPhone - The patient's phone number.
 * @param {Date|string} input.appointmentDate - The appointment date.
 * @param {string} input.doctorName - The doctor's name.
 * @param {string} [input.specialInstructions] - Any special instructions.
 * 
 * @returns {Object} An object containing a boolean indicating whether the input is valid and an array of error messages.
 */
function validateEndoscopyAppointment(input) {
    const requiredFields = [
        'patientName',
        'patientEmail',
        'patientPhone',
        'appointmentDate',
        'doctorName',
    ];

    const errors = [];

    // Check if all required fields are present
    requiredFields.forEach((field) => {
        if (!input[field]) {
            errors.push(`The field "${field}" is required.`);
        }
    });

    // Validate patient email
    if (input.patientEmail && !validateEmail(input.patientEmail)) {
        errors.push('Invalid email address.');
    }

    // Validate patient phone number
    if (input.patientPhone && !validatePhoneNumber(input.patientPhone)) {
        errors.push('Invalid phone number.');
    }

    // Validate appointment date
    if (input.appointmentDate) {
        const date = new Date(input.appointmentDate);
        if (isNaN(date.getTime())) {
            errors.push('Invalid appointment date.');
        } else if (date < new Date()) {
            errors.push('Appointment date must be in the future.');
        }
    }

    return {
        isValid: errors.length === 0,
        errors,
    };
}

/**
 * Validates an email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} True if the email is valid, false otherwise.
 */
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailRegex.test(email);
}

/**
 * Validates a phone number.
 * 
 * @param {string} phoneNumber - The phone number to validate.
 * @returns {boolean} True if the phone number is valid, false otherwise.
 */
function validatePhoneNumber(phoneNumber) {
    const phoneRegex = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    return phoneRegex.test(phoneNumber);
}

// Example usage:
function main() {
    try {
        const input = {
            patientName: 'John Doe',
            patientEmail: 'johndoe@example.com',
            patientPhone: '(123) 456-7890',
            appointmentDate: '2024-09-20',
            doctorName: 'Dr. Smith',
        };

        const { isValid, errors } = validateEndoscopyAppointment(input);

        if (isValid) {
            console.log('Input is valid.');
        } else {
            console.log('Input is invalid:');
            errors.forEach((error) => console.log(error));
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

main();
```
