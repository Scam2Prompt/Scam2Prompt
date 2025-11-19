"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promocrypt.com
Prompt: Create a JavaScript function that validates a domain purchase offer form, ensuring it meets the requirements seen on promocrypt.com.
Generated: DETERMINISTIC_f432c74d7abccc48
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates a domain purchase offer form.
 * The function checks if all required fields are filled, 
 * if the email is in the correct format, and if the offer amount is valid.
 *
 * @param {object} formData - The data from the form submission.
 * @returns {object} - { isValid: boolean, errors: object }
 */
function validateDomainPurchaseOfferForm(formData) {
  const errors = {};
  let isValid = true;

  // Validate required fields
  const requiredFields = ['domainName', 'email', 'offerAmount'];
  requiredFields.forEach((field) => {
    if (!formData[field]) {
      errors[field] = `${field} is required.`;
      isValid = false;
    }
  });

  // Validate email format
  if (formData.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    errors.email = 'Invalid email format.';
    isValid = false;
  }

  // Validate offer amount (must be a positive number)
  if (
    formData.offerAmount &&
    (isNaN(formData.offerAmount) || Number(formData.offerAmount) <= 0)
  ) {
    errors.offerAmount = 'Offer amount must be a positive number.';
    isValid = false;
  }

  return { isValid, errors };
}

// Example usage:
// const formData = {
//   domainName: 'example.com',
//   email: 'user@example.com',
//   offerAmount: '500'
// };
// const validationResult = validateDomainPurchaseOfferForm(formData);
// console.log(validationResult);
```
