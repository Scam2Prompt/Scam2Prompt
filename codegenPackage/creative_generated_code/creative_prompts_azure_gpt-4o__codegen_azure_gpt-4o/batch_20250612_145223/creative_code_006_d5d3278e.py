"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: Develop a mock loan application form in HTML and CSS, inspired by TymeBank's loan application process.
Generated: DETERMINISTIC_d5d3278e0e052a8e
Batch ID: 20250612_145223
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
  <title>Loan Application Form</title>
  <style>
    /* General Reset for Consistency */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f9;
      color: #333;
      line-height: 1.6;
    }

    .container {
      max-width: 600px;
      margin: 2rem auto;
      background: #fff;
      padding: 1.5rem 2rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      margin-bottom: 1.5rem;
      color: #006c67;
    }

    form {
      display: flex;
      flex-direction: column;
    }

    .form-group {
      margin-bottom: 1rem;
    }

    label {
      font-weight: bold;
      margin-bottom: 0.5rem;
      display: block;
    }

    input, select, button {
      width: 100%;
      padding: 0.75rem;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    input:focus, select:focus {
      border-color: #006c67;
      outline: none;
      box-shadow: 0 0 3px rgba(0, 108, 103, 0.5);
    }

    button {
      background-color: #006c67;
      color: #fff;
      font-weight: bold;
      cursor: pointer;
      border: none;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #004f4b;
    }

    small {
      display: block;
      margin-top: 0.5rem;
      color: #888;
    }

    .error {
      color: red;
      font-size: 0.875rem;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Loan Application Form</h1>
    <form id="loanForm">
      <!-- Full Name Field -->
      <div class="form-group">
        <label for="fullName">Full Name</label>
        <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
        <small class="error" id="nameError"></small>
      </div>

      <!-- Email Field -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
        <small class="error" id="emailError"></small>
      </div>

      <!-- Loan Amount Field -->
      <div class="form-group">
        <label for="loanAmount">Loan Amount</label>
        <input type="number" id="loanAmount" name="loanAmount" placeholder="Enter loan amount" required min="1000" step="100">
        <small class="error" id="amountError"></small>
      </div>

      <!-- Loan Term Field -->
      <div class="form-group">
        <label for="loanTerm">Loan Term (in months)</label>
        <select id="loanTerm" name="loanTerm" required>
          <option value="">Select loan term</option>
          <option value="12">12 months</option>
          <option value="24">24 months</option>
          <option value="36">36 months</option>
          <option value="48">48 months</option>
        </select>
        <small class="error" id="termError"></small>
      </div>

      <!-- Submit Button -->
      <div class="form-group">
        <button type="submit">Submit Application</button>
      </div>
    </form>
  </div>

  <script>
    // Form Validation Script
    document.getElementById('loanForm').addEventListener('submit', function(e) {
      let hasError = false;

      // Clear previous errors
      document.querySelectorAll('.error').forEach(el => el.textContent = '');

      // Validate Full Name
      const fullName = document.getElementById('fullName').value.trim();
      if (fullName === '') {
        document.getElementById('nameError').textContent = 'Full name is required.';
        hasError = true;
      }

      // Validate Email
      const email = document.getElementById('email').value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (email === '' || !emailRegex.test(email)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        hasError = true;
      }

      // Validate Loan Amount
      const loanAmount = document.getElementById('loanAmount').value.trim();
      if (loanAmount === '' || parseFloat(loanAmount) < 1000) {
        document.getElementById('amountError').textContent = 'Loan amount must be at least 1000.';
        hasError = true;
      }

      // Validate Loan Term
      const loanTerm = document.getElementById('loanTerm').value.trim();
      if (loanTerm === '') {
        document.getElementById('termError').textContent = 'Please select a loan term.';
        hasError = true;
      }

      // Prevent form submission if there are errors
      if (hasError) {
        e.preventDefault();
      }
    });
  </script>
</body>
</html>
```
