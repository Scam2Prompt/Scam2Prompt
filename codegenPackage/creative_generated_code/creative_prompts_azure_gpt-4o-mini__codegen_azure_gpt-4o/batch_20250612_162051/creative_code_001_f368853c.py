"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Write a JavaScript function that validates student enrollment forms based on the requirements outlined by the Escuela Preparatoria Oficial N.73.
Generated: DETERMINISTIC_f368853c1dd042bf
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
 * Validates a student enrollment form based on the requirements
 * outlined by Escuela Preparatoria Oficial N.73.
 * 
 * @param {Object} formData - The object containing form data.
 * @param {string} formData.name - Student's full name.
 * @param {string} formData.email - Student's email address.
 * @param {string} formData.phone - Student's phone number.
 * @param {number} formData.age - Student's age.
 * @param {string[]} formData.documents - List of submitted document names.
 * @returns {Object} - An object containing validation results.
 * Example: { isValid: true, errors: [] }
 */
function validateEnrollmentForm(formData) {
  const errors = [];

  // Validate name (must be non-empty and only contain letters and spaces)
  if (!formData.name || !/^[A-Za-z\s]+$/.test(formData.name)) {
    errors.push("Invalid name: Name must contain only letters and spaces.");
  }

  // Validate email (must be a valid email format)
  if (
    !formData.email ||
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)
  ) {
    errors.push("Invalid email: Please provide a valid email address.");
  }

  // Validate phone number (must be a 10-digit number)
  if (
    !formData.phone ||
    !/^\d{10}$/.test(formData.phone)
  ) {
    errors.push("Invalid phone: Phone number must be a 10-digit number.");
  }

  // Validate age (must be between 15 and 18)
  if (
    formData.age === undefined || 
    formData.age < 15 || 
    formData.age > 18
  ) {
    errors.push("Invalid age: Age must be between 15 and 18 years.");
  }

  // Validate required documents (must include 'Birth Certificate' and 'Previous School Records')
  const requiredDocuments = ["Birth Certificate", "Previous School Records"];
  if (
    !formData.documents ||
    !Array.isArray(formData.documents) ||
    !requiredDocuments.every(doc => formData.documents.includes(doc))
  ) {
    errors.push(
      `Missing required documents: You must include ${requiredDocuments.join(", ")}.`
    );
  }

  // Return validation result
  return {
    isValid: errors.length === 0,
    errors: errors
  };
}

// Example usage:
const formData = {
  name: "Juan Perez",
  email: "juan.perez@example.com",
  phone: "1234567890",
  age: 16,
  documents: ["Birth Certificate", "Previous School Records"]
};

const validationResult = validateEnrollmentForm(formData);
console.log(validationResult);
```
