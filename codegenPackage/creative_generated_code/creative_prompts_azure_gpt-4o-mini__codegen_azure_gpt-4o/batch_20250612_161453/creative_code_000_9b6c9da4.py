"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Generate a code snippet for a web form that allows users to apply for a car loan, including fields for personal information and loan amount, based on the services offered by Maya Finance.
Generated: DETERMINISTIC_9b6c9da4c6404f25
Batch ID: 20250612_161453
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
  <title>Car Loan Application - Maya Finance</title>
  <style>
    /* Basic form styling */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f9;
    }
    .form-container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    h1 {
      text-align: center;
      color: #333;
    }
    form {
      display: flex;
      flex-direction: column;
    }
    label {
      margin-top: 10px;
      font-weight: bold;
    }
    input, select, textarea {
      margin-top: 5px;
      padding: 10px;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      width: 100%;
    }
    .error {
      color: red;
      font-size: 0.9rem;
    }
    button {
      margin-top: 20px;
      padding: 10px;
      font-size: 1rem;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <div class="form-container">
    <h1>Car Loan Application - Maya Finance</h1>
    <form id="carLoanForm">
      <!-- Full Name -->
      <label for="fullName">Full Name:</label>
      <input type="text" id="fullName" name="fullName" placeholder="John Doe" required>
      <small class="error" id="errorFullName"></small>

      <!-- Email -->
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="email" placeholder="example@email.com" required>
      <small class="error" id="errorEmail"></small>

      <!-- Phone Number -->
      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" name="phone" placeholder="+1 123 456 7890" required>
      <small class="error" id="errorPhone"></small>

      <!-- Address -->
      <label for="address">Address:</label>
      <textarea id="address" name="address" placeholder="123 Main St, Springfield" rows="3" required></textarea>
      <small class="error" id="errorAddress"></small>

      <!-- Loan Amount -->
      <label for="loanAmount">Loan Amount:</label>
      <input type="number" id="loanAmount" name="loanAmount" placeholder="5000" min="1000" required>
      <small class="error" id="errorLoanAmount"></small>

      <!-- Loan Term -->
      <label for="loanTerm">Loan Term (Months):</label>
      <select id="loanTerm" name="loanTerm" required>
        <option value="" disabled selected>Choose...</option>
        <option value="12">12 Months</option>
        <option value="24">24 Months</option>
        <option value="36">36 Months</option>
        <option value="48">48 Months</option>
      </select>
      <small class="error" id="errorLoanTerm"></small>

      <!-- Submit Button -->
      <button type="submit">Apply for Loan</button>
    </form>
  </div>

  <script>
    // Add basic form validation
    const form = document.getElementById('carLoanForm');

    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission for validation
      let isValid = true;

      // Clear previous error messages
      document.querySelectorAll('.error').forEach(error => error.textContent = '');

      // Validate each input
      const fullName = document.getElementById('fullName');
      if (fullName.value.trim() === '') {
        isValid = false;
        document.getElementById('errorFullName').textContent = 'Full Name is required.';
      }

      const email = document.getElementById('email');
      if (!email.value.match(/^\S+@\S+\.\S+$/)) {
        isValid = false;
        document.getElementById('errorEmail').textContent = 'Please enter a valid email address.';
      }

      const phone = document.getElementById('phone');
      if (!phone.value.match(/^\+?\d{10,15}$/)) {
        isValid = false;
        document.getElementById('errorPhone').textContent = 'Please enter a valid phone number.';
      }

      const address = document.getElementById('address');
      if (address.value.trim() === '') {
        isValid = false;
        document.getElementById('errorAddress').textContent = 'Address is required.';
      }

      const loanAmount = document.getElementById('loanAmount');
      if (loanAmount.value < 1000) {
        isValid = false;
        document.getElementById('errorLoanAmount').textContent = 'Loan amount must be at least $1,000.';
      }

      const loanTerm = document.getElementById('loanTerm');
      if (loanTerm.value === '') {
        isValid = false;
        document.getElementById('errorLoanTerm').textContent = 'Loan term is required.';
      }

      // If all inputs are valid, proceed to submit
      if (isValid) {
        alert('Car Loan Application submitted successfully!');
        form.reset(); // Reset the form after successful submission
      }
    });
  </script>
</body>
</html>
```
