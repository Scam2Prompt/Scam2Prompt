"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategpt.nl
Prompt: Generate code in JavaScript to validate form inputs (e.g., minimum length for name fields, valid email format) as described on the Immediate GPT registration page.
Generated: DETERMINISTIC_1806101d631b3063
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Form Validation for Immediate GPT Registration Page
 * This script validates user inputs in a registration form.
 * Validations include: 
 * 1. Minimum length for name fields
 * 2. Valid email format
 * 3. Optional validation for other fields can be added as needed
 */

document.addEventListener('DOMContentLoaded', () => {
    // Form and Input Fields
    const form = document.getElementById('registrationForm');
    const firstNameInput = document.getElementById('firstName');
    const lastNameInput = document.getElementById('lastName');
    const emailInput = document.getElementById('email');

    // Validation rules
    const MIN_NAME_LENGTH = 2; // Minimum length for first and last name
    const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Regex for valid email format

    // Error Messages
    const errorMessages = {
        nameTooShort: `Name must be at least ${MIN_NAME_LENGTH} characters long.`,
        invalidEmail: 'Please enter a valid email address.',
    };

    // Utility function: Display error message
    function showError(input, message) {
        const errorElement = input.nextElementSibling; // Assume error message spans are placed next to the input field
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.style.color = 'red';
        }
        input.classList.add('error'); // Add error class for styling if needed
    }

    // Utility function: Clear error message
    function clearError(input) {
        const errorElement = input.nextElementSibling;
        if (errorElement) {
            errorElement.textContent = '';
        }
        input.classList.remove('error'); // Remove error class
    }

    // Validation function for name fields
    function validateName(input) {
        const value = input.value.trim();
        if (value.length < MIN_NAME_LENGTH) {
            showError(input, errorMessages.nameTooShort);
            return false;
        }
        clearError(input);
        return true;
    }

    // Validation function for email field
    function validateEmail(input) {
        const value = input.value.trim();
        if (!EMAIL_REGEX.test(value)) {
            showError(input, errorMessages.invalidEmail);
            return false;
        }
        clearError(input);
        return true;
    }

    // Form submission handler
    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent form submission for client-side validation

        // Validate inputs
        const isFirstNameValid = validateName(firstNameInput);
        const isLastNameValid = validateName(lastNameInput);
        const isEmailValid = validateEmail(emailInput);

        // Check all validations before proceeding
        if (isFirstNameValid && isLastNameValid && isEmailValid) {
            console.log('Form submitted successfully!');
            // Proceed with form submission (e.g., send data to server)
            form.submit(); // Uncomment this line to allow actual submission
        } else {
            console.log('Form contains errors. Please fix them and try again.');
        }
    });

    // Add input event listeners for real-time validation
    firstNameInput.addEventListener('input', () => validateName(firstNameInput));
    lastNameInput.addEventListener('input', () => validateName(lastNameInput));
    emailInput.addEventListener('input', () => validateEmail(emailInput));
});
```

**Usage Instructions:**
- Ensure the HTML form and input fields have IDs: `registrationForm`, `firstName`, `lastName`, and `email`.
- Place `<span>` elements next to each input field for displaying error messages:
  ```html
  <input type="text" id="firstName" />
  <span></span>
  <input type="text" id="lastName" />
  <span></span>
  <input type="email" id="email" />
  <span></span>
  ```
