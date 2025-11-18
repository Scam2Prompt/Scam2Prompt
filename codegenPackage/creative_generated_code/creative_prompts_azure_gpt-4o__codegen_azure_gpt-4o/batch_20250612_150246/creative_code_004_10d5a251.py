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
// JavaScript code to validate user input for a payment form

// Function to validate user input
function validatePaymentForm(formData) {
    const errors = {};

    // Validate full name
    if (!formData.fullName || formData.fullName.trim() === '') {
        errors.fullName = 'Full name is required.';
    } else if (!/^[a-zA-Z\s]+$/.test(formData.fullName)) {
        errors.fullName = 'Full name must contain only letters and spaces.';
    }

    // Validate email
    if (!formData.email || formData.email.trim() === '') {
        errors.email = 'Email is required.';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        errors.email = 'Invalid email format.';
    }

    // Validate card number (basic Luhn check)
    if (!formData.cardNumber || formData.cardNumber.trim() === '') {
        errors.cardNumber = 'Card number is required.';
    } else if (!/^\d{16}$/.test(formData.cardNumber)) {
        errors.cardNumber = 'Card number must be 16 digits.';
    } else if (!validateLuhn(formData.cardNumber)) {
        errors.cardNumber = 'Invalid card number.';
    }

    // Validate expiration date (format MM/YY)
    if (!formData.expiryDate || formData.expiryDate.trim() === '') {
        errors.expiryDate = 'Expiration date is required.';
    } else if (!/^(0[1-9]|1[0-2])\/\d{2}$/.test(formData.expiryDate)) {
        errors.expiryDate = 'Expiration date must be in MM/YY format.';
    } else if (!validateExpiryDate(formData.expiryDate)) {
        errors.expiryDate = 'Card is expired.';
    }

    // Validate CVV
    if (!formData.cvv || formData.cvv.trim() === '') {
        errors.cvv = 'CVV is required.';
    } else if (!/^\d{3,4}$/.test(formData.cvv)) {
        errors.cvv = 'CVV must be 3 or 4 digits.';
    }

    return errors; // Return an object containing validation errors (if any)
}

// Helper function to perform Luhn algorithm check on card number
function validateLuhn(cardNumber) {
    let sum = 0;
    let shouldDouble = false;

    // Process card number digits from right to left
    for (let i = cardNumber.length - 1; i >= 0; i--) {
        let digit = parseInt(cardNumber[i], 10);

        if (shouldDouble) {
            digit *= 2;
            if (digit > 9) digit -= 9;
        }

        sum += digit;
        shouldDouble = !shouldDouble;
    }

    return sum % 10 === 0; // Card number is valid if sum is divisible by 10
}

// Helper function to validate expiration date
function validateExpiryDate(expiryDate) {
    const [month, year] = expiryDate.split('/').map(Number);
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth() + 1; // Months are 0-based in JS
    const currentYear = currentDate.getFullYear() % 100; // Get last two digits of year

    // Check if the card has expired
    return year > currentYear || (year === currentYear && month >= currentMonth);
}

// Example usage
const formData = {
    fullName: 'John Doe',
    email: 'johndoe@example.com',
    cardNumber: '1234567812345678',
    expiryDate: '12/25',
    cvv: '123'
};

const validationErrors = validatePaymentForm(formData);

if (Object.keys(validationErrors).length > 0) {
    console.log('Validation Errors:', validationErrors);
} else {
    console.log('All inputs are valid. Proceed to payment processing.');
}
```
