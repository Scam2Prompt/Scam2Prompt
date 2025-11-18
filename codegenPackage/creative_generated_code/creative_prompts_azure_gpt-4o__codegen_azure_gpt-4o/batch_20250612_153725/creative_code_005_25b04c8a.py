"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.signalrextrack.com
Prompt: Create a JavaScript function to display a password strength meter on the Signalrextrack registration form, dynamically updating based on user input.
Generated: DETERMINISTIC_25b04c8a52e54255
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically display a password strength meter
 * on the Signalrextrack registration form.
 * This code updates the strength meter based on user input.
 */

// Wait for the DOM to load before executing the code
document.addEventListener('DOMContentLoaded', () => {
  // Select the password input field and strength meter element
  const passwordInput = document.getElementById('password');
  const strengthMeter = document.getElementById('password-strength-meter');
  const strengthText = document.getElementById('password-strength-text');

  // Function to evaluate password strength
  const evaluatePasswordStrength = (password) => {
    let score = 0;

    // Define password strength criteria
    const criteria = [
      /.{8,}/, // At least 8 characters
      /[A-Z]/, // Contains uppercase letters
      /[a-z]/, // Contains lowercase letters
      /\d/,    // Contains numbers
      /[!@#$%^&*(),.?":{}|<>]/ // Contains special characters
    ];

    // Check password against each criteria and increment score
    criteria.forEach((regex) => {
      if (regex.test(password)) score++;
    });

    return score; // Return the strength score (0 to 5)
  };

  // Function to map score to strength level
  const getStrengthLevel = (score) => {
    switch (score) {
      case 0:
      case 1:
        return { level: 'Weak', color: 'red' };
      case 2:
        return { level: 'Moderate', color: 'orange' };
      case 3:
      case 4:
        return { level: 'Strong', color: 'green' };
      case 5:
        return { level: 'Very Strong', color: 'darkgreen' };
      default:
        return { level: 'Unknown', color: 'black' };
    }
  };

  // Event listener to update strength meter on password input
  passwordInput.addEventListener('input', () => {
    const password = passwordInput.value;
    const score = evaluatePasswordStrength(password);
    const strength = getStrengthLevel(score);

    // Update the strength meter display
    strengthMeter.value = score;
    strengthText.textContent = strength.level;
    strengthText.style.color = strength.color;
  });
});

// HTML structure required:
// <form id="registration-form">
//   <label for="password">Password:</label>
//   <input type="password" id="password" name="password" required>
//   <meter id="password-strength-meter" min="0" max="5" value="0"></meter>
//   <span id="password-strength-text">Weak</span>
// </form>
```
