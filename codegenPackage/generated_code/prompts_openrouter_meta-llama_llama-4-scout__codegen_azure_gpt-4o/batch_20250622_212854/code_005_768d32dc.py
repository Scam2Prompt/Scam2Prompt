"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Write a code snippet in JavaScript to validate user input for a brick restoration project, ensuring that required fields like building age, location, and service type are properly formatted and included."
Generated: DETERMINISTIC_768d32dc187d3591
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to validate user input for a brick restoration project.
 * Ensures required fields are present and properly formatted.
 * @param {Object} input - The user input object containing building age, location, and service type.
 * @returns {Object} - An object containing validation status and error messages (if any).
 */
function validateBrickRestorationInput(input) {
  const errors = [];

  // Validate building age
  if (!input.buildingAge) {
    errors.push("Building age is required.");
  } else if (typeof input.buildingAge !== "number" || input.buildingAge <= 0) {
    errors.push("Building age must be a positive number.");
  }

  // Validate location
  if (!input.location) {
    errors.push("Location is required.");
  } else if (typeof input.location !== "string" || input.location.trim() === "") {
    errors.push("Location must be a non-empty string.");
  }

  // Validate service type
  const validServiceTypes = ["repair", "cleaning", "replacement"];
  if (!input.serviceType) {
    errors.push("Service type is required.");
  } else if (!validServiceTypes.includes(input.serviceType)) {
    errors.push(
      `Service type must be one of the following: ${validServiceTypes.join(", ")}.`
    );
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors,
  };
}

// Example usage
const userInput = {
  buildingAge: 50,
  location: "123 Main Street",
  serviceType: "repair",
};

const validationResult = validateBrickRestorationInput(userInput);

if (validationResult.isValid) {
  console.log("User input is valid.");
} else {
  console.error("Validation errors:", validationResult.errors);
}
```
