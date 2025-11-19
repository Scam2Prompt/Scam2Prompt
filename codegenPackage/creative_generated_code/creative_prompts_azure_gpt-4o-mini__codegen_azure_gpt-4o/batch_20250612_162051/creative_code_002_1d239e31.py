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
 * Validates the user input for a skincare product purchase form.
 * @param {Object} formData - The data submitted by the user.
 * @param {string} formData.productName - The name of the skincare product.
 * @param {number} formData.quantity - The quantity of the product to be purchased.
 * @returns {Object} - Returns a validation result object containing `isValid` (boolean) and `errors` (array of error messages).
 */
function validateSkincareForm(formData) {
  const errors = [];

  // Validate productName
  if (!formData.productName || typeof formData.productName !== 'string' || formData.productName.trim().length === 0) {
    errors.push('Product name is required and must be a non-empty string.');
  }

  // Validate quantity
  if (formData.quantity === undefined || typeof formData.quantity !== 'number' || formData.quantity <= 0) {
    errors.push('Quantity is required and must be a positive number.');
  }

  // Check validation result
  const isValid = errors.length === 0;

  return {
    isValid,
    errors,
  };
}

// Example usage:
const formData = {
  productName: 'Facial Cleanser',
  quantity: 2,
};

const validationResult = validateSkincareForm(formData);

if (validationResult.isValid) {
  console.log('Form is valid.');
} else {
  console.error('Form validation failed:', validationResult.errors);
}
```
