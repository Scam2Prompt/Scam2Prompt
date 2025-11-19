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
 * Function to validate user input for a vape product purchase.
 * Ensures the user acknowledges terms, warnings, and meets age restrictions.
 * @param {Object} userInput - The user input object containing age, termsAccepted, and warningsAcknowledged.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateVapePurchase(userInput) {
  // Define minimum age for purchase
  const MINIMUM_AGE = 21;

  // Initialize response object
  const response = {
    isValid: true,
    errors: [],
  };

  try {
    // Validate user input object structure
    if (!userInput || typeof userInput !== 'object') {
      throw new Error("Invalid input: userInput must be an object.");
    }

    // Validate age
    if (typeof userInput.age !== 'number' || userInput.age < MINIMUM_AGE) {
      response.isValid = false;
      response.errors.push(
        `Age validation failed: You must be at least ${MINIMUM_AGE} years old to purchase vape products.`
      );
    }

    // Validate terms acceptance
    if (typeof userInput.termsAccepted !== 'boolean' || !userInput.termsAccepted) {
      response.isValid = false;
      response.errors.push(
        "Terms validation failed: You must accept the website's terms and conditions."
      );
    }

    // Validate warnings acknowledgment
    if (
      typeof userInput.warningsAcknowledged !== 'boolean' ||
      !userInput.warningsAcknowledged
    ) {
      response.isValid = false;
      response.errors.push(
        "Warnings validation failed: You must acknowledge the nicotine warnings."
      );
    }
  } catch (error) {
    // Handle unexpected errors
    response.isValid = false;
    response.errors.push(`Unexpected error: ${error.message}`);
  }

  // Return validation result
  return response;
}

// Example usage:
const userInput = {
  age: 22,
  termsAccepted: true,
  warningsAcknowledged: true,
};

const validationResult = validateVapePurchase(userInput);
console.log(validationResult);
```
