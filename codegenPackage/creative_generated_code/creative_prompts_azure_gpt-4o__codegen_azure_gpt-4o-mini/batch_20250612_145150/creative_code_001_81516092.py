"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Create a function in JavaScript that validates user input for a PIN change request, including checking the PIN Change Number, OTP, and confirming the new PIN as outlined on the Heritage Bank website.
Generated: DETERMINISTIC_81516092825a0624
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a PIN change request.
 * 
 * @param {string} pinChangeNumber - The user's PIN change number.
 * @param {string} otp - The One-Time Password sent to the user.
 * @param {string} newPin - The new PIN the user wishes to set.
 * @param {string} confirmNewPin - Confirmation of the new PIN.
 * @returns {Object} - An object containing the validation result and error message if applicable.
 */
function validatePinChangeRequest(pinChangeNumber, otp, newPin, confirmNewPin) {
    // Initialize an object to hold the validation result
    const result = {
        isValid: true,
        errors: []
    };

    // Validate PIN Change Number (must be numeric and 6 digits)
    const pinChangeNumberRegex = /^\d{6}$/;
    if (!pinChangeNumberRegex.test(pinChangeNumber)) {
        result.isValid = false;
        result.errors.push("Invalid PIN Change Number. It must be a 6-digit number.");
    }

    // Validate OTP (must be numeric and 6 digits)
    const otpRegex = /^\d{6}$/;
    if (!otpRegex.test(otp)) {
        result.isValid = false;
        result.errors.push("Invalid OTP. It must be a 6-digit number.");
    }

    // Validate new PIN (must be numeric and 4 to 6 digits)
    const newPinRegex = /^\d{4,6}$/;
    if (!newPinRegex.test(newPin)) {
        result.isValid = false;
        result.errors.push("New PIN must be a numeric value between 4 and 6 digits.");
    }

    // Validate confirmation of new PIN
    if (newPin !== confirmNewPin) {
        result.isValid = false;
        result.errors.push("New PIN and confirmation PIN do not match.");
    }

    return result;
}

// Example usage:
try {
    const validationResult = validatePinChangeRequest("123456", "654321", "1234", "1234");
    if (validationResult.isValid) {
        console.log("PIN change request is valid.");
    } else {
        console.error("PIN change request is invalid:", validationResult.errors);
    }
} catch (error) {
    console.error("An unexpected error occurred:", error.message);
}
```
