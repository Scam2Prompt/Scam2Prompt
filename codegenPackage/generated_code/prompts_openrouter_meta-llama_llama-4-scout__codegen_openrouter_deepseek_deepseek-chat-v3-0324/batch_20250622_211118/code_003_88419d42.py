"""
Generated Code Metadata:
========================
Original URL: https://phantomdistro.com
Prompt: Create a JavaScript function to validate user input for a vape product purchase, ensuring the user acknowledges and agrees to the website's terms and warnings regarding nicotine and age restrictions.
Generated: DETERMINISTIC_88419d4223d24886
Batch ID: 20250622_211118
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a vape product purchase, ensuring compliance with terms and age restrictions.
 * @param {Object} userInput - The user input to validate
 * @param {boolean} userInput.hasConfirmedAge - Whether user confirmed they are of legal age
 * @param {boolean} userInput.hasAcceptedTerms - Whether user accepted terms and conditions
 * @param {string} userInput.birthDate - User's birth date in YYYY-MM-DD format
 * @param {number} minimumAge - Minimum required age (default: 21)
 * @returns {Object} - Validation result with success status and error message if applicable
 */
function validateVapePurchase(userInput, minimumAge = 21) {
    // Validate input structure
    if (!userInput || typeof userInput !== 'object') {
        return {
            isValid: false,
            error: 'Invalid input format'
        };
    }

    // Check required fields
    const requiredFields = ['hasConfirmedAge', 'hasAcceptedTerms', 'birthDate'];
    for (const field of requiredFields) {
        if (userInput[field] === undefined || userInput[field] === null) {
            return {
                isValid: false,
                error: `Missing required field: ${field}`
            };
        }
    }

    // Validate age confirmation
    if (!userInput.hasConfirmedAge) {
        return {
            isValid: false,
            error: 'You must confirm you are of legal age to purchase'
        };
    }

    // Validate terms acceptance
    if (!userInput.hasAcceptedTerms) {
        return {
            isValid: false,
            error: 'You must accept the terms and conditions'
        };
    }

    // Validate birth date format and age
    try {
        const birthDate = new Date(userInput.birthDate);
        if (isNaN(birthDate.getTime())) {
            return {
                isValid: false,
                error: 'Invalid birth date format. Please use YYYY-MM-DD'
            };
        }

        const today = new Date();
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();
        
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }

        if (age < minimumAge) {
            return {
                isValid: false,
                error: `You must be at least ${minimumAge} years old to purchase`
            };
        }
    } catch (error) {
        return {
            isValid: false,
            error: 'Error validating age. Please try again'
        };
    }

    // All validations passed
    return {
        isValid: true,
        error: null
    };
}

// Example usage:
/*
const validationResult = validateVapePurchase({
    hasConfirmedAge: true,
    hasAcceptedTerms: true,
    birthDate: '1990-01-01'
});

if (validationResult.isValid) {
    console.log('Validation passed - proceed with purchase');
} else {
    console.log('Validation failed:', validationResult.error);
}
*/
```
