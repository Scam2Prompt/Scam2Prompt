"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Write a function in JavaScript to validate user input for a satisfaction survey on an edible printing website.
Generated: DETERMINISTIC_d4703e8d575753fd
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for a satisfaction survey.
 * @param {Object} userInput - The user's input object from the survey.
 * @param {number} userInput.rating - The satisfaction rating (1-5).
 * @param {string} userInput.comments - Optional feedback comments.
 * @returns {Object} Validation result containing isValid (boolean) and errors (array).
 */
function validateSurveyInput(userInput) {
  // Initialize an array to collect validation errors
  const errors = [];

  try {
    // Check if userInput exists and is an object
    if (!userInput || typeof userInput !== 'object') {
      errors.push('Invalid input: expected an object.');
      return { isValid: false, errors };
    }

    // Validate rating (mandatory, should be a number between 1 and 5)
    if (typeof userInput.rating !== 'number' || userInput.rating < 1 || userInput.rating > 5) {
      errors.push('Rating must be a number between 1 and 5.');
    }

    // Validate comments (optional, should be a string if provided)
    if (userInput.comments !== undefined && typeof userInput.comments !== 'string') {
      errors.push('Comments must be a string if provided.');
    }

    // Return validation result
    return {
      isValid: errors.length === 0,
      errors
    };
  } catch (error) {
    // Handle unexpected errors
    return {
      isValid: false,
      errors: ['An unexpected error occurred during validation.', error.message]
    };
  }
}

// Example usage
const surveyInput = {
  rating: 4,
  comments: 'Great edible printing quality!'
};

const validationResult = validateSurveyInput(surveyInput);

if (validationResult.isValid) {
  console.log('Valid input:', surveyInput);
} else {
  console.error('Invalid input:', validationResult.errors);
}
```
