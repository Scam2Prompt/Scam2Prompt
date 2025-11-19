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
 * Validates user input for a vape product purchase.
 * Ensures the user acknowledges and agrees to the website's terms and warnings regarding nicotine and age restrictions.
 * 
 * @param {Object} userInput - User input object containing age, nicotineAcknowledgement, and termsAgreement.
 * @param {number} userInput.age - The user's age.
 * @param {boolean} userInput.nicotineAcknowledgement - Whether the user acknowledges nicotine warnings.
 * @param {boolean} userInput.termsAgreement - Whether the user agrees to the website's terms.
 * @returns {Object} Validation result object with a boolean indicating validity and an array of error messages.
 */
function validateVapeProductPurchase(userInput) {
    // Initialize validation result object
    const validationResult = {
        isValid: false,
        errorMessages: []
    };

    try {
        // Check if userInput is an object
        if (typeof userInput !== 'object' || userInput === null) {
            validationResult.errorMessages.push('User input must be an object');
            return validationResult;
        }

        // Check age
        if (!('age' in userInput) || typeof userInput.age !== 'number' || userInput.age < 0) {
            validationResult.errorMessages.push('Age must be a non-negative number');
        } else if (userInput.age < 18) {
            validationResult.errorMessages.push('You must be at least 18 years old to purchase vape products');
        }

        // Check nicotine acknowledgement
        if (!('nicotineAcknowledgement' in userInput) || typeof userInput.nicotineAcknowledgement !== 'boolean' || !userInput.nicotineAcknowledgement) {
            validationResult.errorMessages.push('You must acknowledge the nicotine warnings');
        }

        // Check terms agreement
        if (!('termsAgreement' in userInput) || typeof userInput.termsAgreement !== 'boolean' || !userInput.termsAgreement) {
            validationResult.errorMessages.push('You must agree to the website\'s terms');
        }

        // If no error messages, mark as valid
        if (validationResult.errorMessages.length === 0) {
            validationResult.isValid = true;
        }

    } catch (error) {
        validationResult.errorMessages.push('An error occurred during validation: ' + error.message);
    }

    return validationResult;
}

// Example usage:
function main() {
    const userInput = {
        age: 25,
        nicotineAcknowledgement: true,
        termsAgreement: true
    };

    const validationResult = validateVapeProductPurchase(userInput);

    console.log('Is valid:', validationResult.isValid);
    console.log('Error messages:', validationResult.errorMessages);
}

main();
```
