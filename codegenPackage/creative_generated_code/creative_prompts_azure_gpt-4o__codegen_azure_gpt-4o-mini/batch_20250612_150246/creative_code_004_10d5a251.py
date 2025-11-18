"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cb-pay-tam.vercel.app
Prompt: Write JavaScript code to validate user input for a payment form in a web app like "CB Pay TAM."
Generated: DETERMINISTIC_10d5a251d16ddb46
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// PaymentFormValidator.js

class PaymentFormValidator {
    constructor(form) {
        this.form = form; // Reference to the payment form
        this.errors = {}; // Object to store validation errors
    }

    // Validate the entire form
    validate() {
        this.errors = {}; // Reset errors
        this.validateCardNumber();
        this.validateExpirationDate();
        this.validateCVV();
        return this.errors; // Return accumulated errors
    }

    // Validate credit card number
    validateCardNumber() {
        const cardNumber = this.form.cardNumber.value.trim();
        const cardNumberRegex = /^[0-9]{16}$/; // Basic validation for 16-digit card number

        if (!cardNumberRegex.test(cardNumber)) {
            this.errors.cardNumber = 'Invalid card number. Must be 16 digits.';
        }
    }

    // Validate expiration date
    validateExpirationDate() {
        const expirationDate = this.form.expirationDate.value.trim();
        const expirationDateRegex = /^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$/; // MM/YY format

        if (!expirationDateRegex.test(expirationDate)) {
            this.errors.expirationDate = 'Invalid expiration date. Format must be MM/YY.';
        } else {
            const [month, year] = expirationDate.split('/').map(Number);
            const today = new Date();
            const currentYear = today.getFullYear() % 100; // Get last two digits of current year
            const currentMonth = today.getMonth() + 1; // Months are zero-based
            // Check if the card is expired
            if (year < currentYear || (year === currentYear && month < currentMonth)) {
                this.errors.expirationDate = 'Credit card is expired.';
            }
        }
    }

    // Validate CVV
    validateCVV() {
        const cvv = this.form.cvv.value.trim();
        const cvvRegex = /^[0-9]{3,4}$/; // 3 or 4 digits

        if (!cvvRegex.test(cvv)) {
            this.errors.cvv = 'Invalid CVV. Must be 3 or 4 digits.';
        }
    }
}

// Event listener for form submission
document.addEventListener('DOMContentLoaded', () => {
    const paymentForm = document.getElementById('payment-form');

    paymentForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission

        const validator = new PaymentFormValidator(paymentForm);
        const errors = validator.validate();

        // Clear previous error messages
        const errorElements = document.querySelectorAll('.error-message');
        errorElements.forEach(el => el.textContent = '');

        // Display new error messages if any
        if (Object.keys(errors).length > 0) {
            for (const [key, message] of Object.entries(errors)) {
                const errorElement = document.getElementById(`${key}-error`);
                if (errorElement) {
                    errorElement.textContent = message; // Display error message
                }
            }
        } else {
            // Proceed with form submission or further processing
            console.log('Form is valid. Proceeding with submission...');
            paymentForm.submit(); // Uncomment this line to enable form submission
        }
    });
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment Form Validation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <form id="payment-form">
        <label for="cardNumber">Card Number:</label>
        <input type="text" id="cardNumber" name="cardNumber" required>
        <span id="cardNumber-error" class="error-message"></span>

        <label for="expirationDate">Expiration Date (MM/YY):</label>
        <input type="text" id="expirationDate" name="expirationDate" required>
        <span id="expirationDate-error" class="error-message"></span>

        <label for="cvv">CVV:</label>
        <input type="text" id="cvv" name="cvv" required>
        <span id="cvv-error" class="error-message"></span>

        <button type="submit">Pay Now</button>
    </form>

    <script src="PaymentFormValidator.js"></script>
</body>
</html>
```

```css
/* styles.css */
.error-message {
    color: red;
    font-size: 0.9em;
}
```
