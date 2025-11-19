"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Create a JavaScript function that validates user input for selecting a palm reading package and submitting questions for a personalized reading.
Generated: DETERMINISTIC_c4863135389a8139
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user input for selecting a palm reading package and submitting questions.
 * @param {string} selectedPackage - The package selected by the user (e.g., "basic", "premium", "professional").
 * @param {string[]} questions - An array of questions submitted by the user for personalized reading.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validatePalmReadingInput(selectedPackage, questions) {
  // Define available packages
  const availablePackages = ["basic", "premium", "professional"];
  
  // Initialize response object
  const validationResponse = {
    isValid: true,
    errors: []
  };

  // Validate package selection
  if (!selectedPackage || typeof selectedPackage !== "string") {
    validationResponse.isValid = false;
    validationResponse.errors.push("Package selection is required and must be a valid string.");
  } else if (!availablePackages.includes(selectedPackage.toLowerCase())) {
    validationResponse.isValid = false;
    validationResponse.errors.push(`Invalid package selection. Available packages are: ${availablePackages.join(", ")}.`);
  }

  // Validate questions
  if (!Array.isArray(questions)) {
    validationResponse.isValid = false;
    validationResponse.errors.push("Questions must be provided as an array of strings.");
  } else {
    questions.forEach((question, index) => {
      if (typeof question !== "string" || question.trim() === "") {
        validationResponse.isValid = false;
        validationResponse.errors.push(`Question ${index + 1} is invalid. Questions must be non-empty strings.`);
      }
    });

    // Check questions length
    if (questions.length === 0) {
      validationResponse.isValid = false;
      validationResponse.errors.push("At least one question must be provided.");
    }
  }

  return validationResponse;
}

// Example usage:
const selectedPackage = "premium";
const questions = ["Will I find love?", "How is my career looking?"];
const validationResult = validatePalmReadingInput(selectedPackage, questions);

if (validationResult.isValid) {
  console.log("Validation successful. Input is valid.");
} else {
  console.error("Validation failed with errors:", validationResult.errors);
}
```
