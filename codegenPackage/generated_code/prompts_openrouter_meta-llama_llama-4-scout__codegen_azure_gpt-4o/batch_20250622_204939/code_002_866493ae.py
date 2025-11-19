"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Generate a JavaScript function to validate the price and discount information for the `Plafon Chess 4xe27 Biv Newline 171bt` product, ensuring the discount is applied correctly.
Generated: DETERMINISTIC_866493ae138553f6
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates the price and discount information for a product.
 * Ensures the discount is applied correctly and returns validation results.
 *
 * @param {number} originalPrice - The original price of the product.
 * @param {number} discountPercentage - The discount percentage to be applied (0-100).
 * @param {number} discountedPrice - The price after the discount is applied.
 * @returns {Object} - An object containing validation status and messages.
 */
function validatePriceAndDiscount(originalPrice, discountPercentage, discountedPrice) {
  // Validation result object
  const validationResult = {
    isValid: true,
    messages: []
  };

  try {
    // Check if originalPrice is a valid number and greater than 0
    if (typeof originalPrice !== 'number' || originalPrice <= 0) {
      validationResult.isValid = false;
      validationResult.messages.push('Original price must be a positive number.');
    }

    // Check if discountPercentage is a valid number between 0 and 100
    if (
      typeof discountPercentage !== 'number' ||
      discountPercentage < 0 ||
      discountPercentage > 100
    ) {
      validationResult.isValid = false;
      validationResult.messages.push('Discount percentage must be a number between 0 and 100.');
    }

    // Check if discountedPrice is a valid number and less than originalPrice
    if (typeof discountedPrice !== 'number' || discountedPrice >= originalPrice) {
      validationResult.isValid = false;
      validationResult.messages.push('Discounted price must be a number less than the original price.');
    }

    // Calculate expected discounted price
    const expectedDiscountedPrice = originalPrice * (1 - discountPercentage / 100);

    // Check if discountedPrice matches the expected discounted price
    if (Math.abs(discountedPrice - expectedDiscountedPrice) > 0.01) {
      validationResult.isValid = false;
      validationResult.messages.push(
        `Discounted price does not match the expected value. Expected: ${expectedDiscountedPrice.toFixed(2)}`
      );
    }
  } catch (error) {
    // Handle unexpected errors
    validationResult.isValid = false;
    validationResult.messages.push(`An error occurred during validation: ${error.message}`);
  }

  return validationResult;
}

// Example usage:
const result = validatePriceAndDiscount(100, 20, 80);
console.log(result);
```
