"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socrates-gm.com
Prompt: Generate code in JavaScript to implement a form for resetting the username and password on the Socrates GM portal, including email validation and security question prompts.
Generated: DETERMINISTIC_ebcd82ed153fc872
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Reset Username and Password Form for Socrates GM Portal
// HTML, CSS, and JavaScript implementation

// HTML Section
const formHTML = `
  <div id="reset-form-container" style="width: 100%; max-width: 500px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
    <h2 style="text-align: center;">Reset Username & Password</h2>
    <form id="reset-form">
      <!-- Email input -->
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required placeholder="Enter your email" style="width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box;">
      
      <!-- Security question -->
      <label for="security-question">Security Question:</label>
      <select id="security-question" name="security-question" required style="width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box;">
        <option value="" disabled selected>Select a security question</option>
        <option value="mother-maiden-name">What is your mother's maiden name?</option>
        <option value="first-pet">What was the name of your first pet?</option>
        <option value="birth-city">In what city were you born?</option>
      </select>

      <!-- Security answer -->
      <label for="security-answer">Answer:</label>
      <input type="text" id="security-answer" name="security-answer" required placeholder="Enter the answer" style="width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box;">

      <!-- New username -->
      <label for="new-username">New Username:</label>
      <input type="text" id="new-username" name="new-username" required placeholder="Enter your new username" style="width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box;">

      <!-- New password -->
      <label for="new-password">New Password:</label>
      <input type="password" id="new-password" name="new-password" required placeholder="Enter your new password" style="width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box;">

      <!-- Confirm password -->
      <label for="confirm-password">Confirm Password:</label>
      <input type="password" id="confirm-password" name="confirm-password" required placeholder="Confirm your new password" style="width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box;">
      
      <!-- Submit button -->
      <button type="submit" style="width: 100%; padding: 10px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">Reset</button>
    </form>
    <div id="form-message" style="margin-top: 20px; color: red;"></div>
  </div>
`;

// Append form to the body
document.body.innerHTML = formHTML;

// JavaScript Section
document.getElementById('reset-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  // Retrieve form data
  const email = document.getElementById('email').value.trim();
  const securityQuestion = document.getElementById('security-question').value;
  const securityAnswer = document.getElementById('security-answer').value.trim();
  const newUsername = document.getElementById('new-username').value.trim();
  const newPassword = document.getElementById('new-password').value.trim();
  const confirmPassword = document.getElementById('confirm-password').value.trim();
  const messageContainer = document.getElementById('form-message');

  // Basic validation
  if (!email || !securityQuestion || !securityAnswer || !newUsername || !newPassword || !confirmPassword) {
    messageContainer.textContent = 'All fields are required.';
    return;
  }

  // Validate email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    messageContainer.textContent = 'Please enter a valid email address.';
    return;
  }

  // Validate password match
  if (newPassword !== confirmPassword) {
    messageContainer.textContent = 'Passwords do not match.';
    return;
  }

  // Simulate form submission (replace this section with real API call)
  try {
    // Sample success response simulation
    const response = {
      success: true,
      message: 'Username and password have been successfully reset.',
    };

    if (response.success) {
      messageContainer.style.color = 'green';
      messageContainer.textContent = response.message;
      // Reset form fields
      document.getElementById('reset-form').reset();
    } else {
      throw new Error(response.message || 'Error resetting credentials.');
    }
  } catch (error) {
    messageContainer.style.color = 'red';
    messageContainer.textContent = error.message;
  }
});
```
