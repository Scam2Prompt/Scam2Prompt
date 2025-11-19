"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rerfiet.blogspot.com
Prompt: How do I implement a custom subscription feature for a Blogger site using JavaScript?
Generated: DETERMINISTIC_070364280c0c8316
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Subscription Feature for Blogger Site

// Function to initialize subscription functionality
(function () {
  // DOM elements
  const subscriptionForm = document.getElementById('subscriptionForm'); // The form element
  const emailInput = document.getElementById('emailInput'); // The email input field
  const successMessage = document.getElementById('successMessage'); // Element for showing success message
  const errorMessage = document.getElementById('errorMessage'); // Element for showing error message

  /**
   * Utility function to validate email format
   * @param {string} email - The email address to validate.
   * @returns {boolean} - Returns true if the email format is valid, otherwise false.
   */
  function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email validation regex
    return emailRegex.test(email);
  }

  /**
   * Utility function to simulate subscription API call
   * @param {string} email - The email to subscribe.
   * @returns {Promise<string>} - Returns a promise that resolves on success or rejects on error.
   */
  function subscribeEmail(email) {
    return new Promise((resolve, reject) => {
      // Simulate network delay
      setTimeout(() => {
        // Simulate success and failure scenarios
        if (Math.random() > 0.2) {
          resolve('Subscription successful!');
        } else {
          reject('Subscription failed. Please try again later.');
        }
      }, 1000);
    });
  }

  // Event listener for form submission
  subscriptionForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    // Clear previous messages
    successMessage.textContent = '';
    errorMessage.textContent = '';

    const email = emailInput.value.trim(); // Get and trim email input value

    // Validate email format
    if (!validateEmail(email)) {
      errorMessage.textContent = 'Invalid email address. Please enter a valid email.';
      return;
    }

    try {
      // Call subscription API
      const response = await subscribeEmail(email);
      // Show success message
      successMessage.textContent = response;
      // Clear the input field
      emailInput.value = '';
    } catch (error) {
      // Show error message
      errorMessage.textContent = error;
    }
  });
})();

/*
HTML structure example:
<form id="subscriptionForm">
  <input type="email" id="emailInput" placeholder="Enter your email" required />
  <button type="submit">Subscribe</button>
</form>
<p id="successMessage" style="color: green;"></p>
<p id="errorMessage" style="color: red;"></p>
*/
```
