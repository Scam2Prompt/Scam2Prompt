"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifemedicos.com.br
Prompt: Create a JavaScript code that validates user input for a life insurance quote form, ensuring compliance with privacy policies like those of MetLife.
Generated: DETERMINISTIC_9a303cf4984d7dd1
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Life Insurance Quote Form Validator

class QuoteFormValidator {
    constructor(formElement) {
        this.form = formElement;
        this.errors = [];
        
        // Bind the validate method to the form submission event
        this.form.addEventListener('submit', (event) => this.validate(event));
    }

    // Main validation method 
    validate(event) {
        this.errors = []; // Reset previous errors
        event.preventDefault(); // Prevent form submission for validation

        // Validate each field
        this.validateName();
        this.validateEmail();
        this.validateAge();
        this.validateCoverageAmount();

        // If there are errors, display them; otherwise, submit the form
        if (this.errors.length > 0) {
            this.displayErrors();
        } else {
            this.submitForm();
        }
    }

    // Validate name field
    validateName() {
        const nameField = this.form.querySelector('input[name="name"]');
        const nameValue = nameField.value.trim();
        if (nameValue.length < 2 || nameValue.length > 50) {
            this.errors.push("Name must be between 2 and 50 characters.");
        }
    }

    // Validate email field
    validateEmail() {
        const emailField = this.form.querySelector('input[name="email"]');
        const emailValue = emailField.value.trim();
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

        if (!emailPattern.test(emailValue)) {
            this.errors.push("Please enter a valid email address.");
        }
    }

    // Validate age field
    validateAge() {
        const ageField = this.form.querySelector('input[name="age"]');
        const ageValue = parseInt(ageField.value.trim(), 10);
        
        if (isNaN(ageValue) || ageValue < 18 || ageValue > 100) {
            this.errors.push("Age must be a number between 18 and 100.");
        }
    }

    // Validate coverage amount
    validateCoverageAmount() {
        const coverageField = this.form.querySelector('input[name="coverage"]');
        const coverageValue = parseFloat(coverageField.value.trim());

        if (isNaN(coverageValue) || coverageValue <= 0) {
            this.errors.push("Coverage amount must be a positive number.");
        }
    }

    // Display validation errors to the user
    displayErrors() {
        const errorContainer = this.form.querySelector('.error-messages');
        errorContainer.innerHTML = this.errors.map(error => `<li>${error}</li>`).join('');
        errorContainer.style.display = 'block'; // Show error messages
    }

    // Submit the form if validation passes (here you would typically send the data to your server)
    submitForm() {
        // Example: send data to server (this is a placeholder)
        console.log("Submitting form with valid data.");
        // You can use fetch or axios to submit the form data to your server
        // fetch('your-server-url', { method: 'POST', body: new FormData(this.form) });
        
        // For demonstration, we will reset the form and hide error messages
        this.form.reset();
        this.form.querySelector('.error-messages').style.display = 'none';
    }
}

// Initialize the form validator on page load
document.addEventListener('DOMContentLoaded', () => {
    const formElement = document.querySelector('#quote-form');
    if (formElement) {
        new QuoteFormValidator(formElement);
    }
});
```

### HTML Structure Required
Make sure your HTML structure includes the necessary elements for the validator to work:

```html
<form id="quote-form">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <input type="number" name="age" placeholder="Your Age" required>
    <input type="number" name="coverage" placeholder="Coverage Amount" required>
    <button type="submit">Get Quote</button>
    <ul class="error-messages" style="display: none;"></ul> <!-- Error messages will be displayed here -->
</form>
```
