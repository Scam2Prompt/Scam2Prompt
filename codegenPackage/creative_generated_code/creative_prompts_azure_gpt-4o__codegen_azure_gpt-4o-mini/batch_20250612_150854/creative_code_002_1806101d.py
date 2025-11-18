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
// FormValidator class to handle form input validation
class FormValidator {
    constructor(formId) {
        this.form = document.getElementById(formId);
        this.errors = {};
        this.init();
    }

    // Initialize event listeners for form submission
    init() {
        this.form.addEventListener('submit', (event) => {
            if (!this.validateForm()) {
                event.preventDefault(); // Prevent form submission if validation fails
                this.displayErrors();
            } else {
                this.clearErrors();
            }
        });
    }

    // Validate the entire form
    validateForm() {
        this.errors = {}; // Reset errors
        const name = this.form.querySelector('input[name="name"]').value;
        const email = this.form.querySelector('input[name="email"]').value;

        // Validate name
        if (!this.validateName(name)) {
            this.errors.name = 'Name must be at least 3 characters long.';
        }

        // Validate email
        if (!this.validateEmail(email)) {
            this.errors.email = 'Please enter a valid email address.';
        }

        // Return true if no errors exist
        return Object.keys(this.errors).length === 0;
    }

    // Validate name with minimum length requirement
    validateName(name) {
        return name.length >= 3;
    }

    // Validate email format using a regular expression
    validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Display error messages on the form
    displayErrors() {
        this.clearErrors(); // Clear previous error messages
        for (const [field, message] of Object.entries(this.errors)) {
            const errorElement = document.createElement('div');
            errorElement.className = 'error';
            errorElement.textContent = message;

            const inputField = this.form.querySelector(`input[name="${field}"]`);
            inputField.parentElement.appendChild(errorElement);
        }
    }

    // Clear previous error messages
    clearErrors() {
        const errorElements = this.form.querySelectorAll('.error');
        errorElements.forEach(errorElement => errorElement.remove());
    }
}

// Usage example: Instantiate the FormValidator for a specific form
document.addEventListener('DOMContentLoaded', () => {
    new FormValidator('registrationForm');
});
```

**HTML Example for Reference:**
```html
<form id="registrationForm">
    <div>
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required>
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required>
    </div>
    <button type="submit">Register</button>
</form>
```
