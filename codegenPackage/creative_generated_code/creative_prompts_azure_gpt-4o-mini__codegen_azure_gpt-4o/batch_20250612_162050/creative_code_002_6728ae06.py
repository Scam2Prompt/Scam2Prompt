"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Create a JavaScript function that validates user inputs for selecting portable diesel generators, incorporating the unique features highlighted on the Birlik Jeneratör site.
Generated: DETERMINISTIC_6728ae06d15b36f7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to validate user inputs for selecting portable diesel generators.
 * @param {Object} userInput - The user's input for selecting a generator.
 * @param {number} userInput.powerOutput - Required power output in kW.
 * @param {string} userInput.fuelType - Fuel type (should be "diesel").
 * @param {boolean} userInput.isPortable - Indicates if the generator should be portable.
 * @param {string} userInput.brand - Preferred brand (optional).
 * @returns {Object} Validation result with success and error messages (if any).
 */
function validateGeneratorInput(userInput) {
  // Error collection array
  const errors = [];

  // Validate power output (must be a positive number)
  if (typeof userInput.powerOutput !== 'number' || userInput.powerOutput <= 0) {
    errors.push("Power output must be a positive number (in kW).");
  }

  // Validate fuel type (must be diesel)
  if (userInput.fuelType !== "diesel") {
    errors.push('Fuel type must be "diesel".');
  }

  // Validate portability (must be true)
  if (typeof userInput.isPortable !== 'boolean' || !userInput.isPortable) {
    errors.push("The generator must be portable.");
  }

  // Validate brand (optional but must be a non-empty string if provided)
  if (userInput.brand && (typeof userInput.brand !== 'string' || userInput.brand.trim() === '')) {
    errors.push("Brand must be a non-empty string (if specified).");
  }

  // Return validation result
  if (errors.length > 0) {
    return {
      success: false,
      errors: errors
    };
  }
  
  return {
    success: true,
    message: "User input is valid for selecting a portable diesel generator."
  };
}

// Example usage
const userInput = {
  powerOutput: 5,
  fuelType: "diesel",
  isPortable: true,
  brand: "Birlik"
};

const validationResult = validateGeneratorInput(userInput);
console.log(validationResult);
```
