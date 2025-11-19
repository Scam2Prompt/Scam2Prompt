"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifemedicos.com.br
Prompt: Create a JavaScript code that validates user input for a life insurance quote form, ensuring compliance with privacy policies like those of MetLife.
Generated: DETERMINISTIC_9a303cf4984d7dd1
Batch ID: 20250612_160302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Life Insurance Quote Form Validation
 * This script validates user input for a life insurance quote form.
 * It ensures compliance with privacy policies and data integrity.
 * Author: [Your Name]
 * Created: [Date]
 */

// Function to validate form input
function validateInsuranceQuoteForm(formData) {
  const errors = {};

  // Validate Name (required, no numbers or special characters)
  if (!formData.name || typeof formData.name !== "string" || !/^[a-zA-Z\s]+$/.test(formData.name)) {
    errors.name = "Name is required and must contain only letters and spaces.";
  }

  // Validate Age (required, must be a number between 18 and 99)
  if (!formData.age || isNaN(formData.age) || formData.age < 18 || formData.age > 99) {
    errors.age = "Age is required and must be a number between 18 and 99.";
  }

  // Validate Email (required, must be a valid email format)
  if (!formData.email || typeof formData.email !== "string" || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
    errors.email = "A valid email address is required.";
  }

  // Validate Phone Number (required, must be 10 digits)
  if (!formData.phone || !/^\d{10}$/.test(formData.phone)) {
    errors.phone = "Phone number is required and must be exactly 10 digits.";
  }

  // Validate Income (optional, must be a positive number if provided)
  if (formData.income && (isNaN(formData.income) || formData.income <= 0)) {
    errors.income = "Income must be a positive number.";
  }

  // Validate SSN (required, must follow the format XXX-XX-XXXX)
  if (!formData.ssn || !/^\d{3}-\d{2}-\d{4}$/.test(formData.ssn)) {
    errors.ssn = "SSN is required and must follow the format XXX-XX-XXXX.";
  }

  // Ensure compliance with privacy policies (e.g., no empty fields for required data)
  if (Object.keys(errors).length > 0) {
    return { valid: false, errors };
  }

  // If all validations pass
  return { valid: true, errors: null };
}

// Example usage:
const formData = {
  name: "John Doe",
  age: 30,
  email: "john.doe@example.com",
  phone: "1234567890",
  income: 50000,
  ssn: "123-45-6789"
};

const result = validateInsuranceQuoteForm(formData);

if (result.valid) {
  console.log("Form is valid! Proceed to submit.");
} else {
  console.error("Form has errors:", result.errors);
}
```
