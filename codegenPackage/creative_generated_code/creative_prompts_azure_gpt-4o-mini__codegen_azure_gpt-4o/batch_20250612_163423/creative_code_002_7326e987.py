"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://johnbarrybaker.com
Prompt: Create a JavaScript function that validates user input for a consultation request form specifically for a personal injury law firm, focusing on fields relevant to car and motorcycle accidents.
Generated: DETERMINISTIC_7326e987b4d49535
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the user input for a consultation request form for a personal injury law firm.
 * Focuses on fields relevant to car and motorcycle accidents.
 *
 * @param {Object} formData - The user input data from the consultation form.
 * @returns {Object} - An object containing validation success and error messages.
 */
function validateConsultationForm(formData) {
  // Validation result object
  const validationResult = {
    isValid: true,
    errors: {}
  };

  // Helper function to check if a value is empty
  const isEmpty = (value) => !value || value.trim() === '';

  try {
    // Validate full name
    if (isEmpty(formData.fullName)) {
      validationResult.isValid = false;
      validationResult.errors.fullName = "Full name is required.";
    } else if (formData.fullName.length > 100) {
      validationResult.isValid = false;
      validationResult.errors.fullName = "Full name cannot exceed 100 characters.";
    }

    // Validate contact information (email or phone)
    if (isEmpty(formData.email) && isEmpty(formData.phone)) {
      validationResult.isValid = false;
      validationResult.errors.contact = "Either email or phone number must be provided.";
    } else {
      // Validate email format if provided
      if (!isEmpty(formData.email)) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(formData.email)) {
          validationResult.isValid = false;
          validationResult.errors.email = "Invalid email format.";
        }
      }

      // Validate phone number format if provided
      if (!isEmpty(formData.phone)) {
        const phoneRegex = /^\+?[1-9]\d{1,14}$/; // E.164 format for international phone numbers
        if (!phoneRegex.test(formData.phone)) {
          validationResult.isValid = false;
          validationResult.errors.phone = "Invalid phone number format.";
        }
      }
    }

    // Validate type of accident
    if (isEmpty(formData.accidentType)) {
      validationResult.isValid = false;
      validationResult.errors.accidentType = "Type of accident is required.";
    } else if (!['car', 'motorcycle'].includes(formData.accidentType.toLowerCase())) {
      validationResult.isValid = false;
      validationResult.errors.accidentType = "Accident type must be 'car' or 'motorcycle'.";
    }

    // Validate date of accident
    if (isEmpty(formData.accidentDate)) {
      validationResult.isValid = false;
      validationResult.errors.accidentDate = "Date of accident is required.";
    } else {
      const accidentDate = new Date(formData.accidentDate);
      if (isNaN(accidentDate.getTime())) {
        validationResult.isValid = false;
        validationResult.errors.accidentDate = "Invalid date format.";
      } else if (accidentDate > new Date()) {
        validationResult.isValid = false;
        validationResult.errors.accidentDate = "Accident date cannot be in the future.";
      }
    }

    // Validate description
    if (isEmpty(formData.description)) {
      validationResult.isValid = false;
      validationResult.errors.description = "Description of the accident is required.";
    } else if (formData.description.length > 1000) {
      validationResult.isValid = false;
      validationResult.errors.description = "Description cannot exceed 1000 characters.";
    }
  } catch (error) {
    // Handle unexpected errors
    validationResult.isValid = false;
    validationResult.errors.general = "An unexpected error occurred during validation.";
    console.error("Validation error: ", error);
  }

  return validationResult;
}

// Example usage
const formData = {
  fullName: "John Doe",
  email: "john.doe@example.com",
  phone: "+1234567890",
  accidentType: "car",
  accidentDate: "2023-05-15",
  description: "I was hit by another car at an intersection."
};

console.log(validateConsultationForm(formData));
```
