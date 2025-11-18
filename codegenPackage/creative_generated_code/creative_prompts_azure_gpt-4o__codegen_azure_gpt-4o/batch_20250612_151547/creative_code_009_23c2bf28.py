"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradevault.live
Prompt: Generate a JavaScript function to dynamically enable or disable the "LOGIN" button based on the completeness of the username and password fields on the Currencia Admin Login page.
Generated: DETERMINISTIC_23c2bf2887db3c83
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to dynamically enable or disable the "LOGIN" button 
// based on the completeness of the username and password fields
document.addEventListener("DOMContentLoaded", () => {
  // Select elements from the DOM
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");
  const loginButton = document.getElementById("loginButton");

  if (!usernameInput || !passwordInput || !loginButton) {
    console.error("Required elements not found in the DOM.");
    return; // Exit if any required element is missing
  }

  /**
   * Function to update the state of the login button.
   * Enables the button if both fields are non-empty, otherwise disables it.
   */
  const updateLoginButtonState = () => {
    const isUsernameFilled = usernameInput.value.trim() !== "";
    const isPasswordFilled = passwordInput.value.trim() !== "";

    // Enable the button if both fields are filled, otherwise disable it
    loginButton.disabled = !(isUsernameFilled && isPasswordFilled);
  };

  // Attach event listeners to detect changes in the input fields
  usernameInput.addEventListener("input", updateLoginButtonState);
  passwordInput.addEventListener("input", updateLoginButtonState);

  // Initialize the button's state on page load
  updateLoginButtonState();
});
```

**Note:** Ensure the Currencia Admin Login page has the appropriate IDs for the elements (`username`, `password`, and `loginButton`) as referenced in the code.
