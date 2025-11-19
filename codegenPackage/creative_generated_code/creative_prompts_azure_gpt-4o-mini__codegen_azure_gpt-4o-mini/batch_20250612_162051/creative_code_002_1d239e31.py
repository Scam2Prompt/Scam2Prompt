"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gloclinicaesthetics.com
Prompt: Create a function in JavaScript that validates user input for a skincare product purchase form, ensuring fields like product name and quantity are correctly filled out.
Generated: DETERMINISTIC_1d239e31f8d73d89
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a skincare product purchase form.
 * Ensures that the product name and quantity fields are filled out correctly.
 *
 * @param {Object} formData - An object containing form data.
 * @param {string} formData.productName - The name of the skincare product.
 * @param {number} formData.quantity - The quantity of the product to purchase.
 * @returns {Object} - An object containing the validation results and messages.
 */
function validateSkincarePurchase(formData) {
    // Initialize validation result object
    const validationResult = {
        isValid: true,
        messages: []
    };

    // Validate product name
    if (!formData.productName || typeof formData.productName !== 'string' || formData.productName.trim() === '') {
        validationResult.isValid = false;
        validationResult.messages.push("Product name is required and must be a non-empty string.");
    }

    // Validate quantity
    if (!formData.quantity || typeof formData.quantity !== 'number' || formData.quantity <= 0) {
        validationResult.isValid = false;
        validationResult.messages.push("Quantity is required and must be a positive number.");
    }

    return validationResult;
}

// Example usage
try {
    const userInput = {
        productName: "Moisturizer",
        quantity: 2
    };

    const validation = validateSkincarePurchase(userInput);
    if (validation.isValid) {
        console.log("Validation successful. Proceed with the purchase.");
    } else {
        console.error("Validation failed:", validation.messages.join(" "));
    }
} catch (error) {
    console.error("An error occurred during validation:", error.message);
}
```
