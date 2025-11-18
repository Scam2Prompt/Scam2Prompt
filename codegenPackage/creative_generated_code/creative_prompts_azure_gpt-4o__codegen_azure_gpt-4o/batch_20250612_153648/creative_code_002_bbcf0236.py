"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.netlify.app
Prompt: Generate JavaScript code for a form validation system that ensures users provide valid input for fields such as name, email, phone, and company website, based on Acme's example form.
Generated: DETERMINISTIC_bbcf02360b180beb
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Form Validation System for Acme's Example Form
document.addEventListener("DOMContentLoaded", () => {
  // Reference to the form and its input fields
  const form = document.getElementById("acmeForm");
  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const phoneInput = document.getElementById("phone");
  const websiteInput = document.getElementById("website");

  // Regular expressions for validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email validation
  const phoneRegex = /^\+?[0-9\s\-()]{10,15}$/; // Allows international phone numbers
  const websiteRegex = /^(https?:\/\/)?([a-z0-9]+[.])+[a-z]{2,6}$/i; // Simple website URL validation

  // Error handling function
  const showError = (input, message) => {
    const errorElement = input.nextElementSibling;
    input.classList.add("error");
    errorElement.textContent = message;
    errorElement.style.display = "block";
  };

  const clearError = (input) => {
    const errorElement = input.nextElementSibling;
    input.classList.remove("error");
    errorElement.textContent = "";
    errorElement.style.display = "none";
  };

  // Validation functions
  const validateName = () => {
    const name = nameInput.value.trim();
    if (name.length === 0) {
      showError(nameInput, "Name is required.");
      return false;
    }
    clearError(nameInput);
    return true;
  };

  const validateEmail = () => {
    const email = emailInput.value.trim();
    if (!emailRegex.test(email)) {
      showError(emailInput, "Please provide a valid email address.");
      return false;
    }
    clearError(emailInput);
    return true;
  };

  const validatePhone = () => {
    const phone = phoneInput.value.trim();
    if (!phoneRegex.test(phone)) {
      showError(phoneInput, "Please provide a valid phone number.");
      return false;
    }
    clearError(phoneInput);
    return true;
  };

  const validateWebsite = () => {
    const website = websiteInput.value.trim();
    if (website.length > 0 && !websiteRegex.test(website)) {
      showError(websiteInput, "Please provide a valid website URL.");
      return false;
    }
    clearError(websiteInput);
    return true;
  };

  // Event listener for form submission
  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent form submission if validation fails

    // Validate all fields
    const isNameValid = validateName();
    const isEmailValid = validateEmail();
    const isPhoneValid = validatePhone();
    const isWebsiteValid = validateWebsite();

    // If all validations pass, submit the form
    if (isNameValid && isEmailValid && isPhoneValid && isWebsiteValid) {
      console.log("Form submitted successfully!");
      form.submit(); // Uncomment if actual form submission is needed
    } else {
      console.log("Form validation failed.");
    }
  });

  // Real-time validation on input blur
  nameInput.addEventListener("blur", validateName);
  emailInput.addEventListener("blur", validateEmail);
  phoneInput.addEventListener("blur", validatePhone);
  websiteInput.addEventListener("blur", validateWebsite);
});
```
