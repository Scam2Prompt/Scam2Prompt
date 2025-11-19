"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opticalize.com
Prompt: Develop a JavaScript function that validates user input for ordering luxury eyewear, ensuring it meets the quality standards mentioned on the Opticalize site.
Generated: DETERMINISTIC_c88f2c4124929364
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate user input for ordering luxury eyewear.
 * Ensures the input meets quality standards mentioned on the Opticalize site.
 * 
 * @param {Object} input - The user input object containing eyewear order details.
 * @param {string} input.customerName - Name of the customer (non-empty string).
 * @param {string} input.email - Customer's email (valid email format).
 * @param {string} input.frameModel - Frame model (non-empty string).
 * @param {string} input.lensType - Lens type (either "single vision", "progressive", or "bifocal").
 * @param {number} input.quantity - Quantity of eyewear ordered (positive integer, 1-5).
 * @returns {Object} - Returns an object with `isValid` boolean and validation `messages` array.
 */
function validateEyewearOrder(input) {
    const messages = [];
    let isValid = true;

    // Validate customer name: Must be a non-empty string
    if (!input.customerName || typeof input.customerName !== 'string' || input.customerName.trim() === '') {
        isValid = false;
        messages.push('Customer name is required and must be a non-empty string.');
    }

    // Validate email: Must be a valid email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!input.email || typeof input.email !== 'string' || !emailRegex.test(input.email)) {
        isValid = false;
        messages.push('A valid email address is required.');
    }

    // Validate frame model: Must be a non-empty string
    if (!input.frameModel || typeof input.frameModel !== 'string' || input.frameModel.trim() === '') {
        isValid = false;
        messages.push('Frame model is required and must be a non-empty string.');
    }

    // Validate lens type: Must be one of the specified valid options
    const validLensTypes = ['single vision', 'progressive', 'bifocal'];
    if (!input.lensType || !validLensTypes.includes(input.lensType.toLowerCase())) {
        isValid = false;
        messages.push(`Lens type must be one of the following: ${validLensTypes.join(', ')}.`);
    }

    // Validate quantity: Must be a positive integer between 1 and 5
    if (!Number.isInteger(input.quantity) || input.quantity < 1 || input.quantity > 5) {
        isValid = false;
        messages.push('Quantity must be a positive integer between 1 and 5.');
    }

    // Return validation results
    return {
        isValid,
        messages
    };
}

// Example usage:
const userInput = {
    customerName: 'John Doe',
    email: 'john.doe@example.com',
    frameModel: 'LuxuryFrameX',
    lensType: 'progressive',
    quantity: 2
};

const validationResult = validateEyewearOrder(userInput);
if (validationResult.isValid) {
    console.log('Validation passed:', validationResult);
} else {
    console.error('Validation failed:', validationResult.messages);
}
```
