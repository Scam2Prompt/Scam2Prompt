"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Develop a simple HTML form that allows users to subscribe to Digielearning's e-book service and securely process their payment information.
Generated: DETERMINISTIC_215d2da2f7a07b7f
Batch ID: 20250612_160158
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
  <title>Digielearning E-Book Subscription</title>
  <style>
    /* Basic styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      padding: 0;
      background-color: #f4f4f4;
    }

    .form-container {
      max-width: 500px;
      margin: 0 auto;
      background: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input[type="text"],
    input[type="email"],
    input[type="password"],
    input[type="number"],
    button {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
      font-size: 1rem;
    }

    button {
      background-color: #28a745;
      color: white;
      border: none;
      cursor: pointer;
      font-weight: bold;
    }

    button:hover {
      background-color: #218838;
    }

    .error-message {
      color: red;
      font-size: 0.9rem;
    }
  </style>
  <script>
    /**
     * Validate form fields before submission
     */
    function validateForm(event) {
      event.preventDefault(); // Prevent form submission

      // Clear any previous error messages
      const errorMessages = document.querySelectorAll('.error-message');
      errorMessages.forEach((msg) => msg.remove());

      let valid = true;

      // Get form fields
      const form = document.getElementById('subscriptionForm');
      const name = form.name.value.trim();
      const email = form.email.value.trim();
      const cardNumber = form.cardNumber.value.trim();
      const cvv = form.cvv.value.trim();
      const expirationDate = form.expirationDate.value.trim();

      // Validate name
      if (!name) {
        showError(form.name, 'Name is required.');
        valid = false;
      }

      // Validate email
      if (!email || !email.includes('@')) {
        showError(form.email, 'Valid email is required.');
        valid = false;
      }

      // Validate card number
      if (!cardNumber || cardNumber.length !== 16 || isNaN(cardNumber)) {
        showError(form.cardNumber, 'Valid 16-digit card number is required.');
        valid = false;
      }

      // Validate CVV
      if (!cvv || cvv.length !== 3 || isNaN(cvv)) {
        showError(form.cvv, 'Valid 3-digit CVV is required.');
        valid = false;
      }

      // Validate expiration date
      if (!expirationDate) {
        showError(form.expirationDate, 'Expiration date is required.');
        valid = false;
      }

      // If all fields are valid, process the payment (mocked for this example)
      if (valid) {
        alert('Payment processed successfully!');
        form.reset(); // Reset form fields
      }
    }

    /**
     * Show error message below the input field
     * @param {HTMLElement} field - The field with an error
     * @param {string} message - The error message
     */
    function showError(field, message) {
      const error = document.createElement('div');
      error.className = 'error-message';
      error.innerText = message;
      field.parentNode.appendChild(error);
    }
  </script>
</head>
<body>
  <div class="form-container">
    <h1>E-Book Subscription</h1>
    <form id="subscriptionForm">
      <!-- Full Name -->
      <div class="form-group">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" placeholder="Enter your full name" required>
      </div>

      <!-- Email Address -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email address" required>
      </div>

      <!-- Card Number -->
      <div class="form-group">
        <label for="cardNumber">Card Number</label>
        <input type="text" id="cardNumber" name="cardNumber" placeholder="Enter your 16-digit card number" maxlength="16" required>
      </div>

      <!-- CVV -->
      <div class="form-group">
        <label for="cvv">CVV</label>
        <input type="number" id="cvv" name="cvv" placeholder="Enter your 3-digit CVV" required>
      </div>

      <!-- Expiration Date -->
      <div class="form-group">
        <label for="expirationDate">Expiration Date</label>
        <input type="text" id="expirationDate" name="expirationDate" placeholder="MM/YY" required>
      </div>

      <!-- Submit Button -->
      <button type="submit" onclick="validateForm(event)">Subscribe</button>
    </form>
  </div>
</body>
</html>
```
