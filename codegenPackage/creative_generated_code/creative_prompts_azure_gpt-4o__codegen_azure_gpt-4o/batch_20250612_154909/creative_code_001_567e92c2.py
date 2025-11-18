"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Generate JavaScript code to validate a login form with a "show password" toggle feature, as seen on the Torin website.
Generated: DETERMINISTIC_567e92c2cfacc40c
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML template for the login form with a "show password" toggle feature
const loginFormHTML = `
  <form id="loginForm">
    <div>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required />
      <small class="error-message" id="emailError"></small>
    </div>
    <div>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required />
      <small class="error-message" id="passwordError"></small>
    </div>
    <div>
      <input type="checkbox" id="showPasswordCheckbox" />
      <label for="showPasswordCheckbox">Show Password</label>
    </div>
    <button type="submit">Login</button>
  </form>
`;

// Append the form to the document body (for demonstration purposes)
document.body.innerHTML = loginFormHTML;

// JavaScript code for validating and handling the login form functionality
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");
  const showPasswordCheckbox = document.getElementById("showPasswordCheckbox");
  const emailError = document.getElementById("emailError");
  const passwordError = document.getElementById("passwordError");

  /**
   * Validates the email field.
   * @returns {boolean} True if the email is valid, otherwise false.
   */
  const validateEmail = () => {
    const email = emailInput.value.trim();
    // Basic regex for email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email) {
      emailError.textContent = "Email is required.";
      return false;
    } else if (!emailRegex.test(email)) {
      emailError.textContent = "Please enter a valid email address.";
      return false;
    }
    emailError.textContent = ""; // Clear error message
    return true;
  };

  /**
   * Validates the password field.
   * @returns {boolean} True if the password is valid, otherwise false.
   */
  const validatePassword = () => {
    const password = passwordInput.value.trim();
    if (!password) {
      passwordError.textContent = "Password is required.";
      return false;
    } else if (password.length < 6) {
      passwordError.textContent = "Password must be at least 6 characters long.";
      return false;
    }
    passwordError.textContent = ""; // Clear error message
    return true;
  };

  // Add event listener to the "Show Password" checkbox
  showPasswordCheckbox.addEventListener("change", () => {
    // Toggle password visibility based on the checkbox state
    passwordInput.type = showPasswordCheckbox.checked ? "text" : "password";
  });

  // Add event listener to the form submit event
  loginForm.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    // Validate email and password fields
    const isEmailValid = validateEmail();
    const isPasswordValid = validatePassword();

    if (isEmailValid && isPasswordValid) {
      // All validations pass, proceed with login (e.g., send data to server)
      console.log("Form submitted successfully.");
      console.log("Email:", emailInput.value);
      console.log("Password:", passwordInput.value);
      // Clear form fields after successful submission (optional)
      loginForm.reset();
    } else {
      console.log("Form submission failed due to validation errors.");
    }
  });

  // Add real-time validation (optional)
  emailInput.addEventListener("input", validateEmail);
  passwordInput.addEventListener("input", validatePassword);
});
```
