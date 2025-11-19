"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Generate a JavaScript function that validates user input for scheduling an endoscopy appointment, ensuring all required fields are filled correctly.
Generated: DETERMINISTIC_049299e2b9d32a7a
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for scheduling an endoscopy appointment.
 * Ensures all required fields are filled correctly.
 * 
 * Required fields:
 * - fullName (string, non-empty)
 * - age (number, positive integer)
 * - appointmentDate (string, valid date format)
 * - contactNumber (string, valid phone number format)
 * - symptoms (array, non-empty)
 * 
 * @param {Object} input - User input object.
 * @returns {Object} - Validation result with `isValid` (boolean) and `errors` (array of strings).
 */
function validateEndoscopyAppointment(input) {
  const errors = [];
  
  // Check for fullName (must be a non-empty string)
  if (!input.fullName || typeof input.fullName !== 'string' || input.fullName.trim() === '') {
    errors.push('Full name is required and must be a non-empty string.');
  }
  
  // Check for age (must be a positive integer)
  if (
    !Number.isInteger(input.age) ||
    input.age <= 0
  ) {
    errors.push('Age is required and must be a positive integer.');
  }
  
  // Check for appointmentDate (must be a valid date string)
  if (
    !input.appointmentDate ||
    isNaN(new Date(input.appointmentDate).getTime())
  ) {
    errors.push('Appointment date is required and must be a valid date.');
  }
  
  // Check for contactNumber (must be a valid phone number format)
  const phoneRegex = /^\+?[1-9]\d{1,14}$/; // Simplified phone validation (E.164 format)
  if (
    !input.contactNumber ||
    typeof input.contactNumber !== 'string' ||
    !phoneRegex.test(input.contactNumber)
  ) {
    errors.push('Contact number is required and must be a valid phone number format.');
  }
  
  // Check for symptoms (must be a non-empty array)
  if (!Array.isArray(input.symptoms) || input.symptoms.length === 0) {
    errors.push('Symptoms are required and must be a non-empty array.');
  }
  
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage:
const userInput = {
  fullName: 'John Doe',
  age: 30,
  appointmentDate: '2023-12-01',
  contactNumber: '+1234567890',
  symptoms: ['Abdominal pain', 'Nausea'],
};

const validationResult = validateEndoscopyAppointment(userInput);
if (!validationResult.isValid) {
  console.error('Validation failed:', validationResult.errors);
} else {
  console.log('Validation passed: Input is valid.');
}
```
