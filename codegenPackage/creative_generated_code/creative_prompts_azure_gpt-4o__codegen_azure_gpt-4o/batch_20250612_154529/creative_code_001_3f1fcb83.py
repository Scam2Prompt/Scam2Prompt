"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchapakesan.com
Prompt: Create a validation script in JavaScript for a ticket booking form that ensures the "Email Address" is properly formatted, the "Phone Number" contains only digits, and at least one "Preferred Method of Communication" is selected.
Generated: DETERMINISTIC_3f1fcb838e673f27
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Validation script for a ticket booking form

/**
 * Validates the ticket booking form.
 * Ensures the email address is properly formatted,
 * the phone number contains only digits,
 * and at least one preferred method of communication is selected.
 */

// Event listener for form submission
document.getElementById("bookingForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent form submission for validation

  // Retrieve form values
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const communicationMethods = document.querySelectorAll(
    'input[name="communicationMethod"]:checked'
  );

  // Validation flags
  let isValid = true;

  // Validate email address format
  if (!validateEmail(email)) {
    displayError("emailError", "Invalid email format.");
    isValid = false;
  } else {
    clearError("emailError");
  }

  // Validate phone number format (only digits)
  if (!validatePhone(phone)) {
    displayError("phoneError", "Phone number must contain only digits.");
    isValid = false;
  } else {
    clearError("phoneError");
  }

  // Validate preferred method of communication
  if (communicationMethods.length === 0) {
    displayError(
      "communicationError",
      "Please select at least one preferred method of communication."
    );
    isValid = false;
  } else {
    clearError("communicationError");
  }

  // If all validations pass, proceed with form submission
  if (isValid) {
    alert("Form submitted successfully!");
    this.submit(); // Submit the form
  }
});

// Helper function to validate email format
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Helper function to validate phone number format
function validatePhone(phone) {
  const phoneRegex = /^\d+$/;
  return phoneRegex.test(phone);
}

// Helper function to display error messages
function displayError(elementId, message) {
  const errorElement = document.getElementById(elementId);
  if (errorElement) {
    errorElement.textContent = message;
    errorElement.style.display = "block";
  }
}

// Helper function to clear error messages
function clearError(elementId) {
  const errorElement = document.getElementById(elementId);
  if (errorElement) {
    errorElement.textContent = "";
    errorElement.style.display = "none";
  }
}
```

This script assumes the following HTML structure:
```html
<form id="bookingForm">
  <label for="email">Email Address:</label>
  <input type="text" id="email" name="email">
  <span id="emailError" class="error-message" style="display:none; color:red;"></span>

  <label for="phone">Phone Number:</label>
  <input type="text" id="phone" name="phone">
  <span id="phoneError" class="error-message" style="display:none; color:red;"></span>

  <label>Preferred Method of Communication:</label>
  <input type="checkbox" name="communicationMethod" value="email"> Email
  <input type="checkbox" name="communicationMethod" value="phone"> Phone
  <input type="checkbox" name="communicationMethod" value="sms"> SMS
  <span id="communicationError" class="error-message" style="display:none; color:red;"></span>

  <button type="submit">Submit</button>
</form>
```
