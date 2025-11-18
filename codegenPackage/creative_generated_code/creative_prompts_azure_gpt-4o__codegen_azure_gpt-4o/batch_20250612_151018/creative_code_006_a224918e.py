"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-140--keen-roentgen-cafcb7.netlify.app
Prompt: Create a newsletter subscription form using JavaScript that mimics the functionality described on Joe Previte's website, including email validation and submission.
Generated: DETERMINISTIC_a224918ea14e5a4d
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Newsletter Subscription</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .form-container {
      max-width: 400px;
      margin: 0 auto;
    }
    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }
    input[type="email"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      padding: 10px 15px;
      border: none;
      background-color: #28a745;
      color: white;
      border-radius: 5px;
      cursor: pointer;
    }
    button:disabled {
      background-color: #6c757d;
      cursor: not-allowed;
    }
    .error {
      color: red;
      margin-bottom: 10px;
    }
    .success {
      color: green;
      margin-top: 10px;
    }
  </style>
</head>
<body>

  <div class="form-container">
    <h2>Subscribe to our Newsletter</h2>
    <form id="subscription-form">
      <label for="email">Email Address</label>
      <input type="email" id="email" name="email" placeholder="Enter your email address" required>
      <p id="error-message" class="error"></p>
      <button type="submit" id="submit-button">Subscribe</button>
      <p id="success-message" class="success"></p>
    </form>
  </div>

  <script>
    // Select necessary elements from the DOM
    const form = document.getElementById('subscription-form');
    const emailInput = document.getElementById('email');
    const errorMessage = document.getElementById('error-message');
    const successMessage = document.getElementById('success-message');
    const submitButton = document.getElementById('submit-button');

    // Function to validate email format
    function isValidEmail(email) {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic regex for email validation
      return emailPattern.test(email);
    }

    // Event listener for form submission
    form.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent default form submission behavior

      // Clear previous messages
      errorMessage.textContent = '';
      successMessage.textContent = '';

      const email = emailInput.value.trim(); // Get the input value and trim whitespace

      // Validate email address
      if (!email) {
        errorMessage.textContent = 'Email address is required.';
        return;
      }

      if (!isValidEmail(email)) {
        errorMessage.textContent = 'Please enter a valid email address.';
        return;
      }

      // Simulate subscription process (e.g., submitting to a server)
      submitButton.disabled = true; // Disable button while processing
      setTimeout(() => {
        // Simulate successful submission
        submitButton.disabled = false; // Re-enable button
        emailInput.value = ''; // Clear input field
        successMessage.textContent = 'Thank you for subscribing!';
      }, 2000); // Simulate a delay
    });
  </script>

</body>
</html>
```
